# HTML Tables — Detailed Explanation

Tables are used to display **structured, relational data** in rows and columns — like a spreadsheet. They should only be used for tabular data, never for page layout (a common mistake in the early web).

---

## 1. Core Table Elements

### Basic Structure

A table is built from several elements that work together hierarchically.

```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Role</th>
      <th>Department</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Jane Doe</td>
      <td>Frontend Developer</td>
      <td>Engineering</td>
      <td>$95,000</td>
    </tr>
    <tr>
      <td>John Smith</td>
      <td>UX Designer</td>
      <td>Design</td>
      <td>$88,000</td>
    </tr>
    <tr>
      <td>Alice Johnson</td>
      <td>Product Manager</td>
      <td>Product</td>
      <td>$110,000</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="3">Average Salary</td>
      <td>$97,667</td>
    </tr>
  </tfoot>
</table>
```

---

### `<table>`

The outermost wrapper that defines the table. Every other table element must be a descendant of it.

```html
<table>
  <!-- All table content goes here -->
</table>
```

By default, browsers render tables with no border and cells sized to fit their content. You almost always override this with CSS.

```css
table {
  width: 100%;
  border-collapse: collapse;   /* Merges cell borders into one line */
  font-size: 0.95rem;
}
```

**`border-collapse`** is one of the most important CSS properties for tables:

```css
/* border-collapse: separate (default) */
/* Each cell has its own border — causes double borders where cells meet */
table { border-collapse: separate; border-spacing: 4px; }

/* border-collapse: collapse (almost always what you want) */
/* Adjacent borders merge into a single border */
table { border-collapse: collapse; }
```

---

### `<thead>` — Table Head

Groups the **header rows** of the table. Typically contains column labels in `<th>` elements. It has semantic meaning — telling the browser and assistive technologies these are the column headings.

```html
<thead>
  <tr>
    <th>Product</th>
    <th>Category</th>
    <th>Price</th>
    <th>Stock</th>
  </tr>
</thead>
```

**Practical behaviour:** When a table is printed across multiple pages, browsers may repeat the `<thead>` rows at the top of each page automatically.

```css
thead {
  background-color: #1e293b;
  color: #f8fafc;
}

thead th {
  padding: 0.875rem 1rem;
  font-weight: 600;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  text-align: left;
}
```

---

### `<tbody>` — Table Body

Groups the **main data rows** of the table. While technically optional in HTML (the browser infers it), you should always write it explicitly for clarity and correct styling.

```html
<tbody>
  <tr>
    <td>MacBook Pro</td>
    <td>Laptop</td>
    <td>$1,999</td>
    <td>In Stock</td>
  </tr>
  <tr>
    <td>iPad Air</td>
    <td>Tablet</td>
    <td>$749</td>
    <td>In Stock</td>
  </tr>
  <tr>
    <td>AirPods Pro</td>
    <td>Audio</td>
    <td>$249</td>
    <td>Out of Stock</td>
  </tr>
</tbody>
```

A table can have **multiple `<tbody>` elements** — useful for grouping rows into logical sections.

```html
<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Price</th>
    </tr>
  </thead>

  <!-- Group 1 -->
  <tbody>
    <tr>
      <td colspan="2" class="group-label">Laptops</td>
    </tr>
    <tr>
      <td>MacBook Air</td>
      <td>$1,099</td>
    </tr>
    <tr>
      <td>MacBook Pro</td>
      <td>$1,999</td>
    </tr>
  </tbody>

  <!-- Group 2 -->
  <tbody>
    <tr>
      <td colspan="2" class="group-label">Tablets</td>
    </tr>
    <tr>
      <td>iPad</td>
      <td>$449</td>
    </tr>
    <tr>
      <td>iPad Pro</td>
      <td>$1,099</td>
    </tr>
  </tbody>
</table>
```

```css
tbody tr:nth-child(even) {
  background-color: #f8fafc;  /* Zebra striping */
}

tbody tr:hover {
  background-color: #eff6ff;  /* Row highlight on hover */
  cursor: pointer;
}

tbody td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #e2e8f0;
  color: #334155;
}
```

