# HTML Images & Media — Detailed Explanation

---

## 1. `<img>` Element

The `<img>` tag embeds an image into the page. It is a **void/self-closing element** (no closing tag needed).

```html
<img src="photo.jpg" alt="A sunset over the mountains" width="800" height="600" loading="lazy" />
```

---

### `src` — Source

Specifies the **path to the image**. Can be a relative path, absolute path, or full URL.

```html
<!-- Relative path -->
<img src="images/photo.jpg" alt="Photo" />

<!-- Absolute path -->
<img src="/assets/images/photo.jpg" alt="Photo" />

<!-- External URL -->
<img src="https://example.com/photo.jpg" alt="Photo" />

<!-- Base64 encoded (inline image) -->
<img src="data:image/png;base64,iVBORw0KGgoAAAANS..." alt="Inline image" />
```

---

### `alt` — Alternative Text

Provides a **text description** of the image. This is one of the most important attributes for accessibility and SEO.

```html
<!-- Descriptive alt text -->
<img src="dog.jpg" alt="A golden retriever playing fetch on a beach" />

<!-- Decorative image — empty alt tells screen readers to skip it -->
<img src="divider-line.png" alt="" />

<!-- Functional image (inside a link) — describe the destination -->
<a href="/home">
  <img src="logo.png" alt="Company Name — Home" />
</a>
```

**Rules for good alt text:**
- Be specific and descriptive — say what the image shows
- Don't start with "image of" or "picture of" — screen readers already announce it as an image
- If the image is purely decorative, use `alt=""` (empty, not missing)
- Never omit the `alt` attribute entirely — that's an accessibility violation

---

### `width` and `height`

Define the **dimensions** of the image in pixels.

```html
<img src="photo.jpg" alt="Photo" width="800" height="600" />
```

**Why they matter beyond just sizing:**
- The browser **reserves space** for the image before it loads, preventing **Cumulative Layout Shift (CLS)** — a Core Web Vitals metric
- You don't have to display the image at those exact dimensions (CSS can resize it), but the aspect ratio should match the actual image

```css
/* Let CSS control the display size, but keep the HTML attributes for layout reservation */
img {
  width: 100%;
  height: auto; /* maintains aspect ratio */
}
```

---

### `loading="lazy"`

Controls when the browser fetches the image.

```html
<!-- Load only when near the viewport (lazy) -->
<img src="below-fold.jpg" alt="..." loading="lazy" />

<!-- Load immediately (default behavior) -->
<img src="hero-banner.jpg" alt="..." loading="eager" />
```

**Values:**
- `lazy` — defers loading until the image is near the viewport. Great for images below the fold.
- `eager` — loads immediately regardless of position (this is the default)

**Best practice:** Use `loading="lazy"` on all images except the **hero image** or any image visible on first load (above the fold). Never lazy-load your LCP (Largest Contentful Paint) image.

---

## 2. Responsive Images

Responsive images serve **different image files** depending on screen size, resolution, or both — saving bandwidth and improving performance.

---

### `srcset` — Source Set

Tells the browser about **multiple versions of the same image** and lets it pick the most appropriate one.

```html
<!-- Width-based srcset (most common) -->
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
  alt="A mountain landscape"
/>
```

Each entry in `srcset` is: `filename widthDescriptor` where `w` means the actual pixel width of that file.

The browser automatically picks the right image based on the viewport and screen density.

---

### `sizes` — Display Sizes Hint

Works alongside `srcset` to tell the browser **how wide the image will be displayed** at different viewport sizes, so it can make a smarter choice before downloading anything.

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw,
         (max-width: 1024px) 50vw,
         800px"
  alt="A mountain landscape"
/>
```

Reading this `sizes` value:
- On screens **≤ 600px** → image will be **100% of viewport width**
- On screens **≤ 1024px** → image will be **50% of viewport width**
- Otherwise → image will be **800px** wide

The browser uses `sizes` + screen width + device pixel ratio to pick the best file from `srcset`.

---

### `<picture>` — Art Direction & Format Switching

The `<picture>` element gives you **full control** over which image is shown. It's used when you need to:
- Serve modern formats (WebP, AVIF) with a fallback
- Show a completely different image crop at different screen sizes (art direction)

```html
<!-- Format switching: serve WebP where supported, fallback to JPEG -->
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="A mountain landscape" />
</picture>
```

```html
<!-- Art direction: different crops for different screen sizes -->
<picture>
  <source media="(max-width: 600px)" srcset="photo-portrait.jpg" />
  <source media="(max-width: 1024px)" srcset="photo-square.jpg" />
  <img src="photo-landscape.jpg" alt="A mountain landscape" />
