# Semantic HTML — Detailed Explanation

Semantic HTML means using elements that **carry meaning** about the content they contain — not just for visual presentation, but to communicate structure and purpose to browsers, search engines, screen readers, and other developers.

The difference between semantic and non-semantic HTML:

```html
<!-- Non-semantic — tells us nothing about the content -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main-content">
  <div class="blog-post">...</div>
  <div class="sidebar">...</div>
</div>
<div class="footer">...</div>

<!-- Semantic — structure is self-documenting and meaningful -->
<header>
  <nav>...</nav>
</header>
<main>
  <article>...</article>
  <aside>...</aside>
</main>
<footer>...</footer>
```

Both render identically in a browser. The semantic version gives browsers, assistive technologies, and search engines real structural information to work with.

---

## 1. Layout Elements

### `<header>`

Represents **introductory content** for its nearest ancestor sectioning element — either the whole page or a specific section/article. It typically contains logos, headings, navigation, or search.

```html
<!-- Page-level header -->
<header>
  <a href="/" aria-label="Company Name — Home">
    <img src="logo.svg" alt="" width="140" height="40" />
  </a>

  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
  </nav>

  <div class="header-actions">
    <a href="/login" class="btn btn--ghost">Log in</a>
    <a href="/signup" class="btn btn--primary">Sign up</a>
  </div>
</header>
```

`<header>` can also appear **inside other sectioning elements** — each article or section can have its own header:

```html
<article>
  <!-- Article-level header -->
  <header>
    <h2>Getting Started with CSS Grid</h2>
    <p class="byline">
      By <a href="/authors/jane">Jane Doe</a> ·
      <time datetime="2026-02-23">February 23, 2026</time> ·
      8 min read
    </p>
    <ul class="tag-list">
      <li><a href="/tags/css">CSS</a></li>
      <li><a href="/tags/layout">Layout</a></li>
    </ul>
  </header>

  <p>CSS Grid is a two-dimensional layout system...</p>
</article>
```

**Rules:**
- There can be **multiple `<header>` elements** per page — one per sectioning context
- A `<header>` cannot be nested inside another `<header>`, `<footer>`, or `<address>`
- The page-level header typically (but not required to) contains the main `<h1>`

---

### `<footer>`

Represents **closing or supplementary content** for its nearest ancestor sectioning element. Typically contains copyright, authorship, related links, contact info, or legal notices.

```html
<!-- Page-level footer -->
<footer>
  <div class="footer-grid">

    <div class="footer-brand">
      <img src="logo-white.svg" alt="Company Name" width="120" height="35" />
      <p>Building better web experiences since 2015.</p>
      <ul class="social-links">
        <li>
          <a href="https://twitter.com/example"
             target="_blank"
             rel="noopener noreferrer"
             aria-label="Follow us on Twitter">
            <!-- Twitter SVG icon -->
          </a>
        </li>
        <li>
          <a href="https://github.com/example"
             target="_blank"
             rel="noopener noreferrer"
             aria-label="View our code on GitHub">
            <!-- GitHub SVG icon -->
          </a>
        </li>
      </ul>
    </div>

    <nav aria-label="Product links">
      <h3>Product</h3>
      <ul>
        <li><a href="/features">Features</a></li>
        <li><a href="/pricing">Pricing</a></li>
        <li><a href="/changelog">Changelog</a></li>
        <li><a href="/roadmap">Roadmap</a></li>
      </ul>
    </nav>

    <nav aria-label="Company links">
      <h3>Company</h3>
      <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/careers">Careers</a></li>
        <li><a href="/press">Press</a></li>
      </ul>
    </nav>

    <nav aria-label="Legal links">
      <h3>Legal</h3>
      <ul>
        <li><a href="/privacy">Privacy Policy</a></li>
        <li><a href="/terms">Terms of Service</a></li>
        <li><a href="/cookies">Cookie Policy</a></li>
      </ul>
    </nav>

  </div>

  <div class="footer-bottom">
    <p>
      <small>© 2026 Example Company Ltd. All rights reserved.</small>
    </p>
    <p>
      <small>Registered in England & Wales. Company No. 12345678.</small>
    </p>
  </div>
</footer>
```

Like `<header>`, footers can live **inside articles and sections**:

```html
<article>
  <header>
    <h2>Understanding Flexbox</h2>
  </header>

  <p>Flexbox is a one-dimensional layout model...</p>

  <!-- Article-level footer -->
  <footer>
    <p>
      Last updated:
      <time datetime="2026-02-23">February 23, 2026</time>
    </p>
    <p>
      Tags:
      <a href="/tags/css">CSS</a>,
      <a href="/tags/flexbox">Flexbox</a>,
      <a href="/tags/layout">Layout</a>
    </p>
    <p>
      <a href="/articles/understanding-flexbox/edit">
        Suggest an edit on GitHub →
      </a>
    </p>
  </footer>
</article>
```

---