---

### `<tfoot>` — Table Footer

Groups **summary or aggregate rows** — totals, averages, counts, or footnotes. Like `<thead>`, it may repeat on each printed page (at the bottom).

```html
<table>
  <thead>
    <tr>
      <th>Product</th>
      <th>Quantity</th>
      <th>Unit Price</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Domain Name</td>
      <td>1</td>
      <td>$12.00</td>
      <td>$12.00</td>
    </tr>
    <tr>
      <td>Hosting (Annual)</td>
      <td>1</td>
      <td>$120.00</td>
      <td>$120.00</td>
    </tr>
    <tr>
      <td>SSL Certificate</td>
      <td>1</td>
      <td>$0.00</td>
      <td>$0.00</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="3">Subtotal</td>
      <td>$132.00</td>
    </tr>
    <tr>
      <td colspan="3">Tax (10%)</td>
      <td>$13.20</td>
    </tr>
    <tr class="total-row">
      <td colspan="3"><strong>Total</strong></td>
      <td><strong>$145.20</strong></td>
    </tr>
  </tfoot>
</table>
```

```css
tfoot {
  background-color: #f1f5f9;
  font-weight: 500;
}

tfoot td {
  padding: 0.75rem 1rem;
  border-top: 2px solid #cbd5e1;
}

.total-row {
  background-color: #1e293b;
  color: white;
  font-size: 1.05rem;
}
```

**Note on source order:** Even though `<tfoot>` appears visually at the bottom of a table, in HTML you can write it either after `<thead>` (before `<tbody>`) or after `<tbody>`. Both are valid. Modern browsers handle both correctly.

---

### `<tr>` — Table Row

Defines a **horizontal row** of cells. Every row in a table must be wrapped in `<tr>`, and it must be a direct child of `<thead>`, `<tbody>`, or `<tfoot>`.

```html
<tr>
  <td>Cell 1</td>
  <td>Cell 2</td>
  <td>Cell 3</td>
</tr>
```

---

### `<th>` — Table Header Cell

Defines a **header cell**. Semantically marks a cell as a label for a row or column. Bold and centered by default in most browsers.

```html
<!-- Column headers -->
<thead>
  <tr>
    <th>Month</th>
    <th>Revenue</th>
    <th>Expenses</th>
    <th>Profit</th>
  </tr>
</thead>

<!-- Row headers in tbody -->
<tbody>
  <tr>
    <th>January</th>       <!-- Row header — labels this row -->
    <td>$42,000</td>
    <td>$31,000</td>
    <td>$11,000</td>
  </tr>
</tbody>
```

`<th>` cells create a **programmatic relationship** between headers and data cells — this is what makes tables accessible to screen readers, which is covered in detail in the accessibility section.

```css
th {
  background-color: #0f172a;
  color: #f8fafc;
  font-weight: 600;
  padding: 0.875rem 1rem;
  text-align: left;
  position: sticky;     /* Sticky column headers */
  top: 0;
  z-index: 1;
}
```

---

### `<td>` — Table Data Cell

Defines a **standard data cell**. Contains the actual content of the table.

```html
<td>Jane Doe</td>
<td>$95,000</td>
<td><span class="badge badge--active">Active</span></td>
<td><a href="/profile/jane">View Profile</a></td>
```

`<td>` can contain any HTML — plain text, links, images, badges, buttons, form inputs, and more.

```html
<!-- Rich cell content -->
<tbody>
  <tr>
    <td>
      <div class="user-cell">
        <img src="avatar.jpg" alt="" class="avatar" />
        <div>
          <strong>Jane Doe</strong>
          <small>jane@example.com</small>
        </div>
      </div>
    </td>
    <td>
      <span class="badge badge--admin">Admin</span>
    </td>
    <td>
      <div class="progress-bar">
        <div class="progress-bar__fill" style="width: 78%"></div>
        <span>78%</span>
      </div>
    </td>
    <td>
      <div class="action-buttons">
        <button class="btn btn--sm btn--secondary">Edit</button>
        <button class="btn btn--sm btn--danger">Delete</button>
      </div>
    </td>
  </tr>
</tbody>
```

