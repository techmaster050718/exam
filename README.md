# Lakshya mock-test platform

A static, multi-subject MCQ practice site built with HTML, CSS, and vanilla JavaScript. It has no build step or backend. All progress stays in the browser under the existing `ibps_mocktest_v1` localStorage key.

## Run locally

The JSON files require a local HTTP server:

```bash
cd /path/to/Exam
python3 -m http.server 8000
```

Open `http://localhost:8000`. Do not open the HTML files directly with `file://`.

## Structure

```
index.html          subject dashboard
subject.html        papers for one subject
test.html           timer-based exam screen
result.html         score, section analysis, and answer review
data/site.json      platform branding
data/subjects.json  subject directory
data/papers.json    paper directory and marking rules
data/*.json         question files
images/             optional question and option images
js/                 application code
css/style.css       responsive styles
```

## Content formats

`data/site.json` controls the name, tagline, and footer everywhere:

```json
{"name":"Lakshya","tagline":"Mock tests for IBPS, CDS & SSB","footer":"Practice smart. Aim higher."}
```

`data/subjects.json` is an array of subject cards:

```json
[{"id":"ibps-aptitude","title":"IBPS - Aptitude & Reasoning","description":"Practice sets","icon":"🧮"}]
```

Register each paper in `data/papers.json`:

```json
{
  "id":"my-paper",
  "subject":"ibps-aptitude",
  "title":"My Practice Paper",
  "subtitle":"Topic description",
  "file":"data/my-paper.json",
  "durationMin":45,
  "correctMark":1,
  "negativeMark":0.25
}
```

Papers without a valid `subject` are safely shown under **General**. A subject with no papers displays as “Coming soon.”

Each question file contains sections and questions:

```json
{
  "id":"my-paper",
  "sections":[{
    "name":"Arithmetic",
    "questions":[{
      "q":"What is 2 + 2?",
      "options":["2","3","4","5"],
      "answer":2,
      "img":"images/my-paper/q1.png",
      "optionImgs":["images/my-paper/a.png",null,null,null]
    }]
  }]
}
```

`answer` is the zero-based option index. `img` and `optionImgs` are optional; omit them for normal text questions. Image paths are relative to the site root.

## Add content

1. Add the question JSON file in `data/`.
2. Add its entry in `data/papers.json`, setting `subject` to an existing subject ID.
3. For a new category, add one entry in `data/subjects.json`.
4. Put any optional visual assets under `images/` and reference their relative paths in questions.

No HTML, CSS, or JavaScript edits are needed to add future subjects or papers.

## Scoring

For each paper, the score is:

`(correct × correctMark) − (wrong × negativeMark)`

Unattempted questions score zero. The percentage is score divided by total available marks. `negativeMark` may be `0`, and marking values can be fractional. Results preserve section-wise marks; the subject page aggregates the weakest completed sections.

## Deploy to GitHub Pages

All internal paths are relative, and `.nojekyll` is included for GitHub Pages sub-path hosting.

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

In the GitHub repository, open **Settings → Pages**, choose **Deploy from a branch**, then select `main` and `/ (root)`.
