# HTML Accessibility (a11y) — Detailed Explanation

Accessibility means building web experiences that **everyone can use** — including people with visual, motor, auditory, and cognitive disabilities. An estimated 1 in 6 people globally live with some form of disability. Accessibility is not a feature you add at the end — it's a fundamental quality of good web development.

The primary standard for web accessibility is **WCAG (Web Content Accessibility Guidelines)**, maintained by the W3C. The current version is WCAG 2.2, with three levels: A, AA (the industry standard target), and AAA.

---

## How Assistive Technologies Work

Before diving into techniques, understanding how screen readers interact with HTML is crucial.

Browsers build an **Accessibility Tree** in parallel with the DOM. The accessibility tree contains only the information relevant to assistive technologies — element roles, names, states, and values. Screen readers (NVDA, JAWS, VoiceOver, TalkBack) read from this tree, not the visual layout.

```
DOM Tree:                     Accessibility Tree:
<button class="btn-primary">  Role: button
  <svg>...</svg>              Name: "Submit form"
  Submit form                 State: enabled, not pressed
</button>
```

What you write in HTML directly shapes the accessibility tree. Semantic HTML elements automatically populate it correctly — ARIA lets you fill gaps where HTML alone isn't enough.

---

## 1. ARIA — Accessible Rich Internet Applications

ARIA is a set of attributes you add to HTML to **supplement or override** what the accessibility tree communicates. The first rule of ARIA is:

> **"If you can use a native HTML element or attribute with the semantics and behaviour you require already built in, instead of re-purposing an element and adding ARIA, then do so."**

ARIA never changes visual appearance or behaviour — it only affects what assistive technologies perceive.

---

### `role` — Defining What an Element Is

The `role` attribute tells assistive technologies what **type of UI element** this is — overriding or supplementing the element's native role.

```html
<!-- Native button already has role="button" — no ARIA needed -->
<button type="button">Click me</button>

<!-- A <div> has no role — add one explicitly -->
<div role="button" tabindex="0">Click me</div>

<!-- A <ul> styled as a tab list -->
<ul role="tablist">
  <li role="presentation">
    <a href="#panel1" role="tab" aria-selected="true" aria-controls="panel1">
      Overview
    </a>
  </li>
  <li role="presentation">
    <a href="#panel2" role="tab" aria-selected="false" aria-controls="panel2">
      Details
    </a>
  </li>
</ul>
```

**Common ARIA roles by category:**

**Landmark roles** (covered in depth in Section 2):
```html
<div role="banner">        <!-- Page header -->
<div role="navigation">    <!-- Nav region -->
<div role="main">          <!-- Main content -->
<div role="complementary"> <!-- Aside/sidebar -->
<div role="contentinfo">   <!-- Footer -->
<div role="search">        <!-- Search region -->
<div role="form">          <!-- Form region -->
<div role="region">        <!-- Generic named region -->
```

**Widget roles:**
```html
<div role="button">        <!-- Interactive button -->
<div role="checkbox">      <!-- Checkbox control -->
<div role="dialog">        <!-- Modal dialog -->
<div role="alertdialog">   <!-- Alert dialog requiring response -->
<div role="listbox">       <!-- Selectable list -->
<div role="option">        <!-- Item in a listbox -->
<div role="menu">          <!-- Menu of commands -->
<div role="menuitem">      <!-- Item in a menu -->
<div role="menuitemcheckbox"> <!-- Checkable menu item -->
<div role="menuitemradio"> <!-- Radio menu item -->
<div role="progressbar">   <!-- Progress indicator -->
<div role="slider">        <!-- Range slider -->
<div role="spinbutton">    <!-- Numeric spin control -->
<div role="switch">        <!-- On/off toggle -->
<div role="tab">           <!-- Tab in a tablist -->
<div role="tablist">       <!-- Container for tabs -->
<div role="tabpanel">      <!-- Content panel for a tab -->
<div role="tooltip">       <!-- Contextual tooltip -->
<div role="tree">          <!-- Tree widget -->
<div role="treeitem">      <!-- Item in a tree -->
<div role="combobox">      <!-- Combined input + listbox -->
<div role="grid">          <!-- Interactive data grid -->
<div role="row">           <!-- Row in a grid or treegrid -->
<div role="gridcell">      <!-- Cell in a grid -->
```

**Document structure roles:**
```html
<div role="article">       <!-- Self-contained content -->
<div role="definition">    <!-- Definition of a term -->
<div role="figure">        <!-- Figure content -->
<div role="heading" aria-level="2"> <!-- Heading at level 2 -->
<div role="img">           <!-- Image or image group -->
<div role="list">          <!-- List of items -->
<div role="listitem">      <!-- Item in a list -->
<div role="math">          <!-- Mathematical expression -->
<div role="note">          <!-- Supplementary note -->
<div role="presentation">  <!-- Removes native semantics -->
<div role="none">          <!-- Same as presentation -->
<div role="separator">     <!-- Divider between sections -->
<div role="term">          <!-- Term being defined -->
<div role="toolbar">       <!-- Toolbar container -->
```

**Live region roles:**
```html
<div role="alert">         <!-- Important, time-sensitive message -->
<div role="log">           <!-- Chat log, error log -->
<div role="marquee">       <!-- Non-essential, frequently updating -->
<div role="status">        <!-- Status update, not urgent -->
<div role="timer">         <!-- Countdown or clock -->
```

---

### `aria-label` — Providing an Accessible Name

`aria-label` gives an element an **accessible name** that overrides or replaces its visible text content. Screen readers announce this label instead of (or in addition to) the element's content.