</picture>
```

**How it works:**
- The browser checks `<source>` elements top to bottom
- It uses the first one whose condition matches
- The `<img>` at the end is the **mandatory fallback** and also holds the `alt` text

**`srcset` vs `<picture>` — when to use which:**

| Scenario | Use |
|---|---|
| Same image, different sizes | `srcset` + `sizes` |
| Different image formats (WebP/AVIF fallback) | `<picture>` with `type` |
| Different image crops per screen size | `<picture>` with `media` |

---

## 3. `<figure>` and `<figcaption>`

`<figure>` is a **semantic container** for self-contained media content (images, diagrams, code, charts) that is referenced from the main content. `<figcaption>` provides a **visible caption** for it.

```html
<figure>
  <img src="chart.png" alt="Bar chart showing revenue growth from 2020 to 2024" width="800" height="400" />
  <figcaption>Figure 1: Annual revenue growth over five years (2020–2024).</figcaption>
</figure>
```

```html
<!-- figure isn't limited to images -->
<figure>
  <pre><code>
    const greet = (name) => `Hello, ${name}!`;
  </code></pre>
  <figcaption>Arrow function syntax in JavaScript.</figcaption>
</figure>
```

**Why use `<figure>` instead of just `<div>`:**
- It's semantically meaningful — tells browsers, search engines, and screen readers this is a self-contained unit
- The `<figcaption>` is programmatically associated with the figure's content
- If you moved the `<figure>` block elsewhere in the document, it should still make sense on its own

**Placement of `<figcaption>`:** It can be the **first or last** child of `<figure>`.

```html
<figure>
  <figcaption>Photo taken at base camp, 2023.</figcaption>
  <img src="mountain.jpg" alt="Climbers at Everest base camp" />
</figure>
```

---

## 4. `<video>` and `<audio>`

### `<video>`

Embeds a video player directly in the page.

```html
<video
  src="movie.mp4"
  width="1280"
  height="720"
  controls
  poster="thumbnail.jpg"
>
  Your browser does not support the video tag.
</video>
```

**Multiple format sources (for browser compatibility):**

```html
<video width="1280" height="720" controls poster="thumbnail.jpg">
  <source src="movie.webm" type="video/webm" />
  <source src="movie.mp4"  type="video/mp4" />
  <p>Your browser doesn't support HTML video. <a href="movie.mp4">Download it</a> instead.</p>
</video>
```

---

### `<audio>`

Embeds an audio player.

```html
<audio controls>
  <source src="song.ogg" type="audio/ogg" />
  <source src="song.mp3" type="audio/mpeg" />
  Your browser does not support the audio tag.
</audio>
```

---

### Shared Key Attributes

**`controls`**
Displays the browser's built-in playback UI (play/pause, volume, seek bar, fullscreen).
```html
<video controls src="video.mp4"></video>
```
Without `controls`, users have no UI to interact with the media (you'd control it via JavaScript).

---

**`autoplay`**
Starts playing the media automatically when the page loads.
```html
<video autoplay muted src="bg-video.mp4"></video>
```
⚠️ Most browsers **block autoplay with sound**. For autoplay to work reliably, you must also add `muted`. This is by design to prevent intrusive experiences.

---

**`loop`**
Makes the media restart from the beginning when it ends.
```html
<video autoplay loop muted src="animation.mp4"></video>
```
Commonly used for background videos and animated banners.

---

**`muted`**
Starts the media without audio. Also **required** for autoplay to work in most browsers.
```html
<video autoplay muted loop src="bg-video.mp4"></video>
```

---

**`poster`** (video only)
Specifies an image to display before the video plays — like a thumbnail.
```html
<video controls poster="video-thumbnail.jpg" src="video.mp4"></video>
```

---

**`preload`**
Hints to the browser how much of the media to load before the user plays it.
```html
<video preload="none" controls src="video.mp4"></video>
```

| Value | Behavior |
|---|---|
| `none` | Don't preload anything — saves bandwidth |
| `metadata` | Load only metadata (duration, dimensions) |
| `auto` | Browser decides (usually downloads some/all) |

---

**`<source>` element**
Used inside `<video>` and `<audio>` to specify multiple file formats. The browser picks the first one it supports.
```html
<video controls>
  <source src="video.av1.mp4" type="video/mp4; codecs=av01" />
  <source src="video.webm" type="video/webm" />
  <source src="video.mp4"  type="video/mp4" />
