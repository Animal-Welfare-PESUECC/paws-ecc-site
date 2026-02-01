import os
import shutil
import gdown
import argparse

GALLERY_DIR = "assets/images/gallery"
DRIVE_FOLDER_ID = "10uheUV80l8U8LRL8m2pAYOFFKK7bC1H1"

def clean_gallery_dir():
    if os.path.exists(GALLERY_DIR):
        print(f"Cleaning {GALLERY_DIR}...")
        for filename in os.listdir(GALLERY_DIR):
            file_path = os.path.join(GALLERY_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        os.makedirs(GALLERY_DIR, exist_ok=True)

def download_images():
    print(f"Downloading images from Drive Folder ID: {DRIVE_FOLDER_ID}")
    url = f"https://drive.google.com/drive/folders/{DRIVE_FOLDER_ID}"
    
    try:
        gdown.download_folder(url, output=GALLERY_DIR, quiet=False, use_cookies=False, remaining_ok=True)
        print("Download complete.")
    except Exception as e:
        print(f"Error downloading images: {e}")

    print("Flattening directory structure...")
    for root, dirs, files in os.walk(GALLERY_DIR):
        if root == GALLERY_DIR:
            continue
        for file in files:
            src = os.path.join(root, file)
            # Handle duplicates by renaming
            dst = os.path.join(GALLERY_DIR, file)
            if os.path.exists(dst):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(os.path.join(GALLERY_DIR, f"{base}_{counter}{ext}")):
                    counter += 1
                dst = os.path.join(GALLERY_DIR, f"{base}_{counter}{ext}")
            
            try:
                shutil.move(src, dst)
            except Exception as e:
                print(f"Failed to move {src}: {e}")
    
    # Cleanup empty dirs
    for root, dirs, files in os.walk(GALLERY_DIR, topdown=False):
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except:
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true", help="Clean gallery directory first")
    args = parser.parse_args()

    if args.clean:
        clean_gallery_dir()
    
    download_images()
    
    print("Processing images into thumbnails...")
    try:
        from PIL import Image
        
        for filename in os.listdir(GALLERY_DIR):
            if filename.endswith("_thumb.webp"):
                continue
                
            file_path = os.path.join(GALLERY_DIR, filename)
            if not os.path.isfile(file_path):
                continue
                
            try:
                # distinct styling for thumbnails
                base_name = os.path.splitext(filename)[0]
                thumb_name = f"{base_name}_thumb.webp"
                thumb_path = os.path.join(GALLERY_DIR, thumb_name)
                
                # specific optimization
                with Image.open(file_path) as img:
                    # Convert to RGB if necessary (e.g. for PNGs with alpha)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Resize to max width 600px
                    max_width = 800
                    if img.width > max_width:
                        ratio = max_width / img.width
                        new_height = int(img.height * ratio)
                        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                    
                    img.save(thumb_path, "WEBP", quality=60)
                    print(f"Generated thumbnail: {thumb_name}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
                
    except ImportError:
        print("Pillow not installed, skipping thumbnail generation. Please install Pillow.")