```html
<!-- Icon-only button — no visible text -->
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true" focusable="false">
    <!-- X icon SVG path -->
  </svg>
</button>

<!-- Navigation with multiple <nav> elements -->
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Breadcrumb">...</nav>
<nav aria-label="Table of contents">...</nav>
<nav aria-label="Pagination">...</nav>

<!-- Search input without visible label -->
<form role="search">
  <input
    type="search"
    aria-label="Search articles"
    placeholder="Search..."
  />
  <button type="submit" aria-label="Submit search">
    <svg aria-hidden="true"><!-- search icon --></svg>
  </button>
</form>

<!-- Ambiguous link text — override for screen readers -->
<a href="/blog/html-guide" aria-label="Read more about HTML accessibility guide">
  Read more
</a>

<!-- Social media icon links -->

  href="https://twitter.com/example"
  target="_blank"
  rel="noopener noreferrer"
  aria-label="Follow us on Twitter (opens in new tab)"
>
  <svg aria-hidden="true" focusable="false"><!-- Twitter SVG --></svg>
</a>

<!-- Describe a chart or complex image -->
<div
  role="img"
  aria-label="Bar chart showing revenue growth of 42% between Q1 and Q4 2025"
>
  <!-- Canvas or complex SVG chart -->
</div>
```

---

### `aria-labelledby` — Referencing Another Element as the Label

`aria-labelledby` points to the `id` of **one or more elements** whose text content becomes the accessible name. It's stronger than `aria-label` — it references visible text already on the page, keeping visual and accessible names in sync.

```html
<!-- Dialog labelled by its heading -->
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
>
  <h2 id="dialog-title">Confirm Account Deletion</h2>
  <p>This action cannot be undone. All your data will be permanently removed.</p>
  <button type="button">Cancel</button>
  <button type="button">Delete Account</button>
</div>

<!-- Form section labelled by a heading -->
<section aria-labelledby="billing-heading">
  <h2 id="billing-heading">Billing Information</h2>
  <form>...</form>
</section>

<!-- Input labelled by multiple elements — concatenated -->
<p id="amount-label">Enter amount</p>
<p id="amount-hint">Must be between $10 and $1,000</p>
<input
  type="number"
  aria-labelledby="amount-label amount-hint"
  min="10"
  max="1000"
/>
<!-- Screen reader announces: "Enter amount Must be between $10 and $1,000" -->

<!-- Table labelled by its caption -->
<table aria-labelledby="sales-caption">
  <caption id="sales-caption">Q4 2025 Sales by Region</caption>
  ...
</table>

<!-- Card with a heading that labels the whole card region -->
<article aria-labelledby="card-1-title">
  <h3 id="card-1-title">Getting Started with React</h3>
  <p>A comprehensive guide for beginners...</p>
  <a href="/react-guide">Read article</a>
</article>
```

**`aria-label` vs `aria-labelledby`:**

| | `aria-label` | `aria-labelledby` |
|---|---|---|
| Source of name | String you write inline | Text from existing DOM element |
| Translatable | No (hardcoded string) | Yes (references visible text) |
| Syncs with visible UI | No | Yes — always in sync |
| Multiple sources | No | Yes — space-separated list of IDs |
| When to use | No visible text exists | Visible text already on page |

---

### `aria-describedby` — Adding Supplementary Description

`aria-describedby` points to elements whose text provides **additional description** — announced after the element's name. It supplements rather than replaces the accessible name.

```html
<!-- Password field with format requirements -->
<label for="password">Password</label>
<input
  type="password"
  id="password"
  name="password"
  aria-describedby="password-requirements"
  required
/>
<p id="password-requirements">
  Must be at least 8 characters and include at least one number and one uppercase letter.
</p>
<!-- Screen reader: "Password, required edit text. Must be at least 8 characters..." -->

<!-- Input with both error and hint -->
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  aria-describedby="email-hint email-error"
  aria-invalid="true"
/>
<p id="email-hint">We'll never share your email with anyone.</p>
<p id="email-error" role="alert">Please enter a valid email address.</p>
<!-- Screen reader: "Email address, invalid edit text. We'll never... Please enter a valid..." -->

<!-- Button with tooltip description -->
<button
  type="button"
  aria-describedby="delete-tooltip"
  aria-label="Delete item"
>
  🗑
</button>
<div role="tooltip" id="delete-tooltip">
  Permanently removes the item. This cannot be undone.
</div>

<!-- Form field with character count hint -->
<label for="bio">Bio</label>
<textarea
  id="bio"
  name="bio"
  maxlength="200"
  aria-describedby="bio-count"
></textarea>
<p id="bio-count">
  <span id="chars-remaining">200</span> characters remaining
</p>

<!-- Image with detailed description -->
<figure>
  <img
    src="complex-chart.png"
    alt="Revenue comparison chart Q1-Q4 2025"
    aria-describedby="chart-description"
  />
  <figcaption id="chart-description">
    Q1: $1.2M, Q2: $1.5M (up 25%), Q3: $1.4M (down 6.7%),
    Q4: $1.9M (up 35.7%). Overall annual growth of 58.3%.
  </figcaption>
</figure>
```

**`aria-labelledby` vs `aria-describedby`:**

| | `aria-labelledby` | `aria-describedby` |
|---|---|---|
| Purpose | Primary name/label | Supplementary description |
| When announced | Immediately — before type/state | After name and type/state |
| Required? | Usually | Optional extra detail |
| Analogy | Book title | Book synopsis |

---

### `aria-hidden` — Hiding from the Accessibility Tree

`aria-hidden="true"` **removes an element and all its descendants** from the accessibility tree. Screen readers completely ignore it. The element remains visually visible.

```html
<!-- Decorative icons — screen readers should skip these -->
<button type="button">
  <svg aria-hidden="true" focusable="false">
    <!-- Save icon SVG -->
  </svg>
  Save Document
</button>
<!-- Screen reader: "Save Document, button" — not "Save icon Save Document" -->

<!-- Decorative separator -->
<span aria-hidden="true"> · </span>

<!-- Duplicate content — visually shown but redundant for screen reader -->
<div class="card" aria-label="MacBook Pro — $1,999">
  <img src="macbook.jpg" alt="MacBook Pro laptop" />
  <h3 aria-hidden="true">MacBook Pro</h3>       <!-- Redundant — in aria-label -->
  <p aria-hidden="true">$1,999</p>              <!-- Redundant — in aria-label -->
  <a href="/macbook-pro">View product</a>
</div>

<!-- Decorative background image text -->
<div class="hero">
  <span aria-hidden="true" class="decorative-text">HELLO</span>
  <h1>Welcome to Our Site</h1>
</div>

<!-- Icon font characters (decorative) -->
<i class="fas fa-star" aria-hidden="true"></i>
<span>4.8 out of 5 stars</span>

<!-- Count badge — context already provided elsewhere -->
<button aria-label="Notifications, 3 unread">
  <svg aria-hidden="true"><!-- bell icon --></svg>
  <span aria-hidden="true" class="badge">3</span>
</button>
```

