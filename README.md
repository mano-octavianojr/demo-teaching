# HTML5 Foundations: Building a Student Portfolio

A DLSU College of Computer Studies demonstration for college beginners. Build the structure of a fictional student portfolio using HTML, then extend it in an assignment. **No CSS or JavaScript is required.** The plain browser appearance is intentional; CSS follows next week.

## Start here

1. Download this repository as a ZIP and extract it, or clone it:

   ```bash
   git clone https://github.com/mano-octavianojr/demo-teaching.git
   cd demo-teaching
   ```

2. Open [the completed portfolio](examples/portfolio-complete/index.html) by double-clicking its local `index.html`, or use your browser's Open File command. A GitHub file link displays source, not a hosted webpage. Download first to see the rendered result.
3. Edit [the starter](examples/portfolio-starter/index.html) with a plain-text editor. Keep its assets folder beside it. Save and refresh to see changes.

No Python, Colab, package installation, server, external font, or network request is needed to run the HTML examples. Internet is only needed to download the materials or read optional external references. The examples contain no remote resources or external navigation destinations.

## Teaching package

- [LaTeX presentation](presentation.tex): **35 slides** with the supplied DLSU CCS branding, one teaching purpose per slide, and speaker notes marking core and optional content.
- [Instructor guide](instructor_guide.md): exactly **17 minutes of core discussion plus a three-minute closing segment**. Optional explanations extend the lesson to about 29 minutes.
- [Portfolio starter](examples/portfolio-starter/index.html), [completed portfolio](examples/portfolio-complete/index.html), and [prepared demo body](examples/portfolio-demo-body.txt).
- [Assignment instructions](exercises/README.md), [assignment starter](exercises/portfolio-starter/index.html), and [separate solution](exercises/portfolio-solution/index.html).
- [Archived Python lesson](archive/README.md): the original slides, notebooks, script, data, requirements, and documentation.

Slide 2 explains that GenAI is allowed as a learning assistant, but students must understand, verify, explain, and modify the HTML they use.

## Independent examples

Every file is a complete HTML document. Open any one directly; none depends on an earlier example. The image example includes its required asset in the adjacent `assets` folder.

| File | Focus |
| --- | --- |
| [01_document_structure.html](examples/independent/01_document_structure.html) | Document structure |
| [02_headings_paragraphs.html](examples/independent/02_headings_paragraphs.html) | Headings and paragraphs |
| [03_lists.html](examples/independent/03_lists.html) | Lists |
| [04_links.html](examples/independent/04_links.html) | Links and anchors |
| [05_images.html](examples/independent/05_images.html) | Images and alternative text |
| [06_semantic_structure.html](examples/independent/06_semantic_structure.html) | Semantic page structure |

## Presentation flow

| Slides | Discussion |
| --- | --- |
| 1–2 | Portfolio goal and outcomes; responsible GenAI use |
| 3–7 | Browser, HTML's role, why foundations precede Bootstrap, related technologies, and portfolio preview |
| 8–13 | Tags, void elements, nesting, attributes, skeleton, metadata |
| 14–20 | Headings, paragraphs, emphasis, lists, links, anchors, images |
| 21–28 | Semantic regions and complete portfolio structure |
| 29–32 | Files, browser workflow, mistakes, accessibility checks |
| 33–35 | Demo (90s), assignment and recap (60s), next week (30s) |

The full deck supports deeper explanations. A 20-minute demo teaches the marked core slides rather than compressing every slide. Learners may review optional slides afterward. Timing is a planned speaking schedule; classroom timing must be rehearsed.

## Expected result and assignment

The portfolio displays Maya Santos, an institutional logo, About, Skills, Projects (including one project article), and a footer. Navigation links target the matching sections. The image is a college mark, not a student portrait; all student details are fictional.

After class, add an **Interests** section with an `h2`, an unordered list of at least two interests, and an **Interests** navigation link. The solution adds two sample interests without removing the existing content. See the assignment instructions for the self-check and submission contents.

## Assets and LaTeX

Keep `DLSU-CCS-Logo-Clear.png` beside `presentation.tex`. Each downloadable portfolio folder has its own `assets/college-logo.png` copy for portability. The supplied logo is reused without modification.

The current source stays open in the Codex LaTeX editor. Its built-in compiler previously could not load the external PNG. If that limitation continues, compile the source and logo together in a project-capable compiler, such as Overleaf or an **existing** local TeX setup. With existing local TeX, compile twice using `pdflatex presentation.tex`. No TeX installation or separate PDF is part of this update.

## Official references

- [MDN: Basic HTML syntax](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax)
- [MDN: Structuring documents](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents)
- [MDN: Images](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/)

“HTML5” is the familiar lesson label; HTML is maintained as a Living Standard. Accessibility checks in this lesson are introductory, not a full audit.
