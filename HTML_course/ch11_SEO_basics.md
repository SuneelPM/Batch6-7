# HTML SEO Basics — Detailed Explanation

Search Engine Optimisation (SEO) is the practice of helping search engines **understand, index, and rank** your pages appropriately. HTML is the foundation of technical SEO — before content quality, backlinks, or any other factor, search engines need to correctly parse and understand your markup.

Modern search engines like Google don't just look for keywords — they try to understand **what a page is about, who it's for, and how authoritative and trustworthy it is**. Good semantic HTML directly serves all three goals.

---

## How Search Engine Crawlers Work

Before diving into techniques, understanding the crawl pipeline helps you make better decisions:

```
1. DISCOVERY    — Crawler finds your URL (via sitemap, backlinks, internal links)
2. CRAWLING     — Googlebot fetches your HTML (like a browser, but headless)
3. RENDERING    — Google renders the page (executes JavaScript, loads CSS)
4. INDEXING     — Google parses, analyses, and stores the page content
5. RANKING      — Google determines where to rank the page for relevant queries
6. SERVING      — Search results displayed to users
```

At the crawling and indexing stages, HTML structure is critical. Crawlers read your HTML to determine:

- What the page is about (title, headings, content)
- How it relates to other pages (internal linking, canonical)
- What type of content it is (structured data)
- How to present it in search results (title, description, rich results)
- Whether to index it at all (meta robots, canonical)

---

## 1. Semantic Structure for Crawlers

Search engines assign **different weights to content** based on where it appears in the document. Content in headings, early paragraphs, and semantic landmark elements carries more significance than content buried in generic divs.

---

### Heading Hierarchy — The Document Outline

The heading structure is one of the first things crawlers analyse to understand a page's topic and subtopics. It creates an outline — like a table of contents — that tells the crawler exactly what the page covers.

```html
<!-- ✅ Clear, hierarchical structure — crawler understands the topic tree -->
<html lang="en">
<head>
  <title>CSS Flexbox Guide — Complete Tutorial with Examples</title>
</head>
<body>
  <main>
    <h1>CSS Flexbox: The Complete Guide</h1>           <!-- Primary topic -->

      <h2>What is Flexbox?</h2>                        <!-- Major subtopic -->
        <h3>Browser Support</h3>                       <!-- Sub-subtopic -->
        <h3>When to Use Flexbox vs Grid</h3>

      <h2>The Flex Container</h2>
        <h3>display: flex</h3>
        <h3>flex-direction</h3>
        <h3>flex-wrap</h3>
        <h3>justify-content</h3>
        <h3>align-items</h3>

      <h2>Flex Items</h2>
        <h3>flex-grow</h3>
        <h3>flex-shrink</h3>
        <h3>flex-basis</h3>

      <h2>Real-World Flexbox Examples</h2>
        <h3>Navigation Bar</h3>
        <h3>Card Grid</h3>
        <h3>Centring Content</h3>
  </main>
</body>
</html>
```

```html
<!-- ❌ Poor structure — crawler struggles to understand the topic tree -->
<body>
  <div class="hero">
    <div class="hero-title">CSS Flexbox: The Complete Guide</div>  <!-- Not an h1 -->
  </div>
  <div class="section">
    <div class="section-header">What is Flexbox?</div>            <!-- Not an h2 -->
    <h3>Browser Support</h3>
    <h1>The Flex Container</h1>   <!-- h1 after h3 — broken hierarchy -->
    <h4>display: flex</h4>        <!-- Skipped h2, h3 -->
  </div>
</body>
```

**Rules for SEO-optimal headings:**
- One `<h1>` per page — matches the page's primary keyword/topic
- `<h1>` text should relate closely to the `<title>` tag (not identical)
- Never skip heading levels — `h2` → `h4` without `h3` signals poor structure
- Put the most important content near the top of the heading hierarchy
- Each heading should accurately describe the content below it

---

### Semantic Elements Signal Content Type

Crawlers understand semantic elements and use them to categorise content:

```html
<!-- <article> signals self-contained, indexable content -->
<article>
  <h1>10 CSS Tips Every Developer Should Know</h1>
  <p>CSS can be complex. Here are ten practical tips...</p>
</article>

<!-- <nav> signals navigation links — less weighted for content -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/css">CSS Guide</a></li>
    <li><a href="/html">HTML Guide</a></li>
  </ul>
</nav>

<!-- <aside> signals supplementary content — lower weight -->
<aside>
  <h2>Related Articles</h2>
  <ul>
    <li><a href="/flexbox">Flexbox Guide</a></li>
  </ul>
</aside>

<!-- <main> signals the primary content — highest weight -->
<main>
  <h1>Primary topic of this page</h1>
  <p>This content is what the page is fundamentally about...</p>
</main>
```

Content inside `<main>` and `<article>` is weighted more heavily than content in `<aside>`, `<nav>`, or `<footer>`. This is why semantic HTML directly impacts rankings — not just accessibility.

---

### URL Structure and Internal Linking

Crawlers follow links to discover and understand relationships between pages. Your internal linking structure is a map of your site's architecture:

```html
<!-- ✅ Descriptive anchor text — tells crawlers what the linked page is about -->
<p>
  Learn more about
  <a href="/css/flexbox-guide">CSS Flexbox layout</a>
  and how it compares to
  <a href="/css/grid-guide">CSS Grid</a>.
</p>

<!-- ❌ Generic anchor text — no signal about destination content -->
<p>
  For layout techniques, <a href="/css/flexbox-guide">click here</a>
  or <a href="/css/grid-guide">read more</a>.
</p>

<!-- ❌ Keyword-stuffed anchor text — over-optimised, looks spammy -->
<p>
  Our <a href="/css/flexbox-guide">
    CSS flexbox guide tutorial learn flexbox CSS layout
  </a> covers everything.
</p>
```

**Internal linking best practices:**
- Use descriptive, natural anchor text that describes the destination
- Link related content together to build topical clusters
- Avoid orphan pages (pages with no internal links pointing to them)
- Use breadcrumb navigation to signal page hierarchy

```html
<!-- Breadcrumb navigation — signals page hierarchy to crawlers -->
<nav aria-label="Breadcrumb">
  <ol>
    <li>
      <a href="/">Home</a>
    </li>
    <li>
      <a href="/css">CSS</a>
    </li>
    <li>
      <a href="/css/layout">Layout</a>
    </li>
    <li aria-current="page">
      Flexbox Guide
    </li>
  </ol>
</nav>
```

---

### Image Optimisation for Crawlers

```html
<!-- ✅ SEO-optimised image -->
<figure>
  <img
    src="/images/css-flexbox-diagram.webp"
    alt="Diagram showing flex container with three flex items arranged in a row using justify-content: space-between"
    width="800"
    height="450"
    loading="lazy"
    decoding="async"
  />
  <figcaption>
    CSS Flexbox container with <code>justify-content: space-between</code>
    applied to three flex items
  </figcaption>
</figure>

<!-- ❌ Images crawlers can't understand -->
<img src="img001.jpg" />                     <!-- No alt, meaningless filename -->
<img src="photo.jpg" alt="image" />          <!-- Vague alt text -->
<img src="DSC_3847.jpg" alt="" />            <!-- Decorative alt on informative image -->
```

**Image SEO checklist:**
- Descriptive filename (hyphens, not underscores) — `css-flexbox-diagram.webp`
- Specific, descriptive `alt` text
- Use modern formats (WebP, AVIF) for performance
- Specify `width` and `height` to prevent layout shift (good Core Web Vitals)
- Use `loading="lazy"` for below-fold images (good LCP score)

---

### Page Speed and Core Web Vitals

Google uses **Core Web Vitals** as ranking signals. Several are directly influenced by HTML:

```html
<!-- LCP (Largest Contentful Paint) — load hero images fast -->
<!-- Preload the hero image — don't lazy load it -->
<link rel="preload" as="image" href="/images/hero.webp" fetchpriority="high" />

<img
  src="/images/hero.webp"
  alt="Frontend development workspace"
  width="1200"
  height="630"
  fetchpriority="high"   <!-- Prioritise loading -->
  loading="eager"        <!-- Never lazy-load the LCP image -->
/>

<!-- CLS (Cumulative Layout Shift) — reserve space for images -->
<!-- Always specify width and height to prevent layout shift -->
<img src="photo.webp" alt="..." width="800" height="600" />

<!-- FID/INP — defer non-critical scripts -->
<script src="analytics.js" defer></script>
<script src="app.js" defer></script>
<script src="ads.js" async></script>

<!-- Preconnect to critical third-party origins -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
```

---

## 2. `<title>` and `<meta name="description">`

These two elements are the **most direct HTML SEO levers** — they control what appears in search engine result pages (SERPs).

---

### `<title>` — The Page Title Tag

The `<title>` tag defines the clickable headline in search results. It is the single most important on-page SEO element.

```html
<head>
  <title>CSS Flexbox Guide: Complete Tutorial with Examples (2026)</title>
</head>
```

This renders in Google search results as the blue clickable link:

```
CSS Flexbox Guide: Complete Tutorial with Examples (2026)
https://example.com/css/flexbox-guide
A comprehensive guide to CSS Flexbox covering all properties...
```

---

#### Writing Effective Title Tags

```html
<!-- ✅ Good title tag patterns -->

<!-- Primary keyword first + brand at end -->
<title>CSS Flexbox Guide — Complete Tutorial | Frontend Academy</title>

<!-- Question format for informational queries -->
<title>What is CSS Flexbox? A Complete Beginner's Guide</title>

<!-- Year for evergreen content that benefits from freshness signal -->
<title>Best CSS Layout Techniques (2026) — Flexbox, Grid & More</title>

<!-- Product page — name + key attributes + brand -->
<title>MacBook Pro 14" M4 Pro 512GB — Apple</title>

<!-- Category page — category name + site name -->
<title>CSS Tutorials & Guides — Frontend Academy</title>

<!-- Homepage — brand name + value proposition -->
<title>Frontend Academy — Learn HTML, CSS & JavaScript</title>

<!-- ❌ Bad title tag patterns -->

<!-- Too vague — no keywords -->
<title>Page 1</title>
<title>Home</title>
<title>Welcome</title>
<title>Untitled Document</title>

<!-- Keyword stuffed — looks spammy, Google rewrites it -->
<title>Flexbox CSS Flexbox Tutorial Learn Flexbox CSS Layout Flexbox Guide</title>

<!-- Too long — gets truncated in SERPs (limit ~60 characters) -->
<title>
  A Complete and Comprehensive Guide to Understanding CSS Flexbox Layout
  Including All Properties, Values, and Real World Examples for Beginners
  and Advanced Developers Alike
</title>

<!-- Duplicate — every page has the same title -->
<title>Frontend Academy</title>  <!-- Used on every single page -->
```