**Critical rules for `aria-hidden`:**

```html
<!-- ❌ NEVER hide focusable elements — keyboard users get trapped -->
<button aria-hidden="true">This is reachable by Tab but invisible to screen readers</button>

<!-- ❌ NEVER hide the focused element -->
<a href="/" aria-hidden="true" id="skip-link">Skip to content</a>

<!-- ✅ If you need to hide a focusable element, also disable it -->
<button aria-hidden="true" tabindex="-1" disabled>Hidden from everyone</button>

<!-- ❌ Never put aria-hidden on <body> or <html> -->
<body aria-hidden="true">  <!-- Hides the entire page from screen readers -->
```

---

### Other Essential ARIA State Attributes

```html
<!-- aria-expanded — collapsible content -->
<button
  type="button"
  aria-expanded="false"
  aria-controls="dropdown-menu"
  id="dropdown-toggle"
>
  Menu ▼
</button>
<ul id="dropdown-menu" hidden>
  <li><a href="/profile">Profile</a></li>
  <li><a href="/settings">Settings</a></li>
  <li><a href="/logout">Log out</a></li>
</ul>

<script>
  const btn = document.getElementById("dropdown-toggle");
  const menu = document.getElementById("dropdown-menu");

  btn.addEventListener("click", () => {
    const isExpanded = btn.getAttribute("aria-expanded") === "true";
    btn.setAttribute("aria-expanded", !isExpanded);
    menu.hidden = isExpanded;
  });
</script>

<!-- aria-current — marks the current item in a set -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>    <!-- current page -->
    <li><a href="/about">About</a></li>
    <li><a href="/blog">Blog</a></li>
  </ul>
</nav>

<ol aria-label="Checkout steps">
  <li><a href="/cart">Cart</a></li>
  <li><a href="/shipping" aria-current="step">Shipping</a></li>  <!-- current step -->
  <li><a href="/payment">Payment</a></li>
  <li><a href="/confirm">Confirm</a></li>
</ol>

<!-- aria-pressed — toggle button state -->
<button type="button" aria-pressed="false" id="mute-btn">
  🔊 Mute
</button>

<script>
  const muteBtn = document.getElementById("mute-btn");
  muteBtn.addEventListener("click", () => {
    const pressed = muteBtn.getAttribute("aria-pressed") === "true";
    muteBtn.setAttribute("aria-pressed", !pressed);
    muteBtn.textContent = pressed ? "🔊 Mute" : "🔇 Unmute";
  });
</script>

<!-- aria-checked — custom checkbox state -->
<div
  role="checkbox"
  aria-checked="false"
  tabindex="0"
  id="custom-check"
>
  Agree to terms
</div>

<!-- aria-selected — selected state in listbox/tabs/grid -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="panel2">Tab 2</button>
</div>

<!-- aria-invalid + aria-errormessage — form validation -->
<label for="username">Username</label>
<input
  type="text"
  id="username"
  aria-invalid="true"
  aria-errormessage="username-error"
/>
<p id="username-error" role="alert">
  Username already taken. Please choose another.
</p>

<!-- aria-required — marks required fields -->
<label for="first-name">
  First name <span aria-hidden="true">*</span>
</label>
<input
  type="text"
  id="first-name"
  aria-required="true"
/>

<!-- aria-disabled — communicates disabled state without preventing focus -->
<button type="button" aria-disabled="true">
  Submit (complete all fields first)
</button>

<!-- aria-live — dynamic content regions -->
<div aria-live="polite" aria-atomic="true" id="status-message">
  <!-- Updated dynamically — announced without stealing focus -->
</div>

<div role="alert" aria-live="assertive" id="error-banner">
  <!-- Critical errors — announced immediately -->
</div>

<!-- aria-controls — element that controls another -->
<button aria-controls="sidebar" aria-expanded="true">
  Toggle Sidebar
</button>
<aside id="sidebar">...</aside>

<!-- aria-owns — indicates ownership when DOM order doesn't reflect it -->
<ul role="tree" aria-owns="subtree-1">
  <li role="treeitem">Parent Node</li>
</ul>
<ul id="subtree-1" role="group">
  <li role="treeitem">Child Node</li>
</ul>

<!-- aria-level — heading level for non-heading elements -->
<div role="heading" aria-level="3">Section Title</div>

<!-- aria-posinset and aria-setsize — position in a set -->
<li role="option" aria-posinset="3" aria-setsize="10">Item 3</li>

<!-- aria-valuemin, aria-valuemax, aria-valuenow, aria-valuetext — range -->
<div
  role="slider"
  aria-valuemin="0"
  aria-valuemax="100"
  aria-valuenow="42"
  aria-valuetext="42 percent"
  tabindex="0"
>
</div>

<!-- aria-modal — tells screen readers to ignore content outside -->
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">Confirm Action</h2>
  ...
</div>
```

---

## 2. Landmark Roles

Landmarks define the **major navigable regions** of a page. Screen reader users can pull up a list of landmarks and jump directly to any region — similar to how sighted users visually scan a page for the header, main content, and navigation.

HTML5 semantic elements automatically create landmark roles. ARIA `role` attributes can add them to non-semantic elements.

---

### The Complete Landmark Map

