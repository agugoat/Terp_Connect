# Backend Engineering Learning Guide

## 1. What the Backend Does in This Project

Backend engineers are responsible for:

- Understanding how web servers handle requests
- Using Flask routes to respond to URLs
- Loading data from a JSON file
- Passing that data into templates (HTML)
- Handling user actions (survey + join forms)
- Keeping the app stable and error-free

## 2. Learn the Core Concepts

These 6 concepts power the entire backend.

### 1. What a Route Is

A route controls what happens when someone visits a URL.

**Learn here:**
- [Flask Quickstart (Routing section)](https://flask.palletsprojects.com/en/stable/quickstart/#routing)

### 2. How to Handle Query Parameters

This is how search and category filtering work:

**Examples:**
- `/clubs?q=soccer`
- `/clubs?cat=Sports`

**Learn here:**
- [Accessing Request Data](https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data)

### 3. How Flask Loads and Passes Data to HTML

Flask uses templates to connect Python → HTML.

You need to understand:

- Template variables
- Template inheritance (base.html)
- Jinja loops

**Learn here:**
- [Flask Template Guide](https://flask.palletsprojects.com/en/stable/templating/)
- [Jinja Template Syntax](https://jinja.palletsprojects.com/en/stable/templates/)

### 4. How to Work With JSON

Our entire "database" is a `.json` file.

Backend engineers must understand:

- What JSON is
- How data is structured (objects, arrays)
- How to read JSON into Python
- How to loop/filter it

**Learn here:**
- [JSON Intro](https://www.w3schools.com/js/js_json_intro.asp)
- [Python + JSON Basics](https://www.geeksforgeeks.org/json-module-in-python/)


### 5. Handling Forms (Survey + Join)

Forms send data from the browser → backend.

Backend engineers must know:

- GET vs POST
- How form fields are sent
- How to read checkboxes
- How to redirect after a form

**Learn here:**
- [Working With Forms in Flask](https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping)

- [MDN Forms (Beginner-Friendly)](https://developer.mozilla.org/en-US/docs/Learn/Forms)

### 6. Application Flow (VERY Important)

Backend devs must understand the full request cycle:

```
Browser → Flask Route → Python Logic → Template → Browser
```

**Learn here (short and visual):**
- ["How Web Backends Work" – FreeCodeCamp](https://www.freecodecamp.org/news/how-the-web-works/)
- [Flask Overview Video (Beginner-Friendly)](https://www.youtube.com/watch?v=Z1RJmh_OqeA)

## 3. Backend Tasks (Conceptual Only — No Code)

Backend engineers are responsible for building the logic for:

### `/clubs`

- How to filter a list based on search text
- How to filter by category
- How to send a list of results to the template

### `/club/<id>`

- How to find one item from a list
- How to handle missing or invalid IDs
- How to prepare data for a "detail page"

### `/survey`

- How form submissions work
- How to capture checkbox values
- How to store them temporarily

### `/join`

- How POST forms send data
- How to extract form fields
- How to show a success page

These concepts come learnable from the links above.

## 4. Suggested Learning Path (1 Week)

### Day 1: Flask Basics

- Routing
- Running a Flask app
- Viewing routes in browser

*(Use Flask Quickstart)*

### Day 2: JSON + Python Logic

- How JSON stores data
- How to read JSON
- How to filter/search lists

*(Use Python JSON tutorials)*

### Day 3: Templates & Jinja

- Passing variables to HTML
- Looping through data
- Template inheritance

*(Use Flask Templates guide)*

### Day 4: Forms (Survey + Join)

- GET vs POST
- How form data is sent
- How to redirect

*(Use MDN Forms + Flask forms section)*

### Day 5: Putting It All Together

- Follow a user flow: `Home → Survey → Clubs → Club → Join`
- Ensure every route returns the correct template
- Make sure app does not crash

### Day 6–7: Debug + Integrate

- Test with frontend
- Fix variable mismatches
- Handle edge cases (empty search, invalid IDs)
- Work with integrator on QA

## 5. Backend Dev Mindset — What They Should Learn Beyond This Project

- How to think in "data → logic → output"
- How to safely handle user input
- How to organize code cleanly
- How frontend and backend communicate

This is foundational for learning bigger frameworks later (Django, FastAPI, Node.js, etc.)
