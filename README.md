# HTML Foundations

Learn HTML by building a page for a fictional **Campus Web Development Meetup**.

Instructor: **Manolito Octaviano Jr.**  
De La Salle University Manila · College of Computer Studies

## What you will learn

- Read opening tags, content, closing tags, and attributes.
- Organize a document with `html`, `head`, and `body`.
- Use headings, paragraphs, emphasis, and lists.
- Add descriptive links and images with alternative text.
- Edit, save, and preview a page in a browser.

No previous HTML experience is required. You need a text editor and a web browser.

## Start here

1. Download this repository using **Code → Download ZIP**, then extract it, or clone it with Git.
2. Open `example/index.html` in your browser to see the finished page.
3. Open the same file in a text editor to inspect its HTML.
4. Change some text, save the file, and refresh your browser.

**Repeat:** Edit → Save → Open/refresh browser → Edit.

The page and its image work locally. Internet access is needed when following the external DLSU link. No installation, web server, CSS, or JavaScript is needed to run these examples.

## Build it in stages

| Example | What to look for |
|---|---|
| [Our smallest complete page](example/our-smallest-complete-page.html) | A document title and one visible main heading; matches slide 17. |
| [Our event page so far](example/our-event-page-so-far.html) | Headings, paragraphs, `strong`, `em`, a preparation list, and an ordered agenda; matches slide 25. |
| [Complete event page](example/index.html) | All the earlier content plus a descriptive campus link and a local image. |

The intermediate examples match the slide snippets. `<!-- Page metadata goes here. -->` is a comment standing in for metadata already introduced. In your complete document, include `<meta charset="UTF-8">` and a meaningful `<title>` inside `<head>`, as shown in `example/index.html`. The final slide recap also uses `<!-- Other content. -->` to abbreviate the earlier body content.

## Make your own announcement

Use the complete example as your starting point:

1. Change both `<title>` and `<h1>` to your own event name.
2. Rewrite the description and schedule. Use `strong` for importance and `em` for emphasis.
3. Add at least two things to bring in a `ul` and three agenda steps in an `ol`.
4. Keep a useful link with descriptive visible text and a valid `href`.
5. Choose a local image. Update `src` to its filename and `alt` to describe its content and purpose.
6. Save, refresh, and check the result.

Keep your HTML and its image together:

```text
my-event/
  index.html
  meetup.jpg
```

If you keep the provided filename, keep `meetup.jpg` beside `index.html`. If your image has a different name or format, update `src` accordingly. Save HTML as UTF-8 and ensure the filename is `index.html`, not `index.html.txt`.

## Check your work

- Your file opens in a browser and displays your event name.
- The browser tab title and visible heading both identify the event.
- Headings form a clear hierarchy, and list items are inside their lists.
- The link opens the intended destination.
- The image displays and has useful alternative text.
- Paired tags match and nest correctly. Void elements such as `img` and `meta` have no closing tag.
- Saving a change and refreshing shows the new content.

Browser defaults control the appearance of these examples. This lesson focuses on structure and meaning.

## Lecture materials

- [Lecture source](lecture/html-foundations.tex): 33 slides, including the opening and closing covers.
- [Teaching guide](html-demo-teaching-outline.md): slide sequence, code examples, preparation instructions, and optional practice.
- `lecture/dlsu-beamer.sty` and `lecture/DLSU-CCS-Logo-Clear.png`: resources needed to compile the lecture source. Keep them beside the `.tex` file.
- `lecture/dlsu_template_example.tex`: supporting template example.

The fictional meetup is a learning example, not an official event announcement.
