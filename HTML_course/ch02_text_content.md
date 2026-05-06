# HTML Text & Content — Detailed Explanation

---

## 1. Headings (`h1`–`h6`), Paragraphs, Line Breaks

### Headings — `<h1>` to `<h6>`

Headings define the **hierarchical structure and outline** of your page's content. There are six levels, `<h1>` being the most important and `<h6>` the least.

```html
<h1>The Complete Guide to HTML</h1>
<h2>Text & Content</h2>
<h3>Headings</h3>
<h4>Accessibility Considerations</h4>
<h5>Screen Reader Behaviour</h5>
<h6>Technical Notes</h6>
```

Browsers render them with decreasing font sizes by default, but their real purpose is **semantic structure**, not visual size. Always use CSS to control appearance.

---

#### Heading Hierarchy — The Document Outline

Think of headings like a book's table of contents. They create an **outline** of your page that browsers, screen readers, and search engines use to understand and navigate your content.

```html
<h1>Web Development Guide</h1>         <!-- Page title — only one per page -->

  <h2>Frontend Development</h2>         <!-- Major section -->

    <h3>HTML</h3>                        <!-- Subsection -->
      <h4>Document Structure</h4>        <!-- Sub-subsection -->
      <h4>Semantic Elements</h4>

    <h3>CSS</h3>
      <h4>Selectors</h4>
      <h4>Box Model</h4>

  <h2>Backend Development</h2>

    <h3>Node.js</h3>
    <h3>Python</h3>

  <h2>Databases</h2>
```

---

#### Rules & Best Practices

**One `<h1>` per page.** It represents the main topic of the page — like the title of a book chapter. Having multiple `<h1>` elements confuses the document outline and weakens SEO.

```html
<!-- ✅ Correct — one h1 per page -->
<h1>Introduction to CSS Flexbox</h1>
<h2>What is Flexbox?</h2>
<h2>Core Concepts</h2>
  <h3>Flex Container</h3>
  <h3>Flex Items</h3>

<!-- ❌ Wrong — multiple h1s -->
<h1>Introduction to CSS</h1>
<h1>What is Flexbox?</h1>   <!-- Should be h2 -->
<h1>Core Concepts</h1>       <!-- Should be h2 -->
```

**Never skip heading levels.** Don't jump from `<h2>` directly to `<h4>` — this breaks the document outline and confuses screen reader users.

```html
<!-- ❌ Wrong — skipped h3 -->
<h2>CSS Layouts</h2>
  <h4>Flexbox Properties</h4>

<!-- ✅ Correct — sequential levels -->
<h2>CSS Layouts</h2>
  <h3>Flexbox</h3>
    <h4>Flexbox Properties</h4>
```

**Don't use headings for visual styling.** A heading's level should reflect its position in the document outline, not how big you want the text to be. Use CSS for size.

```html
<!-- ❌ Wrong — using h3 just because you want smaller text -->
<h3 style="font-size: 0.9rem">This isn't really a heading</h3>

<!-- ✅ Correct — use a paragraph with a CSS class -->
<p class="section-label">This isn't really a heading</p>
```

---

#### Headings and Accessibility

Screen reader users commonly navigate pages **by heading alone** — jumping from heading to heading to get an overview of the page content, much like scanning a table of contents. Tools like NVDA, JAWS, and VoiceOver let users press `H` to jump between headings.

A well-structured heading outline lets a blind user instantly understand the page's structure without reading every word. A broken outline forces them to read everything linearly.

```html
<!-- What a screen reader user hears when navigating by headings: -->
<!-- h1: "Web Development Guide" -->
<!-- h2: "Frontend Development" -->
<!-- h3: "HTML" -->
<!-- h4: "Document Structure" -->
<!-- h4: "Semantic Elements" -->
<!-- h3: "CSS" -->
<!-- h2: "Backend Development" -->
```

---

#### Styling Headings with CSS

