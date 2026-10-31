# Instructor guide

48 slides. Approximately 42 minutes, excluding setup. Follow one report task: represent four students, process their grades, organize reusable steps, and save results.

## Using the materials

Students use one notebook, `notebooks/python_foundations.ipynb`, with six lesson sections and a contents list. The Word student guide is `docs/documentation.docx`; its readable source is `markdown/documentation.md`. Use the README for setup commands and the Colab launch button.

The grade analyzer is the final example program, not an answer checker. Lessons 01–05 introduce the skills; lesson 06 combines them into the saved class report. Expected values assume the bundled fictional CSV has not been edited. A passing threshold of 75 is illustrative.

Use the notebook for runnable demonstrations. Slide snippets are shortened teaching examples and may require earlier definitions. Run the selected lesson's setup cells before demonstrating a later cell. At slide 13, the conversion-error cell in lesson 05 can run by itself because it does not depend on that lesson's function definitions.

Ask students to try practice cells before viewing solutions. Run all executes the solutions too. A student's list mutation and the supplied solution share state: rerun the setup cell before comparing an append exercise, rather than appending the same student again.

## 01. Python Foundations

0:30. Introduce the fictional grade analyzer: four records become a saved class summary. Ask who has used a spreadsheet formula. Connect instructions to familiar calculations. Short demo: begin here for 20 seconds.

## 02. Our task: a class grade report

Begin with the result students will build. Ask what information the report needs. We will represent the data, process it, organize the steps and save the result. 0:40. These are introductory outcomes, not mastery claims. Ask students to name one result they want a program to calculate. Explain that one notebook contains six practice lesson sections.

## 03. Python and a program

0:50. Explain interpreter as the program that runs Python instructions. Avoid installation detail here. Source: https://docs.python.org/3/tutorial/ .

## 04. A brief history of Python

0:40. Explain that Python began as a practical scripting language and grew into a general-purpose language. Avoid a long version timeline. Source: https://docs.python.org/3/faq/general.html.

## 05. Why choose Python?

0:40. Present these as reasons to choose Python for this lesson and rapid prototyping, rather than a claim it is best for every task. Mention that libraries may perform expensive operations using compiled code. Sources: https://www.python.org/doc/essays/blurb/ and https://docs.python.org/3/glossary.html#term-interpreted.

## 06. Interpreter and compiler

Bridge to the first code: we now know what executes our instructions. The next slide shows our first visible result. 0:50. Explain translation versus execution without claiming that Python never compiles or simply executes source line by line. CPython is the standard Python implementation. Bytecode is an intermediate instruction format, not a native machine-code executable. Ask whether Python can use both compilation and interpretation. Answer yes. Source: https://docs.python.org/3/glossary.html#term-interpreted.

## 07. Our first output

0:50. Ask students to predict which line appears first. Explain parentheses call print and quotes delimit text. Run lesson 01 first code cell, whose greeting also includes a welcome line.

## 08. Comments, order, and indentation

0:50. Expected Maya then Grade: 88. Point at the comment and explain it produces no output. Notebook cells share state. Restart and run all to check reproducibility. Explain four spaces later when a real block appears.

## 09. Variables name values

1:10. Ask what changes if grade becomes 90. Explain the right side is evaluated before assignment. Short demo: 30 seconds, show just grade = 88 and print(grade).

## 10. Common value types

1:00. Ask whether quotation marks change the type of 88. Explain Python infers the type from the value, and a name can later refer to another value. Avoid going into memory representation.

## 11. Arithmetic and grouping

1:20. Work the total 330 aloud. Distinguish / division, // floor division, percent remainder and ** power. Optional quick prediction: 7 percent 2 is 1. For 30 minutes omit secondary operators.

## 12. Converting text to numbers

1:30. Predict what string concatenation does: "88" + "2" gives "882". Explain int versus float and that float("absent") will raise ValueError. Do not introduce input prompts into the runnable notebook sequence.

## 13. Common errors and useful feedback

1:30. Demonstrate the caught float("absent") example in lesson 05. Explain reading the last traceback line and checking the indicated source line. Syntax errors must be fixed before a cell can run. For 30 minutes show only one conversion error.

## 14. Strings and formatted output

1:10. Explain strip removes surrounding whitespace and returns new text. Ask why cleaning a CSV name might help. Name dot strip is a method call on the string.

## 15. Lists keep values in order

Bridge from one student to a class: separate grade variables become awkward as the class grows. A list stores several grades in order. 1:20. Have students predict grades[1], answer 72. Explain square brackets create the list or select one element depending on context. Short demo: 30 seconds to show list and first item.

## 16. Adding and counting list items

