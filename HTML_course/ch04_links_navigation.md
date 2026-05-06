# HTML Links & Navigation — Detailed Explanation

---

## 1. The Anchor Tag — `<a>`

The `<a>` element (anchor tag) is the fundamental building block of the web. It creates **hyperlinks** — connections between pages, sections, files, email addresses, phone numbers, and more. Without it, the web would just be a collection of isolated documents.

```html
<a href="https://example.com">Visit Example</a>
```

Everything between the opening and closing tag becomes **clickable**. The `href` attribute defines where clicking takes you.

---

### What Can Go Inside `<a>`?

The anchor tag can wrap almost any content — not just text.

```html
<!-- Text link -->
<a href="/about">About Us</a>

<!-- Image link -->
<a href="/home">
  <img src="logo.png" alt="Company Name — Go to homepage" />
</a>

<!-- Icon + text link -->
<a href="/dashboard">
  <svg>...</svg>
  Dashboard
</a>

<!-- A whole card (block link) -->
<a href="/blog/html-guide" class="card">
  <h3>HTML Complete Guide</h3>
  <p>Learn everything about HTML from scratch.</p>
  <span>Read more →</span>
</a>

<!-- Button styled as a link -->
<a href="/signup" class="btn btn-primary">Get Started</a>
```

**Note on block links (wrapping large content):** Wrapping large blocks like entire cards in `<a>` is valid HTML5. However, make sure the link has meaningful text for screen readers — either visible text or an `aria-label`.

```html
<!-- ✅ Good — visible descriptive text inside -->
<a href="/blog/html-guide" class="card">
  <h3>HTML Complete Guide</h3>
  <p>Learn everything about HTML.</p>
</a>

<!-- ✅ Good — aria-label when inner text isn't descriptive enough -->
<a href="/blog/html-guide" class="card" aria-label="Read article: HTML Complete Guide">
  <img src="thumbnail.jpg" alt="" />
  <span class="tag">HTML</span>
</a>

<!-- ❌ Bad — no text at all, screen reader gets nothing -->
<a href="/blog/html-guide" class="card">
  <img src="thumbnail.jpg" alt="" />
</a>
```

---

## 2. `href` — Hypertext Reference

The `href` attribute defines the **destination** of the link. It accepts several types of values.

---

### Absolute URLs

A full URL including the protocol. Used for linking to **external websites**.

```html
<a href="https://www.google.com">Google</a>
<a href="https://github.com/username/repo">View on GitHub</a>
<a href="http://example.com">Example (HTTP)</a>
```

Always use `https://` for external links where possible — linking to `http://` sends users to an insecure page.

---

### Relative URLs

A path **relative to the current page's location**. Used for linking to pages **within the same website**.

```html
<!-- Link to a page in the same directory -->
<a href="about.html">About</a>

<!-- Link to a page in a subdirectory -->
<a href="blog/html-guide.html">HTML Guide</a>

<!-- Link to a page one level up -->
<a href="../index.html">Home</a>

<!-- Link to a page two levels up -->
<a href="../../contact.html">Contact</a>

<!-- Link from the root of the site (starts with /) -->
<a href="/about">About</a>
<a href="/blog/html-guide">HTML Guide</a>
<a href="/contact">Contact</a>
```

**Root-relative paths (starting with `/`)** are generally the most reliable for internal links in a real project — they work the same regardless of which page you're currently on.

```
Project structure:
/
├── index.html
├── about.html
├── blog/
│   ├── index.html
│   └── html-guide.html
└── contact.html

From blog/html-guide.html:
<a href="../about.html">About</a>       ← relative
<a href="/about.html">About</a>         ← root-relative (preferred)
<a href="/contact.html">Contact</a>     ← root-relative (preferred)
```

---

### Fragment Identifiers — `#id`

Links to a **specific section** of a page by targeting an element's `id`. Clicking the link scrolls the page to that element. Covered in full detail in Section 4.

```html
<a href="#introduction">Jump to Introduction</a>
<a href="/about#team">Our Team</a>
```

---

### `javascript:void(0)` — Avoid This

