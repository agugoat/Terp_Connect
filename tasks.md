# TerpConnect – Team Tasks & Assignments

## Backend Engineers — Muhammad & Caden

### Task 1 — Load JSON Data  (Muhammad)
- Create data/clubs.json
- Load it at startup in app.py
- Validate JSON format
- Confirm app runs

### Task 2 — Implement /clubs Route (Muhammad)
- Add search filter (?q=)
- Add category filter (?cat=)
- Pass variables: clubs, q, cat, categories

### Task 3 — Implement /club/<id>   (Caden)
- Find one club by id
- Handle invalid ids
- Pass club to template

### Task 4 — Implement /survey    (Caden)
- GET: show survey.html
- POST: collect checkboxes
- Store in USER_INTERESTS
- Redirect to /clubs

### Task 5 — Implement /join (caden and Muhammad)
- Receive name and club_id
- Find club
- Pass to joined.html



### Optional Stretch Tasks
- Sort clubs alphabetically
- Add categories to navbar
- Recommended clubs
- Custom 404.html


## Frontend Engineers — Sydney & Joshua

### Task 1 — clubs.html  (sydney)
- Search bar, category dropdown
- Club cards with loop
- View Club link
- Handle no-club case

### Task 2 — club.html (sydney)
- Display club details
- Join form
- Back to clubs link

### Task 3 — survey.html  (joshua)
- Checkbox inputs
- POST to /survey
- Skip link


## Integration Engineer — Isaiah

### Task 1 — System Architecture Diagram
Show:
User → Flask → Backend Routes → Templates → Output

### Task 2 — Test All Routes
- Homepage, clubs, search, filters
- Club detail valid/invalid
- Survey POST
- Join POST

### Task 3 — Maintain Project Structure
Ensure templates/, static/, data/, app.py are clean


### Task 5 — QA Checklist
- No Flask errors
- No broken links
- Template + variable name matching
- Forms use correct inputs