1:00. Explain append changes the list, len returns its size. Ask what index would be invalid for this four-item list. Answer 4 or greater on the positive side.

## 17. Dictionaries name each field

1:20. Contrast a numeric list position with a meaningful dictionary key. Ask students to identify the key and value for grade. No need to discuss hashing.

## 18. A list of student records

1:10. Trace selection in two steps: get the second dictionary, then its name field. These are the same four students introduced in the opening task. The notebook separately practices adding Ari. For 30 minutes give this exercise as follow-up.

## 19. Comparisons produce Boolean values

We have represented the four records. Next we need a rule to decide who passes before repeating that rule for everyone. 1:00. Emphasize assignment = versus equality ==. Ask whether the boundary grade 75 passes under >=. State clearly that this is not an institutional policy.

## 20. A condition selects a branch

1:30. Point out colons and four-space indentation. Ask students to predict grade 74. Only one branch runs. Remind students threshold is illustrative.

## 21. Combining conditions

1:00. Ask students to try -1 and 101 mentally. Mention elif supports additional branches, but do not add another example in the timed lesson. For 30 minutes summarize this slide.

## 22. A loop visits every grade

One condition handles one grade. A loop lets us visit every grade without copying the same instruction four times. 0:35. Define iteration as one repetition. Trace this exact list across the next five slides. Ask how often Finished will print. Short demo: 40 seconds here, summarize the trace slides.

## 23. Loop step 1: grade is 88

0:20. This is a trace of the loop body, not an additional assignment to insert into the loop. Ask learners to predict the next grade.

## 24. Loop step 2: grade is 72

0:20. This is a trace of the loop body, not an additional assignment to insert into the loop. Ask learners to predict the next grade.

## 25. Loop step 3: grade is 95

0:20. This is a trace of the loop body, not an additional assignment to insert into the loop. Ask learners to predict the next grade.

## 26. Loop step 4: grade is 75

0:20. This is a trace of the loop body, not an additional assignment to insert into the loop. Ask whether there is a fifth grade. There is not.

## 27. After the final iteration

0:30. Point back to the unindented statement on the overview slide. A nonempty for loop leaves grade referring to its last assigned item, but focus on flow. Ask how an empty list changes the output: only Finished prints.

## 28. An accumulator builds a total

0:45. Explain total += grade means total = total + grade. The next slide makes every update explicit. Short demo: 45 seconds here.

## 29. The total after each iteration

0:45. Ask learners to calculate each new total before revealing it verbally. Explain why putting total = 0 inside the loop would reset the running total.

## 30. Collecting passing names

Combine the two tools we just learned: repeat over records, then choose names using a condition. The list contains all four original students. 1:30. Demonstrate nested indentation. With all four bundled records, names are Maya, Ari, Bea. Ask whether Bea passes at exactly 75. Lesson 04 in the combined notebook includes all four records.

## 31. Functions organize repeated work

0:40. We can now calculate and filter grades, but want reusable steps. Point to the definition and then the call. Defining the function does not run its body. Introduce parameters and return values only as the following examples need them.

## 32. No parameters, no explicit return

0:40. Explain no return means no explicit return statement. Every Python function still returns a value, None by default. Ask whether the heading prints when the function is only defined.

## 33. With a parameter, no explicit return

0:40. Ask which part changes between calls. Name is a parameter, Maya and Luis are arguments. The printed text is an effect, not a returned string.

## 34. No parameters, with a return value

0:40. Explain the illustrative threshold is fixed inside this function. Calling without print would return 75 to the caller but would not print in a script. Notebook expression display is separate from print.

## 35. With a parameter and a return value

0:50. Sum is the built-in equivalent of the earlier running total. The list enters as an argument and the mean returns to average. Short demo: 45 seconds definition and 30 seconds call.

## 36. Displaying a value and returning it

0:45. First output is the print inside the function. Second output is the implicit return stored in result. Ask how to change the function to return grade instead. Answer replace print(grade) with return grade.

## 37. Handling an empty input

0:40. This replaces the earlier nonempty-only version. Ask what sum and len would be for an empty list. Both are zero. Explain the caller must handle None before formatting a decimal.

## 38. A function with a default

0:40. Identify both parameters. Explain the second call replaces the default. Optional extension: students write grade_label returning a string. For 30 minutes leave this slide for reference.

## 39. Paths locate files

Our reusable code computes a report, but variables disappear when the session ends. A file preserves the result. 1:00. Explain import and Path as a standard-library tool. Slash joins paths across operating systems. Notebook setup resolves root versus notebooks directory. Script resolves repository paths from its own file. Short demo: 25 seconds.

## 40. Writing a text file

1:10. Warn concretely that w replaces existing content, so write to outputs. Short demo: 35 seconds, run and show the file. Existing student CSV is never overwritten automatically.