You may encounter this pattern in older code. It was used to make a link that does nothing but still looks clickable.

```html
<!-- ❌ Old bad practice — never use this -->
<a href="javascript:void(0)" onclick="doSomething()">Click me</a>

<!-- ✅ Use a button instead when there's no navigation -->
<button onclick="doSomething()">Click me</button>

<!-- ✅ Or use href="#" with preventDefault in JS -->
<a href="#" id="trigger">Click me</a>
<script>
  document.getElementById("trigger").addEventListener("click", (e) => {
    e.preventDefault();
    doSomething();
  });
</script>
```

If clicking doesn't navigate anywhere, use a `<button>` — not an `<a>`. Anchors are for navigation; buttons are for actions.

---

### Empty or Placeholder `href`

```html
<!-- Placeholder link — goes nowhere yet, shown during development -->
<a href="#">Coming Soon</a>

<!-- No href — technically valid, renders as non-interactive text -->
<a>Not a link yet</a>
```

An `<a>` without `href` is valid but not focusable by keyboard and not announced as a link by screen readers. Always add `href` for real links.

---

## 3. `target` — Where to Open the Link

The `target` attribute controls **where the linked document opens** — in the current tab, a new tab, a specific frame, etc.

---

### `target="_self"` — Same Tab (Default)

```html
<!-- Opens in the same tab — this is the default behaviour -->
<a href="/about" target="_self">About Us</a>

<!-- Same as writing nothing at all -->
<a href="/about">About Us</a>
```

---

### `target="_blank"` — New Tab or Window

```html
<a href="https://github.com" target="_blank">GitHub</a>
```

Opens the link in a **new browser tab** (or new window, depending on browser settings). This is the most commonly used `target` value.

**⚠️ Security Risk — Always use `rel="noopener noreferrer"` with `_blank`:**

Without it, the opened page can access your page via `window.opener` and redirect it — a technique called **reverse tabnapping**. Malicious sites can exploit this.

```html
<!-- ❌ Insecure — vulnerable to reverse tabnapping -->
<a href="https://external-site.com" target="_blank">External Site</a>

<!-- ✅ Secure — always add rel="noopener noreferrer" -->
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">
  External Site
</a>
```

Modern browsers have started defaulting to `noopener` behaviour on `_blank` links, but explicitly adding the `rel` attribute ensures compatibility with all browsers and makes your intent clear.

**When to use `target="_blank"`:**

```html
<!-- ✅ Good — external sites where leaving the current page would be disruptive -->
<a href="https://docs.external-api.com" target="_blank" rel="noopener noreferrer">
  API Documentation ↗
</a>

<!-- ✅ Good — PDF files the user wants to view alongside your page -->
<a href="/reports/q4-2025.pdf" target="_blank" rel="noopener noreferrer">
  Q4 2025 Report (PDF) ↗
</a>

<!-- ❌ Bad — internal navigation links should stay in same tab -->
<a href="/about" target="_blank">About Us</a>
```

**Accessibility consideration:** Opening a new tab without warning disorients users, especially those using screen readers. Always indicate when a link opens in a new tab:

```html
<!-- Method 1: Visual icon + aria-label -->

  href="https://github.com"
  target="_blank"
  rel="noopener noreferrer"
  aria-label="GitHub (opens in new tab)"
>
  GitHub ↗
</a>

<!-- Method 2: Visually hidden text -->
<a href="https://github.com" target="_blank" rel="noopener noreferrer">
  GitHub
  <span class="sr-only">(opens in new tab)</span>
</a>

<style>
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>
```

---

### `target="_parent"` and `target="_top"`

Used in the context of **frames and iframes** — rarely needed in modern web development.

```html
<!-- Opens in the parent frame (one level up) -->
<a href="/page" target="_parent">Go to parent frame</a>

<!-- Breaks out of all frames and opens in the full window -->
<a href="/page" target="_top">Exit iframe and go here</a>
```

`target="_top"` is occasionally useful when your page is embedded in an iframe and you want a link to break out of the iframe and load in the full browser window.

```html
<!-- Inside an iframe — click breaks out to the full window -->
<a href="https://example.com" target="_top">View full site</a>
```

