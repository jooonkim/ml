# ML learning journal

**[Read the notebook](ML.ipynb)** · **[Open in Colab](https://colab.research.google.com/github/jooonkim/ml/blob/main/ML.ipynb)** · **[Website](https://jooonkim.github.io/ml/)**

One notebook: **ML.ipynb**. It contains all 16 earlier entries, with explanations, equations, personal notes, references, code, and results together.

## Daily workflow

1. Open **ML.ipynb** in Colab.
2. Add a text cell with `## Topic` at the end. Use `### Subtopic` inside it. Dates are optional.
3. Add explanations and code cells. Run experiments and keep useful outputs.
4. Update **Next** near the top.
5. Choose **File → Save a copy in GitHub**, repository `jooonkim/ml`, branch `main`, path **ML.ipynb**. Reuse this path each time.

GitHub tracks revisions. Saving only to Drive does not update GitHub. Include outputs when saving if you want plots to appear publicly. Colab's table of contents navigates topic headings; Quarto generates website navigation from the same headings.

## Running

The migrated examples run on CPU and use NumPy, pandas, Matplotlib, and scikit-learn, normally available in Colab. For local use, install `requirements-notebooks.txt`. Each historical executable example has its imports; run the whole notebook top to bottom to reproduce saved outputs. Illustrative snippets originally marked non-executable are Markdown code blocks, not runnable cells. Add PyTorch imports when you begin the LLM exercises.

## Website

The existing Quarto site links to the notebook on GitHub and keeps the historical pages under `posts/daily/`. It does not render or execute the new notebook. GitHub and Colab are the main reading and editing interfaces; edit **ML.ipynb** going forward.

## Migration

All 16 original notes are mapped in `migration-manifest.json` with original file hashes. Original prose, questions, personal notes, and source links are retained. Formatting changes convert Quarto callouts to Markdown and organize topics. Obsolete rendering setup cells were removed. Executable examples use `np.float64`, include a missing NumPy import, embed the shared perceptron class, and use the bundled Iris dataset to run without downloads. This preserves the learning record; it is not a factual review of the notes.

Optional local shortcut: `./new-topic "Attention"` appends a topic and blank code cell to **ML.ipynb**, refusing duplicate topics. You can simply add text/code cells in Colab instead.