**Title tag rules:**

| Rule | Detail |
|---|---|
| Character limit | ~60 characters (600px pixel width) — longer gets truncated |
| Primary keyword | Include it naturally, ideally near the start |
| Brand name | Include it, usually at the end separated by `—` or `\|` |
| Uniqueness | Every page must have a unique title |
| Accuracy | Must accurately describe the page content |
| Avoid | Keyword stuffing, all caps, vague titles |

**Note:** Google sometimes rewrites your title tag in search results if it determines another option better represents the page. Good semantic HTML (especially your `<h1>`) reduces the chance of this.

---

### `<meta name="description">` — The Search Snippet

The meta description appears as the descriptive text under the title in search results. While Google doesn't use it as a direct ranking signal, it heavily influences **click-through rate (CTR)** — which is a ranking signal.

```html
<head>
  <meta
    name="description"
    content="Learn CSS Flexbox from scratch with this complete guide. Covers flex containers, flex items, alignment, wrapping, and real-world layout examples. No prior knowledge required."
  />
</head>
```

This appears in SERPs as:

```
CSS Flexbox Guide: Complete Tutorial with Examples (2026)
https://example.com/css/flexbox-guide
Learn CSS Flexbox from scratch with this complete guide. Covers flex
containers, flex items, alignment, wrapping, and real-world layout...
```

---

#### Writing Effective Meta Descriptions

```html
<!-- ✅ Good meta descriptions -->

<!-- Informational article — what they'll learn + who it's for -->
<meta
  name="description"
  content="Master CSS Flexbox with this step-by-step guide. Learn flex containers, alignment, wrapping, and responsive layouts with interactive examples. Perfect for beginners."
/>

<!-- Product page — key features + call to action -->
<meta
  name="description"
  content="MacBook Pro 14-inch with M4 Pro chip. Up to 24-core GPU, 48GB unified memory, and 22-hour battery life. Free delivery and returns. Configure yours today."
/>

<!-- Service page — what you offer + differentiator -->
<meta
  name="description"
  content="Professional web development services for startups and enterprises. React, Node.js, and AWS expertise. Fixed-price projects with 30-day post-launch support."
/>

<!-- Category page — what's in it + quantity signal -->
<meta
  name="description"
  content="Browse 200+ CSS tutorials covering selectors, layout, animations, and responsive design. From beginner basics to advanced techniques, all with code examples."
/>

<!-- ❌ Bad meta descriptions -->

<!-- Too short — wastes valuable snippet space -->
<meta name="description" content="A CSS guide." />

<!-- Keyword stuffed — reads unnaturally, won't increase CTR -->
<meta
  name="description"
  content="CSS flexbox flexbox CSS flex layout CSS flexbox tutorial CSS flexbox guide learn flexbox"
/>

<!-- Generic — could apply to any page, doesn't entice clicking -->
<meta
  name="description"
  content="Welcome to our website. We have lots of great content for you to read."
/>

<!-- Too long — truncated in SERPs (limit ~155–160 characters) -->
<meta
  name="description"
  content="This is an incredibly comprehensive, detailed, and thorough guide to CSS Flexbox that covers every single property and value in exhaustive detail with many many examples..."
/>
```

**Meta description rules:**

| Rule | Detail |
|---|---|
| Character limit | ~155–160 characters — longer gets truncated |
| Include keywords | Google **bolds** matching search terms in the snippet |
| Call to action | "Learn", "Discover", "Get started", "Browse" — entices clicks |
| Uniqueness | Every page must have a unique description |
| Accuracy | Must match the page content — Google penalises misleading snippets |
| No quotes | Double quotes can truncate the description in some parsers |

---

### The Full `<head>` SEO Setup