---

## 2. `colspan` and `rowspan`

These attributes allow cells to **span across multiple columns or rows**, creating complex, merged cell layouts.

---

### `colspan` — Span Multiple Columns

Makes a cell occupy the space of **multiple consecutive columns** in the same row.

```html
<table>
  <thead>
    <tr>
      <!-- This header spans 3 columns -->
      <th colspan="3">Q1 2026 Sales Report</th>
    </tr>
    <tr>
      <th>Product</th>
      <th>Units Sold</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Widget A</td>
      <td>1,240</td>
      <td>$24,800</td>
    </tr>
    <tr>
      <td>Widget B</td>
      <td>860</td>
      <td>$34,400</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <!-- Spans first two columns -->
      <td colspan="2">Total Revenue</td>
      <td>$59,200</td>
    </tr>
  </tfoot>
</table>
```

**How it works:** `colspan="3"` means this single cell takes up the space of 3 normal cells. The total number of columns must stay consistent across all rows — if a row has a `colspan="3"` cell plus one regular cell, that equals 4 columns, so all other rows must also total 4 columns.

```html
<!-- Consistent column count example -->
<table>
  <tr>
    <td colspan="2">Spans cols 1–2</td>   <!-- 2 columns -->
    <td>Col 3</td>                          <!-- 1 column -->
    <!-- Total: 3 columns -->
  </tr>
  <tr>
    <td>Col 1</td>                          <!-- 1 column -->
    <td>Col 2</td>                          <!-- 1 column -->
    <td>Col 3</td>                          <!-- 1 column -->
    <!-- Total: 3 columns ✅ Matches -->
  </tr>
</table>
```

---

### `rowspan` — Span Multiple Rows

Makes a cell occupy the space of **multiple consecutive rows** in the same column.

```html
<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Product</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <!-- This cell spans 3 rows — covers all laptop rows -->
      <td rowspan="3">Laptops</td>
      <td>MacBook Air</td>
      <td>$1,099</td>
    </tr>
    <tr>
      <!-- No <td> for Category column — occupied by rowspan above -->
      <td>MacBook Pro 14"</td>
      <td>$1,999</td>
    </tr>
    <tr>
      <td>MacBook Pro 16"</td>
      <td>$2,499</td>
    </tr>
    <tr>
      <!-- Rowspan resets — new category cell -->
      <td rowspan="2">Tablets</td>
      <td>iPad</td>
      <td>$449</td>
    </tr>
    <tr>
      <td>iPad Pro</td>
      <td>$1,099</td>
    </tr>
  </tbody>
</table>
```

**Critical rule:** When a cell has `rowspan="3"`, the **next 2 rows must not include a cell for that column** — the rowspan cell already occupies that space. Adding one would push the layout out of alignment.

```html
<!-- ✅ Correct — row 2 and 3 skip the spanned column -->
<tr>
  <td rowspan="3">Category A</td>   <!-- Occupies column 1 for rows 1–3 -->
  <td>Item 1</td>
  <td>$10</td>
</tr>
<tr>
  <!-- No <td> for column 1 -->
  <td>Item 2</td>
  <td>$20</td>
</tr>
<tr>
  <!-- No <td> for column 1 -->
  <td>Item 3</td>
  <td>$30</td>
</tr>

<!-- ❌ Wrong — row 2 accidentally includes a cell for the spanned column -->
<tr>
  <td rowspan="3">Category A</td>
  <td>Item 1</td>
</tr>
<tr>
  <td>This cell breaks the layout</td>  <!-- Pushes everything right -->
  <td>Item 2</td>
</tr>
```

---

### Combining `colspan` and `rowspan`

Both can be used together for complex table layouts like schedules, timetables, and comparison charts.