### `<main>`

Represents the **dominant, unique content** of the page — the content that is directly related to the page's central topic. There can only be **one `<main>` per page**, and it must not be nested inside `<header>`, `<footer>`, `<nav>`, `<aside>`, or `<article>`.

```html
<body>
  <header>...</header>
  <nav>...</nav>

  <!-- One <main> per page -->
  <main id="main-content">
    <h1>Frontend Development Blog</h1>

    <section aria-labelledby="featured-heading">
      <h2 id="featured-heading">Featured Article</h2>
      <article>...</article>
    </section>

    <section aria-labelledby="recent-heading">
      <h2 id="recent-heading">Recent Posts</h2>
      <ul>
        <li><article>...</article></li>
        <li><article>...</article></li>
      </ul>
    </section>
  </main>

  <aside>...</aside>
  <footer>...</footer>
</body>
```

**Why `<main>` matters:**

Screen readers expose a "Main" landmark that users can jump to directly — skipping headers and navigation entirely. It's the semantic counterpart to your skip navigation link:

```html
<!-- Skip link targets <main> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<header>...</header>

<main id="main-content">
  <!-- Screen reader users jump here directly -->
</main>
```

---

### `<nav>`

Represents a section containing **major navigation links**. Not every group of links needs a `<nav>` — only groups that are significant navigation blocks.

```html
<!-- Primary site navigation -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/services">Services</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<!-- Breadcrumb navigation -->
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/blog/css">CSS</a></li>
    <li aria-current="page">CSS Grid Guide</li>
  </ol>
</nav>

<!-- Pagination navigation -->
<nav aria-label="Article pagination">
  <a href="/blog?page=4" rel="prev">← Previous</a>
  <span>Page 5 of 12</span>
  <a href="/blog?page=6" rel="next">Next →</a>
</nav>

<!-- Table of contents -->
<nav aria-label="Table of contents">
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#core-concepts">Core Concepts</a></li>
    <li><a href="#examples">Examples</a></li>
    <li><a href="#browser-support">Browser Support</a></li>
  </ol>
</nav>

<!-- In-page anchor nav — tab bar style -->
<nav aria-label="Section navigation">
  <ul role="tablist">
    <li><a href="#overview" aria-current="page">Overview</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#pricing">Pricing</a></li>
    <li><a href="#faq">FAQ</a></li>
  </ul>
</nav>
```

**Multiple `<nav>` elements on one page are fine** — distinguish them with `aria-label` so screen readers can tell them apart. A screen reader user navigating by landmarks would hear "Main navigation", "Breadcrumb", and "Table of contents" as separate distinct regions.

**When NOT to use `<nav>`:**
```html
<!-- ❌ Minor list of links — doesn't need <nav> -->
<nav>
  <a href="/privacy">Privacy</a>
  <a href="/terms">Terms</a>
</nav>

<!-- ✅ Just links in a paragraph is fine for minor links -->
<p>
  <a href="/privacy">Privacy Policy</a> ·
  <a href="/terms">Terms of Service</a>
</p>
```

---

### `<aside>`

Represents content that is **tangentially related** to the main content — useful if removed but not central to the page's purpose. Think of it as a sidebar, pull quote, related links, or advertisement.

```html
<!-- Sidebar alongside main content -->
<div class="layout">
  <main>
    <article>
      <h1>A Complete Guide to CSS Grid</h1>
      <p>CSS Grid is a powerful two-dimensional layout system...</p>
    </article>
  </main>

  <aside aria-label="Related content">
    <!-- Related articles -->
    <section>
      <h2>Related Articles</h2>
      <ul>
        <li><a href="/flexbox-guide">CSS Flexbox Guide</a></li>
        <li><a href="/layout-patterns">Common Layout Patterns</a></li>
        <li><a href="/responsive-design">Responsive Design Basics</a></li>
      </ul>
    </section>

    <!-- Newsletter signup -->
    <section>
      <h2>Stay Updated</h2>
      <p>Get weekly frontend tips delivered to your inbox.</p>
      <form action="/subscribe" method="POST">
        <label for="sub-email">Email address</label>
        <input type="email" id="sub-email" name="email" required />
        <button type="submit">Subscribe</button>
      </form>
    </section>

    <!-- Advertising -->
    <section aria-label="Advertisement">
      <p class="sr-only">Advertisement</p>
      <!-- ad content -->
    </section>
  </aside>
</div>
```

`<aside>` can also appear **inline within an article** — for a pullquote or note that's related to nearby content but not the main flow:

```html
<article>
  <h1>The History of CSS</h1>

  <p>CSS was first proposed by Håkon Wium Lie in 1994...</p>

  <!-- Inline aside — pullquote -->
  <aside>
    <blockquote>
      "The power of the Web is in its universality. Access by everyone
      regardless of disability is an essential aspect."
    </blockquote>
    <p>— Tim Berners-Lee</p>
  </aside>

  <p>The first browser to support CSS was...</p>
</article>
```

