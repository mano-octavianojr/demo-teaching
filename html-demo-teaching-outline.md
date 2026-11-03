# HTML Foundations: Demo Teaching Guide

## Teaching brief

- **Instructor:** Manolito Octaviano Jr.
- **Audience:** DLSU undergraduate students; no HTML knowledge assumed.
- **Format:** Approximately 30 minutes of instructor-led discussion and prepared browser demonstrations. Independent practice is optional and follows the presentation.
- **Current deck:** 33 slides in 16:9, including the opening and closing covers. Slide numbers below follow the actual frame order, rather than the older numbered source comments.
- **Story:** Build a page for a fictional Campus Web Development Meetup.
- **Learning outcomes:** Read markup, recognize document structure, choose content elements, and save and preview a web page.
- **Scope:** HTML structure, text, lists, links, images, and local preview. CSS and JavaScript are introduced only by role.

## Files and preparation

| File | Purpose |
|---|---|
| [lecture/html-foundations.tex](lecture/html-foundations.tex) | Current lecture source |
| [lecture/dlsu-beamer.sty](lecture/dlsu-beamer.sty) | Shared Beamer theme and HTML listing style |
| [lecture/DLSU-CCS-Logo-Clear.png](lecture/DLSU-CCS-Logo-Clear.png) | Cover and footer logo |
| [lecture/dlsu_template_example.tex](lecture/dlsu_template_example.tex) | Supporting template example |
| [example/index.html](example/index.html) | Complete runnable event page |
| [example/meetup.jpg](example/meetup.jpg) | Local image used by the complete page |
| [example/our-smallest-complete-page.html](example/our-smallest-complete-page.html) | Exact slide 17 example |
| [example/our-event-page-so-far.html](example/our-event-page-so-far.html) | Exact slide 25 example |

Open the three HTML examples in a browser before teaching and keep their source available in a text editor. The examples use browser defaults, without CSS or JavaScript. The local pages and image work offline; following the DLSU link requires internet access.

The two intermediate examples match the slides. In the second example, `<!-- Page metadata goes here. -->` abbreviates the metadata already taught; restore UTF-8 metadata and a title when building the final page. Comments are placeholders and do not display in the browser. Slide 30 also uses `<!-- Other content. -->` for the earlier introduction and lists.

## Presentation design

The existing deck uses DLSU green (`#006747`), dark green text (`#17312B`), pale code panels (`#F2F6F4`), and the supplied logo. The cover reads “HTML Foundations” with the instructor name and no subtitle; the final slide repeats the cover. Code frames use fragile Beamer frames and monospaced listings. The edit/save/browser workflow is a cycle diagram.

## Pacing

Allow roughly 3 minutes for slides 1–4, 3 minutes for slides 5–8, 3 minutes for slides 9–12, 5 minutes for slides 13–17, 8 minutes for slides 18–25, 6 minutes for slides 26–30, and 2 minutes for slides 31–33. These are rehearsal targets totaling 30 minutes; the recap and closing slides changed the original schedule. Some source notes retain earlier timestamps, so use this sequence for current pacing.

## Slide-by-slide guide

### Slide 01 — HTML Foundations

Repeat the branded cover with the instructor name, institute, and logo.

**Instructor notes:** Introduce the fictional meetup and the goal of creating a readable, working page. No previous coding experience is needed. Transition: What will you be able to explain and build?

### Slide 02 — Today's learning targets

Read HTML markup; recognize document structure; choose elements for content; save and preview a web page.

**Instructor notes:** Set expectations: understand the building blocks now, reproduce the example afterward. The goal is a small working page, not mastery of every HTML tag. Transition: What information would a visitor need?

### Slide 03 — A student organization needs your help

**Teaching points:** Visitors need the event name, purpose, schedule, preparation list, image, and a useful link.

**Instructor notes:** All event details are illustrative, not an official DLSU announcement. Ask which detail students would look for first; take one brief answer. Transition: We can organize that announcement for the web.

### Slide 04 — Our destination: a readable event page