```html
<!DOCTYPE html>
<html lang="en">
<head>...</head>
<body>

  <!--
    role="banner"
    Created by: <header> at the top level (not nested in article/section)
    Purpose: Site header — logo, site name, global nav
    One per page
  -->
  <header>
    <a href="/">
      <img src="logo.svg" alt="Company Name" />
    </a>

    <!--
      role="navigation"
      Created by: <nav>
      Purpose: Major navigation links
      Multiple allowed — distinguish with aria-label
    -->
    <nav aria-label="Main navigation">
      <ul>
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>

    <!--
      role="search"
      Created by: <search> (HTML5.3) or role="search"
      Purpose: Site search functionality
    -->
    <search>
      <form action="/search" method="GET">
        <label for="site-search" class="sr-only">Search the site</label>
        <input type="search" id="site-search" name="q" placeholder="Search..." />
        <button type="submit">Search</button>
      </form>
    </search>

  </header>

  <!--
    role="main"
    Created by: <main>
    Purpose: The primary, unique content of the page
    Only ONE per page
  -->
  <main id="main-content">

    <!--
      role="region"
      Created by: <section> with aria-labelledby or aria-label
      Purpose: Generic named region — only use when no better landmark fits
      Must have an accessible name or it won't be exposed as a landmark
    -->
    <section aria-labelledby="featured-heading">
      <h2 id="featured-heading">Featured Articles</h2>
      <!-- articles -->
    </section>

    <!--
      role="form"
      Created by: <form> with aria-label or aria-labelledby
      Purpose: A form that collects user input
    -->
    <form aria-label="Newsletter subscription">
      ...
    </form>

  </main>

  <!--
    role="complementary"
    Created by: <aside>
    Purpose: Supporting content, tangentially related to main
  -->
  <aside aria-label="Related content">
    <section>
      <h2>Related Articles</h2>
      ...
    </section>
  </aside>

  <!--
    role="contentinfo"
    Created by: <footer> at the top level (not nested)
    Purpose: Site footer — copyright, legal, contact info
    One per page
  -->
  <footer>
    <nav aria-label="Footer navigation">
      ...
    </nav>
    <small>© 2026 Example Company</small>
  </footer>

</body>
</html>
```

---

### Landmark Summary Table

| HTML Element | ARIA Role | Purpose | Multiple? |
|---|---|---|---|
| `<header>` (top-level) | `banner` | Site header | One |
| `<footer>` (top-level) | `contentinfo` | Site footer | One |
| `<main>` | `main` | Primary content | One |
| `<nav>` | `navigation` | Navigation links | Yes — use `aria-label` |
| `<aside>` | `complementary` | Sidebar / supporting | Yes — use `aria-label` |
| `<form>` (named) | `form` | User input form | Yes — use `aria-label` |
| `<section>` (named) | `region` | Named content region | Yes — use `aria-label` |
| `<search>` | `search` | Search functionality | Yes |

---

### Labelling Multiple Landmarks of the Same Type

When you have multiple landmarks of the same type, **each must have a unique label** so screen reader users can distinguish them.

```html
<!-- ✅ Multiple navs — each clearly labelled -->
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Breadcrumb">...</nav>
<nav aria-label="Article sections">...</nav>
<nav aria-label="Pagination">...</nav>

<!-- ✅ Multiple asides -->
<aside aria-label="Author bio">...</aside>
<aside aria-label="Related articles">...</aside>

<!-- ❌ Unlabelled duplicate landmarks — indistinguishable -->
<nav>...</nav>
<nav>...</nav>
```

---

## 3. Tab Order and `tabindex`

The **tab order** is the sequence in which keyboard users move through focusable elements using the `Tab` key. A logical, predictable tab order is essential for keyboard navigation.

---

### Natural Tab Order

By default, the browser focuses elements in **DOM order** — the order they appear in the HTML source. Focusable elements by default include: `<a href>`, `<button>`, `<input>`, `<textarea>`, `<select>`, `<details>`, and any element with `tabindex`.

```html
<!-- Tab order follows DOM order: 1 → 2 → 3 → 4 -->
<a href="/home">Home</a>            <!-- Tab stop 1 -->
<a href="/about">About</a>          <!-- Tab stop 2 -->
<input type="text" name="search" /> <!-- Tab stop 3 -->
<button type="submit">Search</button> <!-- Tab stop 4 -->
```

The golden rule: **keep your visual order and DOM order in sync**. CSS can visually reorder elements without changing the DOM — this breaks keyboard navigation.

```css
/* ❌ Dangerous — visual order differs from DOM order */
.container {
  display: flex;
  flex-direction: row-reverse; /* Reverses visual order but not tab order */
}
```

---

### `tabindex` Values

`tabindex` controls whether and how an element participates in keyboard navigation.

#### `tabindex="0"` — Add to Natural Tab Order

Makes a non-focusable element **focusable in the natural DOM order**. Use this to make custom interactive elements keyboard-accessible.

```html
<!-- Making a custom interactive widget keyboard-focusable -->
<div
  role="button"
  tabindex="0"
  onclick="handleClick()"
  onkeydown="handleKeydown(event)"
>
  Custom Button
</div>

<script>
function handleKeydown(event) {
  // Buttons should activate on Enter and Space
  if (event.key === "Enter" || event.key === " ") {
    event.preventDefault();
    handleClick();
  }
}
</script>

<!-- Custom card that is selectable -->
<div
  class="product-card"
  role="option"
  tabindex="0"
  aria-selected="false"
>
  <img src="product.jpg" alt="Product name" />
  <h3>Product Name</h3>
  <p>$29.99</p>
</div>

<!-- Making a <details> alternative focusable -->
<div
  role="button"
  tabindex="0"
  aria-expanded="false"
  aria-controls="content"
>
  Show more
</div>
<div id="content" hidden>
  Extended content here.
</div>
```

---

#### `tabindex="-1"` — Programmatically Focusable, Not in Tab Order

The element can receive focus **via JavaScript** (`element.focus()`) but is skipped during normal `Tab` key navigation. Essential for focus management in custom components.