---

### `<section>`

Represents a **thematic grouping of content** — a standalone section of a document that would appear in a document outline. Every `<section>` should ideally have a heading.

```html
<!-- Sections on a landing page -->
<main>
  <section aria-labelledby="hero-heading">
    <h1 id="hero-heading">Build better products, faster.</h1>
    <p>The all-in-one platform for modern development teams.</p>
    <a href="/signup" class="btn btn--primary">Get started free</a>
  </section>

  <section aria-labelledby="features-heading">
    <h2 id="features-heading">Everything you need</h2>
    <ul class="feature-grid">
      <li>
        <h3>Fast by default</h3>
        <p>Optimised builds out of the box, no configuration required.</p>
      </li>
      <li>
        <h3>Team collaboration</h3>
        <p>Real-time collaboration tools built for distributed teams.</p>
      </li>
    </ul>
  </section>

  <section aria-labelledby="pricing-heading">
    <h2 id="pricing-heading">Simple, transparent pricing</h2>
    <p>Start free, scale as you grow. No hidden fees.</p>
    <!-- pricing cards -->
  </section>

  <section aria-labelledby="testimonials-heading">
    <h2 id="testimonials-heading">Loved by developers worldwide</h2>
    <!-- testimonials -->
  </section>
</main>
```

---

### `<article>`

Represents a **self-contained, independently distributable piece of content** — something that makes complete sense on its own if you extracted it from the page. If you could share it in a feed reader, email, or tweet standalone — it's an article.

```html
<!-- Blog post -->
<article>
  <header>
    <h1>Understanding CSS Custom Properties</h1>
    <p>
      By <a href="/authors/jane" rel="author">Jane Doe</a> ·
      <time datetime="2026-02-23T09:00:00Z">February 23, 2026</time>
    </p>
  </header>

  <p>CSS custom properties (also called CSS variables) allow you to store...</p>

  <section>
    <h2>Defining Custom Properties</h2>
    <p>Custom properties are defined with a double dash prefix...</p>
    <pre><code>:root {
  --primary-color: #3b82f6;
  --font-size-base: 1rem;
}</code></pre>
  </section>

  <section>
    <h2>Using Custom Properties</h2>
    <p>Access them using the var() function...</p>
  </section>

  <footer>
    <p>Tags: <a href="/tags/css">CSS</a>, <a href="/tags/variables">Variables</a></p>
    <p>
      Share:
      <a href="https://twitter.com/intent/tweet?text=..."
         target="_blank"
         rel="noopener noreferrer">Twitter</a>
    </p>
  </footer>
</article>
```

**Articles can be nested** — a blog post (outer article) containing user comments (inner articles):

```html
<article>
  <h1>Why Semantic HTML Matters</h1>
  <p>Semantic HTML provides meaning and structure...</p>

  <!-- Comments section -->
  <section aria-labelledby="comments-heading">
    <h2 id="comments-heading">Comments (3)</h2>

    <article class="comment">
      <header>
        <img src="avatar-alice.jpg" alt="" />
        <h3>Alice Johnson</h3>
        <time datetime="2026-02-23T10:30:00Z">2 hours ago</time>
      </header>
      <p>Great article! I've been neglecting semantic HTML for too long.</p>
    </article>

    <article class="comment">
      <header>
        <img src="avatar-bob.jpg" alt="" />
        <h3>Bob Smith</h3>
        <time datetime="2026-02-23T11:00:00Z">90 minutes ago</time>
      </header>
      <p>This really clarified the difference between section and article for me.</p>
    </article>

  </section>
</article>
```

---

### `<section>` vs `<article>` — The Key Distinction

This is one of the most confused pairs in semantic HTML.

```
Ask yourself: "Would this content make sense if I copy-pasted it
somewhere else — another website, an email, an RSS feed?"

Yes → <article>
No, it only makes sense in context → <section>
```

```html
<!-- <article> — self-contained, can stand alone -->
<article>
  <h2>10 Tips for Better CSS</h2>
  <p>CSS can be tricky. Here are ten tips to improve your skills...</p>
</article>

<!-- <section> — thematic group, part of a larger whole -->
<section>
  <h2>Our Services</h2>
  <p>We offer a range of web development services...</p>
</section>
```

| | `<section>` | `<article>` |
|---|---|---|
| Self-contained | No — part of the page | Yes — works independently |
| Distributable | No | Yes — RSS, email, sharing |
| Needs a heading | Yes, ideally | Yes, ideally |
| Example | Page section, tab panel | Blog post, comment, product card |

---