Use the DEMO cue to show `example/index.html` in the browser.

**Instructor notes:** Point to each content role without naming every tag yet. The student version will use their own local image. Transition: First, what is HTML?

### Slide 05 — HTML gives content structure

**Teaching points:** HTML means HyperText Markup Language. Markup identifies the roles of content. HTML is a markup language.

```html
<h1>Campus Web Development Meetup</h1>
```

**Instructor notes:** Read this as ``this text is the page's main heading.'' The browser displays the text using its default heading presentation, not the angle-bracket tags. Transition: Where do appearance and interactions fit?

### Slide 06 — HTML, CSS, and JavaScript

**Teaching points:** HTML supplies structure and meaning; CSS controls presentation; JavaScript adds programmed behavior.

**Instructor notes:** A page can display content, images, and working links without custom CSS or JavaScript. Do not introduce their syntax. Transition: Why do some tutorials call it HTML5?

### Slide 07 — HTML vs HTML5: why the name?

**Instructor notes:** HTML and HTML5 are not separate competing languages. The table compares older HTML 4.01 with the changes associated with HTML5. HTML5 expanded semantic structure and native media support while retaining basic markup. Earlier HTML could still display multimedia through other mechanisms. The current WHATWG specification is the HTML Living Standard, maintained continuously rather than as a frozen numbered release. The short doctype requests standards-mode rendering; it does not select a frozen version of HTML5. The semantic and media tags are examples for context only, not additional topics to master today. We will learn modern HTML foundations. Transition: Why learn these foundations before using a framework?

### Slide 08 — Why learn HTML before frameworks?

**Instructor notes:** Frameworks are useful tools built on web fundamentals. Bootstrap provides styling and components, but developers still choose appropriate HTML and supply accessible content. Mention the five benefits briefly; do not introduce framework syntax. Transition: Let's inspect the smallest HTML building block.

### Slide 09 — Anatomy of an element

**Teaching points:** An element usually combines an opening tag, content, and a closing tag. A tag is part of an element.

```html
<p>Learn the basics together.</p>
```

**Instructor notes:** Label <p>, the text, and </p> separately. The slash marks the closing tag. The complete expression is the paragraph element. Transition: What happens when we pair tags incorrectly?

### Slide 10 — Pair tags clearly

**Teaching points:** A common mistake is using different tag names for the opening and closing tags. Be careful: some tags, such as img and meta, do not need an end tag.

```html
<!-- Incorrect pair -->
<h1>Campus Web Development Meetup</p>

<!-- Correct pair -->
<h1>Campus Web Development Meetup</h1>
```

**Instructor notes:** Explain that the gray labels are comments for the slide and are not displayed by the browser. Browsers may recover from mistakes, so visible output alone does not prove correct markup. Do not teach comments as a separate topic. Transition: Elements can also contain other elements.

### Slide 11 — Nest elements inside one another

**Teaching points:** Close the inner element before the outer one. Indentation makes containment easier to read.

```html
<p>A meetup for <strong>beginner web developers</strong>.</p>
```

**Instructor notes:** Trace paragraph $→$ important phrase $→$ close phrase $→$ close paragraph. Explain only the containment now; discuss the meaning of strong later in the text-content discussion. Indentation supports readability; it does not define HTML nesting. Transition: Let us start building the page.

### Slide 12 — From concepts to our first page

Use the “LET'S START DEVELOPING” cue to begin constructing the document.

**Instructor notes:** We understand tags and nesting. Now switch to building the campus event page step by step. Students observe during the discussion and code independently afterward. Transition: Begin with the doctype and root element.

### Slide 13 — Declare the document and its language

**Teaching points:** The doctype declares modern HTML. The html element wraps the document. lang="en" identifies English for tools such as screen readers.

```html
<!DOCTYPE html>
<html lang="en">
</html>
```

**Instructor notes:** The doctype is a declaration, not a visible content element or a paired tag. Treat lang as the document language setting for now; attribute syntax follows before links. This skeleton is intentionally incomplete until the complete-page example. Transition: The document separates information about the page from visible content.

