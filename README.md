# IBPS SO IT Officer (Mains) Practice Tests

A fully offline, single-file MCQ exam practice website built with plain HTML, CSS and vanilla JavaScript — no frameworks, no build tools, no backend.

---

## 🚀 How to Run

> **Important**: The site uses `fetch()` to load JSON data files. This requires a local HTTP server — opening `index.html` directly via `file://` will fail in most browsers (CORS restriction).

### Option 1 — VS Code Live Server (easiest)
1. Install the **Live Server** extension in VS Code.
2. Right-click `index.html` → **Open with Live Server**.
3. Browser opens at `http://127.0.0.1:5500`.

### Option 2 — Python (built-in on macOS/Linux)
```bash
cd /path/to/Exam
python3 -m http.server 8000
# then open http://localhost:8000
```

### Option 3 — Node `http-server`
```bash
npx http-server . -p 8000
# then open http://localhost:8000
```

---

## 🌐 Deploy to GitHub Pages (Static Hosting)

The site is built with 100% vanilla web standards, relative URLs, and an empty `.nojekyll` file, making it directly deployable on GitHub Pages:

1. **Initialize Git & Commit**:
   ```bash
   cd /path/to/Exam
   git init
   git add .
   git commit -m "Initial commit: IBPS SO IT Officer Practice Tests"
   ```

2. **Create a GitHub repository** and link it:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**:
   - In your GitHub repo, go to **Settings** → **Pages**.
   - Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
   - Under **Branch**, select `main` and `/ (root)`, then click **Save**.
   - Your site will be live at `https://<your-username>.github.io/<your-repo-name>/`.
   - Because all internal links and asset paths are relative, it works seamlessly under subpath URLs.

---

## 📂 File Structure

```
Exam/
├── .nojekyll           # Bypasses Jekyll processing on GitHub Pages
├── index.html          # Home / paper list + progress dashboard
├── test.html           # Exam screen (loads via ?paper=<id>)
├── result.html         # Result screen (loads via ?paper=<id>)
├── css/
│   └── style.css       # All styles (light + dark, responsive)
├── js/
│   ├── app.js          # Shared helpers (storage, scoring, loading)
│   ├── home.js         # Home page logic
│   ├── test.js         # Exam screen logic
│   └── result.js       # Result page logic
├── data/
│   ├── papers.json     # List of all papers (master index)
│   ├── paper1.json     # Questions for Paper 1
│   ├── paper2.json     # Questions for Paper 2
│   ├── paper3.json     # Questions for Paper 3
│   └── bonus.json      # Questions for Bonus Paper
└── README.md
```

---

## ➕ How to Add a New Paper (Two Steps Only)

### Step 1 — Create the question file

Create `data/myNewPaper.json` with this structure:

```json
{
  "id": "myNewPaper",
  "sections": [
    {
      "name": "Section Name",
      "questions": [
        {
          "q": "Your question text here. Use ^n for superscript (e.g. O(n^2)).",
          "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
          ],
          "answer": 1
        }
      ]
    },
    {
      "name": "Another Section",
      "questions": [
        {
          "q": "Second question?",
          "options": ["True", "False", "Maybe", "None"],
          "answer": 0
        }
      ]
    }
  ]
}
```

**Rules:**
- `answer` is the **0-based index** of the correct option (0 = A, 1 = B, 2 = C, 3 = D).
- `id` must match the filename (without `.json`).
- You can have any number of sections and any number of questions per section.
- Superscripts: write `^x` or `^(expr)` — rendered as `<sup>x</sup>` safely.

### Step 2 — Register in `papers.json`

Add one entry to `data/papers.json`:

```json
{
  "id": "myNewPaper",
  "title": "My New Paper",
  "subtitle": "Topic description",
  "file": "data/myNewPaper.json",
  "durationMin": 45,
  "correctMark": 1,
  "negativeMark": 0.25
}
```

**That's it.** No JavaScript or HTML changes are ever needed.

---

## 🔢 Scoring Rules

| Result | Marks |
|--------|-------|
| Correct answer | +`correctMark` (default: +1) |
| Wrong answer | −`negativeMark` (default: −0.25) |
| Unattempted | 0 |

- **Total Marks** = Number of questions × `correctMark`
- **Final Score** = (Correct × correctMark) − (Wrong × negativeMark)
- **Percentage** = Score / Total Marks × 100
- Score can be negative (shown clearly on result page)
- These values are set **per paper** in `papers.json`

---

## ⌨️ Keyboard Shortcuts (Exam Screen)

| Key | Action |
|-----|--------|
| `1` or `A` | Select Option A |
| `2` or `B` | Select Option B |
| `3` or `C` | Select Option C |
| `4` or `D` | Select Option D |
| `←` / `→` | Previous / Next question |
| `↑` / `↓` | Previous / Next question |
| `M` | Toggle Mark for Review |
| `X` or `Esc` | Clear selection (unattempt) |

---

## 💾 Data & Privacy

- All progress is stored in your browser's **localStorage** only — nothing is sent to any server.
- **Export** your progress from the home page footer as a JSON file.
- **Import** a previously exported JSON to restore progress.
- **Reset All** wipes all localStorage data (with confirmation).
- Answers are stored in the JSON files. This is intentional for a personal-use tool. Answers are never shown in the UI during the test.

---

## 🎨 Theming

- Supports **Light** and **Dark** mode (toggle button in top-right, or follows your OS preference).
- All colours are CSS custom properties in `:root` inside `css/style.css`.
- Change `--gold-400` / `--gold-500` etc. to change the accent colour sitewide.

---

## 📱 Browser Support

Works in all modern browsers (Chrome, Firefox, Safari, Edge). Requires ES6+.
Backdrop-filter glass effect degrades gracefully on older browsers (solid background fallback).

