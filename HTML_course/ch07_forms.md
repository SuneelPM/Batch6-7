# HTML Forms — Detailed Explanation

Forms are the primary way users **send data to a server** — signing up, logging in, searching, checking out, submitting feedback. They are one of the most complex and important parts of HTML to get right, both functionally and accessibly.

---

## 1. `<form>` — The Form Container

The `<form>` element wraps all form controls and defines **how and where** the data is sent when submitted.

```html
<form action="/submit" method="POST" enctype="application/x-www-form-urlencoded">
  <!-- form controls go here -->
</form>
```

---

### `action` — Where to Send the Data

Specifies the **URL** the form data is sent to when submitted. If omitted, the form submits to the current page URL.

```html
<!-- Submit to a specific endpoint -->
<form action="/api/contact">...</form>

<!-- Submit to an absolute URL -->
<form action="https://api.example.com/subscribe">...</form>

<!-- Submit to current page (default when omitted) -->
<form action="">...</form>
<form>...</form>

<!-- Submit to an email address (opens mail client — rarely used) -->
<form action="mailto:hello@example.com" enctype="text/plain">...</form>
```

---

### `method` — How to Send the Data

Specifies the **HTTP method** used to send the form data.

```html
<!-- GET — appends data to URL as query string -->
<form action="/search" method="GET">
  <input type="text" name="query" />
  <button type="submit">Search</button>
</form>
<!-- Submits as: /search?query=html+forms -->

<!-- POST — sends data in the HTTP request body -->
<form action="/api/login" method="POST">
  <input type="email" name="email" />
  <input type="password" name="password" />
  <button type="submit">Log In</button>
</form>
```

**GET vs POST — when to use which:**

| | `GET` | `POST` |
|---|---|---|
| Data location | URL query string | Request body |
| Visible in URL | Yes | No |
| Bookmarkable | Yes | No |
| Browser history | Yes | No |
| Max data size | ~2,000 chars (browser limit) | No practical limit |
| Sensitive data | Never — visible in URL | Yes |
| Caching | Can be cached | Not cached |
| Best for | Search, filters, navigation | Login, signup, payment, file upload |

---

### `enctype` — Encoding Type

Specifies **how the form data is encoded** before being sent to the server. Only relevant for `method="POST"`.

```html
<!-- Default — key=value pairs, spaces become +, special chars encoded -->
<form method="POST" enctype="application/x-www-form-urlencoded">
  ...
</form>

<!-- Required for file uploads — sends data as multipart chunks -->
<form method="POST" enctype="multipart/form-data">
  <input type="file" name="avatar" />
  <button type="submit">Upload</button>
</form>

<!-- Sends data as plain text — rarely used, only for mailto: forms -->
<form method="POST" enctype="text/plain" action="mailto:hello@example.com">
  ...
</form>
```

**Critical rule:** Always use `enctype="multipart/form-data"` when your form includes a file upload (`<input type="file">`). Without it, only the filename is sent — not the file contents.

---

### Other `<form>` Attributes

```html
<form
  action="/submit"
  method="POST"
  enctype="multipart/form-data"
  autocomplete="on"
  novalidate
  target="_blank"
  name="registration-form"
  id="registration-form"
>
```

| Attribute | Purpose |
|---|---|
| `autocomplete` | `"on"` or `"off"` — enable/disable browser autofill for all fields |
| `novalidate` | Disables browser's built-in HTML5 validation — useful when you handle validation in JavaScript |
| `target` | Where to display the response (`_self`, `_blank`, etc.) |
| `name` | Names the form for legacy JS access via `document.forms` |

---

## 2. `<label>` — Form Labels

`<label>` is possibly the **most important accessibility element** in a form. It associates descriptive text with a form control, so screen readers announce the label when the control receives focus, and clicking the label focuses/activates the control.

---

### Explicit Label — `for` and `id`

The `for` attribute on `<label>` must match the `id` of its associated control exactly.

```html
<!-- Clicking "Email address" focuses the input -->
<label for="email">Email address</label>
<input type="email" id="email" name="email" />

<!-- Clicking "I agree" toggles the checkbox -->
<label for="terms">I agree to the terms and conditions</label>
<input type="checkbox" id="terms" name="terms" />
```

---

### Implicit Label — Wrapping the Control

Wrapping the control inside the `<label>` associates them without needing `for`/`id`.

```html
<label>
  Email address
  <input type="email" name="email" />
</label>

<label>
  <input type="checkbox" name="newsletter" />
  Subscribe to newsletter
</label>
```

Both patterns work — the explicit `for`/`id` approach is generally preferred because it allows more flexible positioning of the label and input in your layout.

---

### What NOT to Do

```html
<!-- ❌ No label at all — screen readers have nothing to announce -->
<input type="email" name="email" placeholder="Enter email" />

<!-- ❌ Using a <div> or <p> instead of <label> — not associated -->
<p>Email address</p>
<input type="email" name="email" />

<!-- ❌ Placeholder as the only label — disappears on input, bad contrast -->
<input type="text" placeholder="First name" />

<!-- ✅ Correct — always use a real <label> -->
<label for="first-name">First name</label>
<input type="text" id="first-name" name="first-name" placeholder="e.g. Jane" />
```

**Placeholder is not a label substitute.** It disappears the moment the user starts typing, is often low contrast, and is not announced reliably by all screen readers.

---

### Visually Hidden Labels

When design requires no visible label (e.g., a search bar with a button), hide it visually but keep it accessible:

```html
<label for="search" class="sr-only">Search the site</label>
<input type="search" id="search" name="q" placeholder="Search..." />
<button type="submit">Search</button>

<style>
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}
</style>
```

---

## 3. Input Types

The `type` attribute on `<input>` fundamentally changes how the field behaves — the keyboard shown on mobile, built-in validation, the picker UI, and what data is expected.

---

### `type="text"` — Single-line Text

The default input type. Accepts any text on a single line.

```html
<label for="username">Username</label>
<input
  type="text"
  id="username"
  name="username"
  placeholder="e.g. janedoe"
  maxlength="30"
  autocomplete="username"
/>
```

---

### `type="email"` — Email Address

Validates that the entered value looks like a valid email address. Mobile keyboards show `@` and `.` prominently.

```html
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  name="email"
  placeholder="you@example.com"
  autocomplete="email"
  required
/>
```

Built-in validation rejects values like `hello` or `hello@` — the browser requires at least `x@y.z` format. Combine with server-side validation — HTML validation can be bypassed.

---

### `type="password"` — Password

Masks the entered characters with dots or asterisks. Prevents the value from being stored in browser history.

```html
<label for="password">Password</label>
<input
  type="password"
  id="password"
  name="password"
  autocomplete="new-password"
  minlength="8"
  required
/>

<!-- Show/hide password toggle -->
<label for="current-password">Current password</label>
<div class="password-wrapper">
  <input
    type="password"
    id="current-password"
    name="current-password"
    autocomplete="current-password"
  />
  <button
    type="button"
    aria-label="Show password"
    onclick="togglePassword()"
  >
    👁
  </button>
</div>

<script>
function togglePassword() {
  const input = document.getElementById("current-password");
  const btn = input.nextElementSibling;
  if (input.type === "password") {
    input.type = "text";
    btn.setAttribute("aria-label", "Hide password");
  } else {
    input.type = "password";
    btn.setAttribute("aria-label", "Show password");
  }
}
</script>
```

---

### `type="number"` — Numeric Input

Accepts only numbers. Shows a numeric keypad on mobile. Renders increment/decrement spinner arrows.

```html
<label for="quantity">Quantity</label>
<input
  type="number"
  id="quantity"
  name="quantity"
  min="1"
  max="99"
  step="1"
  value="1"
/>

<label for="price">Price ($)</label>
<input
  type="number"
  id="price"
  name="price"
  min="0"
  max="10000"
  step="0.01"
  placeholder="0.00"
/>
```

**Caution:** `type="number"` is not ideal for values like credit card numbers, phone numbers, or ZIP codes — use `type="tel"` or `type="text"` with `pattern` for those, since `number` strips leading zeros and behaves unexpectedly with non-numeric input.

---

### `type="tel"` — Telephone Number

Optimised for phone numbers — shows a numeric keypad on mobile but allows any characters (dashes, spaces, parentheses). Does **not** validate phone format automatically — use `pattern` for that.

```html
<label for="phone">Phone number</label>
<input
  type="tel"
  id="phone"
  name="phone"
  placeholder="+1 (555) 000-0000"
  pattern="[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[(]?[0-9]{1,3}[)]?[-\s\.]?[0-9]{4,6}"
  autocomplete="tel"
/>
```

---

### `type="url"` — URL Input

Validates that the value is a properly formatted URL (must include the protocol like `https://`). Mobile keyboards show `/`, `.`, and `.com` keys.

```html
<label for="website">Website</label>
<input
  type="url"
  id="website"
  name="website"
  placeholder="https://example.com"
  autocomplete="url"
/>
```

---

### `type="date"` — Date Picker

Renders the browser's native date picker. Value format is always `YYYY-MM-DD` regardless of display format.

```html
<label for="birthdate">Date of birth</label>
<input
  type="date"
  id="birthdate"
  name="birthdate"
  min="1900-01-01"
  max="2010-12-31"
/>

<label for="appointment">Appointment date</label>
<input
  type="date"
  id="appointment"
  name="appointment"
  min="2026-02-23"
/>

<!-- Reading the value in JavaScript -->
<script>
  const input = document.getElementById("appointment");
  input.addEventListener("change", () => {
    const date = new Date(input.value);
    console.log(date.toLocaleDateString("en-US", {
      weekday: "long", year: "numeric", month: "long", day: "numeric"
    }));
  });
</script>
```

---

### `type="time"` — Time Picker

Renders a native time picker. Value format is `HH:MM` in 24-hour format.

```html
<label for="meeting-time">Meeting time</label>
<input
  type="time"
  id="meeting-time"
  name="meeting-time"
  min="09:00"
  max="17:00"
  step="900"  <!-- 900 seconds = 15-minute intervals -->
  value="09:00"
/>
```

---

### `type="color"` — Color Picker

Renders a native color picker. Value is always a hex color string like `#ff0000`.

```html
<label for="theme-color">Choose your theme color</label>
<input
  type="color"
  id="theme-color"
  name="theme-color"
  value="#3b82f6"
/>

<script>
  document.getElementById("theme-color").addEventListener("input", (e) => {
    document.documentElement.style.setProperty("--primary", e.target.value);
  });
</script>
```

---

### `type="range"` — Slider

Renders a draggable slider. The user selects a number within a range. Combine with a live display for better UX since there's no visible current value by default.