```css
/* Reset browser defaults and apply your own */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  line-height: 1.2;
  color: #111827;
  margin-top: 0;
}

h1 { font-size: 3rem; }
h2 { font-size: 2rem; border-bottom: 2px solid #e5e7eb; padding-bottom: 0.5rem; }
h3 { font-size: 1.5rem; color: #1d4ed8; }
h4 { font-size: 1.25rem; }
h5 { font-size: 1.1rem; }
h6 { font-size: 1rem; color: #6b7280; }
```

---

### Paragraphs — `<p>`

The `<p>` element defines a **paragraph of text**. It is a block-level element — each paragraph starts on a new line and has default top and bottom margins.

```html
<p>
  HTML is the standard markup language for creating web pages. It describes
  the structure of a page using a series of elements and tags.
</p>

<p>
  Each paragraph is a separate block of text. The browser automatically
  adds space between paragraphs using default margin styles.
</p>
```

---

#### Important Behaviours

**Whitespace is collapsed.** Inside a `<p>`, multiple spaces and line breaks in your source code are collapsed into a single space by the browser. The visual output is not affected by how you format your HTML source.

```html
<!-- These two paragraphs render identically -->
<p>This is a paragraph of text.</p>

<p>
  This     is    a
  paragraph    of
  text.
</p>
```

**Paragraphs cannot be nested.** A `<p>` cannot contain another `<p>`, a `<div>`, or any other block-level element. The browser will auto-close the outer paragraph.

```html
<!-- ❌ Wrong — block element inside paragraph -->
<p>
  Some text
  <div>A div inside a p</div>  <!-- Browser auto-closes <p> before this -->
  More text
</p>

<!-- ✅ Correct — keep only inline content inside <p> -->
<p>Some text <span>with a span</span> and more text.</p>
```

**What can go inside `<p>`:** Only **inline content** — `<span>`, `<strong>`, `<em>`, `<a>`, `<img>`, `<br>`, `<code>`, etc.

---

#### Paragraphs vs Divs

A common mistake is using `<div>` for blocks of text instead of `<p>`. Use `<p>` whenever the content is genuinely a paragraph of prose.

```html
<!-- ❌ Meaningless — div carries no semantic value -->
<div>This is a block of text about our company history.</div>

<!-- ✅ Semantic — clearly communicates it's a paragraph -->
<p>This is a block of text about our company history.</p>
```

---

### Line Breaks — `<br>`

The `<br>` element inserts a **single line break** within a block of text without starting a new paragraph. It is a void element (no closing tag).

```html
<p>
  123 Main Street<br />
  Springfield<br />
  IL 62701<br />
  United States
</p>
```

This renders as:
```
123 Main Street
Springfield
IL 62701
United States
```

---

#### When to Use `<br>` — and When Not To

`<br>` is appropriate for content where line breaks are **part of the content's meaning** — not just for visual spacing.

```html
<!-- ✅ Correct uses -->

<!-- Postal addresses -->
<address>
  Jane Doe<br />
  42 Elm Street<br />
  New York, NY 10001
</address>

<!-- Poetry and song lyrics where line breaks are meaningful -->
<p>
  Roses are red,<br />
  Violets are blue,<br />
  HTML is semantic,<br />
  And so should you.
</p>
```

```html
<!-- ❌ Wrong — using <br> for spacing between sections -->
<h2>Section One</h2>
<p>Content here.</p>
<br />
<br />              <!-- Use CSS margin instead -->
<h2>Section Two</h2>
```

Use **CSS `margin`** for visual spacing between elements — not `<br>` tags. Multiple `<br>` tags in a row is always a sign something should be done with CSS instead.

---

### Horizontal Rule — `<hr>`

The `<hr>` element represents a **thematic break** between content — a shift in topic or scene. It renders as a horizontal line by default but its meaning is semantic, not visual.

```html
<section>
  <h2>Chapter 1: The Beginning</h2>
  <p>The story started on a quiet Tuesday morning...</p>
</section>

<hr />

<section>
  <h2>Chapter 2: The Conflict</h2>
  <p>Three months later, everything had changed...</p>
</section>
```

```css
hr {
  border: none;
  border-top: 2px solid #e5e7eb;
  margin: 2rem 0;
}
```