### Full Page Layout — All Elements Together

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Frontend Blog — CSS Grid Guide</title>
</head>
<body>

  <!-- Skip link -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Page header -->
  <header class="site-header">
    <a href="/" aria-label="Frontend Blog — Home">
      <img src="logo.svg" alt="" width="130" height="36" />
    </a>

    <nav aria-label="Main navigation">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/articles">Articles</a></li>
        <li><a href="/tutorials">Tutorials</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>

  <!-- Breadcrumb -->
  <nav aria-label="Breadcrumb" class="breadcrumb">
    <ol>
      <li><a href="/">Home</a></li>
      <li><a href="/articles">Articles</a></li>
      <li aria-current="page">CSS Grid Guide</li>
    </ol>
  </nav>

  <!-- Page body -->
  <div class="page-layout">

    <!-- Main content -->
    <main id="main-content">
      <article>
        <header>
          <h1>A Complete Guide to CSS Grid</h1>
          <p>
            By <a href="/authors/jane" rel="author">Jane Doe</a> ·
            <time datetime="2026-02-23">February 23, 2026</time> ·
            12 min read
          </p>
        </header>

        <!-- In-article table of contents -->
        <nav aria-label="Article sections">
          <ol>
            <li><a href="#introduction">Introduction</a></li>
            <li><a href="#grid-container">Grid Container</a></li>
            <li><a href="#grid-items">Grid Items</a></li>
            <li><a href="#real-world">Real-World Examples</a></li>
          </ol>
        </nav>

        <section id="introduction" aria-labelledby="intro-heading">
          <h2 id="intro-heading">Introduction</h2>
          <p>CSS Grid is a two-dimensional layout system...</p>

          <!-- Inline aside — callout note -->
          <aside class="callout">
            <strong>Note:</strong> CSS Grid is supported in all modern browsers.
            You can safely use it in production today.
          </aside>
        </section>

        <section id="grid-container" aria-labelledby="container-heading">
          <h2 id="container-heading">Grid Container</h2>
          <p>A grid container is created by setting display: grid...</p>
        </section>

        <section id="grid-items" aria-labelledby="items-heading">
          <h2 id="items-heading">Grid Items</h2>
          <p>Direct children of a grid container become grid items...</p>
        </section>

        <section id="real-world" aria-labelledby="examples-heading">
          <h2 id="examples-heading">Real-World Examples</h2>
          <p>Let's build some common layouts using CSS Grid...</p>
        </section>

        <footer>
          <p>
            Last reviewed:
            <time datetime="2026-02-23">February 23, 2026</time>
          </p>
          <p>Tags:
            <a href="/tags/css">CSS</a>,
            <a href="/tags/grid">Grid</a>,
            <a href="/tags/layout">Layout</a>
          </p>
        </footer>
      </article>

      <!-- Comments -->
      <section aria-labelledby="comments-heading">
        <h2 id="comments-heading">Comments</h2>

        <article class="comment">
          <header>
            <h3>Alice Johnson</h3>
            <time datetime="2026-02-23T14:30:00Z">2 hours ago</time>
          </header>
          <p>This is the best CSS Grid guide I've read. Bookmarked!</p>
        </article>
      </section>
    </main>

    <!-- Sidebar -->
    <aside aria-label="Sidebar">
      <section>
        <h2>Related Articles</h2>
        <ul>
          <li><a href="/flexbox">CSS Flexbox Guide</a></li>
          <li><a href="/responsive">Responsive Design</a></li>
        </ul>
      </section>

      <section>
        <h2>Newsletter</h2>
        <p>Weekly frontend tips in your inbox.</p>
        <form action="/subscribe" method="POST">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required />
          <button type="submit">Subscribe</button>
        </form>
      </section>
    </aside>

  </div>

  <!-- Page footer -->
  <footer class="site-footer">
    <nav aria-label="Footer navigation">
      <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
      </ul>
    </nav>
    <p><small>© 2026 Frontend Blog. All rights reserved.</small></p>
  </footer>

</body>
</html>
```

---

## 2. `<details>` and `<summary>`

`<details>` creates a **native disclosure widget** — a collapsible section of content that the user can toggle open and closed with a click. `<summary>` provides the visible, clickable label for it. No JavaScript required.

```html
<!-- Basic details/summary -->
<details>
  <summary>What is your refund policy?</summary>
  <p>
    We offer a full refund within 30 days of purchase, no questions asked.
    Simply contact our support team at
    <a href="mailto:support@example.com">support@example.com</a>
    with your order number.
  </p>
</details>
```

---

### `open` Attribute — Expanded by Default

```html
<!-- Open by default -->
<details open>
  <summary>System requirements</summary>
  <ul>
    <li>Node.js 18 or higher</li>
    <li>4GB RAM minimum, 8GB recommended</li>
    <li>macOS, Windows 10+, or Linux</li>
  </ul>