---

### Named Targets

You can target a **specific named iframe** by giving the iframe a `name` attribute and using that name as the `target`.

```html
<!-- The iframe to load content into -->
<iframe name="preview-frame" src="about:blank"></iframe>

<!-- Clicking this link loads the page inside the iframe above -->
<a href="/preview/page-one" target="preview-frame">Preview Page One</a>
<a href="/preview/page-two" target="preview-frame">Preview Page Two</a>
```

---

## 4. `rel` — Relationship

The `rel` attribute describes the **relationship** between the current page and the linked resource. It communicates meaning to browsers, search engines, and assistive technologies.

---

### `rel="noopener noreferrer"`

The most important `rel` value to know. Always used with `target="_blank"`.

```html
<a href="https://external.com" target="_blank" rel="noopener noreferrer">
  External Link
</a>
```

- **`noopener`** — Prevents the new tab from accessing `window.opener` (security)
- **`noreferrer`** — Prevents the browser from sending the `Referer` HTTP header, so the destination site doesn't know which page you came from. It implies `noopener` as well.

---

### `rel="nofollow"`

Tells search engine crawlers **not to follow this link** or pass SEO authority ("link juice") to the destination.

```html
<!-- User-generated content — don't trust it with your SEO -->
<a href="https://user-posted-link.com" rel="nofollow">User's website</a>

<!-- Paid/sponsored links — required by Google guidelines -->
<a href="https://sponsor.com" rel="nofollow sponsored">Our Sponsor</a>

<!-- Comments section links -->
<a href="https://commenter-site.com" rel="nofollow ugc">Commenter's site</a>
```

**`rel` values for link types:**

| Value | Purpose |
|---|---|
| `nofollow` | Don't pass SEO value; don't follow |
| `sponsored` | Link is paid/sponsored |
| `ugc` | User-generated content (comments, forums) |
| `noopener` | Security — prevents `window.opener` access |
| `noreferrer` | Privacy — don't send referrer info |
| `me` | Profile links verifying identity (Mastodon) |
| `author` | Links to the author's page |
| `license` | Links to the license for this content |
| `prev` / `next` | Pagination relationships |

---

### `rel="prev"` and `rel="next"` — Pagination

Used in `<link>` in the `<head>` or in anchor tags to communicate **paginated content** to search engines.

```html
<!-- Page 3 of a multi-page article -->
<a href="/blog/html-guide?page=2" rel="prev">← Previous</a>
<a href="/blog/html-guide?page=4" rel="next">Next →</a>
```

---

### Combining Multiple `rel` Values

Multiple values are separated by a **space**.

```html
<!-- External sponsored link that opens in a new tab -->

  href="https://sponsor.com"
  target="_blank"
  rel="noopener noreferrer nofollow sponsored"
>
  Our Sponsor ↗
</a>
```

---

## 5. `download` — Download a File

The `download` attribute tells the browser to **download the linked file** instead of navigating to it. Works for files on the same origin (same domain) or data URLs.

```html
<!-- Download with the file's original name -->
<a href="/files/report.pdf" download>Download Report</a>

<!-- Download with a custom filename -->
<a href="/files/q4-report-2025.pdf" download="Q4-2025-Annual-Report.pdf">
  Download Q4 Report
</a>

<!-- Download an image -->
<a href="/images/wallpaper.jpg" download="wallpaper.jpg">
  Download Wallpaper
</a>

<!-- Download a generated CSV -->
<a href="/api/export?format=csv" download="users-export.csv">
  Export as CSV
</a>
```

---

### Dynamically Generated Downloads with JavaScript

You can create download links entirely in JavaScript — useful for dynamically generated content.

```js
// Generate a text file and trigger download
function downloadTextFile(content, filename) {
  const blob = new Blob([content], { type: "text/plain" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  a.click();

  URL.revokeObjectURL(url); // Clean up
}

downloadTextFile("Hello, World!", "greeting.txt");

// Generate a CSV and download it
function downloadCSV(data) {
  const csv = data.map(row => row.join(",")).join("\n");
  const blob = new Blob([csv], { type: "text/csv" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "export.csv";
  a.click();

  URL.revokeObjectURL(url);
}

downloadCSV([
  ["Name", "Email", "Role"],
  ["Jane Doe", "jane@example.com", "Admin"],
  ["John Smith", "john@example.com", "Editor"]
]);
```