```html
<label for="volume">
  Volume: <output id="volume-display">50</output>%
</label>
<input
  type="range"
  id="volume"
  name="volume"
  min="0"
  max="100"
  step="1"
  value="50"
  oninput="document.getElementById('volume-display').textContent = this.value"
/>

<!-- Price range slider -->
<label for="price-range">
  Max price: $<output id="price-display">500</output>
</label>
<input
  type="range"
  id="price-range"
  name="max-price"
  min="0"
  max="1000"
  step="50"
  value="500"
  oninput="document.getElementById('price-display').textContent = this.value"
/>
```

```css
input[type="range"] {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 6px;
  background: #e2e8f0;
  border-radius: 3px;
  outline: none;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #3b82f6;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

input[type="range"]:focus::-webkit-slider-thumb {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}
```

---

### `type="file"` — File Upload

Opens a file browser dialog. The form must use `enctype="multipart/form-data"` for the file to be sent.

```html
<!-- Single file -->
<label for="avatar">Profile photo</label>
<input
  type="file"
  id="avatar"
  name="avatar"
  accept="image/png, image/jpeg, image/webp"
/>

<!-- Multiple files -->
<label for="documents">Upload documents</label>
<input
  type="file"
  id="documents"
  name="documents"
  accept=".pdf,.doc,.docx"
  multiple
/>

<!-- Any file type -->
<label for="attachment">Attachment</label>
<input type="file" id="attachment" name="attachment" />
```

**Custom styled file input:**

```html
<label for="file-upload" class="file-upload-label">
  <span>📁 Choose a file</span>
  <input
    type="file"
    id="file-upload"
    name="file"
    accept="image/*"
    class="sr-only"
  />
</label>
<span id="file-name">No file chosen</span>

<script>
  document.getElementById("file-upload").addEventListener("change", function() {
    const name = this.files[0]?.name || "No file chosen";
    document.getElementById("file-name").textContent = name;
  });
</script>

<style>
.file-upload-label {
  display: inline-block;
  padding: 0.6rem 1.2rem;
  background: #3b82f6;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
}
.file-upload-label:hover { background: #2563eb; }
</style>
```

---

### `type="checkbox"` — Checkbox

A toggle that is either checked or unchecked. Can be used alone (boolean) or in groups (multiple selections).

```html
<!-- Single boolean checkbox -->
<label>
  <input type="checkbox" name="newsletter" value="yes" />
  Subscribe to our newsletter
</label>

<!-- Checkbox group — multiple values with the same name -->
<fieldset>
  <legend>Interests</legend>

  <label>
    <input type="checkbox" name="interests" value="html" />
    HTML
  </label>
  <label>
    <input type="checkbox" name="interests" value="css" />
    CSS
  </label>
  <label>
    <input type="checkbox" name="interests" value="javascript" />
    JavaScript
  </label>
  <label>
    <input type="checkbox" name="interests" value="accessibility" />
    Accessibility
  </label>
</fieldset>
```

**Important:** An unchecked checkbox sends **nothing** to the server — the field is simply absent. If you need to distinguish between "unchecked" and "not answered", use a hidden input:

```html
<!-- Hidden input ensures the field is always sent -->
<input type="hidden" name="newsletter" value="no" />
<label>
  <input type="checkbox" name="newsletter" value="yes" />
  Subscribe to newsletter
</label>
<!-- If checked: newsletter=yes. If unchecked: newsletter=no from hidden input -->
```

**Pre-checked checkbox:**

```html
<label>
  <input type="checkbox" name="terms" value="agreed" checked required />
  I agree to the <a href="/terms">Terms of Service</a>
</label>
```

---

### `type="radio"` — Radio Button

Radio buttons are for **mutually exclusive choices** — selecting one deselects the others. All radios in a group share the same `name`.

```html
<fieldset>
  <legend>Preferred contact method</legend>

  <label>
    <input type="radio" name="contact-method" value="email" checked />
    Email
  </label>

  <label>
    <input type="radio" name="contact-method" value="phone" />
    Phone
  </label>

  <label>
    <input type="radio" name="contact-method" value="sms" />
    SMS
  </label>

  <label>
    <input type="radio" name="contact-method" value="none" />
    Do not contact me
  </label>
</fieldset>
```

**Key rule:** Every radio button in a group must have the **same `name`** and a **unique `value`**. The `name` groups them; the `value` identifies which was selected.

---

### `type="hidden"` — Hidden Input

Sends a value with the form that is **invisible to the user**. Used to pass server-generated data, CSRF tokens, tracking IDs, or pre-determined values.

```html
<!-- CSRF protection token -->
<input type="hidden" name="csrf_token" value="abc123def456ghi789" />

<!-- Pass the user ID without a visible field -->
<input type="hidden" name="user_id" value="42" />

<!-- Track which page the form was submitted from -->
<input type="hidden" name="referrer" value="/pricing" />

<!-- Set by JavaScript before submission -->
<input type="hidden" name="selected_plan" id="selected-plan" value="" />
```

**Security note:** Hidden inputs are NOT secure. Anyone can inspect the page source and see their values. Never use them for sensitive data like prices, permissions, or security flags that users shouldn't be able to modify — validate everything server-side.

---

## 4. `<textarea>` — Multi-line Text Input

`<textarea>` provides a **resizable multi-line text field** for longer content like messages, comments, or descriptions.

```html
<label for="message">Message</label>
<textarea
  id="message"
  name="message"
  rows="6"
  cols="50"
  placeholder="Write your message here..."
  maxlength="1000"
  required
></textarea>
```