```html
<!-- Weekly schedule -->
<table>
  <caption>Weekly Class Schedule</caption>
  <thead>
    <tr>
      <th>Time</th>
      <th>Monday</th>
      <th>Tuesday</th>
      <th>Wednesday</th>
      <th>Thursday</th>
      <th>Friday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9:00 AM</th>
      <!-- Math spans Mon–Tue (colspan) AND 9AM–10AM (rowspan) -->
      <td colspan="2" rowspan="2" class="class--math">Mathematics</td>
      <td class="class--english">English</td>
      <td class="class--free">Free Period</td>
      <td class="class--science">Science</td>
    </tr>
    <tr>
      <th>10:00 AM</th>
      <!-- colspan="2" rowspan="2" from above still occupies Mon–Tue -->
      <td class="class--english">English</td>
      <td class="class--history">History</td>
      <td class="class--science">Science</td>
    </tr>
    <tr>
      <th>11:00 AM</th>
      <td class="class--art">Art</td>
      <td class="class--science">Science</td>
      <td class="class--math">Mathematics</td>
      <td class="class--history">History</td>
      <!-- PE spans Fri 11AM–12PM (rowspan) -->
      <td rowspan="2" class="class--pe">Physical Education</td>
    </tr>
    <tr>
      <th>12:00 PM</th>
      <!-- colspan="4" — Lunch spans all subject columns -->
      <td colspan="4" class="class--lunch">Lunch Break</td>
      <!-- rowspan from PE above still occupies Friday -->
    </tr>
  </tbody>
</table>
```

---

## 3. `<caption>` and `scope` — Accessibility

Accessible tables ensure that **screen reader users get the same information** that sighted users get from visual context.

---

### `<caption>` — Table Caption

The `<caption>` element provides a **title and description for the entire table**. It must be the **first child** of `<table>`. Screen readers announce it before reading the table content, giving users immediate context about what the table contains.

```html
<table>
  <caption>Q4 2025 Sales Performance by Region</caption>
  <thead>
    <tr>
      <th>Region</th>
      <th>Target</th>
      <th>Actual</th>
      <th>Variance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>North America</td>
      <td>$500,000</td>
      <td>$542,000</td>
      <td class="positive">+$42,000</td>
    </tr>
    <tr>
      <td>Europe</td>
      <td>$400,000</td>
      <td>$378,000</td>
      <td class="negative">−$22,000</td>
    </tr>
  </tbody>
</table>
```

By default, `<caption>` renders centered above the table. You can style it freely:

```css
caption {
  caption-side: top;          /* or bottom */
  text-align: left;
  font-size: 1.1rem;
  font-weight: 700;
  color: #0f172a;
  padding: 0 0 0.75rem 0;
  margin-bottom: 0.5rem;
}
```

```css
/* Caption below the table */
caption {
  caption-side: bottom;
  font-size: 0.85rem;
  color: #64748b;
  padding-top: 0.5rem;
  font-style: italic;
}
```

**Visually hide the caption but keep it for screen readers:**

Sometimes your design doesn't want a visible caption (you might have a heading above the table instead), but you still need it for accessibility. Use the visually-hidden pattern:

```html
<table>
  <caption class="sr-only">Monthly revenue data for 2025</caption>
  ...
</table>

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

### `scope` — Header Cell Scope

The `scope` attribute on `<th>` tells screen readers **which cells the header applies to** — which direction it describes. Without `scope`, screen readers have to guess which data cells belong to which header.

```html
<table>
  <caption>Employee Directory</caption>
  <thead>
    <tr>
      <!-- scope="col" — this header describes the column below it -->
      <th scope="col">Name</th>
      <th scope="col">Department</th>
      <th scope="col">Location</th>
      <th scope="col">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <!-- scope="row" — this header describes the row it's in -->
      <th scope="row">Jane Doe</th>
      <td>Engineering</td>
      <td>New York</td>
      <td>Active</td>
    </tr>
    <tr>
      <th scope="row">John Smith</th>
      <td>Design</td>
      <td>London</td>
      <td>Active</td>
    </tr>
  </tbody>