---

### `download` Limitations

```html
<!-- ✅ Works — same origin file -->
<a href="/files/report.pdf" download>Download</a>

<!-- ✅ Works — data URL -->
<a href="data:text/plain;charset=utf-8,Hello!" download="hello.txt">Download</a>

<!-- ❌ Won't work as download — cross-origin files ignore the attribute -->
<!-- Browser navigates to the file instead of downloading it -->
<a href="https://external-site.com/file.pdf" download>Download</a>
```

For cross-origin downloads, you'd need a server-side proxy or the server must respond with the correct `Content-Disposition: attachment` HTTP header.

---

## 6. Fragment Identifiers — `#id`

Fragment identifiers create links that scroll to a **specific section of a page** by targeting an element's `id` attribute. When clicked, the browser smoothly (or instantly) scrolls the target element into view and updates the URL.

```html
<!-- The link -->
<a href="#introduction">Jump to Introduction</a>

<!-- The target element anywhere on the page -->
<section id="introduction">
  <h2>Introduction</h2>
  <p>Welcome to the guide...</p>
</section>
```

---

### Linking to a Section on Another Page

You can combine a URL with a fragment to link to a **specific section of a different page**.

```html
<!-- Jump to the #pricing section of the /features page -->
<a href="/features#pricing">See Pricing</a>

<!-- Jump to #contact on the homepage from any page -->
<a href="/#contact">Contact Us</a>

<!-- Jump to a section on an external page -->
<a href="https://example.com/docs#installation" rel="noopener noreferrer">
  Installation Guide
</a>
```

---

### Building a Table of Contents

Fragment links are the standard way to build a navigable table of contents.

```html
<!-- Table of contents -->
<nav aria-label="Table of contents">
  <ol>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#installation">Installation</a></li>
    <li>
      <a href="#configuration">Configuration</a>
      <ol>
        <li><a href="#config-basic">Basic Setup</a></li>
        <li><a href="#config-advanced">Advanced Options</a></li>
      </ol>
    </li>
    <li><a href="#api-reference">API Reference</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
  </ol>
</nav>

<!-- Page sections -->
<section id="overview">
  <h2>Overview</h2>
  <p>...</p>
</section>

<section id="installation">
  <h2>Installation</h2>
  <p>...</p>
</section>

<section id="configuration">
  <h2>Configuration</h2>

  <section id="config-basic">
    <h3>Basic Setup</h3>
    <p>...</p>
  </section>

  <section id="config-advanced">
    <h3>Advanced Options</h3>
    <p>...</p>
  </section>
</section>

<section id="api-reference">
  <h2>API Reference</h2>
  <p>...</p>
</section>

<section id="troubleshooting">
  <h2>Troubleshooting</h2>
  <p>...</p>
</section>
```

---

### Skip Navigation Links

A **skip link** is a fragment link that lets keyboard and screen reader users **skip past repetitive navigation** directly to the main content. It's a critical accessibility feature on every page.

```html
<!-- Place this as the very first element inside <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<header>
  <nav>
    <!-- Lots of navigation links... -->
  </nav>
</header>

<main id="main-content">
  <h1>Page Title</h1>
  <p>Main content starts here.</p>
</main>
```

```css
/* Visually hidden by default, visible on focus (keyboard users) */
.skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  background: #1d4ed8;
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 0 0 8px 8px;
  font-weight: 600;
  text-decoration: none;
  z-index: 9999;
  transition: top 0.2s;
}

.skip-link:focus {
  top: 0; /* Slides into view when focused via keyboard Tab */
}
```

When a sighted keyboard user or screen reader user presses `Tab` as their first action on the page, this link appears and they can press `Enter` to jump past the entire navigation directly to the content.

---

### Smooth Scrolling