```html
<head>
  <!-- Always first -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- Core SEO -->
  <title>CSS Flexbox Guide: Complete Tutorial with Examples (2026)</title>
  <meta
    name="description"
    content="Master CSS Flexbox with this step-by-step guide covering flex containers, alignment, wrapping, and real-world responsive layout examples."
  />

  <!-- Crawler directives -->
  <meta name="robots" content="index, follow" />
  <!-- or for pages you don't want indexed: -->
  <!-- <meta name="robots" content="noindex, nofollow" /> -->

  <!-- Canonical URL (prevents duplicate content) -->
  <link rel="canonical" href="https://example.com/css/flexbox-guide" />

  <!-- Hreflang for multilingual sites -->
  <link rel="alternate" hreflang="en" href="https://example.com/css/flexbox-guide" />
  <link rel="alternate" hreflang="es" href="https://example.com/es/css/guia-flexbox" />
  <link rel="alternate" hreflang="fr" href="https://example.com/fr/css/guide-flexbox" />
  <link rel="alternate" hreflang="x-default" href="https://example.com/css/flexbox-guide" />

  <!-- Open Graph -->
  <meta property="og:title" content="CSS Flexbox Guide: Complete Tutorial with Examples" />
  <meta property="og:description" content="Master CSS Flexbox with this step-by-step guide covering containers, alignment, wrapping, and responsive layouts." />
  <meta property="og:image" content="https://example.com/images/og/flexbox-guide.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="CSS Flexbox Guide cover image showing flex layout diagram" />
  <meta property="og:url" content="https://example.com/css/flexbox-guide" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Frontend Academy" />
  <meta property="og:locale" content="en_US" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@frontendacademy" />
  <meta name="twitter:creator" content="@janedoe" />
  <meta name="twitter:title" content="CSS Flexbox Guide: Complete Tutorial with Examples" />
  <meta name="twitter:description" content="Master CSS Flexbox with this step-by-step guide covering containers, alignment, wrapping, and responsive layouts." />
  <meta name="twitter:image" content="https://example.com/images/twitter/flexbox-guide.jpg" />
  <meta name="twitter:image:alt" content="CSS Flexbox Guide cover showing flex layout diagram" />

  <!-- Performance -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="icon" type="image/png" href="/favicon.png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />

  <!-- Web App Manifest -->
  <link rel="manifest" href="/site.webmanifest" />
</head>
```

---

## 3. Open Graph and Twitter Card Meta Tags

Open Graph (OG) tags and Twitter Card tags control how your page appears when **shared on social media** — Facebook, LinkedIn, Twitter/X, WhatsApp, Slack, Discord, iMessage, and more. Without them, platforms guess what to show — usually poorly.

---

### Open Graph Protocol

Open Graph was created by Facebook and is now the universal standard adopted by virtually every social platform and messaging app.

```html
<!-- The four required OG tags — minimum for any page -->
<meta property="og:title" content="Page Title Here" />
<meta property="og:type" content="website" />
<meta property="og:image" content="https://example.com/og-image.jpg" />
<meta property="og:url" content="https://example.com/page-url" />
```

---

### `og:type` Values

The `type` tells platforms what kind of content this is, enabling type-specific features:

```html
<!-- Generic page or homepage -->
<meta property="og:type" content="website" />

<!-- Blog posts, news articles -->
<meta property="og:type" content="article" />

<!-- Product pages (used with og:price etc.) -->
<meta property="og:type" content="product" />

<!-- Video content -->
<meta property="og:type" content="video.movie" />
<meta property="og:type" content="video.episode" />
<meta property="og:type" content="video.tv_show" />

<!-- Audio content -->
<meta property="og:type" content="music.song" />
<meta property="og:type" content="music.album" />

<!-- Books -->
<meta property="og:type" content="book" />

<!-- User profiles -->
<meta property="og:type" content="profile" />
```

---

### Article-specific Open Graph Tags

When `og:type` is `article`, additional tags provide richer metadata:

```html
<meta property="og:type" content="article" />

<!-- Article-specific tags -->
<meta property="article:published_time" content="2026-02-23T09:00:00Z" />
<meta property="article:modified_time"  content="2026-02-23T14:30:00Z" />
<meta property="article:author"         content="https://example.com/authors/jane-doe" />
<meta property="article:section"        content="CSS" />
<meta property="article:tag"            content="CSS" />
<meta property="article:tag"            content="Flexbox" />
<meta property="article:tag"            content="Layout" />
<meta property="article:expiration_time" content="2027-01-01T00:00:00Z" />
```

---

### OG Image Specifications

The OG image is the **most important visual element** in a social share card. Platform specifications:

```html
<!-- Recommended: 1200×630px, under 1MB -->
<meta property="og:image"        content="https://example.com/og/flexbox-guide.jpg" />
<meta property="og:image:width"  content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:type"   content="image/jpeg" />
<meta property="og:image:alt"    content="CSS Flexbox Guide — diagram showing flex container properties" />

<!-- Provide a secure HTTPS version explicitly -->
<meta property="og:image:secure_url" content="https://example.com/og/flexbox-guide.jpg" />

<!-- Multiple images — first is preferred, others are fallbacks -->
<meta property="og:image" content="https://example.com/og/flexbox-1200x630.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />

<meta property="og:image" content="https://example.com/og/flexbox-600x315.jpg" />
<meta property="og:image:width" content="600" />
<meta property="og:image:height" content="315" />
```

**OG image requirements by platform:**

| Platform | Min Size | Recommended | Max File Size | Aspect Ratio |
|---|---|---|---|---|
| Facebook | 200×200 | 1200×630 | 8MB | 1.91:1 |
| LinkedIn | 200×200 | 1200×627 | 5MB | ~1.91:1 |
| Twitter | 144×144 | 1200×628 | 5MB (card) | 2:1 |
| WhatsApp | — | 1200×630 | — | 1.91:1 |
| Slack | — | 1200×630 | — | 1.91:1 |