```html
<!-- Modal dialog — focused programmatically when opened, not in tab flow when closed -->
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-heading"
  id="confirm-modal"
  tabindex="-1"
>
  <h2 id="modal-heading">Confirm deletion</h2>
  <p>Are you sure? This cannot be undone.</p>
  <button type="button">Cancel</button>
  <button type="button">Confirm</button>
</div>

<!-- Individual items in a custom listbox — only one in tab order at a time -->
<ul role="listbox" aria-label="Colour options" tabindex="0">
  <li role="option" aria-selected="true"  tabindex="-1">Red</li>
  <li role="option" aria-selected="false" tabindex="-1">Green</li>
  <li role="option" aria-selected="false" tabindex="-1">Blue</li>
</ul>

<!-- Error summary — jumped to programmatically on form submission -->
<div id="error-summary" tabindex="-1" role="alert">
  <h2>Please fix the following errors:</h2>
  <ul>
    <li><a href="#email">Email address is invalid</a></li>
    <li><a href="#password">Password must be at least 8 characters</a></li>
  </ul>
</div>
```

```js
// Open modal and focus it
function openModal() {
  const modal = document.getElementById("confirm-modal");
  modal.hidden = false;
  modal.focus(); // Works because tabindex="-1"
}

// Focus error summary after failed form submission
function submitForm() {
  if (hasErrors) {
    const summary = document.getElementById("error-summary");
    summary.hidden = false;
    summary.focus(); // Bring keyboard users to the error list
  }
}
```

---

#### `tabindex` > 0 — Positive Values (Almost Always Wrong)

Positive `tabindex` values set an **explicit tab order**, focusing elements with lower values first before any `tabindex="0"` elements. This seems helpful but almost always creates worse experiences:

```html
<!-- ❌ Positive tabindex — creates a confusing tab sequence -->
<input type="text" tabindex="3" />   <!-- Focused 3rd -->
<input type="text" tabindex="1" />   <!-- Focused 1st -->
<input type="text" tabindex="2" />   <!-- Focused 2nd -->
<input type="text" />                <!-- Focused 4th (natural order) -->

<!-- ✅ Better — fix the DOM order instead -->
<input type="text" />   <!-- First in DOM = focused first -->
<input type="text" />
<input type="text" />
<input type="text" />
```

If you feel the urge to use `tabindex="1"` or higher, it's almost always a sign you should reorder your HTML instead.

---

### Visible Focus Indicators

Every focusable element **must have a visible focus indicator** — the outline that appears when an element receives keyboard focus. Removing focus outlines without a replacement is one of the most common and damaging accessibility violations.

```css
/* ❌ Never do this — removes all focus indication */
* {
  outline: none;
}

button:focus {
  outline: 0;
}

/* ✅ Remove default and replace with custom — better looking AND accessible */
:focus {
  outline: none;                           /* Remove browser default */
  box-shadow: 0 0 0 3px #3b82f6,          /* Blue ring */
              0 0 0 5px rgba(59,130,246,0.2); /* Subtle outer glow */
  border-radius: 4px;
}

/* ✅ Use :focus-visible to only show focus for keyboard users */
/* Hides outline when clicking with a mouse, shows it for keyboard */
:focus-visible {
  outline: 3px solid #3b82f6;
  outline-offset: 2px;
}

:focus:not(:focus-visible) {
  outline: none;
}

/* ✅ High contrast mode support */
@media (forced-colors: active) {
  :focus-visible {
    outline: 3px solid ButtonText;
  }
}
```

**WCAG 2.2 Focus requirements:**
- Focus must be visible — WCAG 1.4.11, 2.4.7
- Focus indicator must have adequate contrast — WCAG 2.4.11
- Focus must not be entirely hidden (e.g. scrolled off-screen) — WCAG 2.4.12

---

## 4. Skip Navigation Links

A **skip link** is a hidden-until-focused link that lets keyboard and screen reader users **jump over repetitive navigation** directly to the main content. Without it, users must tab through every navigation item on every page.

```html
<!DOCTYPE html>
<html lang="en">
<body>

  <!-- ✅ Must be the first focusable element in the document -->
  <a href="#main-content" class="skip-link">
    Skip to main content
  </a>

  <header>
    <nav aria-label="Main navigation">
      <!-- 40+ navigation links the user wants to skip -->
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/services">Services</a></li>
        <!-- ... many more links -->
      </ul>
    </nav>
  </header>

  <main id="main-content" tabindex="-1">
    <!-- tabindex="-1" ensures focus() works on non-focusable element -->
    <h1>Page Title</h1>
    <p>Main content starts here.</p>
  </main>

</body>
</html>
```

```css
/* Hidden visually, but visible when focused */
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  z-index: 10000;
  padding: 1rem 1.5rem;
  background: #1d4ed8;
  color: #ffffff;
  font-weight: 700;
  font-size: 1rem;
  text-decoration: none;
  border-radius: 0 0 8px 0;
  transition: top 0.2s ease;

  /* Prevent layout shift when it appears */
  white-space: nowrap;
}

.skip-link:focus {
  top: 0; /* Slides into view when keyboard user presses Tab first */
}

/* High contrast mode */
@media (forced-colors: active) {
  .skip-link {
    border: 2px solid ButtonText;
  }
}
```

---

### Multiple Skip Links

For complex pages, provide multiple skip links for different regions:

```html
<!-- Multiple skip links for power users -->
<nav aria-label="Skip links" class="skip-links">
  <ul>
    <li>
      <a href="#main-content" class="skip-link">Skip to main content</a>
    </li>
    <li>
      <a href="#search" class="skip-link">Skip to search</a>
    </li>
    <li>
      <a href="#site-footer" class="skip-link">Skip to footer</a>
    </li>
  </ul>
</nav>

<header>
  <form id="search" role="search">...</form>
  <nav aria-label="Main navigation">...</nav>
</header>

<main id="main-content" tabindex="-1">...</main>

<footer id="site-footer" tabindex="-1">...</footer>
```

---

## 5. Alt Text Best Practices

The `alt` attribute on `<img>` provides a **text alternative** for images. Screen readers read it aloud; it appears when images fail to load; search engines index it.

---

### The Core Question

> **"What information would be lost if this image were removed?"**

Your alt text should convey exactly that information, nothing more.

---

### Informative Images

