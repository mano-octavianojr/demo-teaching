# Python Foundations

A beginner college lesson using a fictional **student grade analyzer**. The 48-slide presentation covers Python through text and CSV file reading and writing. Allow **42 minutes**, or use the instructor guide for 30-minute, 45-minute, and 6-minute routes.

Django (web applications), NumPy (numerical arrays for analysis), and TensorFlow (machine learning) are examples of later applications. They are not dependencies of this course.

For detailed instructions, see the [project documentation](docs/documentation.docx).

## How to access

### Run in Google Colab

Click an **Open in Colab** button in the lessons table to run the combined notebook in your browser, then use its contents list to choose a lesson. No local installation is needed. Sign in to Google if prompted, then choose **File → Save a copy in Drive** to keep your notebook work. Run cells in order using **Shift+Enter**, or choose **Runtime → Run all**.

Lesson 06 automatically **creates its fictional sample data when no local copy exists**. It does not fetch data from GitHub, request uploads, or mount Google Drive. Existing CSV data are preserved. Reports are replaced on repeat runs.

To keep a generated report, open the **Files** sidebar, refresh the listing, find `outputs/grade_summary.txt`, open its menu, and choose **Download**. Runtime files are temporary. Saving the notebook to Drive does not automatically preserve generated files.

### Run locally

Install **Python 3.10 or newer**, then clone [this repository](https://github.com/mano-octavianojr/demo-teaching) or download and extract its ZIP. Open a terminal in the project folder.

```bash
git clone https://github.com/mano-octavianojr/demo-teaching.git
cd demo-teaching
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyter lab
```

If PowerShell blocks activation, use the environment's executable directly, without changing system policy:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

In JupyterLab open `notebooks/python_foundations.ipynb`, use its contents links to choose a lesson, and start with lesson 01, and press **Shift+Enter** to run each cell. Each lesson section also works independently; run its cells in order. To reset notebook state, restart the kernel and run all cells from the beginning. Standard-library lesson code needs no package installation in Colab. `requirements.txt` installs local notebook tools.

### Run the complete script

From the project folder, using the activated environment:

```bash
python examples/grade_analyzer.py
```

The script needs no third-party packages. You can also use `python3 examples/grade_analyzer.py` on macOS/Linux without activating an environment. It resolves repository paths from the script's location, so it also works when launched from another folder.

## Lessons

| Notebook | Python focus | Run online |
| --- | --- | --- |
| [01 — First Steps](notebooks/python_foundations.ipynb#lesson-01) | Printing, strings, comments | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb#lesson-01) |
| [02 — Variables and Calculations](notebooks/python_foundations.ipynb#lesson-02) | Variables, types, operators, conversion | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb#lesson-02) |
| [03 — Student Records](notebooks/python_foundations.ipynb#lesson-03) | Strings, lists, dictionaries | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb#lesson-03) |
| [04 — Decisions and Repetition](notebooks/python_foundations.ipynb#lesson-04) | Conditions, loops, accumulation | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb#lesson-04) |
| [05 — Reusable Functions](notebooks/python_foundations.ipynb#lesson-05) | Functions, return values, errors | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb#lesson-05) |
| [06 — Files and Grade Analyzer](notebooks/python_foundations.ipynb#lesson-06) | Text/CSV files and complete analyzer | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb#lesson-06) |

All lesson links open sections of the combined notebook. Colab badges open the same notebook; use its contents list to jump to the lesson.

## Expected result

The sample CSV contains Maya (88), Luis (72), Ari (95), and Bea (75). Both lesson 06 and the script produce:

```text
Students: 4
Class average: 82.50
Passing threshold (illustrative): 75
Passing students: 3
Names: Maya, Ari, Bea
```

The report is `outputs/grade_summary.txt`. A final `Saved:` line prints its runtime-specific location. A threshold of **75 is a teaching example**, not institutional policy. With a threshold of 90, only Ari passes and the mean remains 82.50.

CSV headers must be `name,grade`. Grades must be finite numbers from 0 to 100 and names must be nonempty. A header-only file gives `No student records.`. Invalid data produce an explanatory error. Edit a copy of the fictional CSV for practice. The notebook chooses the repository root when started in `notebooks/`, otherwise the current working folder. The script always uses the repository root, resolved from its location in `examples/`.

## Presentation

- `lectures/presentation.tex`: standalone 16:9 LaTeX Beamer deck, exactly 48 slides. Code uses `listings` and needs no shell escape or Python package. The DLSU CCS logo is the supplied `template/DLSU-CCS-Logo-Clear.png`, referenced by its relative path from `lectures/`.
- `markdown/instructor_guide.md`: slide-by-slide speaking notes, timing, questions, and the 6-minute live demo script. Setup happens before the timed lesson.

The source remains open in Codex's built-in LaTeX editor. Its current single-file compiler cannot load the separate logo PNG, so the branded deck requires a project-capable LaTeX compiler (for example an existing local TeX setup or Overleaf) with both `lectures/` and `template/` preserving their relative layout. The student view hides notes by default. The instructor guide explains how to enable notes. With an existing local LaTeX installation, run `cd lectures`, then compile twice using `pdflatex presentation.tex` or use `latexmk -pdf presentation.tex`. Do not run these commands inside a Python cell.

| Slides | Content | Suggested time |
| --- | --- | --- |
| 1–6 | The report task, Python background, and execution | 4 min |
| 7–14 | One student: output, values, calculations, and errors | 9 min |
| 15–18 | A class: lists and student dictionaries | 5 min |
| 19–30 | Processing records: decisions and loop traces | 9 min |
| 31–38 | Organizing reusable functions | 6 min |
| 39–43 | Keeping results: text files and CSV input | 5 min |
| 44–48 | Complete analyzer, saved report, practice, and applications | 4 min |

Slide notes target approximately 42 minutes. Running Python setup stays in this README rather than the slides. For 45 minutes add three minutes of guided practice. For 30 minutes summarize designated reference slides. The short route has a separate six-minute schedule in the instructor guide. Timing is a delivery target, not a recorded classroom rehearsal.

## Repository

```text
template/        # Shared presentation assets
docs/            # Project documentation
lectures/        # LaTeX lecture deck
notebooks/       # Combined notebook with six lesson sections
data/            # Fictional sample data
examples/         # Grade analyzer script
README.md
requirements.txt
markdown/        # Other Markdown files, including the instructor guide
```

Generated reports go to the ignored `outputs/` folder at the repository root.


The materials are hosted at [mano-octavianojr/demo-teaching](https://github.com/mano-octavianojr/demo-teaching) on the `main` branch. All examples use fictional student data.

## Official references

- [Python tutorial](https://docs.python.org/3/tutorial/) — supplementary reference, assumes some programming knowledge.
- [Python files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), [csv](https://docs.python.org/3/library/csv.html), and [pathlib](https://docs.python.org/3/library/pathlib.html).
- [Django](https://www.djangoproject.com/), [NumPy](https://numpy.org/), and [TensorFlow](https://www.tensorflow.org/).
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html).