### Slide 14 — The head describes the page

**Teaching points:** head holds document metadata. UTF-8 declares the character encoding; save the file as UTF-8 too.

```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
  </head>
  <!-- Body content will go here. -->
</html>
```

**Instructor notes:** Place this inside html. Explain that meta is a void element and needs no closing tag. Metadata is not the visible event announcement. Transition: One piece of metadata gives the browser tab a name.

### Slide 15 — Title names the browser tab

**Teaching points:** Put title inside head. The tab title and visible page heading serve different roles.

```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Campus Web Development Meetup</title>
  </head>
  <!-- Body content will go here. -->
</html>
```

**Instructor notes:** Show the prepared browser tab. The text will also appear in the body as an h1, but neither element replaces the other. Transition: Where do visitors see the actual announcement?

### Slide 16 — Body holds the visible content

**Teaching points:** body follows head, inside html. Visible headings, paragraphs, lists, links, and images go here.

```html
<html lang="en">
  <head>
    <!-- Page metadata goes here. -->
  </head>
  <body>
    <h1>Campus Web Development Meetup</h1>
  </body>
</html>
```

**Instructor notes:** Contrast this heading with the tab title. The other event content will be inserted below the heading. Transition: Put the pieces together.

### Slide 17 — Our smallest complete page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Campus Web Development Meetup</title>
</head>
<body>
  <h1>Campus Web Development Meetup</h1>
</body>
</html>
```

**Instructor notes:** Trace the complete structure once. Expected output: a tab title and one visible main heading. Keep the code large enough to read; use the full slide for the example. Transition: Our page needs more useful information.

### Slide 18 — Headings organize the announcement

**Teaching points:** Use one main h1 in this page, then h2 for sections. HTML offers h1 through h6; choose levels for hierarchy rather than visual size.

```html
<h1>Campus Web Development Meetup</h1>
<h2>About the meetup</h2>
```

**Instructor notes:** Explain the page-title/section relationship. We only need levels 1 and 2 for this small document. Transition: Add the information beneath each heading.

### Slide 19 — Paragraphs explain the event

**Teaching points:** A paragraph groups related prose. Source-code line breaks and extra spaces do not normally produce matching visual spacing.

```html
<p>A meetup for beginner web developers.</p>
<p>Schedule: Friday, 3:00 PM.</p>
```

**Instructor notes:** These become separate paragraphs. Use paragraph elements rather than repeated blank lines in the editor. The first paragraph receives emphasis in the next slide. Transition: Some words deserve meaningful emphasis.

### Slide 20 — Mark importance and emphasis

**Teaching points:** strong marks importance; em marks stress emphasis. Browsers usually show bold and italic respectively, but the elements communicate meaning.

```html
<p>A meetup for <strong>beginner web developers</strong>.</p>
<p><em>No prior HTML experience is required.</em></p>
```

**Instructor notes:** Link back to nesting: the paragraph contains another element. Avoid presenting these as general-purpose styling tools. Transition: Our event introduction now has structure and meaning.

### Slide 21 — Preview the event introduction

**Teaching points:** Combine familiar elements into a readable introduction.

```html
<h2>About the meetup</h2>
<p>A meetup for <strong>beginner web developers</strong>.</p>
<p><em>No prior HTML experience is required.</em></p>
<p>Schedule: Friday, 3:00 PM.</p>
```

**Instructor notes:** Show the matching browser section. Ask which element is the section heading; answer h2. This is a body excerpt, not a second complete document. Transition: Visitors also need a preparation checklist and an agenda.

### Slide 22 — Unordered lists group items

**Teaching points:** ul represents a list whose order is not significant. Each item belongs in li.

```html
<h2>Things to bring</h2>
<ul>
  <li>Laptop</li>
  <li>Notebook</li>