</details>
```

---

### FAQ Section with Multiple `<details>`

```html
<section aria-labelledby="faq-heading">
  <h2 id="faq-heading">Frequently Asked Questions</h2>

  <details>
    <summary>How do I get started?</summary>
    <p>
      Sign up for a free account, then follow our
      <a href="/getting-started">Getting Started guide</a>.
      You'll be up and running in under 5 minutes.
    </p>
  </details>

  <details>
    <summary>What payment methods do you accept?</summary>
    <p>We accept all major credit and debit cards (Visa, Mastercard, Amex),
    PayPal, and bank transfers for annual plans.</p>
  </details>

  <details>
    <summary>Can I change my plan at any time?</summary>
    <p>Yes. You can upgrade or downgrade your plan at any time from your
    account settings. Changes take effect immediately.</p>
  </details>

  <details>
    <summary>Do you offer a free trial?</summary>
    <p>Yes — our Free plan gives you full access to core features with no
    time limit. No credit card required.</p>
  </details>

  <details>
    <summary>Is my data secure?</summary>
    <p>All data is encrypted in transit (TLS 1.3) and at rest (AES-256).
    We are SOC 2 Type II certified and GDPR compliant.</p>
  </details>
</section>
```

---

### Rich `<summary>` Content

`<summary>` can contain more than just plain text — you can put headings, icons, or styled elements inside:

```html
<details class="accordion">
  <summary>
    <h3>Advanced Configuration</h3>
    <span class="icon" aria-hidden="true">▼</span>
  </summary>
  <div class="accordion-content">
    <p>Configure advanced settings by editing the config file...</p>
    <pre><code>{
  "timeout": 5000,
  "retries": 3,
  "debug": false
}</code></pre>
  </div>
</details>
```

```css
details {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  margin-bottom: 0.75rem;
}

summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.25rem;
  cursor: pointer;
  font-weight: 600;
  list-style: none;         /* Remove default triangle marker */
  user-select: none;
}

/* Remove default marker in webkit */
summary::-webkit-details-marker { display: none; }

.icon {
  transition: transform 0.2s ease;
  font-size: 0.8rem;
  color: #64748b;
}

/* Rotate icon when open */
details[open] .icon {
  transform: rotate(180deg);
}

.accordion-content {
  padding: 0 1.25rem 1.25rem;
  border-top: 1px solid #e2e8f0;
}

details summary:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: -2px;
  border-radius: 8px;
}
```

---

### Listening for Toggle Events

```js
const details = document.querySelectorAll("details");

details.forEach(detail => {
  detail.addEventListener("toggle", () => {
    if (detail.open) {
      console.log("Opened:", detail.querySelector("summary").textContent);
      // Track analytics, animate, load lazy content, etc.
    } else {
      console.log("Closed:", detail.querySelector("summary").textContent);
    }
  });
});

// Accordion behaviour — close others when one opens
function makeAccordion(container) {
  const allDetails = container.querySelectorAll("details");

  allDetails.forEach(detail => {
    detail.addEventListener("toggle", () => {
      if (detail.open) {
        allDetails.forEach(other => {
          if (other !== detail) other.open = false;
        });
      }
    });
  });
}

makeAccordion(document.querySelector(".faq-section"));
```

---

## 3. `<time>`, `<address>`, `<progress>`, `<meter>`

### `<time>` — Dates and Times

`<time>` marks a **specific point or range in time** in a human-readable format, paired with a machine-readable `datetime` attribute that browsers, search engines, and calendar applications can parse reliably.

```html
<!-- Date only -->
<time datetime="2026-02-23">February 23, 2026</time>
<time datetime="2026-02-23">23 Feb 2026</time>
<time datetime="2026-02-23">Today</time>  <!-- Any text is fine, datetime is the truth -->

<!-- Time only -->
<time datetime="14:30">2:30 PM</time>
<time datetime="14:30:00">14:30</time>

<!-- Date and time (UTC) -->
<time datetime="2026-02-23T14:30:00Z">February 23, 2026 at 2:30 PM UTC</time>

<!-- Date and time (with timezone offset) -->
<time datetime="2026-02-23T09:00:00-05:00">9:00 AM Eastern Time</time>

<!-- Month and year only -->
<time datetime="2026-02">February 2026</time>

<!-- Year only -->
<time datetime="2026">2026</time>

<!-- Duration -->
<time datetime="PT2H30M">2 hours and 30 minutes</time>
<time datetime="P3D">3 days</time>
<time datetime="P1Y2M">1 year and 2 months</time>
```

**`datetime` format reference:**

| Format | Example | Meaning |
|---|---|---|
| `YYYY-MM-DD` | `2026-02-23` | Date only |
| `HH:MM` | `14:30` | Time only |
| `YYYY-MM-DDTHH:MM:SSZ` | `2026-02-23T14:30:00Z` | Full UTC datetime |
| `YYYY-MM-DDTHH:MM:SS±HH:MM` | `2026-02-23T09:00:00-05:00` | With timezone |
| `YYYY-MM` | `2026-02` | Month and year |
| `YYYY` | `2026` | Year only |
| `PTxHxMxS` | `PT2H30M` | Duration |

**Real-world usage:**

```html
<!-- Article publish date -->
<p>
  Published
  <time datetime="2026-02-23T09:00:00Z">February 23, 2026</time>
