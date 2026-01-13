# Contributing to PAWS ECC Site

Welcome to the PAWS ECC website project! We welcome contributions from members and volunteers. This guide will help you set up the project locally and add content.

## Getting Started

### Prerequisites
- **Node.js**: Install from [nodejs.org](https://nodejs.org/) (v16+ recommended).
- **Python**: Install Python 3.8+.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/paws-ecc-site.git
    cd paws-ecc-site
    ```

2.  **Install dependencies:**
    This command installs both Node.js packages and sets up a Python virtual environment with required libraries.
    ```bash
    npm install
    ```

3.  **Run Development Server:**
    This starts a local server. Changes to files will automatically trigger a rebuild.
    ```bash
    npm run dev
    ```
    Open `http://localhost:5173` (or the URL shown in the terminal) to view the site.

---

## Adding Content

### 1. Adding a Team Member
Team members are stored as individual files in `content/team/`.

1.  Create a new Markdown file: `content/team/firstname.md` (e.g., `content/team/john.md`).
2.  Use the following template:
    ```yaml
    ---
    layout: team-member
    name: "John Doe"
    role: "Volunteer Coordinator"
    image: "https://example.com/john.jpg"
    bio: "John loves dogs and has been volunteering for 2 years."
    order: 5  # Higher numbers appear later in the list
    socials:
      - name: Instagram
        url: "https://instagram.com/john"
        icon: instagram
      - name: Mail
        url: "mailto:john@example.com"
        icon: mail
    ---
    ```
3.  **Images**: It is best to place images in `assets/images/` and verify they are referenced correctly.

### 2. Adding a Doggo
Dog profiles are stored in `content/doggos/`.

1.  Create a new Markdown file: `content/doggos/dogname.md` (e.g., `content/doggos/rocky.md`).
2.  Use the following template:
    ```yaml
    ---
    layout: doggo-profile
    name: "Rocky"
    age: "4 years"
    gender: "Male"
    short_desc: "A playful energetic boy."
    image: "https://example.com/rocky.jpg"
    story: "Rocky was found near the south gate..."
    personality: "Playful, Guard dog"
    health_status: "Vaccinated"
    order: 4
    ---
    ```

### 3. Adding a Blog Post
Blog posts live in `content/posts/`.

1.  Create a folder for your post: `content/posts/my-new-post/`.
2.  Create an `index.md` inside that folder.
3.  Use the following template:
    ```yaml
    ---
    layout: post
    title: "My New Blog Post"
    date: 2024-01-01
    description: "Summary of the post."
    tags: ["events", "updates"]
    ---
    
    Write your content here in Markdown format.
    ```

---

## 🛠️ Building for Production

To generate the final static site (output to `dist/`):

```bash
npm run build
```

This commands runs the Python generator and Vite optimizations to produce production-ready HTML, CSS, and images.

---

## 🎨 Icons
We use SVG icons in `templates/icons/`. If you need a new icon for the social links:
1.  Download or create an SVG.
2.  Name it clearly (e.g., `linkedin.svg`).
3.  Place it in `templates/icons/`.
4.  Reference it in the YAML frontmatter as `icon: linkedin` (without extension).