**Generating dynamic OG images** — rather than static images, many sites generate OG images programmatically (using tools like Vercel's `@vercel/og`, Cloudinary URL API, or Puppeteer):

```html
<!-- Cloudinary dynamic OG image with title overlay -->
<meta
  property="og:image"
  content="https://res.cloudinary.com/example/image/upload/w_1200,h_630,c_fill/l_text:Arial_48_bold:CSS%20Flexbox%20Guide/og-template.jpg"
/>
```

---

### Full Open Graph Implementation by Page Type

```html
<!-- ── Homepage ── -->
<meta property="og:title"       content="Frontend Academy — Learn HTML, CSS & JavaScript" />
<meta property="og:description" content="Free, comprehensive tutorials for web developers. From HTML basics to advanced JavaScript patterns." />
<meta property="og:image"       content="https://frontendacademy.com/og/homepage.jpg" />
<meta property="og:url"         content="https://frontendacademy.com/" />
<meta property="og:type"        content="website" />
<meta property="og:site_name"   content="Frontend Academy" />
<meta property="og:locale"      content="en_US" />

<!-- ── Blog post ── -->
<meta property="og:title"       content="CSS Flexbox: The Complete Guide" />
<meta property="og:description" content="Everything you need to know about CSS Flexbox — from basic concepts to advanced real-world layout patterns." />
<meta property="og:image"       content="https://frontendacademy.com/og/flexbox-guide.jpg" />
<meta property="og:image:alt"   content="CSS Flexbox guide cover image" />
<meta property="og:url"         content="https://frontendacademy.com/css/flexbox-guide" />
<meta property="og:type"        content="article" />
<meta property="og:site_name"   content="Frontend Academy" />
<meta property="article:published_time" content="2026-02-23T09:00:00Z" />
<meta property="article:author"         content="https://frontendacademy.com/authors/jane-doe" />
<meta property="article:tag"            content="CSS" />
<meta property="article:tag"            content="Flexbox" />

<!-- ── Product page (e-commerce) ── -->
<meta property="og:title"       content="MacBook Pro 14-inch M4 Pro" />
<meta property="og:description" content="Supercharged by M4 Pro. Up to 24-core GPU and 48GB unified memory. From $1,999." />
<meta property="og:image"       content="https://example.com/og/macbook-pro-14.jpg" />
<meta property="og:url"         content="https://example.com/products/macbook-pro-14" />
<meta property="og:type"        content="product" />
<meta property="product:price:amount"   content="1999.00" />
<meta property="product:price:currency" content="USD" />
```

---

### Twitter / X Card Tags

Twitter reads OG tags as fallbacks, but its own `twitter:` tags take priority when both are present.

```html
<!-- Card type — choose one -->
<meta name="twitter:card" content="summary_large_image" />
<!--
  summary              — Small square thumbnail + text (good for general pages)
  summary_large_image  — Large 2:1 banner image + text (recommended for articles)
  app                  — Mobile app card with download links
  player               — Video/audio player embedded in tweet
-->

<!-- Site and author handles -->
<meta name="twitter:site"    content="@frontendacademy" />  <!-- Site's Twitter handle -->
<meta name="twitter:creator" content="@janedoe" />           <!-- Author's Twitter handle -->

<!-- Content -->
<meta name="twitter:title"       content="CSS Flexbox: The Complete Guide" />
<meta name="twitter:description" content="Everything you need to know about CSS Flexbox — from basic concepts to advanced real-world layout patterns." />
<meta name="twitter:image"       content="https://frontendacademy.com/og/flexbox-guide.jpg" />
<meta name="twitter:image:alt"   content="CSS Flexbox guide cover image showing flex layout diagram" />

<!-- For app cards -->
<meta name="twitter:app:name:iphone"    content="My App" />
<meta name="twitter:app:id:iphone"      content="123456789" />
<meta name="twitter:app:name:googleplay" content="My App" />
<meta name="twitter:app:id:googleplay"  content="com.example.myapp" />
```

---

### Testing Social Cards

Always test your OG tags before publishing. Official debugging tools:

```html
<!--
  Facebook Sharing Debugger:     https://developers.facebook.com/tools/debug/
  Twitter Card Validator:        https://cards-dev.twitter.com/validator
  LinkedIn Post Inspector:       https://www.linkedin.com/post-inspector/
  Open Graph Check (general):    https://www.opengraph.xyz/

  These tools show exactly how your page will look when shared,
  and let you force a re-scrape if you've updated your OG tags.
-->
```

---

## 4. Canonical Links

A **canonical link** tells search engines which URL is the **definitive, authoritative version** of a page when the same or very similar content is accessible at multiple URLs.

```html
<link rel="canonical" href="https://example.com/css/flexbox-guide" />
```

---

### Why Duplicate Content Happens

Without canonicals, Google discovers the same content at multiple URLs and must guess which to index — it often guesses wrong, splitting your ranking signals:

```
Same page accessible at:
https://example.com/css/flexbox-guide          ← your preferred URL
https://example.com/css/flexbox-guide/         ← trailing slash variant
https://example.com/css/flexbox-guide?ref=newsletter  ← UTM parameter
https://example.com/css/flexbox-guide?sort=date      ← filter parameter
https://example.com/css/flexbox-guide?page=1         ← pagination parameter
http://example.com/css/flexbox-guide           ← HTTP version
https://www.example.com/css/flexbox-guide      ← www subdomain variant
https://example.com/CSS/Flexbox-Guide          ← case variant
```

All of these can be crawled independently, causing duplicate content issues. Canonical tags consolidate them.

---

### Self-Referencing Canonicals

Every page should have a canonical tag pointing to itself — even if you have no duplicates. This defends against external sites scraping your content and republishing it:

```html
<!-- On https://example.com/css/flexbox-guide -->
<link rel="canonical" href="https://example.com/css/flexbox-guide" />

<!-- On https://example.com/about -->
<link rel="canonical" href="https://example.com/about" />

<!-- On https://example.com/ -->
<link rel="canonical" href="https://example.com/" />
```

---

### Canonicalising Duplicate and Variant URLs

```html
<!-- All variants of the page point to the canonical URL -->

<!-- On https://example.com/css/flexbox-guide?ref=newsletter -->
<link rel="canonical" href="https://example.com/css/flexbox-guide" />

<!-- On https://example.com/css/flexbox-guide?sort=date -->
<link rel="canonical" href="https://example.com/css/flexbox-guide" />

<!-- On https://example.com/css/flexbox-guide/ (trailing slash) -->
<link rel="canonical" href="https://example.com/css/flexbox-guide" />

<!-- On http://example.com/css/flexbox-guide (HTTP) -->
<link rel="canonical" href="https://example.com/css/flexbox-guide" />
```

---

### Pagination and Canonical

Paginated content (page 2, 3 of a blog listing) should canonicalise to themselves — not to page 1:

```html
<!-- Page 1 of blog listing — canonical to itself -->
<!-- https://example.com/blog -->
<link rel="canonical" href="https://example.com/blog" />
<link rel="next" href="https://example.com/blog?page=2" />

<!-- Page 2 — canonical to itself, not page 1 -->
<!-- https://example.com/blog?page=2 -->
<link rel="canonical" href="https://example.com/blog?page=2" />
<link rel="prev" href="https://example.com/blog" />
<link rel="next" href="https://example.com/blog?page=3" />

<!-- Page 3 -->
<!-- https://example.com/blog?page=3 -->
<link rel="canonical" href="https://example.com/blog?page=3" />
<link rel="prev" href="https://example.com/blog?page=2" />
```

---

### Cross-Domain Canonicals — Syndicated Content

When you publish your content on another site (Medium, dev.to, LinkedIn Articles), the republished page should point back to your original:

```html
<!-- Your original article at: https://yourblog.com/flexbox-guide -->
<link rel="canonical" href="https://yourblog.com/flexbox-guide" />

<!-- The Medium republication should have: -->
<!-- published on medium.com/your-article -->
<link rel="canonical" href="https://yourblog.com/flexbox-guide" />
<!-- This tells Google your original is the authoritative version -->
```

---

### Canonical Common Mistakes

```html
<!-- ❌ Relative URL — must be absolute -->
<link rel="canonical" href="/css/flexbox-guide" />

<!-- ✅ Absolute URL with protocol and domain -->
<link rel="canonical" href="https://example.com/css/flexbox-guide" />

<!-- ❌ Canonical pointing to a redirect — should point to final destination -->
<link rel="canonical" href="https://example.com/old-url" />
<!-- (old-url redirects to new-url) -->

<!-- ✅ Point directly to the final, live URL -->
<link rel="canonical" href="https://example.com/new-url" />

<!-- ❌ Multiple canonical tags — Google may ignore both -->
<link rel="canonical" href="https://example.com/page-a" />
<link rel="canonical" href="https://example.com/page-b" />

<!-- ✅ One canonical per page only -->
<link rel="canonical" href="https://example.com/page-a" />

<!-- ❌ Canonical pointing to a noindex page -->
<link rel="canonical" href="https://example.com/page" />
<!-- But /page has <meta name="robots" content="noindex" /> -->
<!-- Conflicting signals — Google may ignore the canonical -->
```

---

## 5. Structured Data — Schema.org

Structured data is **machine-readable metadata** embedded in your HTML that tells search engines precisely what your content is — not just what the words say, but the semantic meaning. It enables **rich results** (also called rich snippets) in SERPs — star ratings, FAQ dropdowns, breadcrumbs, event listings, recipe cards, and more.

The most common format is **JSON-LD** (JavaScript Object Notation for Linked Data) — a `<script>` block in your `<head>` containing structured data. Google recommends JSON-LD over the alternatives (Microdata, RDFa).

---

### JSON-LD Basics

```html
<head>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "CSS Flexbox: The Complete Guide",
    "description": "Master CSS Flexbox with this comprehensive guide.",
    "author": {
      "@type": "Person",
      "name": "Jane Doe",
      "url": "https://example.com/authors/jane-doe"
    },
    "datePublished": "2026-02-23T09:00:00Z",
    "dateModified": "2026-02-23T14:30:00Z"
  }
  </script>
</head>
```

`@context` tells parsers to use the Schema.org vocabulary. `@type` specifies the content type. Everything else is type-specific properties.

---

### Article Schema

For blog posts, news articles, and tutorial content:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "CSS Flexbox: The Complete Guide",
  "description": "Master CSS Flexbox with this step-by-step guide covering flex containers, alignment, and real-world examples.",
  "image": {
    "@type": "ImageObject",
    "url": "https://example.com/images/flexbox-guide.jpg",
    "width": 1200,
    "height": 630
  },
  "author": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://example.com/authors/jane-doe",
    "sameAs": [
      "https://twitter.com/janedoe",
      "https://linkedin.com/in/janedoe"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Frontend Academy",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png",
      "width": 200,
      "height": 60
    }
  },
  "datePublished": "2026-02-23T09:00:00Z",
  "dateModified": "2026-02-23T14:30:00Z",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/css/flexbox-guide"
  },
  "keywords": ["CSS", "Flexbox", "Web Development", "Frontend", "Layout"],
  "articleSection": "CSS",
  "wordCount": 3500,
  "inLanguage": "en-US"
}
</script>
```

---

### FAQ Schema — FAQ Rich Results

FAQ schema can make your page display expandable questions directly in Google Search:

```html
<!-- The visible FAQ content on the page -->
<section>
  <h2>Frequently Asked Questions</h2>

  <details>
    <summary>What is CSS Flexbox?</summary>
    <p>CSS Flexbox is a one-dimensional layout model that allows you to distribute space and align items in a container, even when their sizes are unknown or dynamic.</p>
  </details>

  <details>
    <summary>When should I use Flexbox vs CSS Grid?</summary>
    <p>Use Flexbox for one-dimensional layouts — arranging items in a single row or column. Use CSS Grid for two-dimensional layouts — controlling both rows and columns simultaneously.</p>
  </details>

  <details>
    <summary>Is Flexbox supported in all browsers?</summary>
    <p>Yes. CSS Flexbox is supported in all modern browsers including Chrome, Firefox, Safari, Edge, and Opera. Global browser support is over 99%.</p>
  </details>
