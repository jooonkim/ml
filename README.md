# ML Notes

One running document: **[index.qmd](index.qmd)**.

Read it at https://jooonkim.github.io/ml/.

## Write

Edit `index.qmd` locally or use **Edit this page** on the website.
Put new topics near the top, below the insertion marker:

```markdown
## Attention masks

My explanation, question, code snippet, or result.

### A small example

More detail when useful.
```

- `## Topic` creates a topic and adds it to the website’s topic navigation.
- `### Subtopic` creates a heading inside a topic.
- No dates, categories, or per-topic metadata needed. GitHub commit history records saved revisions after you commit and push.
- Update **Next** whenever you want a reminder of where to resume.
- Plain code fences (for example, three backticks followed by `python`) display code. The running notebook does not execute code during publishing.

## Optional shortcut

```sh
./new-topic "Attention masks"
```

This inserts a heading and writing placeholder at the top of the notebook. It preserves existing text and refuses duplicate topic names. With no arguments, it asks for a topic. Requires Python 3. You can always type `##` yourself instead.

## Preview and publish

Preview locally with `quarto preview`. Commit and push to `main` when ready; GitHub Actions renders and deploys the website automatically.

One-time GitHub setup: **Settings → Pages → Build and deployment → Source → GitHub Actions**.

Existing notes remain under `posts/daily/` with their original URLs, linked as **Older notes**. Other old source files remain available in the repository.

Publishing does not run Python examples. Existing frozen results are reused where available; other examples display as code. Run experiments separately and paste or link results you want to keep.