**Key differences from `<input>`:**
- Uses a closing tag — default content goes between the tags, NOT in a `value` attribute
- `rows` and `cols` set the visible size (but CSS `width`/`height` overrides these)
- Resizable by the user by default

```html
<!-- Default content between tags -->
<textarea id="bio" name="bio">Tell us about yourself...</textarea>

<!-- Count remaining characters -->
<label for="bio">Bio <span id="char-count">0/200</span></label>
<textarea
  id="bio"
  name="bio"
  maxlength="200"
  rows="4"
  oninput="
    document.getElementById('char-count').textContent =
      this.value.length + '/200'
  "
></textarea>
```

```css
textarea {
  width: 100%;
  resize: vertical;      /* Allow only vertical resizing */
  min-height: 120px;
  font-family: inherit;  /* Textareas don't inherit font by default */
  font-size: 1rem;
  padding: 0.75rem;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  line-height: 1.6;
}

/* resize: none      — not resizable at all */
/* resize: horizontal — only horizontal */
/* resize: vertical   — only vertical (most common) */
/* resize: both       — both directions (default) */

textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}
```

---

## 5. `<select>`, `<option>`, `<optgroup>` — Dropdown

`<select>` creates a dropdown menu. `<option>` defines each choice. `<optgroup>` groups options with a label.

---

### Basic Select

```html
<label for="country">Country</label>
<select id="country" name="country" required>
  <!-- Disabled placeholder option -->
  <option value="" disabled selected>Select your country...</option>
  <option value="us">United States</option>
  <option value="uk">United Kingdom</option>
  <option value="ca">Canada</option>
  <option value="au">Australia</option>
  <option value="in">India</option>
</select>
```

---

### Pre-selected Option

```html
<select name="size">
  <option value="xs">Extra Small</option>
  <option value="sm">Small</option>
  <option value="md" selected>Medium</option>   <!-- Pre-selected -->
  <option value="lg">Large</option>
  <option value="xl">Extra Large</option>
</select>
```

---

### `<optgroup>` — Grouped Options

```html
<label for="timezone">Timezone</label>
<select id="timezone" name="timezone">
  <option value="" disabled selected>Select timezone...</option>

  <optgroup label="Americas">
    <option value="America/New_York">Eastern Time (ET)</option>
    <option value="America/Chicago">Central Time (CT)</option>
    <option value="America/Denver">Mountain Time (MT)</option>
    <option value="America/Los_Angeles">Pacific Time (PT)</option>
    <option value="America/Sao_Paulo">Brasília Time (BRT)</option>
  </optgroup>

  <optgroup label="Europe">
    <option value="Europe/London">GMT / BST</option>
    <option value="Europe/Paris">Central European Time (CET)</option>
    <option value="Europe/Helsinki">Eastern European Time (EET)</option>
  </optgroup>

  <optgroup label="Asia & Pacific">
    <option value="Asia/Dubai">Gulf Standard Time (GST)</option>
    <option value="Asia/Kolkata">India Standard Time (IST)</option>
    <option value="Asia/Tokyo">Japan Standard Time (JST)</option>
    <option value="Australia/Sydney">Australian Eastern Time (AET)</option>
  </optgroup>
</select>
```

---

### `multiple` — Multi-select

```html
<label for="skills">Skills (hold Ctrl/Cmd to select multiple)</label>
<select id="skills" name="skills" multiple size="6">
  <option value="html">HTML</option>
  <option value="css">CSS</option>
  <option value="javascript">JavaScript</option>
  <option value="react">React</option>
  <option value="node">Node.js</option>
  <option value="sql">SQL</option>
</select>
```

`size` controls how many rows are visible without scrolling. The `multiple` attribute lets the user select multiple options. For a better UX, consider a custom multi-select or checkbox group instead — native multi-select is notoriously hard for users to discover.

---

## 6. `<button>` — Buttons

The `<button>` element creates a clickable button. The `type` attribute is critical and often forgotten.

---

### `type="submit"` — Submit the Form

Submits the form when clicked. This is the **default type** — if you forget the `type` attribute, the button behaves as `submit`.

```html
<button type="submit">Create Account</button>

<!-- With loading state via JavaScript -->
<button type="submit" id="submit-btn">
  Sign Up
</button>

<script>
  document.querySelector("form").addEventListener("submit", function() {
    const btn = document.getElementById("submit-btn");
    btn.disabled = true;
    btn.textContent = "Creating account...";
  });
</script>
```

---

### `type="reset"` — Reset the Form

Resets all form fields to their **initial default values**. Use sparingly — users accidentally clicking reset and losing all their data is a frustrating UX experience.

```html
<button type="reset">Clear Form</button>

<!-- Better UX — add confirmation -->
<button
  type="reset"
  onclick="return confirm('Are you sure you want to clear all fields?')"
>
  Reset
</button>
```

---

### `type="button"` — No Default Behaviour

Does **nothing** by default — you attach behaviour entirely via JavaScript. Use this for any button that isn't submitting or resetting a form.

```html
<button type="button" onclick="openModal()">Open Settings</button>
<button type="button" id="toggle-theme">🌙 Dark Mode</button>
<button type="button" onclick="copyToClipboard()">📋 Copy Code</button>
<button type="button" aria-expanded="false" aria-controls="dropdown">
  Menu ▼
</button>
```

**Why `type="button"` matters:** If a `<button>` without a `type` is inside a `<form>`, it defaults to `type="submit"` and will submit the form when clicked — even if you only wanted it to trigger a JavaScript action.

