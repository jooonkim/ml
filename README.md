# Joon Kim's ML Notes

A repository of ML notes as I learn in public. Hosted on [Quarto](https://quarto.org) and GitHub Pages.

This site separates my notes into:

```daily/``` — daily learning logs

```concepts/``` — polished concept explainers

```math/``` — derivations and math notes

```projects/``` — experiments, notebooks, demos

```readings/``` — book & paper notes

Everything is organized into standalone “posts” using Quarto’s built-in listing system.

## 🚀 Quick Start (Note to Self)
### 0) Install Quarto (https://quarto.org/docs/get-started)
### 1) Preview locally
```bash 
quarto preview
```
### 2) Initialize git and push to GitHub
```bash
git init
git add .
git commit -m "init: structured ml notes"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

# 3) Publish to GitHub Pages (creates gh-pages branch)
```bash
quarto publish gh-pages
```

The live site will be served from the gh-pages branch, automatically updated whenever you run quarto publish.

## 🗓 Creating a New Daily ML Note

This project includes a helper script called new-daily that automatically creates a daily ML post in the correct folder structure and inserts a template for consistent note-taking.

One-time setup
```bash
chmod +x new-daily
```

Usage
```bash
./new-daily
```

This generates:
```bash
posts/daily/YYYY-MM-DD/index.qmd
```

With frontmatter:
```yaml
---
title: "YYYY-MM-DD"
date: YYYY-MM-DD
categories: [daily]
---
```

And a template body:
```markdown
## Notes
-

## Questions I still have
-

## Tomorrow's plan
-
```

You can then edit the file normally.

### How it works

- Determines today’s date using date +%Y-%m-%d
- Creates the folder posts/daily/YYYY-MM-DD/
- Writes an index.qmd file with the appropriate metadata + sections
- Compatible with Quarto 1.8+ (which removed quarto create post)
If desired, this script can be extended to accept manual dates, open VS Code automatically, or auto-commit + auto-publish.

## ✏️ Creating New Notes (Quarto 1.8+)

Posts are created by simply making a folder and adding an ```index.qmd```.

This approach is simple, future-proof, and fully compatible with Quarto’s listing system.

### 📝 Concept Explainer

Example: “Softmax Intuition”
```bash
mkdir -p posts/concepts/softmax-intuition
nano posts/concepts/softmax-intuition/index.qmd
```

Frontmatter:
```yaml
---
title: "Softmax Intuition"
date: YYYY-MM-DD
categories: [concepts]
---
```
Write the explainer below the YAML block.

🧮 Math Derivation
```bash
mkdir -p posts/math/relu-backprop
nano posts/math/relu-backprop/index.qmd
```

Frontmatter:
```yaml
---
title: "Backprop Through ReLU"
date: YYYY-MM-DD
categories: [math]
---
```
🧪 Project Notebook

Projects live under:
```bash
posts/projects/<project-name>/
```

Add notebooks directly:
```bash
mkdir -p posts/projects/mnist-from-scratch
cp mnist.ipynb posts/projects/mnist-from-scratch/
```

Quarto automatically renders ```.ipynb``` files when publishing.

📚 Reading Notes
```bash
mkdir -p posts/readings/murphy-ch3
nano posts/readings/murphy-ch3/index.qmd
```

Frontmatter:
```yaml
---
title: "Murphy — Chapter 3 Notes"
date: YYYY-MM-DD
categories: [readings]
---
```

Reference citations via the included ```references.bib```.

## 🐙 Understanding main vs. gh-pages

- ```main``` branch: Contains all source files (.qmd, .ipynb, posts, images, config). This is where editing happens.

- ```gh-pages``` branch: Contains the rendered HTML website. Do NOT edit this branch manually—Quarto overwrites it on each publish.

Publishing workflow:
```bash
quarto publish gh-pages
```

This:

1. Builds the site → ```_site/```
2. Writes it into ```gh-pages``` branch
3. Pushes it to GitHub Pages

Your live site updates instantly.

## 📁 Project Structure Overview
ml/
├── _quarto.yml
├── index.qmd
├── references.bib
└── posts/
    ├── daily/
    │   └── YYYY-MM-DD/
    │       └── index.qmd
    ├── concepts/
    │   └── <topic>/index.qmd
    ├── math/
    │   └── <topic>/index.qmd
    ├── projects/
    │   └── <project>/index.qmd or *.ipynb
    └── readings/
        └── <source>/index.qmd


Quarto automatically lists posts on the homepage and within category pages.

## 🧠 Notes to Future Joon

Always edit ```main``` branch, never ```gh-pages```

Use ```./new-daily``` every day when taking notes

Publish updates with:
```bash
quarto publish gh-pages
```

Preview locally first:
```bash
quarto 
```