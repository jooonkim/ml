# ML Notes — Quarto + GitHub Pages (Structured)

This is a **structured ML notes site** using [Quarto](https://quarto.org) and GitHub Pages.

It separates:
- `daily/` — daily learning logs
- `concepts/` — polished concept explainers
- `math/` — derivations and math notes
- `projects/` — code-heavy experiments, demos
- `readings/` — paper & textbook notes

## Quick start

```bash
# 0) Install Quarto (https://quarto.org/docs/get-started)
# 1) Preview locally
quarto preview

# 2) Initialize git and push to GitHub
git init
git add .
git commit -m "init: structured ml notes"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main

# 3) Publish to GitHub Pages (creates gh-pages branch)
quarto publish gh-pages
```

## Creating new notes

### Daily log

```bash
quarto create post "Daily ML Log — 2025-11-13" \
  --date 2025-11-13 \
  --dir posts/daily/2025-11-13
```

### Concept explainer

```bash
quarto create post "Softmax Intuition" \
  --dir posts/concepts/softmax-intuition
```

### Math derivation

```bash
quarto create post "Backprop Through ReLU" \
  --dir posts/math/relu-backprop
```

### Project notebook

Put your notebook under:

```text
posts/projects/<project-name>/<something>.ipynb
```

Quarto will render it as a post.