---

## 2. Inline Elements

Inline elements sit **within a line of text** and only take up as much width as their content. They do not start on a new line.

---

### `<span>`

`<span>` is a **generic inline container** with no semantic meaning. It's the inline equivalent of `<div>` — used purely as a hook for CSS styling or JavaScript targeting.

```html
<p>The price is <span class="price">$29.99</span> per month.</p>
<p>Status: <span class="badge badge--active">Active</span></p>
<p>Your score is <span id="score">0</span> points.</p>
```

```css
.price { color: #16a34a; font-weight: 700; font-size: 1.25rem; }
.badge { padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.8rem; }
.badge--active { background: #dcfce7; color: #15803d; }
```

```js
// Targeting a specific inline portion of text
document.getElementById("score").textContent = 42;
```

Use `<span>` only when no other semantic inline element fits. If the text is important, use `<strong>`. If it's emphasised, use `<em>`.

---

### `<strong>` vs `<b>`

Both render text in **bold** by default, but they carry completely different meanings.

#### `<strong>` — Semantic Importance

`<strong>` indicates that its content has **strong importance, seriousness, or urgency**. Screen readers may announce it with added stress or a different tone.

```html
<p>
  <strong>Warning:</strong> Do not expose this chemical to open flame.
</p>

<p>
  Your session will expire in <strong>5 minutes</strong>. Please save your work.
</p>

<p>
  The deadline is <strong>Friday, February 28th</strong>. No extensions will be granted.
</p>
```

#### `<b>` — Stylistic Bold Without Importance

`<b>` draws **visual attention** to text without implying it's more important than surrounding content. It carries no semantic weight — screen readers treat it the same as plain text.

```html
<!-- Keywords in a product description -->
<p>
  This laptop features a <b>14-inch display</b>, <b>16GB RAM</b>,
  and a <b>512GB SSD</b>.
</p>

<!-- Lead sentence of an article (stylistic convention) -->
<p><b>The conference drew over 5,000 attendees from 40 countries.</b></p>

<!-- Key terms in a glossary that aren't urgent -->
<p>The term <b>semantic HTML</b> refers to using elements for their intended meaning.</p>
```

**Decision guide:**

| Situation | Use |
|---|---|
| Warnings, critical instructions | `<strong>` |
| The most important word in a sentence | `<strong>` |
| Product specs, keywords (stylistic) | `<b>` |
| Lead sentence of an article | `<b>` |
| Just want bold text with no meaning | `<b>` or CSS |

---

### `<em>` vs `<i>`

Similarly, both render in *italic* by default but mean different things.

#### `<em>` — Semantic Stress Emphasis

`<em>` marks **stressed emphasis** — the kind you'd convey with vocal stress when speaking. Screen readers may actually change their tone or pitch when reading `<em>` content. Its meaning changes the interpretation of the sentence.

```html
<!-- The emphasis changes the meaning in each case -->
<p><em>I</em> didn't say she stole the money.</p>   <!-- Someone else said it -->
<p>I didn't <em>say</em> she stole the money.</p>    <!-- I implied it -->
<p>I didn't say <em>she</em> stole the money.</p>    <!-- Someone else did -->
<p>I didn't say she <em>stole</em> the money.</p>    <!-- She borrowed it -->
```

#### `<i>` — Idiomatic Text, Technical Terms, Thoughts

`<i>` marks text that is **set apart from the normal prose** for a reason other than stress — a technical term, a foreign phrase, a thought, or a taxonomic name. It's typographically italic without semantic emphasis.

```html
<!-- Foreign words and phrases -->
<p>The chef described the dish as having a certain <i lang="fr">je ne sais quoi</i>.</p>

<!-- Technical or domain-specific terms (first use) -->
<p>The process of converting sugar to alcohol is called <i>fermentation</i>.</p>

<!-- Taxonomic names (biology convention) -->
<p>The domestic cat, <i>Felis catus</i>, is a carnivorous mammal.</p>

<!-- Internal thoughts in fiction -->
<p>She stared at the locked door. <i>Who could have left it open?</i> she wondered.</p>

<!-- Names of ships, films, books (in running text) -->
<p>The RMS <i>Titanic</i> sank in April 1912.</p>
```