Describe what the image shows and why it matters in context:

```html
<!-- ✅ Specific and informative -->
<img
  src="ceo-headshot.jpg"
  alt="Jane Doe, CEO of Example Company, smiling in a blue blazer"
/>

<!-- ✅ Action in progress -->
<img
  src="developer-coding.jpg"
  alt="Developer writing code on a laptop with dual monitors"
/>

<!-- ✅ Chart — describe the key insight, not just "a chart" -->
<img
  src="revenue-chart.png"
  alt="Line chart showing company revenue growing from $1.2M in Q1 to $1.9M in Q4 2025, a 58% increase"
/>

<!-- ✅ Screenshot — describe what's shown and why it matters -->
<img
  src="settings-panel.png"
  alt="Settings panel with the 'Dark mode' toggle highlighted in the Appearance section"
/>

<!-- ❌ Bad — too vague, no useful information -->
<img src="photo.jpg" alt="image" />
<img src="photo.jpg" alt="photo" />
<img src="photo.jpg" alt="picture of something" />

<!-- ❌ Bad — redundant prefix -->
<img src="dog.jpg" alt="Image of a golden retriever" />
<!-- Screen reader already says "image" — alt should be "Golden retriever playing fetch" -->

<!-- ❌ Bad — keyword stuffing (SEO abuse of alt text) -->
<img src="product.jpg" alt="buy shoes cheap shoes discount shoes size 10 shoes" />
```

---

### Decorative Images — `alt=""`

If an image is purely decorative — it adds visual interest but conveys no information — use an **empty `alt` attribute**. This tells screen readers to skip it entirely.

```html
<!-- Decorative background shape -->
<img src="background-blob.svg" alt="" role="presentation" />

<!-- Decorative divider -->
<img src="wave-divider.png" alt="" />

<!-- Icon that duplicates adjacent text — skip the icon -->
<a href="/settings">
  <img src="gear-icon.svg" alt="" />
  Settings
</a>
<!-- Screen reader: "Settings, link" — not "gear icon Settings link" -->

<!-- Avatar in a list where the name is already shown -->
<li>
  <img src="avatar-jane.jpg" alt="" />
  <span>Jane Doe</span>
</li>
```

**Critical distinction:**

```html
<!-- alt="" is intentionally empty — skip this image -->
<img src="decoration.png" alt="" />

<!-- Missing alt attribute — screen reader reads the filename (terrible UX) -->
<img src="decoration.png" />
<!-- Screen reader: "decoration dot png" or full file path -->
```

---

### Functional Images — Describe the Function

When an image is inside a link or button with no other text, the alt text must describe **what the action does**, not what the image looks like:

```html
<!-- Logo as homepage link — describe the destination -->
<a href="/">
  <img src="logo.svg" alt="Example Company — Return to homepage" />
</a>

<!-- ❌ Wrong — describes appearance, not function -->
<a href="/">
  <img src="logo.svg" alt="Blue circular logo with company name" />
</a>

<!-- Icon buttons — describe the action -->
<button type="button">
  <img src="search-icon.png" alt="Search" />
</button>

<button type="button">
  <img src="print-icon.png" alt="Print this page" />
</button>

<button type="button">
  <img src="close-icon.png" alt="Close dialog" />
</button>
```

---

### Complex Images — Long Descriptions

For charts, diagrams, infographics, and maps that require detailed descriptions:

```html
<!-- Method 1: Describe inline with aria-describedby -->
<figure>
  <img
    src="org-chart.png"
    alt="Company organisational chart"
    aria-describedby="org-chart-desc"
  />
  <figcaption id="org-chart-desc">
    The company has a CEO at the top, with three direct reports:
    CTO (overseeing Engineering and DevOps), CMO (overseeing Marketing
    and Design), and CFO (overseeing Finance and Legal).
  </figcaption>
</figure>

<!-- Method 2: Link to a full description page -->
<figure>
  <img src="complex-diagram.png" alt="Network topology diagram" />
  <figcaption>
    Network topology diagram.
    <a href="/diagrams/network-topology-description">
      View full text description
    </a>
  </figcaption>
</figure>

<!-- Method 3: For SVG — embed description inside -->
<svg role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">Monthly Active Users 2025</title>
  <desc id="chart-desc">
    Bar chart showing MAU growing from 42K in January to 128K in December,
    with a notable spike of 156K in August during the product launch period.
  </desc>
  <!-- SVG chart elements -->
</svg>
```

---

### Context-Dependent Alt Text

The same image can require different alt text depending on how it's used:

```html
<!-- Used as illustration — describe what you see -->
<img
  src="golden-retriever.jpg"
  alt="Golden retriever puppy sitting in autumn leaves"
/>

<!-- Used as a link in a dog breed guide — describe the breed context -->
<a href="/breeds/golden-retriever">
  <img
    src="golden-retriever.jpg"
    alt="Golden Retriever — View breed information"
  />
</a>

<!-- Used as decorative header on golden retriever page — already in context -->
<h1>Golden Retriever</h1>
<img src="golden-retriever.jpg" alt="" />  <!-- Redundant — page title says it all -->
```

---

### Alt Text Decision Flowchart

```
Does the image convey meaningful information?
│
├── No (purely decorative) ──────────────────────── alt=""
│
└── Yes
    │
    ├── Does it contain text?
    │   ├── Yes — include that exact text in alt
    │   └── No — continue
    │
    ├── Is it inside a link or button?
    │   ├── Yes ─ describe the destination/action
    │   └── No — continue
    │
    ├── Is it a chart, graph, or diagram?
    │   ├── Yes ─ describe the key insight + provide long description
    │   └── No — continue
    │
    └── Describe what it shows and why it matters in this context
```

---

## 6. Focus Management

Focus management means **programmatically controlling which element has focus** — essential for dynamic UI patterns like modals, drawers, toasts, and single-page app navigation.

---

### Modal Dialogs — Complete Focus Trap Pattern

When a modal opens, focus must move inside it. The user must not be able to Tab to elements behind the modal. When it closes, focus must return to the element that opened it.