</section>

<!-- Matching structured data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is CSS Flexbox?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CSS Flexbox is a one-dimensional layout model that allows you to distribute space and align items in a container, even when their sizes are unknown or dynamic."
      }
    },
    {
      "@type": "Question",
      "name": "When should I use Flexbox vs CSS Grid?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use Flexbox for one-dimensional layouts — arranging items in a single row or column. Use CSS Grid for two-dimensional layouts — controlling both rows and columns simultaneously."
      }
    },
    {
      "@type": "Question",
      "name": "Is Flexbox supported in all browsers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. CSS Flexbox is supported in all modern browsers including Chrome, Firefox, Safari, Edge, and Opera. Global browser support is over 99%."
      }
    }
  ]
}
</script>
```

This can produce a SERP result like:

```
CSS Flexbox: The Complete Guide
https://example.com/css/flexbox-guide

What is CSS Flexbox?                                    ▼
When should I use Flexbox vs CSS Grid?                  ▼
Is Flexbox supported in all browsers?                   ▼
```

---

### BreadcrumbList Schema

Breadcrumb structured data creates a breadcrumb trail directly in search results:

```html
<!-- Visible breadcrumb -->
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="https://example.com/">Home</a></li>
    <li><a href="https://example.com/css">CSS</a></li>
    <li><a href="https://example.com/css/layout">Layout</a></li>
    <li aria-current="page">Flexbox Guide</li>
  </ol>