**Decision guide:**

| Situation | Use |
|---|---|
| Vocal stress that changes meaning | `<em>` |
| Foreign words or phrases | `<i>` with `lang` attribute |
| Technical/scientific terms | `<i>` |
| Character's internal thoughts | `<i>` |
| Titles of works (in prose) | `<i>` |
| Just want italic text with no meaning | `<i>` or CSS |

---

### `<mark>`

`<mark>` represents text that is **highlighted** for reference or notation purposes — like text highlighted with a marker pen. It indicates relevance in a particular context, such as search results.

```html
<!-- Search results — highlight the matched query term -->
<p>
  Results for "flexbox":
</p>
<p>
  CSS <mark>flexbox</mark> is a layout model that arranges items in a
  single dimension. The <mark>flexbox</mark> specification was introduced
  in CSS3.
</p>

<!-- Highlighting relevant passage in a document -->
<blockquote>
  The agreement shall remain in effect for a period of <mark>five (5) years</mark>
  from the date of signing, unless terminated earlier.
</blockquote>

<!-- Highlighting the correct answer -->
<ul>
  <li>Paris</li>
  <li><mark>London</mark></li>   <!-- Correct answer -->
  <li>Berlin</li>
</ul>
```

```css
mark {
  background-color: #fef08a;  /* Yellow highlight */
  color: inherit;
  padding: 0.1em 0.2em;
  border-radius: 3px;
}

/* Dark mode friendly */
@media (prefers-color-scheme: dark) {
  mark {
    background-color: #854d0e;
    color: #fef9c3;
  }
}
```