</p>

<!-- Relative time (update via JavaScript) -->
<p>
  Last updated
  <time datetime="2026-02-23T08:45:00Z" id="last-updated">
    35 minutes ago
  </time>
</p>

<!-- Event listing -->
<article class="event">
  <h2>Frontend Conference 2026</h2>
  <p>
    <time datetime="2026-06-15">June 15</time>–
    <time datetime="2026-06-17">17, 2026</time>
  </p>
  <p>Doors open at <time datetime="09:00">9:00 AM</time></p>
</article>

<!-- Copyright year -->
<footer>
  <small>© <time datetime="2026">2026</time> Example Company</small>
</footer>

<!-- JavaScript relative time formatting -->
<script>
  const timeEl = document.getElementById("last-updated");
  const publishTime = new Date(timeEl.getAttribute("datetime"));
  const now = new Date();
  const diffMinutes = Math.floor((now - publishTime) / 60000);

  const formatter = new Intl.RelativeTimeFormat("en", { numeric: "auto" });
  timeEl.textContent = diffMinutes < 60
    ? formatter.format(-diffMinutes, "minutes")
    : formatter.format(-Math.floor(diffMinutes / 60), "hours");
</script>
```

---

### `<address>` — Contact Information

`<address>` marks **contact information** for the nearest `<article>` or `<body>` — typically the author or the organization responsible for the content. It does NOT mean any postal address — it means contact details in context.

```html
<!-- Page-level contact info (in footer) -->
<footer>
  <address>
    <strong>Example Company Ltd.</strong><br />
    123 Main Street<br />
    London, EC1A 1BB<br />
    United Kingdom<br />
    <br />
    <a href="tel:+442071234567">+44 20 7123 4567</a><br />
    <a href="mailto:hello@example.com">hello@example.com</a>
  </address>
</footer>

<!-- Article author contact -->
<article>
  <h1>Understanding Web Accessibility</h1>

  <address>
    Written by
    <a href="/authors/jane" rel="author">Jane Doe</a>.
    Questions? <a href="mailto:jane@example.com">Email Jane</a>.
  </address>

  <p>Web accessibility ensures that people with disabilities...</p>
</article>

<!-- Contact page -->
<main>
  <h1>Contact Us</h1>

  <address>
    <p>
      <strong>Head Office</strong><br />
      42 Innovation Drive<br />
      San Francisco, CA 94105<br />
      USA
    </p>
    <p>
      Phone: <a href="tel:+14155551234">+1 (415) 555-1234</a><br />
      Email: <a href="mailto:contact@example.com">contact@example.com</a><br />
      Hours: Monday–Friday, 9 AM – 5 PM PST
    </p>
  </address>
</main>
```

**What `<address>` is NOT for:**

```html
<!-- ❌ Wrong — a random postal address in body text -->
<p>
  The Eiffel Tower is located at
  <address>Champ de Mars, 5 Av. Anatole France, 75007 Paris</address>
</p>

<!-- ✅ Correct — just use a <p> for non-contact addresses -->
<p>
  The Eiffel Tower is located at
  Champ de Mars, 5 Av. Anatole France, 75007 Paris.
</p>
```

---

### `<progress>` — Task Completion Progress

`<progress>` represents the **completion state of a task** — like a file upload, installation, or multi-step form. It renders as a native progress bar.

```html
<!-- Determinate progress — known completion percentage -->
<label for="upload-progress">Upload progress</label>
<progress id="upload-progress" value="65" max="100">65%</progress>

<!-- Indeterminate progress — task in progress, duration unknown -->
<label>Loading...</label>
<progress>Loading...</progress>  <!-- No value attribute = indeterminate -->

<!-- Multi-step form progress -->
<p>Step 2 of 4</p>
<progress value="2" max="4" aria-label="Form completion: step 2 of 4"></progress>

<!-- File upload with JavaScript -->
<label for="file-progress">
  Uploading file.pdf — <span id="percent">0</span>%
</label>
<progress id="file-progress" value="0" max="100"></progress>
```

```js
// Simulate upload progress
function simulateUpload() {
  const bar = document.getElementById("file-progress");
  const percent = document.getElementById("percent");
  let value = 0;

  const interval = setInterval(() => {
    value += Math.random() * 10;
    if (value >= 100) {
      value = 100;
      clearInterval(interval);
      percent.textContent = "100 — Complete!";
    } else {
      percent.textContent = Math.round(value);
    }
    bar.value = value;
  }, 300);
}
```

```css
progress {
  width: 100%;
  height: 8px;
  border: none;
  border-radius: 4px;
  overflow: hidden;
  background: #e2e8f0;
  appearance: none;
}

/* Webkit (Chrome, Safari) */
progress::-webkit-progress-bar {
  background: #e2e8f0;
  border-radius: 4px;
}