</nav>

<!-- Structured data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "CSS",
      "item": "https://example.com/css"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Layout",
      "item": "https://example.com/css/layout"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Flexbox Guide",
      "item": "https://example.com/css/flexbox-guide"
    }
  ]
}
</script>
```

Produces SERP result: `example.com › css › layout › Flexbox Guide`

---

### Organization Schema — Knowledge Panel

Helps Google understand your organisation and may populate the knowledge panel on branded searches:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Frontend Academy",
  "alternateName": "FEA",
  "url": "https://frontendacademy.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://frontendacademy.com/logo.png",
    "width": 300,
    "height": 100
  },
  "description": "Free, comprehensive tutorials for web developers covering HTML, CSS, and JavaScript.",
  "foundingDate": "2020",
  "founders": [
    {
      "@type": "Person",
      "name": "Jane Doe"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street",
    "addressLocality": "San Francisco",
    "addressRegion": "CA",
    "postalCode": "94105",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-415-555-1234",
    "contactType": "customer support",
    "email": "hello@frontendacademy.com",
    "availableLanguage": ["English"]
  },
  "sameAs": [
    "https://twitter.com/frontendacademy",
    "https://github.com/frontendacademy",
    "https://linkedin.com/company/frontendacademy",
    "https://youtube.com/frontendacademy"
  ]
}
</script>
```

---

### WebSite Schema — Sitelinks Search Box

Enables Google to show a search box directly in your SERP listing for branded searches:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Frontend Academy",
  "url": "https://frontendacademy.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://frontendacademy.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