By default, clicking a fragment link **jumps instantly** to the target. You can enable smooth animated scrolling with CSS:

```css
/* Enable smooth scrolling for the entire page */
html {
  scroll-behavior: smooth;
}
```

Or with JavaScript for more control:

```js
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));

    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });
    }
  });
});
```

**Accessibility note:** Respect the user's motion preferences. Some users have vestibular disorders and prefer reduced motion.

```css
html {
  scroll-behavior: smooth;
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto; /* Instant jump for users who prefer it */
  }
}
```

---

### Scroll Margin — Accounting for Fixed Headers

When you have a **fixed/sticky header**, clicking a fragment link scrolls the target element behind the header. Fix this with `scroll-margin-top`:

```css
/* Push the scroll target down by the height of your fixed header */
section[id],
h2[id],
h3[id] {
  scroll-margin-top: 80px; /* Adjust to match your header height */
}
```

```html
<header style="position: fixed; top: 0; height: 80px;">
  <nav>...</nav>
</header>

<main style="margin-top: 80px;">
  <!-- Without scroll-margin-top, the heading would hide under the header -->
  <section id="installation">
    <h2>Installation</h2>
    <p>...</p>
  </section>
</main>
```

---

## 7. `mailto:` Links — Email Links

The `mailto:` scheme opens the user's **default email client** with a pre-filled compose window.

```html
<!-- Basic email link -->
<a href="mailto:hello@example.com">Send us an email</a>

<!-- With a pre-filled subject -->
<a href="mailto:hello@example.com?subject=Website Enquiry">
  Email us about your website
</a>

<!-- With subject and body -->
<a href="mailto:hello@example.com?subject=Support Request&body=Hello, I need help with...">
  Contact Support
</a>

<!-- Multiple recipients -->
<a href="mailto:jane@example.com,john@example.com?subject=Team Update">
  Email the team
</a>

<!-- With CC and BCC -->
<a href="mailto:primary@example.com?cc=manager@example.com&bcc=archive@example.com&subject=Monthly Report">
  Send Report
</a>
```

---

### Full `mailto:` Parameter Reference

All parameters go after `?` and are separated by `&`:

| Parameter | Description | Example |
|---|---|---|
| (address) | Recipient email | `hello@example.com` |
| `subject` | Email subject line | `subject=Hello` |
| `body` | Pre-filled email body | `body=Hi there` |
| `cc` | Carbon copy recipients | `cc=manager@co.com` |
| `bcc` | Blind carbon copy | `bcc=archive@co.com` |

**Encoding special characters:** Spaces and special characters in values should be URL-encoded. Most browsers handle spaces in `mailto:` links, but it's safer to encode them.

```html
<!-- Properly encoded -->
<a href="mailto:hello@example.com?subject=Website%20Enquiry&body=Hello%2C%0A%0AI%20would%20like%20to%20enquire%20about...">
  Contact Us
</a>
```

In JavaScript you can build these dynamically:

```js
function createMailtoLink(to, subject, body) {
  const params = new URLSearchParams({ subject, body });
  return `mailto:${to}?${params.toString()}`;
}

const link = createMailtoLink(
  "hello@example.com",
  "Website Enquiry",
  "Hello,\n\nI would like to enquire about..."
);

document.querySelector("#contact-link").href = link;
```

---

### Protecting Email Addresses from Spam Bots

`mailto:` links expose email addresses to web crawlers that harvest addresses for spam. Some protective techniques:

```html
<!-- Method 1: CSS direction trick (visual only, not robust) -->
<style>
  .email { unicode-bidi: bidi-override; direction: rtl; }
</style>
<span class="email">moc.elpmaxe@olleh</span>

<!-- Method 2: HTML entity encoding (bots sometimes decode these) -->
<a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#104;&#101;&#108;&#108;&#111;&#64;&#101;&#120;&#97;&#109;&#112;&#108;&#101;&#46;&#99;&#111;&#109;">
  Email Us
</a>

<!-- Method 3: JavaScript obfuscation (most effective) -->
<a href="#" id="email-link">Email Us</a>
<script>
  const user = "hello";
  const domain = "example.com";
  const link = document.getElementById("email-link");
  link.href = `mailto:${user}@${domain}`;
</script>

<!-- Method 4: Contact form (best UX + best spam protection) -->
<a href="/contact">Contact Us</a>
```

