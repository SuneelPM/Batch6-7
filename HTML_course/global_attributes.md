# HTML Global Attributes — Detailed Explanation

Global attributes are attributes that can be applied to **any HTML element**, regardless of what tag it is. They provide universal functionality across the entire document.

---

## 1. `id`

The `id` attribute assigns a **unique identifier** to an element. No two elements on the same page should share the same `id`.

```html
<div id="main-header">Welcome</div>
```

**Use cases:**
- CSS targeting: `#main-header { color: red; }`
- JavaScript selection: `document.getElementById("main-header")`
- Fragment linking: `<a href="#main-header">Go to header</a>` — clicking this scrolls the page to that element
- ARIA references: `aria-labelledby="main-header"`

**Rules:**
- Must be unique per page
- Cannot contain spaces
- Case-sensitive (`Header` ≠ `header`)

---

## 2. `class`

The `class` attribute assigns one or more **reusable class names** to an element. Multiple elements can share the same class, and one element can have multiple classes.

```html
<p class="text-large bold highlight">Hello World</p>
```

**Use cases:**
- CSS styling: `.highlight { background: yellow; }`
- JavaScript selection: `document.querySelectorAll(".highlight")`
- Used heavily by CSS frameworks like Tailwind and Bootstrap

**Key difference from `id`:**

| | `id` | `class` |
|---|---|---|
| Uniqueness | Must be unique | Can be reused |
| Count per element | Only one | Multiple allowed |
| CSS specificity | Higher | Lower |

---

## 3. `style`

The `style` attribute applies **inline CSS** directly to an element, overriding external and internal stylesheets.

```html
<p style="color: blue; font-size: 18px; margin-top: 10px;">Styled paragraph</p>
```

**When to use it:**
- Quick prototyping or debugging
- Dynamically applying styles via JavaScript: `element.style.color = "red"`
- Situations where CSS classes aren't practical (e.g., email templates)

**Why to avoid overusing it:**
- Hard to maintain and override (high specificity)
- Mixes presentation with structure
- Can't use pseudo-classes (`:hover`, `:focus`) inline
- Not reusable across elements

---

## 4. `title`

The `title` attribute provides **advisory/supplementary information** about an element. It appears as a **tooltip** when the user hovers over the element.

```html
<p title="This is additional context">Hover over me</p>
<abbr title="HyperText Markup Language">HTML</abbr>
<a href="docs.pdf" title="Opens a PDF file">Documentation</a>
```

**Common uses:**
- Expanding abbreviations with `<abbr>`
- Giving extra context to links
- Describing icon buttons

**Accessibility caveat:**
The `title` tooltip is not reliably accessible to keyboard users or screen readers on all devices. Don't rely on it as the only source of important information — use visible text or `aria-label` instead.

---

## 5. `lang`

The `lang` attribute declares the **language of the element's content** using a BCP 47 language tag.

```html
<!-- Set for the entire document -->
<html lang="en">

<!-- Override for a specific section -->
<p lang="fr">Bonjour, comment ça va?</p>
<p lang="ar" dir="rtl">مرحبا بالعالم</p>
```

**Common language codes:**

| Code | Language |
|------|----------|
| `en` | English |
| `fr` | French |
| `de` | German |
| `es` | Spanish |
| `ar` | Arabic |
| `hi` | Hindi |
| `zh` | Chinese |
| `ja` | Japanese |

**Why it matters:**
- Screen readers use it to select the correct voice/pronunciation engine
- Browsers apply correct hyphenation and typography rules
- Search engines use it for language-specific indexing
- CSS `hyphens: auto` depends on it to work correctly

---

## 6. `dir`

The `dir` attribute specifies the **text direction** of an element's content.

```html
<p dir="ltr">Left to right — English, default</p>
<p dir="rtl">Right to left — Arabic, Hebrew</p>
<p dir="auto">Let the browser figure it out</p>
```

**Values:**
- `ltr` — Left to Right (default for most languages)
- `rtl` — Right to Left (Arabic, Hebrew, Persian, Urdu)
- `auto` — Browser detects direction based on the content

**Practical use:**
```html
<!-- A chat app message from an Arabic user -->
<div dir="auto" lang="ar">مرحبا</div>
```

Using `dir="auto"` is ideal for user-generated content where the language isn't known in advance.

---

## 7. `data-*` Custom Attributes

The `data-*` attributes let you **store custom data** directly on HTML elements without using non-standard attributes or hidden inputs. The `*` can be any name you choose.

```html
<button data-user-id="42" data-role="admin" data-action="delete">
  Delete User
</button>
```

**Accessing in JavaScript:**

```js
const btn = document.querySelector("button");

// Reading
console.log(btn.dataset.userId);   // "42"   (note: kebab-case → camelCase)
console.log(btn.dataset.role);     // "admin"
console.log(btn.dataset.action);   // "delete"

// Writing
btn.dataset.status = "active";     // adds data-status="active"

// Deleting
delete btn.dataset.action;
```

**Accessing in CSS:**

```css
/* Style based on data attribute */
[data-role="admin"] {
  background-color: red;
}

/* Display data value using content */
button::after {
  content: attr(data-action);
}
```

**Real-world use cases:**
- Passing config to JavaScript (e.g., `data-api-url`, `data-timeout`)
- Tracking analytics events (`data-event="click"`, `data-category="nav"`)
- Controlling UI behavior (`data-toggle="modal"`, `data-target="#popup"`)
- Storing state without hidden inputs

**Rules:**
- Must start with `data-`
- Cannot contain uppercase letters in the attribute name
- The value is always a string (parse if you need a number/boolean)

---

## 8. `hidden`

The `hidden` attribute is a **boolean attribute** that hides an element from the page entirely — both visually and from accessibility tools (unlike `visibility: hidden` which just makes it invisible but still occupies space).