</table>
```

**`scope` values:**

| Value | Meaning | Used on |
|---|---|---|
| `col` | Header for all cells in this column | `<th>` in `<thead>` |
| `row` | Header for all cells in this row | `<th>` in `<tbody>` |
| `colgroup` | Header for a group of columns | `<th>` spanning multiple columns |
| `rowgroup` | Header for a group of rows | `<th>` spanning multiple rows |

---

### `scope="colgroup"` and `scope="rowgroup"` — Multi-level Headers

For tables with grouped headers (like comparing across multiple categories), use `colgroup` and `rowgroup`.

```html
<table>
  <caption>Quarterly Revenue by Product Line</caption>
  <thead>
    <tr>
      <td></td>   <!-- Empty corner cell -->
      <!-- These headers span 2 columns each — scope="colgroup" -->
      <th colspan="2" scope="colgroup">Hardware</th>
      <th colspan="2" scope="colgroup">Software</th>
      <th colspan="2" scope="colgroup">Services</th>
    </tr>
    <tr>
      <td></td>
      <!-- These are sub-headers within each colgroup -->
      <th scope="col">Q3</th>
      <th scope="col">Q4</th>
      <th scope="col">Q3</th>
      <th scope="col">Q4</th>
      <th scope="col">Q3</th>
      <th scope="col">Q4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North America</th>
      <td>$1.2M</td>
      <td>$1.5M</td>
      <td>$0.8M</td>
      <td>$0.9M</td>
      <td>$0.5M</td>
      <td>$0.6M</td>
    </tr>
    <tr>
      <th scope="row">Europe</th>
      <td>$0.9M</td>
      <td>$1.1M</td>
      <td>$0.6M</td>
      <td>$0.7M</td>
      <td>$0.4M</td>
      <td>$0.5M</td>
    </tr>
  </tbody>
</table>
```

---

### `id` and `headers` — Explicit Header Association

For very complex tables where `scope` isn't enough, you can explicitly link data cells to their headers using `id` and `headers` attributes. This is the most explicit and bulletproof accessibility approach.

```html
<table>
  <caption>Course Grades</caption>
  <thead>
    <tr>
      <td></td>
      <th id="midterm">Midterm</th>
      <th id="final">Final</th>
      <th id="project">Project</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="alice">Alice</th>
      <!-- headers lists every <th> that applies to this cell -->
      <td headers="alice midterm">88</td>
      <td headers="alice final">91</td>
      <td headers="alice project">95</td>
    </tr>
    <tr>
      <th id="bob">Bob</th>
      <td headers="bob midterm">76</td>
      <td headers="bob final">82</td>
      <td headers="bob project">79</td>
    </tr>
  </tbody>
</table>
```

When a screen reader lands on the cell `<td headers="alice midterm">88</td>`, it announces: *"Alice, Midterm, 88"* — giving the user full context.

---

### `<colgroup>` and `<col>` — Column Grouping and Styling

`<colgroup>` and `<col>` let you apply styles or attributes to **entire columns** without having to style each cell individually. They go right after `<caption>` and before `<thead>`.

```html
<table>
  <caption>Product Inventory</caption>

  <colgroup>
    <col style="width: 30%;" />                        <!-- Product name column -->
    <col style="width: 15%;" />                        <!-- Category column -->
    <col style="width: 15%; background: #fefce8;" />   <!-- Price — highlighted -->
    <col style="width: 15%;" />                        <!-- Stock column -->
    <col style="width: 25%;" />                        <!-- Actions column -->
  </colgroup>

  <thead>
    <tr>
      <th scope="col">Product</th>
      <th scope="col">Category</th>
      <th scope="col">Price</th>
      <th scope="col">In Stock</th>
      <th scope="col">Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MacBook Pro</td>
      <td>Laptop</td>
      <td>$1,999</td>
      <td>142</td>
      <td><button>Edit</button> <button>Delete</button></td>
    </tr>
  </tbody>
</table>
```

You can also **span columns** with `<col>`:

```html
<colgroup>
  <col />                    <!-- Column 1 -->
  <col span="2" class="highlight" />  <!-- Columns 2 and 3 together -->
  <col />                    <!-- Column 4 -->
