# Integration & QA Engineering Learning Guide

## 1. What Integration Engineers Do

Integration Engineers are responsible for:

- Making sure backend & frontend communicate correctly
- Keeping GitHub branches organized
- Reviewing pull requests
- Ensuring that every page loads without errors
- Checking that template names match route names
- Helping teammates fix environment or project-structure issues
- Documenting issues, fixes, and workflow

They make sure the project runs smoothly as a whole.

## 2. Concepts They Must Learn

These four areas are essential.

### 1. Flask Project Structure

Integration engineers must understand at a high level:

- `app.py` → runs all routes
- `templates/` → HTML files (frontend)
- `static/` → CSS, images
- `data/` → JSON file (backend data)

**Learn here:**
- [Flask Project Layout Guide](https://flask.palletsprojects.com/en/stable/patterns/packages/)

### 2. How Backend Passes Data to Frontend

They must understand:

- Jinja template rendering
- How variables get passed into HTML
- How loops render dynamic pages

**Learn here:**
- [Flask Templating Overview](https://flask.palletsprojects.com/en/stable/templating/)
- [Jinja Template Basics](https://jinja.palletsprojects.com/en/stable/templates/)

Their job is NOT to write Jinja but to verify that:

- Backend variable names match HTML expectations
- Templates use the right names
- Nothing crashes due to mismatches

### 3. Git & GitHub Branching Workflow

Integrators must understand how to:

- Pull before starting work
- Push to the correct branch
- Resolve merge conflicts
- Open + review pull requests
- Merge safely into main

**Learn here (simple + visual):**
- [Git Branching Basics (Atlassian Tutorial)](https://www.atlassian.com/git/tutorials/using-branches)
- [GitHub Pull Requests (Video)](https://www.youtube.com/watch?v=rgbCcBNZcdQ)

### 4. Testing & QA Basics

They are responsible for:

- Clicking every button
- Loading every page
- Testing route edge cases
- Ensuring no broken links
- Running the server often
- Checking error messages in terminal
- Making sure teammates didn't accidentally break a page

**Learn here (gentle intro):**
- [Software Testing Basics (GeeksForGeeks)](https://www.geeksforgeeks.org/software-testing-basics/)
- [QA Testing for Beginners (Video)](https://www.youtube.com/watch?v=H7QfF0a0Dbs)

## 3. What Integration Engineers Do in This Project (Conceptual)

### 1. Verify Project Runs Everywhere

Checklist they should follow each work session:

- Can everyone activate `.venv`?
- Can everyone run `python app.py`?
- Does the homepage load?
- Are all packages installed?

They fix team environment issues.

### 2. Maintain Project Structure

They make sure files are in the right place:

- HTML → `templates/`
- CSS/images → `static/`
- JSON → `data/`
- Python logic → `app.py`

They prevent the entire project from breaking due to misplaced files.

### 3. Translate Between Backend ↔ Frontend

Integration engineers communicate for both sides:

- If backend sends `clubs`, frontend must use `clubs`
- If frontend expects `club.description`, backend must provide that key
- If template name changes, route must match it

They ensure consistency.




### 4. Review Pull Requests

They check PRs for:

- Did the change break a route?
- Does the app still run afterward?
- Are files placed correctly?
- Does the naming still match?
- Are there merge conflicts?

They do light reviews — not deep code reviews.

### 5. Create a QA Checklist

They maintain a simple test document:

**Example checklist:**
- Does `/clubs` load?
- Does the page crash when search is empty?
- Does `/club/<id>` work for valid & invalid IDs?
- Does survey redirect correctly?
- Does "Join" show the correct club?
- Are card layouts consistent?

This keeps the whole app stable.

## 4. System Architecture Diagram (Concept-Level)

Below is a simple chart that Integration Engineers should recreate (in Google Docs, Figma, or draw.io).

```
                ┌─────────────────────────────┐
                │           User              │
                │ (Browser clicks & actions)  │
                └──────────────┬──────────────┘
                               │
                               ▼
              ┌──────────────────────────────────┐
              │             Flask App             │
              │             (app.py)              │
              └───────┬─────────────┬────────────┘
                      │             │
                      │             │
        ┌─────────────▼──────┐   ┌──▼──────────────────┐
        │   Backend Logic    │   │ Template Renderer    │
        │  (Routes, Filters, │   │  (Jinja → HTML)      │
        │   Search, Forms)   │   └───────────┬──────────┘
        └─────────────┬──────┘               │
                      │                      │
                      ▼                      ▼
        ┌──────────────────────┐    ┌──────────────────────┐
        │   clubs.json (data)  │    │  templates/*.html     │
        │ (name, category, etc)│    │ (frontend UI pages)   │
        └──────────────────────┘    └─────────┬────────────┘
                                              │
                                              ▼
                                ┌────────────────────────────┐
                                │         Final Output        │
                                │   Rendered HTML → Browser   │
                                └────────────────────────────┘
```

Integration engineers must understand how every arrow flows.

## 5. One-Week Learning Plan

### Day 1 — Understand Project Structure

**Read:**
- Flask project layout
- How data files + templates + routes interact

### Day 2 — Learn GitHub Workflow

**Study:**
- Branches
- Pull requests
- Merge conflicts

**Practice:**
- Create a branch
- Make a small change
- Merge safely

### Day 3 — Learn How Backend Passes Data to Frontend

**Study:**
- Jinja variables
- Template rendering
- `render_template()` concepts

### Day 4 — QA Basics

**Study how to:**
- Test every route
- Test empty search inputs
- Test invalid IDs
- Document bugs

### Day 5 — Build the Architecture Diagram

Create the system chart showing:

```
User → Flask → Backend → Templates → Output
```

### Day 6 — Run Integration Tests

Verify end-to-end flow:

- Home → Survey
- Survey → Clubs
- Clubs → Club Detail
- Join → Confirmation

### Day 7 — Final Stability Check

- All pages load
- No 500 errors
- No missing templates
- Data flows correctly
- No mismatched names

## Final Message to Integration Engineers

Your job is not to code the features — your job is to make the project work as one piece.

You are the:

- Connector
- Tester
- Communicator
- Quality gate
- System map designer

If you understand how:

- Routes work,
- Templates load,
- JSON feeds data, and
- GitHub merges code…

Then the entire team will be able to finish on time.