```html
<!-- ❌ Dangerous — clicking "Show Preview" submits the form -->
<form action="/submit">
  <input type="text" name="content" />
  <button onclick="showPreview()">Show Preview</button>  <!-- type defaults to submit! -->
  <button type="submit">Publish</button>
</form>

<!-- ✅ Correct — explicit types prevent accidental submission -->
<form action="/submit">
  <input type="text" name="content" />
  <button type="button" onclick="showPreview()">Show Preview</button>
  <button type="submit">Publish</button>
</form>
```

---

### Button vs Input Submit

```html
<!-- Old way — input submit (still valid) -->
<input type="submit" value="Submit" />

<!-- Modern way — button (preferred, more flexible) -->
<button type="submit">Submit</button>

<!-- Button can contain HTML — input cannot -->
<button type="submit">
  <svg aria-hidden="true"><!-- send icon --></svg>
  Send Message
</button>
```

Always prefer `<button>` over `<input type="submit">` — buttons can contain HTML like icons, and are easier to style.

---

### `form` Attribute — External Buttons

A button can submit a form it's **not nested inside** using the `form` attribute pointing to the form's `id`.

```html
<form id="settings-form" action="/settings" method="POST">
  <input type="text" name="display-name" />
  <input type="email" name="email" />
</form>

<!-- This button is outside the form but still submits it -->
<div class="sticky-footer">
  <button type="submit" form="settings-form">Save Changes</button>
</div>
```

---

## 7. `<fieldset>` and `<legend>`

`<fieldset>` **groups related form controls** into a logical section. `<legend>` provides a caption/label for that group. This is essential for accessibility — especially with radio buttons and checkboxes.

```html
<fieldset>
  <legend>Personal Information</legend>

  <label for="first-name">First name</label>
  <input type="text" id="first-name" name="first-name" />

  <label for="last-name">Last name</label>
  <input type="text" id="last-name" name="last-name" />

  <label for="dob">Date of birth</label>
  <input type="date" id="dob" name="dob" />
</fieldset>

<fieldset>
  <legend>Account Details</legend>

  <label for="username">Username</label>
  <input type="text" id="username" name="username" />

  <label for="new-password">Password</label>
  <input type="password" id="new-password" name="password" autocomplete="new-password" />
</fieldset>
```

---

### Essential Use — Radio and Checkbox Groups

Screen readers read the `<legend>` text along with each radio/checkbox label — so the user hears *"Payment method, Credit Card"* instead of just *"Credit Card"* out of context.

```html
<!-- Radio group -->
<fieldset>
  <legend>Payment method</legend>

  <label>
    <input type="radio" name="payment" value="credit-card" checked />
    Credit / Debit Card
  </label>

  <label>
    <input type="radio" name="payment" value="paypal" />
    PayPal
  </label>

  <label>
    <input type="radio" name="payment" value="bank-transfer" />
    Bank Transfer
  </label>
</fieldset>

<!-- Checkbox group -->
<fieldset>
  <legend>Email preferences</legend>

  <label>
    <input type="checkbox" name="emails" value="product-updates" checked />
    Product updates and new features
  </label>

  <label>
    <input type="checkbox" name="emails" value="weekly-digest" />
    Weekly digest
  </label>

  <label>
    <input type="checkbox" name="emails" value="promotions" />
    Promotions and offers
  </label>
</fieldset>
```

---

### Disabled Fieldset

Setting `disabled` on a `<fieldset>` **disables all controls inside it** at once — saving you from disabling each one individually.

```html
<fieldset disabled id="billing-section">
  <legend>Billing Information</legend>
  <input type="text" name="card-number" placeholder="Card number" />
  <input type="text" name="expiry" placeholder="MM/YY" />
  <input type="text" name="cvv" placeholder="CVV" />
</fieldset>

<!-- Enable when user selects card payment -->
<script>
  document.querySelectorAll('input[name="payment"]').forEach(radio => {
    radio.addEventListener("change", (e) => {
      const billing = document.getElementById("billing-section");
      billing.disabled = e.target.value !== "credit-card";
    });
  });
</script>
```

---

### Styling `<fieldset>`

Browsers apply default border and padding to `<fieldset>`. You'll almost always override this:

```css
fieldset {
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1.5rem;
  margin: 0 0 1.5rem 0;
}

legend {
  font-weight: 700;
  font-size: 1rem;
  color: #0f172a;
  padding: 0 0.5rem;
}

/* Completely remove default styling */
fieldset.no-style {
  border: none;
  padding: 0;
  margin: 0;
}

fieldset.no-style legend {
  font-weight: 600;
  margin-bottom: 0.75rem;
}
```

---

## 8. `<datalist>` — Autocomplete Suggestions

`<datalist>` provides a **list of predefined suggestions** for an `<input>` while still allowing the user to type any custom value. It combines the flexibility of a text input with the convenience of a select dropdown.

```html
<!-- Link input to datalist via list attribute and datalist id -->
<label for="browser">Favourite browser</label>
<input
  type="text"
  id="browser"
  name="browser"
  list="browsers"
  placeholder="Start typing..."
/>
<datalist id="browsers">
  <option value="Chrome"></option>
  <option value="Firefox"></option>
  <option value="Safari"></option>
  <option value="Edge"></option>
  <option value="Opera"></option>
  <option value="Brave"></option>
  <option value="Vivaldi"></option>
</datalist>
```

---

### Datalist with Descriptions

