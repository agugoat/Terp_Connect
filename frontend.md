# Frontend Engineering Learning Guide

## 1. What the Frontend Does in This Project

Frontend engineers are responsible for:

- Designing all user-facing pages
- Structuring content with HTML
- Making pages look clean using CSS + Bootstrap
- Displaying data coming from the backend using Jinja templates
- Building forms for search, survey, and "Join"
- Ensuring pages are clear, simple, and responsive

Frontend = the look and feel of TerpConnect.

## 2. The 4 Skills Frontend Engineers Need

You only need four things to build this entire project.

### 1. HTML (Page Structure)

HTML is the skeleton of your webpage.

**Learn:**
- Tags (`<div>`, `<h1>`, `<p>`, `<a>`, `<form>`)
- Page layout
- Linking pages
- Forms

**Beginner links (super easy to understand):**
- [HTML Basics – MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
- [HTML Tutorial – W3Schools](https://www.w3schools.com/html/default.asp)

**Why it matters:**
Every page you build starts with HTML.

### 2. CSS (Visual Styling)

CSS controls how things look.

**Learn:**
- Colors
- Margin & padding
- Alignment
- Font resizing
- Layout basics

**Beginner links:**
- [CSS Basics – W3Schools](https://www.w3schools.com/css/css_intro.asp)
- [CSS Layout Guide](https://www.w3schools.com/css/css_boxmodel.asp)
- [Flexbox Visual Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

**Why it matters:**
CSS makes the site look clean instead of messy.

### 3. Bootstrap (Make It Look Good Quickly)

Bootstrap gives you pre-made layouts so you don't need to hand-write CSS.

You only need:

- Grid system (row, col)
- Cards
- Buttons
- Navbars
- Spacing utilities (`mb-3`, `mt-4`, `p-3`)

**Learn here:**
- [Bootstrap Getting Started](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Cards (important for clubs)](https://getbootstrap.com/docs/5.3/components/card/)
- [Buttons](https://getbootstrap.com/docs/5.3/components/buttons/)
- [Grid System](https://getbootstrap.com/docs/5.3/layout/grid/)

**Why it matters:**
It lets you build professional-looking pages FAST.

### 4. Jinja Templates (Connecting Frontend → Backend)

Jinja allows HTML to display Python data.

**Learn:**
- `{{ variable }}`
- `{% for item in list %}`
- `{% extends "base.html" %}`
- `{% block content %}`

**Learn here:**
- [Flask Template Basics](https://flask.palletsprojects.com/en/stable/templating/)
- [Jinja Template Syntax (short & clear)](https://jinja.palletsprojects.com/en/stable/templates/)

**Why it matters:**
This is how the club data gets displayed on the page.

## 3. What You Will Build (Conceptually)

Frontend engineers will build four pages for the MVP:

### `base.html`

Your "master layout" that all pages extend.

Should contain:

- Navbar
- Bootstrap imports
- `{% block content %}`

**Learn template inheritance:**
- [Flask Template Inheritance](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/)

### `home.html`

Simple landing page.

Contains:

- Title
- Intro text
- Buttons → "Browse Clubs" / "Survey"

### `clubs.html` (most important page)

Contains:

- Search bar
- Category dropdown
- Grid of cards
- Jinja loop to display each club

**Study:**
- Bootstrap Cards
- Bootstrap Grid
- Jinja For-Loops

### `club.html`

The detail page for ONE club.

Contains:

- Title
- Description
- Contact info
- "I'm Interested" form

**Learn:**
- [MDN Forms (Beginner-friendly)](https://developer.mozilla.org/en-US/docs/Learn/Forms)

**Optional (If Time Allows):**
- `survey.html`
- `joined.html`


## 4. One-Week Learning Schedule 

This matches the backend schedule.

### Day 1 — Learn HTML Basics

- Read MDN HTML intro
- Build a basic page layout
- Understand headers, text, divs

### Day 2 — Learn CSS + Spacing

- Learn margin, padding, and layout
- Experiment with simple styles
- Try centering content & spacing sections

### Day 3 — Learn Bootstrap for Layouts

Focus only on:

- Container
- Row / col
- Card
- Buttons
- Spacing

### Day 4 — Learn Jinja Template Basics

Understand how to:

- Display a variable (`{{ club.name }}`)
- Loop over clubs (`{% for club in clubs %}`)
- Extend `base.html`

### Day 5 — Build `clubs.html` layout

Combine Bootstrap + Jinja concepts.

### Day 6 — Detail Page + Forms

Build a clean club detail page.

Learn:

- How forms submit data
- How Flask passes it back

### Day 7 — Polish UI + Fix Layouts

- Test on mobile & desktop
- Check spacing, card alignment, nav links

## 5. Frontend Developer Mindset

Frontend engineers should focus on:

- Consistency over complexity
- Clean spacing
- Readable layout
- Matching class names to backend variables
- Not writing unnecessary CSS
- Using Bootstrap instead of reinventing styles
- Testing pages frequently

Frontend = make it look good + make it clear.

