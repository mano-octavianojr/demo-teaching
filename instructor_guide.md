# Instructor guide: HTML5 student portfolio

Audience: college beginners. The deck has **35 slides**, not 35 mandatory stops.

## Timing and routes

- **Core route: 20 minutes.** Slides 1–32 contribute exactly 17 minutes when only the core slides below are taught. All 35 slides remain available.
- **Final three minutes:** slide 33 demonstration (90 seconds), slide 34 assignment and recap (60 seconds), slide 35 next-week outline (30 seconds).
- **Optional support:** slides 6, 9, 13, 15, 16, 26, 29, 30, 31. Skip them using slide navigation during the core route. Each gets about one additional minute in the extended route. They introduce no required dependency missing from the core explanations.
- **Extended route: about 29 minutes**, teaching every supporting slide. Student practice beyond the assignment briefing needs additional time.


Core slide sequence before the final segment: 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 32.

Do not rush through the optional slides as if they were core. The core route is selected in advance. At 17:00 begin slide 33.

## Prepare the demonstration

1. Open `examples/portfolio-starter/index.html` in a plain-text editor and browser. Keep the original starter available to restore after rehearsal.
2. Open `examples/portfolio-demo-body.txt` and copy its entire contents. It contains only the finished body, not another HTML document.
3. Keep the completed portfolio available as a fallback. Its image must load from its local assets folder.
4. At the demonstration, select only the starter content between `<body>` and `</body>`, paste, save, refresh, and activate Projects.
5. Rehearse with a timer. The demonstration has a 90-second script below. No live installation, downloads, or typing of an entire page is planned.

## Assignment assessment

Students work after class. Award one check each for: a section inside main with unique `id="interests"`; an `h2` heading; a list with at least two items; a nav link targeting that ID; preservation of original content and assets; and an explanation of their changes. The expected appearance uses browser defaults. A solution is in `exercises/portfolio-solution/index.html`. The sample list items are not mandatory answers. Ask for the whole folder and a screenshot through your normal submission channel; no deadline or platform is invented here.

## Speaker notes in LaTeX

The source hides notes by default. For a notes handout, replace `\setbeameroption{hide notes}` with `\setbeameroption{show only notes}`. For presenter view use `\setbeameroption{show notes on second screen=right}`. Keep one option active. The source uses the supplied logo PNG, so use a compiler supporting project assets for the branded version if the built-in single-file compiler cannot access it.

## Slide-by-slide teaching notes

### 01. HTML5 Foundations

**Core: 35 seconds.** Introduce Maya, a fictional student who needs one portfolio page. The end product is a readable page, using default browser styles. Explain that we will add CSS next week.

### 02. Generative AI as a learning assistant

**Core: 25 seconds.** Ask students to use AI for explanations and feedback, then test the result themselves. Ask what an unfamiliar tag means before copying it. Do not introduce an AI account or tool setup.

### 03. A webpage in a browser

**Core: 45 seconds.** Use the familiar browser tab as the starting point. Explain that local files work for today, while a web server can deliver the same kinds of files online. Avoid suggesting that browsers only render HTML. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 04. HTML describes content

**Core: 40 seconds.** Read h1 as a main heading and p as a paragraph. Ask which text looks like a heading. Describe markup as adding meaningful labels, rather than writing calculations or decision logic. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 05. Why HTML5 before frameworks?

**Core: 40 seconds.** Use Bootstrap as the concrete example of a frontend UI framework/toolkit. It supplies CSS and JavaScript features, but developers still write the HTML structure. No framework setup or code is needed today. This is a recommended learning order, not a requirement to master all HTML before beginning a framework. Connect this back to the portfolio: its headings and section links still need meaningful markup after styling. Source: https://getbootstrap.com/docs/5.3/getting-started/introduction/.

### 06. HTML, CSS, and JavaScript

**Optional support: about 60 seconds.** Optional context. Use one heading as the example for all three roles. HTML can provide built-in interactions such as links; JavaScript is not required for every interaction. Do not teach CSS rules or JavaScript code.

### 07. Our portfolio destination

**Core: 40 seconds.** Briefly show the completed local page already open before class, then return to slides. Emphasize that we will build the structure ourselves, not copy a visual template. The supplied college image is a logo, not a portrait.

### 08. An element and its tags

**Core: 50 seconds.** An element includes the tags and content. Point at the slash in the closing tag. The next supporting slide explains the exception for void elements. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 09. Elements without closing tags

**Optional support: about 60 seconds.** Optional clarification. The attributes will be taught next, and images later. Explain that a closing img tag should not be added. meta is another void element we will meet in the document head. A self-closing slash is not required in HTML. Source: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img.

### 10. Nesting creates a hierarchy

**Core: 45 seconds.** Section and h2 roles are coming later; here focus on structure. Point out indentation as a reading aid. Indentation makes nesting easier to read; the tags determine the structure. Ask which element contains the paragraph. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 11. Attributes add information

**Core: 40 seconds.** Explain that an attribute supplies information about an element. The fragment destination will make sense after IDs. Ask which part is visible text. Answer My projects, not the href value. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 12. The HTML5 document skeleton

**Core: 80 seconds.** Allow 80 seconds on the core route. Explain doctype as standards mode, html as root, lang as the document language, head as metadata and body as displayed content. The title names the browser tab, while h1 names the page content. Full files include charset and viewport metadata shown on the next supporting slide. HTML5 is common teaching terminology; HTML now develops as a Living Standard. Source: https://html.spec.whatwg.org/multipage/.

### 13. Metadata in the head

