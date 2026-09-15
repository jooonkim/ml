# ML learning journal

**[Read the journal](ML.ipynb)** · **[Open the first chapter in Colab](https://colab.research.google.com/github/jooonkim/ml/blob/main/notebooks/chapter-01.ipynb)** · **[Website](https://jooonkim.github.io/ml/)**

`ML.ipynb` preserves my original 16 ML notes. The seven notebooks in `notebooks/` are the active chapter-by-chapter learning path.

## Daily workflow

1. Open the current `notebooks/chapter-XX.ipynb` in Colab.
2. Read the matching Raschka chapter offline before coding.
3. Write the explanation and type the important code into the TODO cells.
4. Attempt an exercise, change one thing, and record the result in that chapter notebook.
5. Save the notebook to GitHub at the same path.

GitHub tracks revisions. Saving only to Drive does not update GitHub. Include outputs when saving if you want plots to appear publicly. Colab's table of contents navigates topic headings; Quarto generates website navigation from the same headings.

## Raschka’s study method, made daily

This project follows [Sebastian Raschka's five-stage approach to technical books](https://sebastianraschka.com/blog/2025/reading-books.html). For each chapter or small topic, use this loop:

1. **First read — 20 minutes, offline.** Read for the big picture. Do not code or search for answers yet. Mark confusing ideas.
2. **Second read — code.** Open the matching chapter notebook in Colab. Type and run the important code yourself. If results differ, check seeds, package versions, hardware, and the upstream repository.
3. **Exercise.** Attempt at least one exercise before looking at the solution.
4. **Review.** Return to your highlights. Look up only the questions that still matter, then write the useful explanation in the chapter notebook.
5. **Use it.** Change one thing or apply the idea to a small experiment. Record the result and choose the next step.

### The everyday checklist

```text
[ ] Read for 20 minutes without coding
[ ] Re-type and run one small code section
[ ] Change one variable or try one exercise
[ ] Write: what I learned / what is unclear / what I will try next
[ ] Save the chapter notebook to GitHub
```

One checkbox session is enough. A chapter may take several sessions: first read, code, exercises, review, then project. Easy chapters can be skimmed; difficult chapters deserve more than one pass.

## Running

The chapter notebooks are deliberately unfinished: their TODO cells are where I type the important code. Colab provides the working environment; I add packages only when a chapter needs them.

## My chapter notebooks

The main learning path is now seven small companion notebooks. They follow Raschka’s chapter headings, but they do not copy the implementation. The important code cells are TODO prompts so I have to type, run, and understand the code myself.

| Chapter | Notebook |
|---|---|
| 1. Understanding Large Language Models | [chapter-01.ipynb](notebooks/chapter-01.ipynb) |
| 2. Working with Text Data | [chapter-02.ipynb](notebooks/chapter-02.ipynb) |
| 3. Coding Attention Mechanisms | [chapter-03.ipynb](notebooks/chapter-03.ipynb) |
| 4. Implementing a GPT Model | [chapter-04.ipynb](notebooks/chapter-04.ipynb) |
| 5. Pretraining on Unlabeled Data | [chapter-05.ipynb](notebooks/chapter-05.ipynb) |
| 6. Finetuning for Text Classification | [chapter-06.ipynb](notebooks/chapter-06.ipynb) |
| 7. Finetuning to Follow Instructions | [chapter-07.ipynb](notebooks/chapter-07.ipynb) |

The full upstream course remains available at [Raschka’s repository](https://github.com/rasbt/LLMs-from-scratch), including bonus notebooks and solutions. Use the source notebook for comparison only after attempting the TODO cell yourself.

## Website

The site is a small landing page for the journal and chapter notebooks. GitHub and Colab are the main reading and editing interfaces.
