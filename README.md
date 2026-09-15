# Joon’s machine learning notes

This repository has two parts:

- [`foundational-notes.ipynb`](foundational-notes.ipynb) — general machine learning concepts and my original notes.
- [`notebooks/`](notebooks/) — my active companion notebooks for Raschka’s LLM chapters.

The companion notebooks follow the book’s headings, but the important code is left for me to type. Raschka’s original notebooks are linked inside each one.

## The daily workflow

Work on one small section at a time.

1. Open the current chapter notebook in Colab.
2. Read that section of the book for 20 minutes without coding.
3. Return to the notebook and write what the section is doing in your own words.
4. Type the important code into the TODO cell and run it.
5. Attempt one exercise or change one thing.
6. Write three short lines at the bottom:

```text
What I learned:
What is still unclear:
What I will try next:
```

7. Save the notebook back to GitHub at the same path.

That is a complete study session. A chapter can take several sessions.

## Where to start

Chapter 1 is reading-only, so the active path begins with Chapter 2.

| Notebook | Topic |
|---|---|
| [Chapter 2](notebooks/chapter-02.ipynb) | Working with Text Data |
| [Chapter 3](notebooks/chapter-03.ipynb) | Coding Attention Mechanisms |
| [Chapter 4](notebooks/chapter-04.ipynb) | Implementing a GPT Model |
| [Chapter 5](notebooks/chapter-05.ipynb) | Pretraining on Unlabeled Data |
| [Chapter 6](notebooks/chapter-06.ipynb) | Fine-tuning for Text Classification |
| [Chapter 7](notebooks/chapter-07.ipynb) | Fine-tuning to Follow Instructions |

## Opening a notebook

Use the **Open in Colab** link inside each notebook. When you finish a session, choose **File → Save a copy in GitHub**, select `jooonkim/ml`, and save over the same notebook path.

The website is a simple map of the notebooks. GitHub stores the files and history. Colab is where the code runs.

## Source

The chapter structure follows [Sebastian Raschka’s LLMs-from-scratch book and repository](https://github.com/rasbt/LLMs-from-scratch). The reading workflow is based on [his technical-book recommendations](https://sebastianraschka.com/blog/2025/reading-books.html).