## 41. Reading a text file

1:00. Explain end empty avoids printing a second newline because the file already contains one. Ask which mode should preserve old text while adding more. Answer a. Short demo: 25 seconds.

## 42. CSV stores rows and columns

We have saved and reopened text. Now move the original student records into a structured file so we can read a class without typing each dictionary. 0:50. Explain CSV means comma-separated values. Show data/grades.csv. No downloads are needed in Colab because lesson 06 creates this data if missing. Ask what happens if we add a fifth row.

## 43. Reading CSV records

1:10. This is the core reading pattern, assuming valid data. The full notebook adds header and grade validation. DictReader maps column headers to string fields. newline empty lets csv handle line endings. Source: https://docs.python.org/3/library/csv.html .

## 44. The complete grade analyzer

Connect the project before showing helper calls: read records, summarize them, then write a report. These helper names refer to the complete notebook implementation. 0:40. Run lesson 06 end to end before class. During teaching show the final execution cell. Local equivalent is python examples/grade_analyzer.py. Short demo: 20 seconds to connect the small mean-file example to the completed project.

## 45. The saved summary

0:50. Connect each helper to earlier ideas. Show actual generated report. Explain empty classes receive a message and invalid CSV grades receive feedback. Files in a Colab runtime are temporary: download reports before runtime reset.

## 46. Practice: a different threshold

0:40. Answer: Ari only, average remains 82.50. The solution is separated in lesson 06. For 45 minutes allocate an additional three minutes to this exercise. Ask why changing the threshold does not change the class average.

## 47. Where Python can lead

The saved report completes our original task. Relate the same skills to future tools: Django accepts and saves records, NumPy processes numeric collections, TensorFlow learns from data. 1:00. Ask which application interests the class. Clarify these are separate tools in the Python ecosystem and are not needed for this lesson. Sources: https://www.djangoproject.com/ , https://numpy.org/ , https://www.tensorflow.org/ .

## 48. What comes next

0:40. Exit ticket: explain one input, one processing step and one output of the analyzer. Short demo: 15 seconds. Reference links and full setup instructions are in README. Plan approximately 42 minutes for the complete narrative, excluding setup.

## Delivery routes

**Full lesson:** approximately 42 minutes for the presentation and brief demonstrations, excluding setup and completion of every notebook exercise. The slide-note allocations total 41 minutes 50 seconds. Allow additional time if students work through all practice cells during class. Add three minutes of paired practice on slide 46 for 45 minutes.

**30 minutes:** summarize history, interpreter details, secondary operators, and errors. Walk quickly through the four loop traces. Keep the four function patterns, leaving defaults and empty-input handling as reference. Demonstrate files rather than retyping. Assign the final exercise as follow-up.

**Six-minute demo:** pre-open a scratch cell and use slide 1 (20s), slide 9 (30s), slide 15 (30s), slide 22 (40s), slide 28 (45s), slide 35 (75s), slide 39 (25s), slide 40 (35s), slide 41 (25s), slide 44 (20s), slide 48 (15s). On the function slide, allow 45 seconds for the definition and 30 seconds for the call. Total 360 seconds. This short route demonstrates a mean-only file, `outputs/demo_mean.txt`; it does not build the complete CSV analyzer or the final class report. Show the prepared lesson 06 report when connecting to the final project.

```python
from pathlib import Path

grade = 88
print(grade)
grades = [88, 72, 95, 75]
for grade in grades:
    print(grade)
total = 0
for grade in grades:
    total += grade
print(f"Average: {total / len(grades):.2f}")

def mean_grade(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

average = mean_grade(grades)
output_dir = Path("outputs")
output_dir.mkdir(parents=True, exist_ok=True)
report_path = output_dir / "demo_mean.txt"
with report_path.open("w", encoding="utf-8") as file:
    file.write(f"Class average: {average:.2f}\n")
with report_path.open("r", encoding="utf-8") as file:
    print(file.read(), end="")
```

## Before class

Open `notebooks/python_foundations.ipynb` and run the full notebook once. Check the contents navigation and locate the default and high-threshold reports produced by lesson 06. Reset the session and clear outputs for learner predictions. Keep a copy of the expected report available in README. Check display size and use a timer. Offer Colab as the setup path when students have no local installation.

Compile and check the presentation using the README instructions. Keep the logo in `template/` when sharing the source project.

## Notes in Beamer

`lectures/presentation.tex` hides notes in the default student view. Replace `\setbeameroption{hide notes}` with `\setbeameroption{show notes on second screen=right}` for speaker notes, or `\setbeameroption{show only notes}` for a notes document. Keep exactly one of these options active.