The most user-friendly and spam-resistant approach is a **contact form** — it hides the email address entirely and can include CAPTCHA protection.

---

## 8. `tel:` Links — Telephone Links

The `tel:` scheme opens the **phone dialler** on mobile devices or a VOIP app on desktop when clicked. Essential for mobile-first websites.

```html
<!-- Basic phone link -->
<a href="tel:+12125551234">Call Us</a>

<!-- Display formatted, link unformatted -->
<a href="tel:+12125551234">(212) 555-1234</a>

<!-- UK number -->
<a href="tel:+442071234567">+44 20 7123 4567</a>

<!-- With extension (some diallers support it) -->
<a href="tel:+12125551234;ext=42">(212) 555-1234 ext. 42</a>
```

---

### `tel:` Number Formatting Rules

Always use the **E.164 international format** for `href` values — even if you display the number in a local format:

```
+[country code][area code][number]
```

```html
<!-- US: +1 (country) 212 (area) 5551234 (number) -->
<a href="tel:+12125551234">(212) 555-1234</a>

<!-- UK: +44 (country) 20 (area code without leading 0) 71234567 -->
<a href="tel:+442071234567">020 7123 4567</a>

<!-- India: +91 (country) 98765 43210 -->
<a href="tel:+919876543210">+91 98765 43210</a>

<!-- Australia: +61 (country) 2 (area without leading 0) 91234567 -->
<a href="tel:+61291234567">02 9123 4567</a>
```

The `+` in the `href` represents the international dialling prefix. Do not add spaces, dashes, or parentheses in the `href` value — only include digits and `+`.

---

### Real-World Usage Patterns

```html
<!-- Contact section -->
<address>
  <p>
    📞 <a href="tel:+12125551234">(212) 555-1234</a>
  </p>
  <p>
    ✉️ <a href="mailto:hello@example.com">hello@example.com</a>
  </p>
</address>

<!-- Header contact info -->
<header>
  <div class="contact-bar">
    <a href="tel:+12125551234" aria-label="Call us at (212) 555-1234">
      <svg aria-hidden="true"><!-- phone icon --></svg>
      (212) 555-1234
    </a>
    <a href="mailto:hello@example.com" aria-label="Email us">
      <svg aria-hidden="true"><!-- email icon --></svg>
      hello@example.com
    </a>
  </div>
</header>

<!-- Call-to-action button on mobile -->
<a href="tel:+12125551234" class="btn btn-call">
  📞 Call Now — (212) 555-1234
</a>

<!-- Only show on mobile using CSS -->
<style>
  .mobile-only-call { display: none; }

  @media (max-width: 768px) {
    .mobile-only-call { display: inline-flex; }
  }
</style>

<a href="tel:+12125551234" class="mobile-only-call btn">
  Tap to Call
</a>
```

---

### Other Link Schemes

Beyond `mailto:` and `tel:`, there are several other useful URI schemes:

```html
<!-- SMS link — opens messaging app with pre-filled number -->
<a href="sms:+12125551234">Send us a text</a>

<!-- SMS with pre-filled body (iOS/Android syntax varies) -->
<a href="sms:+12125551234?body=Hello, I'd like to book an appointment">
  Book via SMS
</a>

<!-- FaceTime (Apple devices only) -->
<a href="facetime:+12125551234">FaceTime Us</a>
<a href="facetime:hello@example.com">FaceTime via Apple ID</a>

<!-- WhatsApp link -->
<a href="https://wa.me/12125551234" rel="noopener noreferrer">
  WhatsApp Us
</a>

<!-- WhatsApp with pre-filled message -->
<a href="https://wa.me/12125551234?text=Hello%2C%20I%27d%20like%20to%20enquire%20about..." rel="noopener noreferrer">
  Chat on WhatsApp
</a>
```

---

## Complete Navigation Example