</colgroup>
```

---

## Complete Accessible Table Example

A fully built, real-world data table with all best practices:

```html
<div class="table-wrapper" role="region" aria-labelledby="table-caption" tabindex="0">
  <table>
    <caption id="table-caption">
      2025 Annual Employee Performance Summary
      <span class="caption-detail">Showing 5 of 248 employees. Sorted by performance score.</span>
    </caption>

    <colgroup>
      <col style="width: 20%;" />
      <col style="width: 15%;" />
      <col style="width: 15%;" />
      <col style="width: 12%;" />
      <col style="width: 12%;" />
      <col style="width: 26%;" />
    </colgroup>

    <thead>
      <tr>
        <th scope="col">Employee</th>
        <th scope="col">Department</th>
        <th scope="col">Location</th>
        <th scope="col">Score</th>
        <th scope="col">Status</th>
        <th scope="col">Actions</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th scope="row">Jane Doe</th>
        <td>Engineering</td>
        <td>New York</td>
        <td>
          <span class="score score--high" aria-label="Score: 98 out of 100">98</span>
        </td>
        <td>
          <span class="badge badge--active">Active</span>
        </td>
        <td>
          <a href="/employees/jane-doe">View</a> ·
          <a href="/employees/jane-doe/edit">Edit</a>
        </td>
      </tr>
      <tr>
        <th scope="row">John Smith</th>
        <td>Design</td>
        <td>London</td>
        <td>
          <span class="score score--high" aria-label="Score: 94 out of 100">94</span>
        </td>
        <td>
          <span class="badge badge--active">Active</span>
        </td>
        <td>
          <a href="/employees/john-smith">View</a> ·
          <a href="/employees/john-smith/edit">Edit</a>
        </td>
      </tr>
      <tr>
        <th scope="row">Alice Johnson</th>
        <td>Product</td>
        <td>San Francisco</td>
        <td>
          <span class="score score--mid" aria-label="Score: 78 out of 100">78</span>
        </td>
        <td>
          <span class="badge badge--active">Active</span>
        </td>
        <td>
          <a href="/employees/alice-johnson">View</a> ·
          <a href="/employees/alice-johnson/edit">Edit</a>
        </td>
      </tr>
      <tr>
        <th scope="row">Bob Williams</th>
        <td>Marketing</td>
        <td>Chicago</td>
        <td>
          <span class="score score--mid" aria-label="Score: 72 out of 100">72</span>
        </td>
        <td>
          <span class="badge badge--on-leave">On Leave</span>
        </td>
        <td>
          <a href="/employees/bob-williams">View</a> ·
          <a href="/employees/bob-williams/edit">Edit</a>
        </td>
      </tr>
      <tr>
        <th scope="row">Carol Davis</th>
        <td>Finance</td>
        <td>Austin</td>
        <td>
          <span class="score score--low" aria-label="Score: 61 out of 100">61</span>
        </td>
        <td>
          <span class="badge badge--inactive">Inactive</span>
        </td>
        <td>
          <a href="/employees/carol-davis">View</a> ·
          <a href="/employees/carol-davis/edit">Edit</a>
        </td>
      </tr>
    </tbody>

    <tfoot>
      <tr>
        <td colspan="3">
          <strong>Team Average</strong>
        </td>
        <td colspan="3">
          <strong>80.6 / 100</strong>
        </td>
      </tr>
    </tfoot>
  </table>
</div>
```

```css
/* ── Wrapper ── */
.table-wrapper {
  overflow-x: auto;            /* Horizontal scroll on small screens */
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

/* ── Table base ── */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  font-family: 'Inter', sans-serif;
}

/* ── Caption ── */
caption {
  text-align: left;
  padding: 1rem 1.25rem;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  caption-side: top;
  font-weight: 700;
  font-size: 1rem;
  color: #0f172a;
}

.caption-detail {
  display: block;
  font-weight: 400;
  font-size: 0.8rem;
  color: #64748b;
  margin-top: 0.2rem;
}