</video>
```

---

**JavaScript control:**
```js
const video = document.querySelector("video");

video.play();
video.pause();
video.currentTime = 30;     // Jump to 30 seconds
video.volume = 0.5;         // Set volume to 50%
video.playbackRate = 1.5;   // 1.5x speed
```

---

## 5. `<iframe>` — Embedding External Content

The `<iframe>` (inline frame) embeds **another HTML document** or external web page inside your page. It creates a completely separate browsing context.

```html
<iframe
  src="https://www.google.com/maps/embed?..."
  width="600"
  height="450"
  allowfullscreen
  loading="lazy"
  title="Office location on Google Maps"
></iframe>
```

**Common use cases:**
- Embedding Google Maps
- Embedding YouTube videos
- Embedding social media posts
- Third-party payment forms (Stripe, PayPal)
- Sandboxed previews (like CodePen)

---

### Key `<iframe>` Attributes

**`src`** — The URL of the page to embed.

**`title`** — Required for accessibility. Screen readers use it to describe the iframe's content.
```html
<iframe src="..." title="YouTube video: How HTML works"></iframe>
```

**`width` and `height`** — Dimensions of the frame.

**`allowfullscreen`** — Allows the iframe content to go fullscreen (needed for YouTube, Vimeo).

**`loading="lazy"`** — Defers iframe loading until it's near the viewport, just like images.

**`sandbox`** — Applies security restrictions to the embedded content.
```html
<!-- Heavily sandboxed -->
<iframe src="untrusted.html" sandbox></iframe>

<!-- Allow only scripts and same-origin content -->
<iframe src="widget.html" sandbox="allow-scripts allow-same-origin"></iframe>
```

Common sandbox values:

| Value | What it allows |
|---|---|
| `allow-scripts` | JavaScript execution |
| `allow-same-origin` | Treats content as same origin |
| `allow-forms` | Form submission |
| `allow-popups` | Opening new windows |
| `allow-modals` | `alert()`, `confirm()`, etc. |

**`allow`** — Grants permissions to the embedded content (Permissions Policy).
```html
<iframe
  src="https://example.com"
  allow="camera; microphone; geolocation"
></iframe>
```

---

### YouTube Embed Example

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/dQw4w9WgXcQ"
  title="YouTube video player"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen
  loading="lazy"
></iframe>
```

---

### Security Considerations

- Iframes from untrusted sources can be a security risk — always use `sandbox`
- Your own pages can be protected from being embedded in iframes using the `X-Frame-Options` HTTP header or `Content-Security-Policy: frame-ancestors`
- Never embed sensitive pages (login, payments) in an unsandboxed iframe

---

## 6. `<canvas>` and `<svg>`

Both are used to render **graphics on the web**, but they work very differently.

---

### `<canvas>`

`<canvas>` provides a **blank pixel-based drawing surface** that you draw onto entirely with JavaScript. It is resolution-dependent (raster-based).

```html
<canvas id="myCanvas" width="500" height="300">
  Your browser does not support the canvas element.
</canvas>
```

```js
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Draw a rectangle
ctx.fillStyle = "steelblue";
ctx.fillRect(50, 50, 200, 100);

// Draw a circle
ctx.beginPath();
ctx.arc(300, 100, 50, 0, Math.PI * 2);
ctx.fillStyle = "coral";
ctx.fill();

// Draw text
ctx.font = "24px Arial";
ctx.fillStyle = "white";
ctx.fillText("Hello Canvas!", 60, 110);

// Draw a line
ctx.beginPath();
ctx.moveTo(0, 0);
ctx.lineTo(500, 300);
ctx.strokeStyle = "black";
ctx.lineWidth = 2;
ctx.stroke();
```