```html
<div hidden>This content is not visible or accessible</div>

<!-- Toggle with JavaScript -->
<p id="message" hidden>You have saved successfully!</p>
```

```js
// Show it
document.getElementById("message").hidden = false;

// Hide it again
document.getElementById("message").hidden = true;
```

**Comparison with CSS alternatives:**

| Method | Visible | Takes up space | Screen reader |
|---|---|---|---|
| `hidden` attribute | No | No | Hidden |
| `display: none` | No | No | Hidden |
| `visibility: hidden` | No | **Yes** | Hidden |
| `opacity: 0` | No | **Yes** | **Readable** |

**Important:** CSS `display` can override `hidden`. If a stylesheet sets `display: block` on a `[hidden]` element, it will appear. You can prevent this with:
```css
[hidden] { display: none !important; }
```

---

## 9. `contenteditable`

The `contenteditable` attribute makes an element's content **directly editable by the user** in the browser, like a simple rich-text field.

```html
<div contenteditable="true">
  Click here and start typing to edit this content!
</div>
```

**Values:**
- `"true"` or empty string `""` — editable
- `"false"` — not editable (useful to disable it on a child of an editable parent)
- `"plaintext-only"` — editable but strips HTML formatting

```html
<!-- Parent is editable, child is locked -->
<div contenteditable="true">
  Edit this freely.
  <span contenteditable="false">But not this part.</span>
</div>
```

**Reading content with JavaScript:**
```js
const editor = document.querySelector("[contenteditable]");
console.log(editor.innerText);   // plain text
console.log(editor.innerHTML);   // with HTML tags
```

**Real-world use cases:**
- Lightweight in-page text editors
- Inline editing in CMS tools (like Notion-style editors)
- Custom rich-text editors built with JavaScript (Quill, ProseMirror use it internally)

**Caveat:** It doesn't have form submission support natively — you'd need to manually extract the content and submit it via JavaScript.

---

## 10. `draggable`

The `draggable` attribute specifies whether an element **can be dragged** by the user using the HTML Drag and Drop API.

```html
<div draggable="true">Drag me!</div>
<div draggable="false">I cannot be dragged</div>
```

**Values:**
- `"true"` — element is draggable
- `"false"` — element is not draggable
- Default behavior: images and links are draggable by default; everything else is not

**Working with drag events in JavaScript:**

```html
<div draggable="true" id="card">🃏 Card</div>
<div id="dropzone">Drop here</div>
```

```js
const card = document.getElementById("card");
const dropzone = document.getElementById("dropzone");

card.addEventListener("dragstart", (e) => {
  e.dataTransfer.setData("text/plain", "card");
});

dropzone.addEventListener("dragover", (e) => {
  e.preventDefault(); // Required to allow dropping
});

dropzone.addEventListener("drop", (e) => {
  e.preventDefault();
  const data = e.dataTransfer.getData("text/plain");
  dropzone.textContent = `Dropped: ${data}`;
});
```

**Use cases:**
- Kanban boards (Trello-style)
- File upload zones
- Sortable lists
- Drag-and-drop builders

---

## 11. `spellcheck`

The `spellcheck` attribute controls whether the **browser's spell checker** is enabled on an element's text content.

```html
<!-- Enable spell checking (default on most editable elements) -->
<textarea spellcheck="true"></textarea>

<!-- Disable spell checking -->
<input type="text" spellcheck="false" placeholder="No red squiggly lines here" />

<!-- Useful for code editors -->
<div contenteditable="true" spellcheck="false">
  const foo = "bar";
</div>
```

**Values:**
- `"true"` — spell checking enabled
- `"false"` — spell checking disabled
- Default: browsers typically enable it for `<textarea>` and `contenteditable` elements, and disable it for `<input>` fields (varies by browser)

**When to disable it:**
- Code editors (you don't want `querySelector` underlined in red)
- Technical or domain-specific input fields (e.g., SKU codes, API keys)
- Fields with structured data like addresses or product names

---

## 12. `translate`

The `translate` attribute tells **browser translation tools and services** (like Google Translate) whether the content of an element should be translated.

```html
<!-- Translate this content (default behavior) -->
<p translate="yes">Welcome to our website!</p>

<!-- Do NOT translate this content -->
<p>Our product is called <span translate="no">CloudSync Pro</span></p>
<code translate="no">npm install react</code>
<p translate="no">John Doe</p>
```

**Values:**
- `"yes"` — content should be translated (default)
- `"no"` — content should not be translated

**When to use `translate="no"`:**
- Brand names and product names
- Code snippets and command-line instructions
- Proper nouns (person names, place names)
- Technical terms that must stay in their original form
- Legal or trademarked terms

---

## Quick Reference Summary

| Attribute | Purpose | Example Value |
|---|---|---|
| `id` | Unique element identifier | `"main-nav"` |
| `class` | Reusable style/behavior hooks | `"btn btn-primary"` |
| `style` | Inline CSS | `"color: red"` |
| `title` | Tooltip / advisory info | `"Click to expand"` |
| `lang` | Content language | `"en"`, `"fr"` |
| `dir` | Text direction | `"ltr"`, `"rtl"`, `"auto"` |
| `data-*` | Custom data storage | `data-user-id="5"` |
| `hidden` | Hide element completely | (boolean) |
| `contenteditable` | Make content editable | `"true"`, `"false"` |
| `draggable` | Enable drag behavior | `"true"`, `"false"` |
| `spellcheck` | Browser spell checking | `"true"`, `"false"` |
| `translate` | Translation tool hint | `"yes"`, `"no"` |

Understanding and using global attributes correctly leads to cleaner markup, better accessibility, and more maintainable frontend code.