**`<mark>` vs `<strong>`:** `<mark>` is about **relevance in context** (highlighted for the reader's attention right now). `<strong>` is about **inherent importance** (this content is intrinsically critical).

---

### `<small>`

`<small>` represents **side comments, fine print, and legal disclaimers** — secondary information that is subordinate to the main content. By default, text renders one font size smaller than its parent.

```html
<!-- Legal fine print -->
<p>
  Buy one, get one free.
  <small>Offer valid in-store only. Excludes sale items. Ends February 28th.</small>
</p>

<!-- Copyright notice in footer -->
<footer>
  <small>© 2026 Acme Corp. All rights reserved.</small>
</footer>

<!-- Price with tax disclaimer -->
<p>
  <strong>$49.99</strong>
  <small>excl. VAT</small>
</p>

<!-- Attribution under an image -->
<figure>
  <img src="photo.jpg" alt="Mountain landscape at dawn" />
  <figcaption>
    <small>Photo by Jane Doe, licensed under CC BY 4.0</small>
  </figcaption>
</figure>
```

**`<small>` is semantic, not just visual.** Don't use it just to make text smaller — use CSS `font-size` for that. Use `<small>` when the content truly is a side comment or legal fine print.

---

### `<sub>` and `<sup>`

#### `<sub>` — Subscript

Renders text **below the baseline**, smaller than normal. Used in chemical formulas, mathematical notation, and footnotes.

```html
<!-- Chemical formulas -->
<p>Water is composed of two hydrogen atoms and one oxygen atom: H<sub>2</sub>O</p>
<p>Carbon dioxide: CO<sub>2</sub></p>
<p>Sulphuric acid: H<sub>2</sub>SO<sub>4</sub></p>

<!-- Footnote references -->
<p>
  The theory was first proposed in 1905<sub><a href="#fn1">1</a></sub>
  and later expanded upon in 1915<sub><a href="#fn2">2</a></sub>.
</p>

<!-- Mathematical sequences -->
<p>The Fibonacci sequence: a<sub>n</sub> = a<sub>n-1</sub> + a<sub>n-2</sub></p>
```

#### `<sup>` — Superscript

Renders text **above the baseline**, smaller than normal. Used in mathematical exponents, ordinal numbers, and trademark symbols.

```html
<!-- Mathematical exponents -->
<p>The area of a square: A = s<sup>2</sup></p>
<p>Einstein's equation: E = mc<sup>2</sup></p>
<p>2<sup>10</sup> = 1024</p>

<!-- Ordinal numbers -->
<p>She finished in 1<sup>st</sup> place.</p>
<p>The meeting is on the 23<sup>rd</sup> of February.</p>

<!-- Trademark and copyright symbols -->
<p>Product Name<sup>™</sup></p>
<p>Registered Brand<sup>®</sup></p>

<!-- Footnote markers in text -->
<p>
  Climate change is accelerating.<sup><a href="#source1">1</a></sup>
  Scientists warn of irreversible tipping points.<sup><a href="#source2">2</a></sup>
</p>
```

```css
sub, sup {
  font-size: 0.75em;
  line-height: 0; /* Prevents sub/sup from affecting line height */
  position: relative;
  vertical-align: baseline;
}
sup { top: -0.5em; }
sub { bottom: -0.25em; }
```

---

## 3. Preformatted Text

### `<pre>` — Preformatted Text Block

`<pre>` preserves **all whitespace exactly as written** in the HTML source — including spaces, tabs, and line breaks. Unlike normal HTML, whitespace inside `<pre>` is not collapsed.

```html
<pre>
  Name:     Jane Doe
  Role:     Frontend Developer
  Location: New York, NY
  Skills:   HTML, CSS, JavaScript
</pre>
```

This renders exactly as typed — with all the spacing and line breaks intact. Useful for ASCII art, code, or any content where precise spacing is meaningful.

```html
<!-- ASCII art -->
<pre>
   /\_____/\
  /  o   o  \
 ( ==  ^  == )
  )         (
 (           )
( (  )   (  ) )
(__(__)___(__)__)
</pre>
```

```css
pre {
  font-family: 'Courier New', Courier, monospace;
  background: #1e1e1e;
  color: #d4d4d4;
  padding: 1.5rem;
  border-radius: 8px;
  overflow-x: auto;       /* Horizontal scroll for long lines */
  white-space: pre;       /* Default, but explicit for clarity */
  line-height: 1.6;
}
```

---

### `<code>` — Inline Code

`<code>` marks a fragment of **computer code** — a variable name, function call, file name, HTML element, or short code snippet. It's an inline element and renders in a monospace font by default.

```html
<!-- Variable or function names in prose -->
<p>Call the <code>getElementById()</code> method to select a DOM element.</p>

<!-- HTML elements in documentation -->
<p>Use the <code>&lt;nav&gt;</code> element for navigation menus.</p>

<!-- File names and paths -->
<p>Save the file as <code>index.html</code> in your project root.</p>

<!-- CSS properties -->
<p>Set <code>display: flex</code> on the container to enable flexbox.</p>

<!-- Keyboard shortcuts as code (less semantic than <kbd>) -->
<p>Press <code>Ctrl + S</code> to save.</p>

<!-- Values and settings -->
<p>Set the <code>loading</code> attribute to <code>"lazy"</code>.</p>
```

---

#### `<pre>` + `<code>` Together — Code Blocks

For **multi-line code blocks**, always wrap `<code>` inside `<pre>`. This combines preformatted whitespace with the semantic meaning of code.

```html
<pre><code>
function greet(name) {
  if (!name) {
    return "Hello, stranger!";
  }
  return `Hello, ${name}!`;
}

console.log(greet("World")); // Hello, World!
</code></pre>
```

Note: There should be **no whitespace between `<pre>` and `<code>`** or you'll get an extra blank line at the top of your code block.

```html
<!-- ❌ Wrong — extra blank line at top of rendered output -->
<pre>
  <code>
    const x = 1;
  </code>
</pre>

<!-- ✅ Correct — no whitespace between tags -->
<pre><code>const x = 1;</code></pre>
```

Most syntax highlighting libraries like **Prism.js** and **highlight.js** look for `<pre><code>` and use the `class` attribute for the language:

```html
<!-- Prism.js language classes -->
<pre><code class="language-javascript">
const add = (a, b) => a + b;
console.log(add(2, 3)); // 5
</code></pre>

<pre><code class="language-css">
.container {
  display: flex;
  gap: 1rem;
}
</code></pre>

<pre><code class="language-html">
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;meta charset="UTF-8" /&gt;
  &lt;/head&gt;
&lt;/html&gt;
</code></pre>
```

---

### `<kbd>` — Keyboard Input

`<kbd>` represents **keyboard keys, voice commands, or other user input**. Semantically distinct from `<code>` — it marks what the user types or presses, not code that runs.

```html
<!-- Single key -->
<p>Press <kbd>Enter</kbd> to submit the form.</p>
<p>Press <kbd>Escape</kbd> to cancel.</p>

<!-- Key combinations -->
<p>Use <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy text.</p>
<p>Use <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> to open the command palette.</p>

<!-- Nested for key combos — semantically wraps the whole combination -->
<p>
  <kbd>
    <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Delete</kbd>
  </kbd>
  opens the task manager.
</p>

<!-- Menu navigation -->
<p>Go to <kbd>File</kbd> → <kbd>Save As</kbd> → <kbd>PDF</kbd>.</p>
```

```css
kbd {
  display: inline-block;
  padding: 0.15em 0.45em;
  font-family: 'Courier New', monospace;
  font-size: 0.85em;
  background-color: #f3f4f6;
  color: #111827;
  border: 1px solid #d1d5db;
  border-bottom: 3px solid #9ca3af;  /* 3D key effect */
  border-radius: 4px;
  box-shadow: 0 1px 0 rgba(0,0,0,0.2);
  white-space: nowrap;
}
```

This CSS gives the classic **physical keyboard key** appearance you see in documentation sites.

---

### `<samp>` — Sample Output

`<samp>` represents **output from a computer program** — what the terminal, application, or system prints back to the user.

```html
<!-- Terminal output -->
<p>After running the command, you should see:</p>
<samp>Server running on http://localhost:3000</samp>

<!-- Error messages -->
<p>If the file is missing, you will see this error:</p>
<samp>Error: Cannot find module './config.js'</samp>

<!-- Combined with <kbd> for a terminal interaction -->
<pre>
<kbd>npm install</kbd>
<samp>
added 243 packages in 4.521s
found 0 vulnerabilities
</samp>

<kbd>npm run dev</kbd>
<samp>
  VITE v5.0.0  ready in 312 ms
  ➜  Local:   http://localhost:5173/
</samp>
</pre>
```

```css
samp {
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
  background: #0f172a;
  color: #4ade80;     /* Green terminal text */
  padding: 0.75rem 1rem;
  border-radius: 6px;
  display: block;
}
```

---

#### Summary — When to Use Which Code Element

| Element | Represents | Example |
|---|---|---|
| `<code>` | A fragment of computer code | `getElementById()`, `display: flex` |
| `<pre>` | Preformatted text (whitespace preserved) | Code blocks, ASCII art |
| `<kbd>` | User keyboard input or commands | `Ctrl + S`, `Enter` |
| `<samp>` | Output from a program | Error messages, terminal output |

---

## 4. Quotations

### `<blockquote>` — Block Quotation

`<blockquote>` represents a **long quotation from an external source** that is set apart from the surrounding content as its own block. It's used when quoting passages from books, articles, speeches, or other documents.

```html
<!-- Basic blockquote -->
<blockquote>
  <p>
    The only way to do great work is to love what you do. If you haven't
    found it yet, keep looking. Don't settle.
  </p>
</blockquote>

<!-- With a cite attribute pointing to the source URL -->
<blockquote cite="https://www.w3.org/TR/html52/">
  <p>
    The blockquote element represents a section that is quoted from another source.
    Content inside a blockquote must be quoted from another source, whose address,
    if it has one, may be cited in the cite attribute.
  </p>
</blockquote>

<!-- With attribution using <footer> and <cite> -->
<blockquote>
  <p>
    Programs must be written for people to read, and only incidentally
    for machines to execute.
  </p>
  <footer>
    — <cite>Harold Abelson</cite>,
    <cite><em>Structure and Interpretation of Computer Programs</em></cite>
  </footer>
</blockquote>
```

The `cite` attribute on `<blockquote>` is a URL pointing to the original source. It is **not displayed visually** — it's machine-readable metadata for browsers and search engines.

```css
blockquote {
  border-left: 4px solid #3b82f6;
  margin: 1.5rem 0;
  padding: 1rem 1.5rem;
  background: #eff6ff;
  border-radius: 0 8px 8px 0;
  font-style: italic;
  color: #374151;
}

blockquote p {
  margin: 0 0 0.5rem 0;
}

blockquote footer {
  font-style: normal;
  font-size: 0.9rem;
  color: #6b7280;
}
```

---

### `<q>` — Inline Quotation

`<q>` marks a **short, inline quotation** — one that flows within a sentence rather than being set apart as its own block. Browsers automatically add language-appropriate quotation marks around its content.

```html
<p>
  As Einstein once said, <q>Imagination is more important than knowledge.</q>
</p>

<p>
  The documentation states that <q cite="https://html.spec.whatwg.org/">
  authors are encouraged to use the cite attribute</q> when possible.
</p>

<!-- Nested quotes — browsers handle the inner/outer quote marks -->
<p>
  She said, <q>He told me <q>I'll be there by noon</q> but never arrived.</q>
</p>
```

**Default browser rendering:** `"Imagination is more important than knowledge."` — quotation marks are added by the browser, not by you. The marks automatically adapt to the document's language (`lang` attribute):

| Language | Opening | Closing |
|---|---|---|
| English (`en`) | " | " |
| German (`de`) | „ | " |
| French (`fr`) | « | » |
| Japanese (`ja`) | 「 | 」|

```css
/* Override default quotation marks */
q {
  quotes: "\201C" "\201D" "\2018" "\2019"; /* " " ' ' */
}

/* Or use custom styling */
q::before { content: open-quote; color: #3b82f6; font-size: 1.2em; }
q::after  { content: close-quote; color: #3b82f6; font-size: 1.2em; }
```

---

#### `<blockquote>` vs `<q>` — When to Use Which

| | `<blockquote>` | `<q>` |
|---|---|---|
| Length | Long, multi-sentence passages | Short phrases within a sentence |
| Display | Block — on its own line | Inline — within a sentence |
| Quotation marks | Added via CSS manually | Added automatically by browser |
| Best for | Article excerpts, book passages, speeches | Brief attributed phrases |

```html
<!-- Use <q> for a short attribution in prose -->
<p>Darwin wrote that natural selection works by <q>the preservation of favourable variations and the rejection of injurious variations.</q></p>

<!-- Use <blockquote> for a longer passage set apart from prose -->
<blockquote>
  <p>
    It is not the strongest of the species that survives, nor the most intelligent
    that survives. It is the one that is most adaptable to change.
  </p>
  <footer>— <cite>Charles Darwin</cite></footer>
</blockquote>
```

---

### `<cite>` — Citation / Title of a Work

`<cite>` marks the **title of a creative or intellectual work** — a book, article, film, song, painting, or other referenced work. It renders in italic by default.

```html
<!-- Books -->
<p>I just finished reading <cite>The Pragmatic Programmer</cite>.</p>

<!-- Articles -->
<p>This technique was described in <cite>A List Apart</cite>.</p>

<!-- Films -->
<p>The scene is reminiscent of <cite>2001: A Space Odyssey</cite>.</p>

<!-- Songs and albums -->
<p>The album <cite>Kind of Blue</cite> by Miles Davis defined modal jazz.</p>

<!-- Websites -->
<p>According to <cite>MDN Web Docs</cite>, the element is fully supported.</p>

<!-- Inside a blockquote attribution -->
<blockquote>
  <p>Simplicity is the ultimate sophistication.</p>
  <footer>— <cite>Leonardo da Vinci</cite></footer>
</blockquote>
```

**Important distinction:** `<cite>` marks the **title of a work or name of a creator**, not just any citation or source. It is NOT meant to be used as a general "source" label.

```html
<!-- ✅ Correct — title of a work -->
<cite>JavaScript: The Good Parts</cite>

<!-- ❌ Wrong — <cite> is not for labelling sources in general -->
<cite>Source: Wikipedia</cite>   <!-- Use <a> with a regular link instead -->
```

---

### `<abbr>` — Abbreviation

`<abbr>` marks an **abbreviation or acronym** and uses the `title` attribute to provide the full expansion. When users hover over it, a tooltip shows the full form.

```html
<!-- Basic abbreviations -->
<p>
  <abbr title="HyperText Markup Language">HTML</abbr> is the standard
  language for creating web pages.
</p>

<p>
  We use <abbr title="Cascading Style Sheets">CSS</abbr> to style our pages.
</p>

<!-- Acronyms in full sentences -->
<p>
  The <abbr title="World Wide Web Consortium">W3C</abbr> sets the standards
  for the web. Their <abbr title="Application Programming Interface">API</abbr>
  guidelines are published on their website.
</p>

<!-- Technical abbreviations -->
<p>
  The server responded with a
  <abbr title="HyperText Transfer Protocol">HTTP</abbr>
  status code of 200.
</p>

<!-- Medical abbreviations -->
<p>
  The patient was diagnosed with
  <abbr title="Attention Deficit Hyperactivity Disorder">ADHD</abbr>.
</p>

<!-- First use convention — define on first use, use plainly after -->
<p>
  <abbr title="Search Engine Optimisation">SEO</abbr> is critical for
  organic traffic growth. Good SEO practice includes semantic HTML,
  fast page loads, and quality content.
</p>
```

```css
abbr[title] {
  text-decoration: underline dotted;  /* Dotted underline indicates expandable */
  cursor: help;                        /* Help cursor on hover */
  text-decoration-color: #6b7280;
}

abbr[title]:hover::after {
  /* Custom tooltip with CSS (accessibility note: not reliable for all users) */
  content: " (" attr(title) ")";
  font-size: 0.85em;
  color: #6b7280;
}
```

**Accessibility note:** The `title` tooltip only appears on hover and is not accessible to keyboard users or touch device users. For critical expansions, consider writing the full term in the text itself on first use:

```html
<!-- Best practice for accessibility — show full form first -->
<p>
  HyperText Markup Language (<abbr>HTML</abbr>) is the standard language
  for creating web pages.
</p>
```

---

## Quick Reference Summary

| Element | Category | Purpose |
|---|---|---|
| `<h1>`–`<h6>` | Structure | Page headings in hierarchical order |
| `<p>` | Structure | Paragraph of text |
| `<br>` | Structure | Line break within text |
| `<hr>` | Structure | Thematic break between content sections |
| `<span>` | Inline | Generic inline container for CSS/JS hooks |
| `<strong>` | Inline | Important, serious, or urgent text |
| `<b>` | Inline | Stylistically bold text without importance |
| `<em>` | Inline | Stress emphasis that changes sentence meaning |
| `<i>` | Inline | Technical terms, foreign phrases, thoughts |
| `<mark>` | Inline | Highlighted text relevant to current context |
| `<small>` | Inline | Fine print, disclaimers, side comments |
| `<sub>` | Inline | Subscript (H₂O, footnotes) |
| `<sup>` | Inline | Superscript (x², ordinals, trademarks) |
| `<pre>` | Preformatted | Preserves whitespace exactly as written |
| `<code>` | Preformatted | Inline fragment of computer code |
| `<kbd>` | Preformatted | User keyboard input or key presses |
| `<samp>` | Preformatted | Output from a computer program |
| `<blockquote>` | Quotation | Long block quotation from an external source |
| `<q>` | Quotation | Short inline quotation |
| `<cite>` | Quotation | Title of a creative or intellectual work |
| `<abbr>` | Quotation | Abbreviation or acronym with expansion |

Understanding and correctly using these elements gives your HTML genuine meaning — making it more accessible, more readable, and more useful to search engines, screen readers, and other developers.