</script>
```

---

### Product Schema — E-commerce Rich Results

Enables star ratings, price, and availability in SERPs:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Advanced CSS Course",
  "description": "Master CSS with 40 hours of video content, coding challenges, and real-world projects.",
  "image": [
    "https://example.com/courses/advanced-css/cover.jpg"
  ],
  "sku": "CSS-ADV-001",
  "brand": {
    "@type": "Brand",
    "name": "Frontend Academy"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/courses/advanced-css",
    "priceCurrency": "USD",
    "price": "99.00",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": {
      "@type": "Organization",
      "name": "Frontend Academy"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "1247",
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "Alice Johnson"
      },
      "reviewBody": "Best CSS course I've taken. The projects are very realistic."
    }
  ]
}
</script>
```

---

### HowTo Schema — Step-by-step Guides

Can produce rich results with steps shown directly in SERPs:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Centre a Div with CSS Flexbox",
  "description": "A step-by-step guide to perfectly centring any element using CSS Flexbox.",
  "totalTime": "PT5M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "USD",
    "value": "0"
  },
  "tool": [
    {
      "@type": "HowToTool",
      "name": "Text editor"
    },
    {
      "@type": "HowToTool",
      "name": "Web browser"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Create the container",
      "text": "Create a parent div element that will act as the flex container.",
      "image": "https://example.com/steps/step1.jpg",
      "url": "https://example.com/center-div-flexbox#step-1"
    },
    {
      "@type": "HowToStep",
      "name": "Apply display: flex",
      "text": "Add display: flex to the container's CSS to enable flexbox.",
      "url": "https://example.com/center-div-flexbox#step-2"
    },
    {
      "@type": "HowToStep",
      "name": "Centre horizontally",
      "text": "Add justify-content: center to centre the child element horizontally.",
      "url": "https://example.com/center-div-flexbox#step-3"
    },
    {
      "@type": "HowToStep",
      "name": "Centre vertically",
      "text": "Add align-items: center and set a height on the container to centre vertically.",
      "url": "https://example.com/center-div-flexbox#step-4"
    }
  ]
}
</script>
```

---

### Multiple Schema Types on One Page

A page can have multiple `<script type="application/ld+json">` blocks:

```html
<head>
  <!-- Article schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "CSS Flexbox: The Complete Guide"
    ...
  }
  </script>

  <!-- Breadcrumb schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [...]
  }
  </script>

  <!-- FAQ schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [...]
  }
  </script>
</head>
```

Or combine them using `@graph`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://example.com/flexbox-guide#article",
      "headline": "CSS Flexbox: The Complete Guide"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://example.com/flexbox-guide#breadcrumb",
      "itemListElement": [...]
    },
    {
      "@type": "WebPage",
      "@id": "https://example.com/flexbox-guide",
      "breadcrumb": { "@id": "https://example.com/flexbox-guide#breadcrumb" },
      "mainEntity": { "@id": "https://example.com/flexbox-guide#article" }
    }
  ]
}
</script>
```

---

### Testing and Validating Structured Data

```html
<!--
  Google Rich Results Test:
  https://search.google.com/test/rich-results
  — Tests if your page is eligible for rich results
  — Shows which schema types were detected
  — Shows any errors or warnings

  Schema.org Validator:
  https://validator.schema.org/
  — Validates your JSON-LD against the schema.org spec
  — More comprehensive than Google's tool

  Google Search Console:
  https://search.google.com/search-console
  — "Enhancements" section shows real-world rich result performance
  — Shows pages eligible for rich results and any issues

  Important: Structured data must accurately reflect visible page content.
  Google will penalise misuse (e.g., adding review stars to pages with no reviews).
-->
```

---

## Quick Reference Summary

| Element / Tag | SEO Purpose |
|---|---|
| `<title>` | Primary SERP headline — most important on-page SEO tag |
| `<meta name="description">` | SERP snippet text — influences click-through rate |
| `<meta name="robots">` | Controls crawling and indexing |
| `<h1>`–`<h6>` | Signals page topic and structure to crawlers |
| `<main>`, `<article>` | High-value content regions — weighted more heavily |
| `<nav>`, `<aside>` | Navigation/supplementary — lower content weight |
| `alt` on `<img>` | Image indexing — signals image context |
| `<link rel="canonical">` | Prevents duplicate content, consolidates ranking signals |
| `<link rel="alternate" hreflang>` | Targets correct content to correct locale |
| `<link rel="next">`/`<link rel="prev">` | Signals paginated content relationships |
| `og:title` | Social share card headline |
| `og:description` | Social share card description |
| `og:image` | Social share card image — most impactful visual element |
| `og:type` | Content type for social platforms |
| `twitter:card` | Twitter/X share card format |
| JSON-LD `Article` | Enables article rich results |
| JSON-LD `FAQPage` | Enables expandable FAQ in SERPs |
| JSON-LD `BreadcrumbList` | Shows breadcrumb trail in SERP URL |
| JSON-LD `Product` | Enables price, rating, availability rich results |
| JSON-LD `Organization` | Powers knowledge panel on branded searches |
| JSON-LD `WebSite` | Enables sitelinks search box |
| `fetchpriority="high"` | Prioritise LCP image loading (Core Web Vitals) |
| `width` + `height` on img | Prevents layout shift — improves CLS score |

SEO and accessibility share a common foundation — both require meaningful, well-structured semantic HTML. A page built correctly for screen readers is almost always built correctly for search engines, and vice versa. There is no conflict between them; good HTML serves both simultaneously.