</ul>
```

**Instructor notes:** Expected output: a section heading and two bullet items. The bullets come from default browser presentation. Transition: The agenda has a sequence, so it needs a different list.

### Slide 23 — Ordered lists show sequence

**Teaching points:** ol represents an ordered list. It uses the same li elements; the browser normally numbers them.

```html
<h2>Agenda</h2>
<ol>
  <li>Meet the group</li>
  <li>Explore HTML</li>
  <li>Build a page</li>
</ol>
```

**Instructor notes:** Contrast ``what to bring'' with ``what happens first, next, last.'' Students do not need to type numbers into the item text. Transition: Check that each item belongs inside its list.

### Slide 24 — Put list items inside their list

**Teaching points:** Nest li elements inside ul or ol. Close each item before starting the next in our examples.

```html
<ul>
  <li>Laptop</li>
  <li>Notebook</li>
</ul>
```

**Instructor notes:** Trace the outer list and its two children. Ask ``Which element changes for a numbered agenda?'' Answer: replace ul with ol. This lesson does not introduce multilevel lists. Transition: Some elements need extra information.

### Slide 25 — Our event page so far

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Page metadata goes here. -->
</head>
<body>
  <h1>Campus Web Development Meetup</h1>
  <h2>About the meetup</h2>
  <p>A meetup for <strong>beginner web developers</strong>.</p>
  <p><em>No prior HTML experience is required.</em></p>
  <p>Schedule: Friday, 3:00 PM.</p>
  <h2>Things to bring</h2>
  <ul>
    <li>Laptop</li><li>Notebook</li>
  </ul>
  <h2>Agenda</h2>
  <ol>
    <li>Meet the group</li><li>Explore HTML</li><li>Build a page</li>
  </ol>
</body>
</html>
```

**Instructor notes:** Recap the combined output of slides 18–24: the main heading, introduction, emphasis, schedule, preparation list, and ordered agenda. The metadata comment stands in for the head content already taught. Each list item is a separate element even when shown on the same source line. Transition: Some elements need extra information, supplied through attributes.

### Slide 26 — Attributes supply details: links connect pages

**Teaching points:** Attributes appear in the opening tag. In today's examples they use name="value". Use lowercase names and quote values consistently.

```html
<a href="https://www.dlsu.edu.ph/">Visit the DLSU website</a>
```

**Instructor notes:** Label the element name, attribute name, URL value, and visible link text. This example uses an absolute URL and opens in the same tab by default. It is a campus information link, not an event registration form. Do not imply that every HTML attribute requires a value; this lesson uses valued attributes. Transition: Make the destination clear before someone clicks.

### Slide 27 — Write useful link text

**Teaching points:** Descriptive link text helps readers and assistive technology users understand the destination. Keep the URL inside href.

```html
<h2>Campus information</h2>
<p>
  <a href="https://www.dlsu.edu.ph/">Visit the DLSU website</a>
</p>
```

**Instructor notes:** Compare the phrase verbally with the vague ``click here.'' Read the section as a visitor would. Internet access is needed to load the external site, but not to display the local HTML page. Transition: Finally, add an image that supports the announcement.

### Slide 28 — Images use a source path

**Teaching points:** img embeds an image. src locates the file. img is void: it has no closing tag.

```html
<img src="meetup.jpg"
     alt="Students collaborating on a web page">
```

**Instructor notes:** Put meetup.jpg beside index.html. This is a relative file path; it must match the real filename and extension. The alternative text is explained next. Use a suitably sized image in the prepared preview; no sizing attributes are introduced here. Transition: What should this image communicate when it cannot be seen?

### Slide 29 — Alternative text describes the image's purpose

**Teaching points:** alt supplies a text alternative for informative images, including for screen readers. Describe useful content rather than the filename.

```html
<h2>Meetup snapshot</h2>
<img src="meetup.jpg"
     alt="Students collaborating on a web page">
```

**Instructor notes:** The description must match the actual photo. If a student uses a different image, they must change the alt text. Purely decorative images use empty alt=""; today's example is informative. Broken images may expose the alternative text, but alt is not a substitute for fixing a path. Transition: We now have all the parts of our announcement.