**Canvas is best for:**
- Games and physics simulations
- Real-time data visualizations (charts with many data points)
- Image manipulation and filters
- Particle systems and animations
- Video processing frame by frame

**Limitations:**
- Not accessible (it's just pixels — no DOM elements inside)
- Doesn't scale well (looks blurry when enlarged unless you account for `devicePixelRatio`)
- Not indexable by search engines

---

### `<svg>` — Scalable Vector Graphics

SVG is an **XML-based vector format** that describes graphics as shapes, paths, and text. It's part of the DOM, meaning you can style and manipulate it with CSS and JavaScript.

```html
<!-- Inline SVG directly in HTML -->
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">

  <!-- Circle -->
  <circle cx="100" cy="100" r="80" fill="steelblue" />

  <!-- Rectangle -->
  <rect x="20" y="20" width="80" height="50" fill="coral" rx="8" />

  <!-- Line -->
  <line x1="0" y1="0" x2="200" y2="200" stroke="black" stroke-width="2" />

  <!-- Text -->
  <text x="50" y="150" font-size="20" fill="white">Hello SVG</text>

  <!-- Path (custom shape) -->
  <path d="M 10 80 Q 95 10 180 80" stroke="green" fill="none" stroke-width="3" />

</svg>
```

**Styling SVG with CSS:**
```css
circle {
  fill: steelblue;
  transition: fill 0.3s;
}
circle:hover {
  fill: coral;
}
```

**Manipulating SVG with JavaScript:**
```js
const circle = document.querySelector("circle");
circle.setAttribute("fill", "purple");
circle.setAttribute("r", "50");
```

**SVG is best for:**
- Icons and logos (sharp at any size)
- Charts and infographics with interactive elements
- Illustrations and diagrams
- Animations with CSS or SMIL
- Any graphic that needs to scale without pixelation

---

### Ways to use SVG in HTML

```html
<!-- 1. Inline (most flexible — full CSS/JS access) -->
<svg>...</svg>

<!-- 2. As an <img> source (no CSS/JS access to internals) -->
<img src="icon.svg" alt="Settings icon" />

<!-- 3. As a CSS background (decorative only) -->
<div style="background-image: url('pattern.svg')"></div>

<!-- 4. Via <object> (separate document, some JS access) -->
<object type="image/svg+xml" data="diagram.svg"></object>
```

---

### Canvas vs SVG — When to Use Which

| | `<canvas>` | `<svg>` |
|---|---|---|
| **Type** | Raster (pixels) | Vector (shapes) |
| **Scalability** | Pixelates when scaled | Infinitely sharp |
| **DOM access** | No internal DOM | Full DOM access |
| **CSS styling** | No | Yes |
| **Accessibility** | Poor | Good (with ARIA) |
| **Performance** | Better for thousands of objects | Better for fewer, complex shapes |
| **Best for** | Games, image processing, real-time rendering | Icons, charts, illustrations, interactive diagrams |
| **Interactivity** | Manual hit detection | Native event listeners on elements |

---

## Quick Reference Summary

| Element / Attribute | Purpose |
|---|---|
| `<img src alt width height loading>` | Display images with accessibility and performance in mind |
| `srcset` + `sizes` | Serve different image sizes based on viewport/density |
| `<picture>` | Full art direction and format switching |
| `<figure>` + `<figcaption>` | Semantic wrapper for media with visible caption |
| `<video>` + `<audio>` | Native media playback |
| `controls` | Show browser's native media controls |
| `autoplay` + `muted` | Auto-play without user interaction |
| `loop` | Repeat media playback |
| `poster` | Video thumbnail before playback |
| `<source>` | Multiple media format fallbacks |
| `<iframe>` | Embed external documents and services |
| `sandbox` | Restrict iframe permissions for security |
| `<canvas>` | Pixel-based graphics drawn via JavaScript |
| `<svg>` | Vector graphics, scalable and DOM-accessible |

Mastering images and media in HTML is critical for building fast, accessible, and visually rich web experiences.