```html
<label for="framework">JavaScript framework</label>
<input type="text" id="framework" name="framework" list="frameworks" />
<datalist id="frameworks">
  <option value="React">Meta — Component-based UI library</option>
  <option value="Vue">Evan You — Progressive framework</option>
  <option value="Angular">Google — Full MVC framework</option>
  <option value="Svelte">Rich Harris — Compiler-based framework</option>
  <option value="Solid">Ryan Carniato — Fine-grained reactivity</option>
</datalist>
```

---

### Datalist with Number and Range Inputs

```html
<!-- Suggest common values while allowing any number -->
<label for="font-size">Font size (px)</label>
<input type="number" id="font-size" name="font-size" list="font-sizes" min="8" max="72" />
<datalist id="font-sizes">
  <option value="12"></option>
  <option value="14"></option>
  <option value="16"></option>
  <option value="18"></option>
  <option value="24"></option>
  <option value="32"></option>
  <option value="48"></option>
</datalist>

<!-- Tick marks on a range slider -->
<label for="satisfaction">Satisfaction level</label>
<input type="range" id="satisfaction" name="satisfaction"
       min="1" max="5" list="satisfaction-levels" />
<datalist id="satisfaction-levels">
  <option value="1" label="Very Unhappy"></option>
  <option value="2" label="Unhappy"></option>
  <option value="3" label="Neutral"></option>
  <option value="4" label="Happy"></option>
  <option value="5" label="Very Happy"></option>
</datalist>
```

**`<datalist>` vs `<select>`:**

| | `<datalist>` | `<select>` |
|---|---|---|
| Custom input | Yes — type anything | No — only listed options |
| Suggestions | Yes — shows as you type | No |
| Required choices | No — user can ignore list | Yes — must choose from list |
| Best for | Flexible with helpful hints | Fixed set of required options |

---

## 9. Form Validation Attributes

HTML5 provides built-in validation attributes that the browser enforces before allowing submission.

---

### `required`

Prevents form submission if the field is empty. Works on `input`, `textarea`, and `select`.

```html
<input type="email" name="email" required />
<textarea name="message" required></textarea>
<select name="country" required>
  <option value="">Select country...</option>
  <option value="us">United States</option>
</select>

<!-- Checkbox required — user must check it -->
<label>
  <input type="checkbox" name="terms" required />
  I accept the terms and conditions
</label>
```

---

### `disabled`

Completely **disables** the control — users cannot interact with it at all. Disabled fields are **not submitted** with the form.

```html
<input type="text" name="auto-id" value="USR-00042" disabled />
<button type="submit" disabled>Submit (disabled)</button>
<select name="region" disabled>...</select>
```

Because disabled fields aren't submitted, use a hidden input if you still need the value sent:

```html
<input type="hidden" name="auto-id" value="USR-00042" />
<input type="text" value="USR-00042" disabled aria-label="User ID (auto-generated)" />
```

---

### `readonly`

Makes the field **non-editable** but still visible and still **submitted** with the form. The user can focus it, select text, and copy it — just not change it.

```html
<!-- Auto-calculated field -->
<label for="total">Order total</label>
<input type="text" id="total" name="total" value="$145.20" readonly />

<!-- Username shown but not editable -->
<label for="username-display">Username</label>
<input type="text" id="username-display" name="username" value="janedoe" readonly />
```

**`disabled` vs `readonly`:**

| | `disabled` | `readonly` |
|---|---|---|
| User can interact | No | Focus + select only |
| Submitted with form | No | Yes |
| Appears greyed out | Yes | No (usually) |
| CSS `:disabled` pseudo | Yes | No |
| CSS `:read-only` pseudo | No | Yes |
| Best for | Controls irrelevant to user | Calculated/locked values to submit |

---

### `placeholder`

Provides **hint text** displayed inside the input when it's empty. Disappears as soon as the user starts typing.

```html
<input type="text" name="name" placeholder="e.g. Jane Doe" />
<input type="email" name="email" placeholder="you@example.com" />
<textarea name="bio" placeholder="Tell us about yourself (max 200 characters)"></textarea>
```

**Best practices:**
- Use it as a **format hint**, not as a label replacement
- Keep it short and descriptive
- Don't use it for critical instructions — they disappear when the user types
- Ensure sufficient contrast — browsers default to low-contrast placeholder text

```css
::placeholder {
  color: #94a3b8;
  font-style: italic;
}
```

---

### `autofocus`

Automatically focuses the field when the page loads. Use sparingly — only one element per page should have this.

```html
<!-- Search page — focus the search input immediately -->
<input type="search" name="q" autofocus placeholder="Search..." />

<!-- Login page — jump straight to the email field -->
<input type="email" name="email" autofocus />
```

**Accessibility caution:** `autofocus` can disorient screen reader users who start reading from the top of the page — the focus jumps unexpectedly. Avoid it on pages with significant content above the form.

---

### `autocomplete`

Controls **browser autofill behaviour** for the field. Uses standardised token values that tell the browser what kind of data the field expects.

```html
<input type="text"     name="name"     autocomplete="name" />
<input type="text"     name="fname"    autocomplete="given-name" />
<input type="text"     name="lname"    autocomplete="family-name" />
<input type="email"    name="email"    autocomplete="email" />
<input type="tel"      name="phone"    autocomplete="tel" />
<input type="password" name="password" autocomplete="current-password" />
<input type="password" name="new-pass" autocomplete="new-password" />
<input type="text"     name="address"  autocomplete="street-address" />
<input type="text"     name="city"     autocomplete="address-level2" />
<input type="text"     name="postcode" autocomplete="postal-code" />
<input type="text"     name="country"  autocomplete="country-name" />
<input type="text"     name="card"     autocomplete="cc-number" />
<input type="text"     name="expiry"   autocomplete="cc-exp" />
<input type="text"     name="cvv"      autocomplete="cc-csc" />

<!-- Disable autofill for a specific field -->
<input type="text" name="captcha" autocomplete="off" />
```