progress::-webkit-progress-value {
  background: linear-gradient(90deg, #3b82f6, #6366f1);
  border-radius: 4px;
  transition: width 0.3s ease;
}

/* Firefox */
progress::-moz-progress-bar {
  background: linear-gradient(90deg, #3b82f6, #6366f1);
  border-radius: 4px;
}

/* Indeterminate animation */
progress:not([value]) {
  animation: indeterminate 1.5s infinite linear;
}
```

---

### `<meter>` — Scalar Measurement

`<meter>` represents a **scalar value within a known range** — not a progress bar, but a measurement or gauge. Think battery level, disk usage, test score, signal strength.

```html
<!-- Disk usage -->
<label for="disk-usage">Disk usage</label>
<meter
  id="disk-usage"
  value="70"
  min="0"
  max="100"
  low="60"
  high="85"
  optimum="30"
>
  70GB of 100GB used
</meter>

<!-- Test score -->
<p>
  Your score:
  <meter value="82" min="0" max="100" low="50" high="75" optimum="100">
    82 out of 100
  </meter>
  82/100
</p>

<!-- Password strength -->
<label for="pass-strength">Password strength</label>
<meter
  id="pass-strength"
  value="3"
  min="0"
  max="4"
  low="1"
  high="3"
  optimum="4"
  aria-label="Password strength: Strong"
>
  Strong
</meter>

<!-- Battery level -->
<p>
  Battery:
  <meter value="0.25" min="0" max="1" low="0.2" high="0.5" optimum="1">
    25%
  </meter>
  25%
</p>
```

**`<meter>` attributes explained:**

| Attribute | Description |
|---|---|
| `value` | The current value |
| `min` | Minimum value (default 0) |
| `max` | Maximum value (default 1) |
| `low` | Below this = "low" zone (rendered yellow/red) |
| `high` | Above this = "high" zone |
| `optimum` | The ideal/optimal value — determines which zone is "good" |

**How `optimum` affects colour rendering:**

```html
<!-- optimum is HIGH — high values are green, low are red -->
<!-- Like a score — higher is better -->
<meter value="80" min="0" max="100" low="40" high="70" optimum="100">80%</meter>

<!-- optimum is LOW — low values are green, high are red -->
<!-- Like disk usage — lower is better -->
<meter value="80" min="0" max="100" low="60" high="80" optimum="0">80GB</meter>

<!-- optimum is in the MIDDLE — middle is green, extremes are yellow -->
<meter value="5" min="0" max="10" low="2" high="8" optimum="5">5</meter>
```

**`<progress>` vs `<meter>`:**

| | `<progress>` | `<meter>` |
|---|---|---|
| Represents | Task completion | Scalar measurement |
| Range known | May not be (indeterminate) | Always known |
| Has `low`/`high`/`optimum` | No | Yes |
| Colour zones | No | Yes (good/bad/warning) |
| Example | File upload, install | Battery, disk, score, signal |

---

## 4. Choosing `<div>` vs Semantic Tags

`<div>` is a **generic block container** with no semantic meaning. It's essential for layout and grouping when no semantic element fits — but it's massively overused.

---

### The Decision Framework

Ask these questions in order when deciding what element to use:

```
1. Is there a semantic HTML element that describes this content?
   Yes → Use it.
   No  → Go to step 2.

2. Does this need a landmark role for navigation?
   Yes → Add role="..." to a <div>
   No  → Use <div> or <span>
```

---

### Semantic Element Decision Tree

```
Block of content?
│
├── Page-level chrome?
│   ├── Top of page (logo, nav) ──────────────────── <header>
│   ├── Bottom of page (copyright, links) ────────── <footer>
│   ├── Primary navigation ────────────────────────── <nav>
│   └── Dominant page content ──────────────────────── <main>
│
├── Content region?
│   ├── Thematic grouping with heading ──────────── <section>
│   ├── Self-contained, distributable content ──── <article>
│   └── Tangentially related / sidebar ──────────── <aside>
│
├── Specific content type?
│   ├── Date or time ────────────────────────────── <time>
│   ├── Contact information ────────────────────── <address>
│   ├── Task progress ──────────────────────────── <progress>
│   ├── Scalar measurement ──────────────────────── <meter>
│   ├── Collapsible content ─────────────────────── <details> + <summary>
│   ├── Quoted content (block) ─────────────────── <blockquote>
│   ├── Figure with caption ─────────────────────── <figure> + <figcaption>
│   └── Code / preformatted ─────────────────────── <pre> + <code>
│
└── No semantic element fits → <div>
```

---

### Side-by-Side Comparisons

```html
<!-- ❌ All divs — meaningless soup -->
<div class="page-header">
  <div class="logo"><img src="logo.svg" alt="Brand" /></div>
  <div class="main-nav">
    <div class="nav-item"><a href="/">Home</a></div>
    <div class="nav-item"><a href="/about">About</a></div>
  </div>
</div>

<div class="page-body">
  <div class="content">
    <div class="post">
      <div class="post-header">
        <div class="post-title">My Blog Post</div>
        <div class="post-date">February 23, 2026</div>
      </div>
      <div class="post-body">
        <p>Content here...</p>
      </div>
    </div>
  </div>
  <div class="sidebar">
    <div class="widget">
      <div class="widget-title">Related</div>
    </div>
  </div>
</div>

<div class="page-footer">
  <div class="copyright">© 2026 Example</div>
</div>

<!-- ✅ Semantic — meaningful and self-documenting -->
<header>
  <a href="/"><img src="logo.svg" alt="Brand" /></a>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <header>
      <h1>My Blog Post</h1>
      <time datetime="2026-02-23">February 23, 2026</time>
    </header>
    <p>Content here...</p>
  </article>
</main>

<aside aria-label="Related content">
  <section>
    <h2>Related</h2>
  </section>
</aside>

<footer>
  <small>© 2026 Example</small>
</footer>
```

---

### When `<div>` IS the Right Choice

`<div>` is still essential and correct in many situations — don't force a semantic element where none fits.

```html
<!-- ✅ Layout wrapper — pure CSS/JS container -->
<div class="grid-layout">
  <main>...</main>
  <aside>...</aside>
</div>

<!-- ✅ CSS utility wrapper — no semantic meaning needed -->
<div class="container">
  <div class="card">
    <img src="photo.jpg" alt="..." />
    <div class="card-body">
      <h3>Card Title</h3>
      <p>Card description.</p>
    </div>
  </div>
</div>

<!-- ✅ JavaScript hook — target for JS without semantic meaning -->
<div id="modal-root"></div>
<div id="toast-container" aria-live="polite"></div>

<!-- ✅ Styling group — wraps elements purely to apply CSS -->
<div class="input-group">
  <span class="input-prefix">$</span>
  <input type="number" name="price" />
  <span class="input-suffix">USD</span>
</div>

<!-- ✅ Accordion panel body — wraps toggled content -->
<details>
  <summary>Configuration</summary>
  <div class="panel-body">  <!-- <div> is fine here -->
    <p>Settings go here...</p>
  </div>
</details>
```

---

### The Impact of Semantic HTML

Understanding WHY semantics matter makes you more motivated to use them correctly.

**Screen readers** expose landmark regions to users who can jump directly between them. With all `<div>` elements, there are no landmarks — screen reader users must read everything linearly.

```
With semantic HTML, a screen reader user sees:
  Landmarks: header, navigation (Main), main, complementary (Sidebar), footer
  Headings:  h1 "Blog Post", h2 "Section 1", h2 "Comments"

With div soup, they see:
  Landmarks: (none)
  Headings:  (depends on whether you used heading elements)
```

**Search engines** use semantic structure to understand what's important on your page. Content inside `<article>` is weighted more heavily than content inside `<aside>`. Navigation links in `<nav>` are understood as navigation, not page content.

**Developer experience** — semantic HTML is self-documenting. A new developer reading your code immediately understands the page structure from the element names alone, without reading any class names or comments.

```html
<!-- Which is easier to understand at a glance? -->

<!-- Option A: div soup -->
<div class="l-wrapper">
  <div class="l-header">
    <div class="c-logo">...</div>
    <div class="c-nav">...</div>
  </div>
  <div class="l-main">
    <div class="c-article">...</div>
    <div class="c-sidebar">...</div>
  </div>
</div>

<!-- Option B: Semantic HTML -->
<body>
  <header>
    <a href="/">Logo</a>
    <nav>...</nav>
  </header>
  <main>
    <article>...</article>
    <aside>...</aside>
  </main>
</body>
```

---

## Quick Reference Summary

| Element | Purpose | Key Rule |
|---|---|---|
| `<header>` | Introductory/header content | Multiple allowed, one per sectioning context |
| `<footer>` | Closing/supplementary content | Multiple allowed, one per sectioning context |
| `<main>` | Primary page content | Only **one** per page |
| `<nav>` | Major navigation blocks | Use `aria-label` when multiple on page |
| `<aside>` | Tangentially related content | Sidebar, callouts, pull quotes |
| `<section>` | Thematic content group | Always needs a heading |
| `<article>` | Self-contained distributable content | Can be nested |
| `<details>` | Native collapsible widget | No JavaScript needed |
| `<summary>` | Label for `<details>` | Must be first child of `<details>` |
| `<time>` | Dates and times | Always use machine-readable `datetime` |
| `<address>` | Contact information | For author/org contact, not arbitrary addresses |
| `<progress>` | Task completion bar | No `value` = indeterminate |
| `<meter>` | Scalar measurement gauge | Use `low`/`high`/`optimum` for colour zones |
| `<div>` | Generic block container | Use when no semantic element fits |

Semantic HTML is not about being pedantic — it is the foundation of accessible, discoverable, and maintainable web pages. Getting it right costs almost nothing and benefits every single user who visits your site.