**Optional support: about 60 seconds.** Optional detail. These lines live inside head in all complete examples. Viewport metadata alone does not make a layout responsive. It prepares a normal mobile viewport for later CSS. meta has no closing tag. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 14. Headings describe the outline

**Core: 55 seconds.** Use one main h1 in this lesson. Projects is a section, and the project title nests below it. Ask why choosing h3 just for a smaller font is unhelpful. CSS will control size next week. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 15. Paragraphs organize text

**Optional support: about 60 seconds.** Optional practice. Explain ordinary whitespace generally collapses in HTML rendering. Use p elements instead of repeated br tags to divide paragraphs. HTML source can wrap across lines for readability. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 16. Importance and emphasis

**Optional support: about 60 seconds.** Optional enrichment. Browsers usually render these as bold and italic, but the meaning matters. Avoid teaching strong and em as mere visual formatting commands. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 17. Lists organize related items

**Core: 50 seconds.** Use the portfolio skills as the example. Ask when order matters: editing, saving and refreshing are ordered steps. The independent list example demonstrates both ul and ol. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 18. Links connect destinations

**Core: 40 seconds.** This relative link points to a file in the same folder. A full URL can point to another website. Tell students that linking to a page is not the same as embedding it. Avoid opening external sites during this offline lesson. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 19. Navigation targets an ID

**Core: 50 seconds.** Trace projects in both places. ID values should be unique; the href includes the hash while the id value does not. This is the exact pattern used in the assignment. Navigation can work even without CSS or JavaScript. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 20. Images need a source and alternative text

**Core: 50 seconds.** The local image is supplied and makes the folder work offline. Explain that decorative images use empty alt, but this meaningful institutional mark has descriptive text. The example files use the fuller official names. Image dimensions preserve the image aspect ratio. Source: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img.

### 21. Semantic HTML names the role

**Core: 45 seconds.** We already know how tags nest. Now choose the right tags for each part of the portfolio. Semantics alone do not produce a layout or guarantee accessibility. CSS handles presentation. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 22. Header: the introduction

**Core: 35 seconds.** Use the portfolio introduction students saw at the start. Header can also introduce a section or article; this example is the page-level header. It is different from head, which contains metadata. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 23. Nav: the major links

**Core: 35 seconds.** Point back to matching IDs. Explain aria-label briefly as a name for this navigation region; it is an attribute, not a replacement for meaningful link text. The complete page uses a list inside nav. Not every group of links needs nav. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 24. Main: the primary content

**Core: 35 seconds.** Show the relationship between the page-level header, nav, main and footer. The full portfolio places About, Skills and Projects sections inside main. Repeated navigation belongs outside this main content. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 25. Section: a related topic

**Core: 40 seconds.** About, Skills and Projects are separate topics inside main. This pattern prepares students to add Interests after class. Use div for a generic grouping without a semantic role when appropriate, rather than making every wrapper a section. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 26. Article: a self-contained item

**Optional support: about 60 seconds.** Optional deeper explanation. Projects is the surrounding section; one complete project description can be an article. Not every paragraph or decorative box is an article. Ask whether this description could make sense if shared separately. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 27. Footer: the closing information

**Core: 25 seconds.** Use a brief authorship or contextual note. Footer is semantic, not an instruction to pin content to the bottom of the window. Positioning belongs to CSS. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 28. The portfolio structure together

**Core: 70 seconds.** Allow 70 seconds. Walk through the map from top to bottom. The dots deliberately omit details; the completed example contains real content and the article. Ask students where Interests should go: inside main as a new section, not in head. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 29. Files that travel together

**Optional support: about 60 seconds.** Optional setup. This listing is a folder map, not HTML code. Keep assets with the HTML when copying or submitting a portfolio. Renaming or moving an image without updating src breaks the path.

### 30. Edit, save, and refresh

**Optional support: about 60 seconds.** Optional workflow. Demonstrate this during the final live segment rather than spending core time on setup. Ensure the extension is .html rather than .html.txt. A local server is not needed.

### 31. Common mistakes to check

**Optional support: about 60 seconds.** Optional troubleshooting. Browsers repair some invalid markup, so a page looking acceptable does not prove the source is correct. Refer to the full examples for comparison. No deliberately broken code is included in learner files. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax.

### 32. A quick accessibility check

**Core: 50 seconds.** Allow 40 seconds on the core route. Ask students to name one check they can perform without a special tool. This is a starter checklist, not a full accessibility audit. Link it to reviewing AI-generated HTML. Source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents.

### 33. Live demo: assemble the portfolio

**Core: 90 seconds.** Exactly 90 seconds. Before class, copy examples/portfolio-demo-body.txt to the clipboard and open examples/portfolio-starter/index.html in both an editor and browser. 0–15 seconds identify the body placeholder; 15–40 replace only its contents; 40–55 save; 55–75 refresh and point to the sections; 75–90 activate Projects and explain the matching ID. Keep document metadata unchanged. Use the completed example as a fallback if an editor fails.

### 34. Assignment: add Interests

**Core: 60 seconds.** Exactly 60 seconds. Students complete this after class, not inside this one-minute slot. Give exercises/portfolio-starter as the starting folder. 0–25 seconds explain the task; 25–45 state the expected new heading, list and working link; 45–60 recap structure, content and meaningful regions. Ask learners to explain their own code, including AI-assisted lines. A separate solution is provided.

### 35. Next week: styling with CSS

**Core: 30 seconds.** Exactly 30 seconds. Show how this lesson becomes the foundation for the next, without adding CSS syntax today. The portfolio will look plain by design until styling is introduced.