### Slide 30 — Last part of our event page

```html
<!DOCTYPE html>
<html lang="en">
<head><!-- Page metadata goes here. --></head>
<body>
  <!-- Other content. -->
  <h2>Campus information</h2>
  <p>
    <a href="https://www.dlsu.edu.ph/">Visit the DLSU website</a>
  </p>
  <h2>Meetup snapshot</h2>
  <img src="meetup.jpg"
       alt="Students collaborating on a web page">
</body>
</html>
```

**Instructor notes:** Recap the link and image examples together inside the body. The comments stand in for metadata and earlier event content. Identify href as the link destination, src as the image path, and alt as its text alternative. Keep meetup.jpg beside index.html and match the alternative text to the actual image. Transition: How do students run this example after the discussion?

### Slide 31 — Edit, save, open, refresh

**Diagram:** Edit → Save → Open / refresh browser → back to Edit. Save as `index.html`; open once and refresh after subsequent saves.

**Instructor notes:** Demonstrate using prepared windows. Warn about accidentally saving index.html.txt. Keep the image beside the file. Full instructions are in Appendix B. Transition: If the result surprises you, check a few simple things first.

### Slide 32 — Three common mistakes

**Teaching points:** Check tag pairs, image paths, and the difference between tab title and visible heading.

**Instructor notes:** Deliver these as three fast checks. Remind students that a browser can display malformed HTML without a clear error message. Transition: Return to the cover to close the discussion.

### Slide 33 — HTML Foundations — closing cover

Repeat the branded cover with the instructor name, institute, and logo.

## Appendix A — Complete HTML example

The runnable source is [example/index.html](example/index.html), with the supplied [meetup.jpg](example/meetup.jpg) beside it.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Campus Web Development Meetup</title>
</head>
<body>
  <h1>Campus Web Development Meetup</h1>

  <h2>About the meetup</h2>
  <p>A meetup for <strong>beginner web developers</strong>.</p>
  <p><em>No prior HTML experience is required.</em></p>
  <p>Schedule: Friday, 3:00 PM.</p>

  <h2>Things to bring</h2>
  <ul>
    <li>Laptop</li>
    <li>Notebook</li>
  </ul>

  <h2>Agenda</h2>
  <ol>
    <li>Meet the group</li>
    <li>Explore HTML</li>
    <li>Build a page</li>
  </ol>

  <h2>Campus information</h2>
  <p>
    <a href="https://www.dlsu.edu.ph/">Visit the DLSU website</a>
  </p>

  <h2>Meetup snapshot</h2>
  <img src="meetup.jpg"
       alt="Students collaborating on a web page">
</body>
</html>
```

Expected output: a named browser tab, a main heading, five section headings, descriptive paragraphs, two preparation bullets, three agenda steps, a campus link, and a local image.

## Appendix B — Setup and image instructions

### Instructor preparation before class

1. Prepare the Appendix A example in a plain-text editor and a browser before presenting. Use a local copy to avoid relying on internet access for the preview.
2. Use the supplied `example/meetup.jpg`, or choose another suitable image and update its alternative text. A roughly 480-pixel-wide copy keeps the unstyled image manageable in the demo.
3. Save that image as `meetup.jpg` beside `index.html`. Confirm that its actual format is JPEG; renaming a PNG extension does not convert it.
4. Confirm the image displays and the campus hyperlink is correctly formed. Opening the external destination requires internet access.
5. Prepare a source view and a browser preview for quick switching. Rehearse within the listed timings.

### Student execution after the discussion

1. Create a folder named `campus-meetup`.
2. Open a plain-text editor, paste or type Appendix A, and save as `index.html` with UTF-8 encoding. In Windows Notepad, select “All files” if necessary so it does not append `.txt`.
3. Put the supplied image in the same folder. If using a different real image filename or format, change `src` to match and write appropriate `alt` text.
4. Open `index.html` in a web browser by double-clicking it or using the browser's Open File command.
5. Make a change in the editor, save it, then refresh the browser.

```text
campus-meetup/
  index.html
  meetup.jpg