```html
<button type="button" id="open-modal">Delete Account</button>

<div
  id="confirm-modal"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-desc"
  hidden
  tabindex="-1"
>
  <h2 id="modal-title">Delete your account?</h2>
  <p id="modal-desc">
    This will permanently delete your account and all associated data.
    This action cannot be undone.
  </p>
  <button type="button" id="cancel-btn">Cancel</button>
  <button type="button" id="confirm-delete-btn">Delete Account</button>
</div>

<div id="overlay" hidden></div>
```

```js
class Modal {
  constructor(modalEl, triggerEl) {
    this.modal = modalEl;
    this.trigger = triggerEl;
    this.focusableSelectors = [
      'a[href]', 'button:not([disabled])', 'input:not([disabled])',
      'textarea:not([disabled])', 'select:not([disabled])',
      '[tabindex]:not([tabindex="-1"])'
    ].join(', ');
  }

  open() {
    this.modal.hidden = false;
    document.getElementById("overlay").hidden = false;

    // Prevent background scroll
    document.body.style.overflow = "hidden";

    // Move focus into modal
    this.modal.focus();

    // Set up event listeners
    this.handleKeydown = this.trapFocus.bind(this);
    this.modal.addEventListener("keydown", this.handleKeydown);
  }

  close() {
    this.modal.hidden = true;
    document.getElementById("overlay").hidden = true;
    document.body.style.overflow = "";

    this.modal.removeEventListener("keydown", this.handleKeydown);

    // ✅ Return focus to the element that opened the modal
    this.trigger.focus();
  }

  trapFocus(event) {
    const focusable = Array.from(
      this.modal.querySelectorAll(this.focusableSelectors)
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (event.key === "Tab") {
      if (event.shiftKey) {
        // Shift+Tab — going backwards
        if (document.activeElement === first) {
          event.preventDefault();
          last.focus(); // Wrap to last
        }
      } else {
        // Tab — going forwards
        if (document.activeElement === last) {
          event.preventDefault();
          first.focus(); // Wrap to first
        }
      }
    }

    // Close on Escape
    if (event.key === "Escape") {
      this.close();
    }
  }
}

// Usage
const modal = new Modal(
  document.getElementById("confirm-modal"),
  document.getElementById("open-modal")
);

document.getElementById("open-modal").addEventListener("click", () => modal.open());
document.getElementById("cancel-btn").addEventListener("click", () => modal.close());
document.getElementById("confirm-delete-btn").addEventListener("click", () => {
  // Handle deletion
  modal.close();
});
```

---

### Dynamic Content — Announcements Without Focus Changes

When content updates dynamically (notifications, form errors, cart updates), you often need to **announce the change** without moving focus. Use ARIA live regions:

```html
<!-- Polite — waits for user to finish current interaction -->
<div
  aria-live="polite"
  aria-atomic="true"
  class="sr-only"
  id="status-announcer"
></div>

<!-- Assertive — interrupts immediately (use sparingly) -->
<div
  aria-live="assertive"
  aria-atomic="true"
  class="sr-only"
  id="error-announcer"
></div>
```

```js
function announce(message, type = "polite") {
  const announcer = document.getElementById(
    type === "assertive" ? "error-announcer" : "status-announcer"
  );

  // Clear first to ensure re-announcement if same message
  announcer.textContent = "";

  // Small delay ensures screen reader detects the change
  setTimeout(() => {
    announcer.textContent = message;
  }, 100);
}

// Usage examples
announce("Item added to cart. Cart now has 3 items.");
announce("Form submitted successfully. Check your email for confirmation.");
announce("Error: Email address is invalid.", "assertive");
announce("Loading complete. 24 results found.");
```

---

### SPA Page Navigation — Focus After Route Change

In Single Page Applications, navigating between routes doesn't trigger a page reload — screen readers don't know the page has changed.

```js
// After every route change in your SPA router
function onRouteChange(newPath, pageTitle) {
  // Update document title
  document.title = `${pageTitle} — My App`;

  // Announce the navigation
  announce(`Navigated to ${pageTitle}`);

  // Option 1: Focus the main heading
  const h1 = document.querySelector("main h1");
  if (h1) {
    h1.setAttribute("tabindex", "-1");
    h1.focus();
    // Clean up tabindex after focus moves away
    h1.addEventListener("blur", () => h1.removeAttribute("tabindex"), { once: true });
  }

  // Option 2: Focus the main landmark
  const main = document.querySelector("main");
  if (main) {
    main.focus(); // Works if main has tabindex="-1"
  }
}

// React example (useEffect in router)
useEffect(() => {
  document.title = `${pageTitle} — My App`;
  const heading = document.querySelector("h1");
  if (heading) {
    heading.tabIndex = -1;
    heading.focus();
  }
}, [pathname]);
```

---

### Toast Notifications — Non-Intrusive Announcements

```html
<!-- Toast container — live region -->
<div
  id="toast-region"
  aria-live="polite"
  aria-relevant="additions"
  class="toast-container"
>
  <!-- Toasts injected here by JavaScript -->
</div>
```

```js
function showToast(message, type = "info", duration = 5000) {
  const container = document.getElementById("toast-region");

  const toast = document.createElement("div");
  toast.className = `toast toast--${type}`;
  toast.setAttribute("role", "status");

  // Close button
  const closeBtn = document.createElement("button");
  closeBtn.type = "button";
  closeBtn.setAttribute("aria-label", "Dismiss notification");
  closeBtn.textContent = "✕";
  closeBtn.addEventListener("click", () => toast.remove());

  toast.textContent = message;
  toast.appendChild(closeBtn);
  container.appendChild(toast);

  // Auto-remove after duration
  setTimeout(() => {
    toast.remove();
  }, duration);
}

showToast("Your changes have been saved.", "success");
showToast("File upload failed. Please try again.", "error");
```

---

### Form Validation — Focus on Errors

After a failed form submission, users need to know what went wrong and get to the errors quickly:

```html
<div
  id="form-errors"
  role="alert"
  aria-labelledby="errors-heading"
  tabindex="-1"
  hidden
>
  <h2 id="errors-heading">
    Please correct the following errors:
  </h2>
  <ul id="error-list">
    <!-- Dynamically populated -->
  </ul>
</div>

<form id="signup-form" novalidate>
  <div class="form-group">
    <label for="email">Email address</label>
    <input
      type="email"
      id="email"
      name="email"
      aria-describedby="email-error"
      aria-invalid="false"
    />
    <p id="email-error" class="field-error" hidden></p>
  </div>

  <button type="submit">Create Account</button>
</form>
```

```js
document.getElementById("signup-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const errors = validateForm();

  if (errors.length > 0) {
    // Populate error summary
    const summary = document.getElementById("form-errors");
    const list = document.getElementById("error-list");

    list.innerHTML = errors.map(err =>
      `<li><a href="#${err.fieldId}">${err.message}</a></li>`
    ).join("");

    // Show and focus the error summary
    summary.hidden = false;
    summary.focus(); // tabindex="-1" allows this

    // Mark individual fields as invalid
    errors.forEach(err => {
      const field = document.getElementById(err.fieldId);
      const errorEl = document.getElementById(`${err.fieldId}-error`);

      field.setAttribute("aria-invalid", "true");
      errorEl.textContent = err.message;
      errorEl.hidden = false;
    });

  } else {
    submitForm();
  }
});
```

---

## Complete Accessible Component — Tabs

Combining everything — ARIA roles, keyboard navigation, focus management, and live regions:

```html
<div class="tabs">

  <!-- Tab list -->
  <div role="tablist" aria-label="Account settings">

    <button
      role="tab"
      id="tab-profile"
      aria-selected="true"
      aria-controls="panel-profile"
      tabindex="0"
    >
      Profile
    </button>

    <button
      role="tab"
      id="tab-security"
      aria-selected="false"
      aria-controls="panel-security"
      tabindex="-1"
    >
      Security
    </button>

    <button
      role="tab"
      id="tab-notifications"
      aria-selected="false"
      aria-controls="panel-notifications"
      tabindex="-1"
    >
      Notifications
    </button>

  </div>

  <!-- Tab panels -->
  <div
    role="tabpanel"
    id="panel-profile"
    aria-labelledby="tab-profile"
    tabindex="0"
  >
    <h2>Profile Settings</h2>
    <p>Manage your profile information...</p>
  </div>

  <div
    role="tabpanel"
    id="panel-security"
    aria-labelledby="tab-security"
    tabindex="0"
    hidden
  >
    <h2>Security Settings</h2>
    <p>Manage your password and 2FA...</p>
  </div>

  <div
    role="tabpanel"
    id="panel-notifications"
    aria-labelledby="tab-notifications"
    tabindex="0"
    hidden
  >
    <h2>Notification Preferences</h2>
    <p>Control what emails you receive...</p>
  </div>

</div>
```

```js
class TabWidget {
  constructor(container) {
    this.tabs = Array.from(container.querySelectorAll('[role="tab"]'));
    this.panels = Array.from(container.querySelectorAll('[role="tabpanel"]'));

    this.tabs.forEach((tab, i) => {
      tab.addEventListener("click", () => this.activate(i));
      tab.addEventListener("keydown", (e) => this.handleKeydown(e, i));
    });
  }

  activate(index) {
    // Deactivate all
    this.tabs.forEach(tab => {
      tab.setAttribute("aria-selected", "false");
      tab.setAttribute("tabindex", "-1");
    });
    this.panels.forEach(panel => panel.hidden = true);

    // Activate selected
    this.tabs[index].setAttribute("aria-selected", "true");
    this.tabs[index].setAttribute("tabindex", "0");
    this.panels[index].hidden = false;
    this.tabs[index].focus();
  }

  handleKeydown(event, index) {
    const total = this.tabs.length;

    // Arrow key navigation within tablist
    if (event.key === "ArrowRight") {
      event.preventDefault();
      this.activate((index + 1) % total);       // Wrap forward
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      this.activate((index - 1 + total) % total); // Wrap backward
    } else if (event.key === "Home") {
      event.preventDefault();
      this.activate(0);                           // First tab
    } else if (event.key === "End") {
      event.preventDefault();
      this.activate(total - 1);                   // Last tab
    }
  }
}

new TabWidget(document.querySelector(".tabs"));
```

---

## Quick Reference Summary

| Attribute / Element | Purpose |
|---|---|
| `role` | Defines what type of element this is for assistive tech |
| `aria-label` | Provides an accessible name (no visible text) |
| `aria-labelledby` | Points to existing visible text as the accessible name |
| `aria-describedby` | Points to supplementary description text |
| `aria-hidden="true"` | Removes element from accessibility tree entirely |
| `aria-expanded` | State of collapsible elements |
| `aria-pressed` | State of toggle buttons |
| `aria-current` | Current item in a set (page, step, date) |
| `aria-selected` | Selected state in tabs, listboxes |
| `aria-invalid` | Marks an invalid form field |
| `aria-live` | Marks a region that updates dynamically |
| `aria-modal` | Tells screen readers to ignore background content |
| `aria-controls` | Points to the element this one controls |
| `tabindex="0"` | Adds element to natural tab order |
| `tabindex="-1"` | Focusable via JS only, skipped by Tab key |
| `tabindex > 0` | Explicit tab order — almost always wrong |
| `:focus-visible` | Style focus only for keyboard users |
| Skip link | First focusable element, jumps to `#main-content` |
| `alt=""` | Marks image as decorative — screen readers skip it |
| `alt="description"` | Describes image content or function |
| Focus trap | Keeps focus inside modals during their lifecycle |
| `aria-live="polite"` | Announces updates without interrupting user |
| `aria-live="assertive"` | Announces immediately — use sparingly |
| `.focus()` | Programmatically moves focus |

Accessibility is not a checklist — it is a mindset. Every decision about HTML structure, interactive behaviour, and visual design has an accessibility dimension. Building with accessibility from the start is always easier, cheaper, and more effective than retrofitting it later.