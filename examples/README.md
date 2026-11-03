# HTML examples: read, change, refresh

HTML (HyperText Markup Language) describes the structure of a webpage. A browser
reads elements and displays their content. Most elements have an opening tag,
content, and a closing tag; void elements such as `img` have no closing tag.

Reference: [W3Schools HTML Introduction](https://www.w3schools.com/html/html_intro.asp).
The examples and discussions here use the fictional student portfolio from this
lesson. Semantic regions, lists, links, and images extend the introduction into
a complete page.

Open each HTML file directly in a browser and in a text editor. Read its visible
**Quick discussion**, make the **Try it** change, save, and refresh. Each example
is independent and works offline, with no CSS, JavaScript, or installation.

| Example | Short discussion |
| --- | --- |
| [Document structure](independent/01_document_structure.html) | Trace the doctype, root, head, title, and body. Compare the browser tab title with the visible heading, then identify an element's tags and content. |
| [Headings and paragraphs](independent/02_headings_paragraphs.html) | Use heading levels to describe the outline and paragraphs to group text. Nest importance and emphasis inside a paragraph. |
| [Lists](independent/03_lists.html) | Compare unordered skills with ordered practice steps. Both lists contain `li` elements; choose the list type based on whether order matters. |
| [Links and anchors](independent/04_links.html) | Follow a link's `href` to the matching unique `id`. Compare the destination attribute with the visible link text. |
| [Images](independent/05_images.html) | Trace a local `src` path, explain the image's `alt` text, and identify dimensions. An image is a void element. |
| [Semantic structure](independent/06_semantic_structure.html) | Identify the roles of header, navigation, main content, sections, articles, and footer. These roles describe meaning rather than visual layout. |

## Put the examples together

- [Portfolio starter](portfolio-starter/index.html): a complete document skeleton
  with placeholder body content. Identify its metadata before replacing the body.
- [Prepared demo body](portfolio-demo-body.txt): the markup to paste **between**
  the starter's body tags. It is a fragment, not a second complete document.
- [Completed portfolio](portfolio-complete/index.html): combines headings,
  paragraphs, a local image, lists, section links, and semantic regions. Follow
  Projects and explain why its destination matches the section ID.

Keep each portfolio's `assets` folder beside its HTML file when copying it.
For the next practice task, use the separate [assignment instructions](../exercises/README.md).