Using correct `autocomplete` values dramatically improves UX — browsers and password managers use them to fill forms automatically, saving users time.

---

### `pattern` — Regular Expression Validation

Validates the field value against a **regular expression**. The form won't submit if the value doesn't match.

```html
<!-- Only uppercase letters, 2–4 characters -->
<label for="country-code">Country code</label>
<input
  type="text"
  id="country-code"
  name="country-code"
  pattern="[A-Z]{2,4}"
  title="2 to 4 uppercase letters (e.g. US, GBR)"
  placeholder="e.g. US"
/>

<!-- UK postcode -->
<label for="postcode">Postcode</label>
<input
  type="text"
  id="postcode"
  name="postcode"
  pattern="[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}"
  title="Valid UK postcode (e.g. SW1A 1AA)"
  placeholder="SW1A 1AA"
/>

<!-- Password — min 8 chars, at least one number and letter -->
<label for="pass">Password</label>
<input
  type="password"
  id="pass"
  name="password"
  pattern="(?=.*\d)(?=.*[a-z]).{8,}"
  title="At least 8 characters, including at least one letter and one number"
  minlength="8"
/>

<!-- US ZIP code — 5 digits or ZIP+4 format -->
<input
  type="text"
  name="zip"
  pattern="[0-9]{5}(-[0-9]{4})?"
  title="5-digit ZIP code, optionally followed by a dash and 4 more digits"
  placeholder="90210"
/>
```

**`title` attribute with `pattern`:** Always include a `title` that explains the required format — browsers show it in the validation tooltip when the pattern fails.

---

### `min`, `max`, `step` — Range Constraints

Control the **acceptable range and increments** for numeric, date, time, and range inputs.

```html
<!-- Number constraints -->
<label for="age">Age</label>
<input type="number" id="age" name="age" min="18" max="120" step="1" />

<!-- Price with 2 decimal places -->
<label for="amount">Amount ($)</label>
<input type="number" id="amount" name="amount" min="0.01" max="9999.99" step="0.01" />

<!-- Date range — only allow future dates -->
<label for="departure">Departure date</label>
<input type="date" id="departure" name="departure" min="2026-02-23" />

<!-- Date range — only allow past dates (for birthdate) -->
<label for="birthdate">Date of birth</label>
<input type="date" id="birthdate" name="birthdate"
       min="1900-01-01" max="2010-01-01" />

<!-- Time in 30-minute steps -->
<label for="time">Meeting time</label>
<input type="time" id="time" name="time"
       min="09:00" max="17:30" step="1800" />

<!-- Range with step -->
<label for="rating">Rating (1–10)</label>
<input type="range" id="rating" name="rating"
       min="1" max="10" step="1" value="5" />
```

---

### `minlength` and `maxlength`

Control the **minimum and maximum number of characters** allowed in text inputs and textareas.

```html
<!-- Username: 3–20 characters -->
<label for="username">Username</label>
<input
  type="text"
  id="username"
  name="username"
  minlength="3"
  maxlength="20"
  required
/>

<!-- Tweet-style character limit -->
<label for="tweet">
  Tweet
  <span id="remaining">280</span> characters remaining
</label>
<textarea
  id="tweet"
  name="tweet"
  maxlength="280"
  rows="3"
  oninput="
    document.getElementById('remaining').textContent =
    280 - this.value.length
  "
></textarea>
```

---

## Complete Form Example

A real-world, fully accessible registration form bringing everything together:

```html
<form
  id="registration-form"
  action="/api/register"
  method="POST"
  enctype="multipart/form-data"
  novalidate
>
  <!-- CSRF token -->
  <input type="hidden" name="csrf_token" value="xK9mP2qR7vN4wL1j" />

  <!-- Personal Details -->
  <fieldset>
    <legend>Personal Details</legend>

    <div class="form-group">
      <label for="reg-first-name">First name <span aria-hidden="true">*</span></label>
      <input
        type="text"
        id="reg-first-name"
        name="first_name"
        autocomplete="given-name"
        placeholder="e.g. Jane"
        required
        minlength="2"
        maxlength="50"
      />
    </div>

    <div class="form-group">
      <label for="reg-last-name">Last name <span aria-hidden="true">*</span></label>
      <input
        type="text"
        id="reg-last-name"
        name="last_name"
        autocomplete="family-name"
        placeholder="e.g. Doe"
        required
        minlength="2"
        maxlength="50"
      />
    </div>

    <div class="form-group">
      <label for="reg-dob">Date of birth</label>
      <input
        type="date"
        id="reg-dob"
        name="dob"
        autocomplete="bday"
        min="1900-01-01"
        max="2010-01-01"
      />
    </div>

    <div class="form-group">
      <label for="reg-avatar">Profile photo</label>
      <input
        type="file"
        id="reg-avatar"
        name="avatar"
        accept="image/png, image/jpeg, image/webp"
      />
      <small>JPG, PNG or WebP. Max 2MB.</small>
    </div>
  </fieldset>

  <!-- Account Details -->
  <fieldset>
    <legend>Account Details</legend>

    <div class="form-group">
      <label for="reg-email">Email address <span aria-hidden="true">*</span></label>
      <input
        type="email"
        id="reg-email"
        name="email"
        autocomplete="email"
        placeholder="you@example.com"
        required
      />
    </div>

    <div class="form-group">
      <label for="reg-username">Username <span aria-hidden="true">*</span></label>
      <input
        type="text"
        id="reg-username"
        name="username"
        autocomplete="username"
        placeholder="e.g. janedoe92"
        pattern="[a-zA-Z0-9_]{3,20}"
        title="3–20 characters. Letters, numbers, and underscores only."
        required
        minlength="3"
        maxlength="20"
      />
    </div>

    <div class="form-group">
      <label for="reg-password">Password <span aria-hidden="true">*</span></label>
      <input
        type="password"
        id="reg-password"
        name="password"
        autocomplete="new-password"
        minlength="8"
        pattern="(?=.*\d)(?=.*[a-zA-Z]).{8,}"
        title="At least 8 characters, including at least one letter and one number."
        required
      />
    </div>
  </fieldset>

  <!-- Preferences -->
  <fieldset>
    <legend>Preferences</legend>

    <div class="form-group">
      <label for="reg-plan">Plan <span aria-hidden="true">*</span></label>
      <select id="reg-plan" name="plan" required>
        <option value="" disabled selected>Select a plan...</option>
        <optgroup label="Individual">
          <option value="free">Free — $0/month</option>
          <option value="pro">Pro — $9/month</option>
        </optgroup>
        <optgroup label="Business">
          <option value="team">Team — $29/month</option>
          <option value="enterprise">Enterprise — Custom</option>
        </optgroup>
      </select>
    </div>

    <div class="form-group">
      <label for="reg-referral">
        How did you hear about us?
      </label>
      <input
        type="text"
        id="reg-referral"
        name="referral"
        list="referral-sources"
        placeholder="Start typing or choose..."
      />
      <datalist id="referral-sources">
        <option value="Google Search"></option>
        <option value="Twitter / X"></option>
        <option value="LinkedIn"></option>
        <option value="YouTube"></option>
        <option value="Friend or colleague"></option>
        <option value="Blog post or article"></option>
        <option value="Podcast"></option>
        <option value="Other"></option>
      </datalist>
    </div>

    <div class="form-group">
      <label for="reg-bio">Bio</label>
      <textarea
        id="reg-bio"
        name="bio"
        rows="4"
        maxlength="200"
        placeholder="Tell us a bit about yourself (optional)..."
      ></textarea>
    </div>
  </fieldset>

  <!-- Email preferences -->
  <fieldset>
    <legend>Email preferences</legend>

    <label class="checkbox-label">
      <input type="checkbox" name="emails" value="product" checked />
      Product updates and announcements
    </label>
    <label class="checkbox-label">
      <input type="checkbox" name="emails" value="digest" />
      Weekly digest
    </label>
    <label class="checkbox-label">
      <input type="checkbox" name="emails" value="offers" />
      Promotions and offers
    </label>
  </fieldset>

  <!-- Terms -->
  <div class="form-group">
    <label class="checkbox-label">
      <input type="checkbox" name="terms" value="agreed" required />
      I agree to the <a href="/terms">Terms of Service</a>
      and <a href="/privacy">Privacy Policy</a>
      <span aria-hidden="true">*</span>
    </label>
  </div>

  <p class="required-note">
    <span aria-hidden="true">*</span> Required fields
  </p>

  <!-- Actions -->
  <div class="form-actions">
    <button type="submit">Create Account</button>
    <a href="/login">Already have an account? Sign in</a>
  </div>
</form>
```

---

## Quick Reference Summary

| Element / Attribute | Purpose |
|---|---|
| `<form action method enctype>` | Form container — where and how to send data |
| `<label for>` | Associates text label with a control |
| `<input type="text">` | Single-line text input |
| `<input type="email">` | Email with format validation |
| `<input type="password">` | Masked password input |
| `<input type="number">` | Numeric input with spinner |
| `<input type="tel">` | Phone number — numeric mobile keyboard |
| `<input type="url">` | URL with format validation |
| `<input type="date">` | Native date picker |
| `<input type="time">` | Native time picker |
| `<input type="color">` | Native color picker |
| `<input type="range">` | Draggable slider |
| `<input type="file">` | File upload browser |
| `<input type="checkbox">` | Boolean or multi-select toggle |
| `<input type="radio">` | Mutually exclusive single selection |
| `<input type="hidden">` | Hidden value sent with form |
| `<textarea>` | Multi-line text input |
| `<select>` + `<option>` | Dropdown selection |
| `<optgroup>` | Groups options with a label |
| `<button type="submit">` | Submits the form |
| `<button type="reset">` | Resets all fields to defaults |
| `<button type="button">` | Custom action via JavaScript |
| `<fieldset>` + `<legend>` | Groups related controls with a caption |
| `<datalist>` | Autocomplete suggestion list |
| `required` | Field must be filled before submit |
| `disabled` | Field inactive and not submitted |
| `readonly` | Field visible but not editable — is submitted |
| `placeholder` | Hint text inside empty field |
| `autofocus` | Auto-focus on page load |
| `autocomplete` | Browser autofill token |
| `pattern` | Regex validation pattern |
| `min` / `max` | Minimum/maximum value |
| `step` | Value increment amount |
| `minlength` / `maxlength` | Character count constraints |

Forms are where users interact most deeply with your application — building them with correct semantics, full accessibility, and proper validation ensures a great experience for every user.