```

If an image is missing, check the folder, filename, extension, and capitalization. If the page displays source text, check that the file really ends in `.html` and is opened in a browser. If edits are absent, save and refresh the correct file.

## Appendix C — Independent exercise

**Suggested duration:** 15–20 minutes after the discussion; adjust separately from the presentation schedule.

Reproduce the sample, then turn it into an announcement for your own fictional campus activity:

1. Update `title` and `h1` to your event name.
2. Rewrite the description and schedule. Keep one meaningful `strong` phrase and one `em` phrase.
3. Include at least two preparation items in a `ul` and three sequenced agenda items in an `ol`.
4. Retain the campus information link or replace it with a relevant, valid destination and descriptive link text.
5. Add a local image and alternative text that matches its content and purpose.
6. Save, open, and inspect the complete page. Explain the difference between an element and an attribute to a classmate.

**Expected submission:** `index.html` and the image it references, together in one folder. No CSS or JavaScript is required.

**Answer guidance:** Appendix A is the structural answer. Personalized wording, relevant URLs, and image choices may vary. Evaluate correct structure and meaningful content rather than matching exact text or browser styling.

## Appendix D — Completion checklist

- [ ] The file is named `index.html` and opens in a browser.
- [ ] It includes a doctype, `html lang="en"`, `head`, UTF-8 metadata, `title`, and `body`.
- [ ] The tab title and visible main heading both identify the event.
- [ ] It uses one main heading and logical section headings.
- [ ] Paragraphs contain the description and schedule, with meaningful `strong` and `em` examples.
- [ ] The preparation list uses `ul` and `li`; the agenda uses `ol` and `li`.
- [ ] The hyperlink has a valid `href` and descriptive visible text.
- [ ] The image displays, its `src` matches the local file, and its `alt` describes the actual image.
- [ ] Tags are correctly paired and nested; void elements have no closing tags.
- [ ] Saving a changed heading and refreshing shows the new text.

## Appendix E — Reference map and deferred topics

| Lesson content | W3Schools reference |
|---|---|
| HTML purpose and document structure | [Introduction](https://www.w3schools.com/html/html_intro.asp), [Basic examples](https://www.w3schools.com/html/html_basic.asp) |
| Editor and local preview workflow | [Editors](https://www.w3schools.com/html/html_editors.asp) |
| Tags, nesting, and void elements | [Elements](https://www.w3schools.com/html/html_elements.asp) |
| Attribute syntax, language, encoding, and title | [Attributes](https://www.w3schools.com/html/html_attributes.asp), [Head](https://www.w3schools.com/html/html_head.asp) |
| Heading hierarchy and prose | [Headings](https://www.w3schools.com/html/html_headings.asp), [Paragraphs](https://www.w3schools.com/html/html_paragraphs.asp) |
| Importance and emphasis | [Formatting](https://www.w3schools.com/html/html_formatting.asp) |
| Preparation and agenda lists | [Lists](https://www.w3schools.com/html/html_lists.asp) |
| Destinations and link text | [Links](https://www.w3schools.com/html/html_links.asp) |
| Local image paths and alternatives | [Images](https://www.w3schools.com/html/html_images.asp) |

Combine related chapters rather than covering the tutorial sequentially. Only the beginner subset described in this outline belongs in the timed lesson. Defer CSS/styles/colors, advanced formatting and quotations, tables, forms, layout systems, multimedia, scripting, and publishing to later classes.

## Maintenance checks

- Keep the 33 slide entries aligned with the actual frame order.
- Keep Appendix A synchronized with `example/index.html`.
- Keep intermediate examples synchronized with slides 17 and 25.
- Preserve both placeholder comments on slide 30.
- Keep `meetup.jpg` beside the final HTML file.
- After changing the lecture source, compile `lecture/html-foundations.tex` and check code readability, overflow, logo proportions, and footer clearance.