Putting it all together — a fully accessible, real-world navigation component:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Example Site</title>
</head>
<body>

  <!-- Skip link — must be first focusable element -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <header>
    <!-- Logo link back to homepage -->
    <a href="/" aria-label="Example Company — Go to homepage">
      <img src="logo.svg" alt="" width="120" height="40" />
    </a>

    <!-- Primary navigation -->
    <nav aria-label="Main navigation">
      <ul>
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/about">About</a></li>
        <li>
          <a href="/services" aria-haspopup="true">Services</a>
          <ul>
            <li><a href="/services/design">Design</a></li>
            <li><a href="/services/development">Development</a></li>
            <li><a href="/services/consulting">Consulting</a></li>
          </ul>
        </li>
        <li>
          
            href="https://blog.example.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            Blog
            <span class="sr-only">(opens in new tab)</span>
          </a>
        </li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>

    <!-- Utility links -->
    <div class="header-utils">
      <a href="tel:+12125551234" aria-label="Call us: (212) 555-1234">
        📞 <span class="hide-mobile">(212) 555-1234</span>
      </a>
      <a href="/get-started" class="btn btn-primary">Get Started</a>
    </div>
  </header>

  <!-- Main content target -->
  <main id="main-content">

    <!-- In-page anchor navigation -->
    <nav aria-label="Page sections">
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#faq">FAQ</a></li>
      </ul>
    </nav>

    <section id="overview">
      <h2>Overview</h2>
      <p>...</p>
    </section>

    <section id="features">
      <h2>Features</h2>
      <p>...</p>
    </section>

    <section id="pricing">
      <h2>Pricing</h2>
      <p>...</p>
    </section>

    <section id="faq">
      <h2>FAQ</h2>
      <p>...</p>
    </section>

  </main>

  <footer>
    <nav aria-label="Footer navigation">
      <ul>
        <li><a href="/privacy" rel="nofollow">Privacy Policy</a></li>
        <li><a href="/terms" rel="nofollow">Terms of Service</a></li>
        <li>
          
            href="https://github.com/example"
            target="_blank"
            rel="noopener noreferrer nofollow"
          >
            GitHub ↗
          </a>
        </li>
      </ul>
    </nav>

    <address>
      <a href="mailto:hello@example.com">hello@example.com</a> ·
      <a href="tel:+12125551234">(212) 555-1234</a>
    </address>

    <!-- Download links -->
    <a href="/assets/brochure.pdf" download="Example-Brochure.pdf">
      Download Brochure (PDF)
    </a>

    <small>© 2026 Example Company. All rights reserved.</small>
  </footer>

</body>
</html>
```

---

## Quick Reference Summary

| Attribute / Feature | Purpose | Example |
|---|---|---|
| `href` (absolute) | Link to external page | `href="https://example.com"` |
| `href` (relative) | Link within same site | `href="/about"` |
| `href="#id"` | Jump to page section | `href="#pricing"` |
| `href="mailto:"` | Open email client | `href="mailto:hi@example.com"` |
| `href="tel:"` | Open phone dialler | `href="tel:+12125551234"` |
| `href="sms:"` | Open messaging app | `href="sms:+12125551234"` |
| `download` | Download file instead of navigating | `download="report.pdf"` |
| `target="_blank"` | Open in new tab | `target="_blank"` |
| `target="_top"` | Break out of iframe | `target="_top"` |
| `rel="noopener noreferrer"` | Security for `_blank` links | Always with `target="_blank"` |
| `rel="nofollow"` | Don't pass SEO value | External / UGC links |
| `rel="sponsored"` | Mark paid links | Affiliate / ad links |
| `aria-current="page"` | Mark active nav item | Current page in nav |
| `aria-label` | Accessible name override | Icon-only or ambiguous links |
| Skip link | Jump to main content | `.skip-link` + `#main-content` |
| `scroll-behavior: smooth` | Smooth scroll to anchors | CSS on `html` element |
| `scroll-margin-top` | Account for fixed header | On section targets |

Links are the foundation of the web's interconnected nature — using them correctly and accessibly ensures every user, regardless of how they browse, can navigate your content with ease.