/* ── Header ── */
thead {
  background: #0f172a;
  color: #f8fafc;
}

thead th {
  padding: 0.875rem 1.25rem;
  text-align: left;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  white-space: nowrap;
  position: sticky;
  top: 0;
}

/* ── Body ── */
tbody tr {
  border-bottom: 1px solid #e2e8f0;
  transition: background-color 0.15s ease;
}

tbody tr:last-child { border-bottom: none; }
tbody tr:nth-child(even) { background-color: #f8fafc; }
tbody tr:hover { background-color: #eff6ff; }

tbody td,
tbody th {
  padding: 0.875rem 1.25rem;
  color: #334155;
  vertical-align: middle;
}

tbody th[scope="row"] {
  font-weight: 600;
  color: #0f172a;
  white-space: nowrap;
}

/* ── Footer ── */
tfoot td {
  padding: 0.875rem 1.25rem;
  background: #f1f5f9;
  border-top: 2px solid #cbd5e1;
  color: #0f172a;
}

/* ── Scores ── */
.score {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 50%;
  font-weight: 700;
  font-size: 0.85rem;
}

.score--high { background: #dcfce7; color: #15803d; }
.score--mid  { background: #fef9c3; color: #854d0e; }
.score--low  { background: #fee2e2; color: #b91c1c; }

/* ── Badges ── */
.badge {
  display: inline-block;
  padding: 0.2rem 0.65rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  white-space: nowrap;
}

.badge--active   { background: #dcfce7; color: #15803d; }
.badge--on-leave { background: #fef9c3; color: #854d0e; }
.badge--inactive { background: #fee2e2; color: #b91c1c; }

/* ── Responsive ── */
@media (max-width: 640px) {
  thead { display: none; }       /* Hide header on mobile */

  tbody tr {
    display: block;
    margin-bottom: 1rem;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
  }

  tbody td,
  tbody th {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
    border-bottom: 1px solid #f1f5f9;
  }

  /* Show column label using data attributes */
  tbody td::before {
    content: attr(data-label);
    font-weight: 600;
    font-size: 0.75rem;
    text-transform: uppercase;
    color: #64748b;
    letter-spacing: 0.05em;
  }
}
```

For the responsive mobile layout, add `data-label` to each `<td>`:

```html
<tr>
  <th scope="row">Jane Doe</th>
  <td data-label="Department">Engineering</td>
  <td data-label="Location">New York</td>
  <td data-label="Score">98</td>
  <td data-label="Status"><span class="badge badge--active">Active</span></td>
  <td data-label="Actions"><a href="#">View</a></td>
</tr>
```

---

## Quick Reference Summary

| Element | Purpose |
|---|---|
| `<table>` | Root wrapper for the entire table |
| `<thead>` | Groups header rows — column labels |
| `<tbody>` | Groups main data rows |
| `<tfoot>` | Groups footer rows — totals, summaries |
| `<tr>` | A horizontal row of cells |
| `<th>` | A header cell — bold, semantic, announces to screen readers |
| `<td>` | A data cell — regular table content |
| `<caption>` | Title/description for the whole table |
| `<colgroup>` | Groups columns for styling |
| `<col>` | Applies styles to a specific column |

| Attribute | Element | Purpose |
|---|---|---|
| `colspan` | `<th>`, `<td>` | Span across multiple columns |
| `rowspan` | `<th>`, `<td>` | Span across multiple rows |
| `scope="col"` | `<th>` | Header applies to its column |
| `scope="row"` | `<th>` | Header applies to its row |
| `scope="colgroup"` | `<th>` | Header applies to a group of columns |
| `scope="rowgroup"` | `<th>` | Header applies to a group of rows |
| `headers` | `<td>` | Explicitly links a cell to its header `id`s |
| `border-collapse` | CSS on `table` | Merges adjacent cell borders |
| `caption-side` | CSS on `caption` | Position caption top or bottom |

Used correctly, HTML tables give your data a clear structure that is navigable, readable, and fully accessible — for all users, on all devices.