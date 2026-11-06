# Extra instructions (read together with the main prompt)

## Data is already provided
The /data folder in this package already contains the REAL questions:
data/papers.json, paper1.json, paper2.json, paper3.json, bonus.json
(60 + 60 + 60 + 40 = 220 questions). Use these files as-is.
Do NOT create sample questions and do NOT change the JSON format.
Copy the /data folder into the project root.

## Deployment target: GitHub Pages (static hosting)
- Site must work when hosted at https://<username>.github.io/<repo-name>/ (a sub-path!).
  So use ONLY relative paths everywhere ("css/style.css", "data/paper1.json",
  "test.html?paper=paper1"). Never use paths starting with "/".
- Add an empty `.nojekyll` file in the project root.
- localStorage keys must be unique to this app (e.g. "ibps_mocktest_v1").
- Add a short "Deploy to GitHub Pages" section in README.md:
  git init -> git add . -> git commit -> create repo -> git remote add origin -> git push -> 
  Settings > Pages > Deploy from branch > main / root.
- No build step. The root folder is the deployable site.
