# Policy Hackathon Site
Website for a policy hackathon with different challenge tracks spanning AI, health, climate, economics, and more. Built with plain HTML/CSS, deployed via GitHub Pages.


A plain HTML/CSS site — no build tools, no backend. `index.html` shows all 11
challenge tracks as cards; each card links to its own page in `/challenges/`.

## File structure

```
site/
├── index.html              ← main page, links to all 11 tracks
├── css/
│   └── style.css           ← shared styles for every page
└── challenges/
    ├── track-a.html
    ├── track-b.html
    ├── ... (11 total, one per track)
    └── track-l.html
```

## 1. Put it on GitHub (step by step)

1. Go to https://github.com and log in (create a free account if you don't
   have one).
2. Click the **+** icon top-right → **New repository**.
3. Name it something like `policy-hackathon` → set it to **Public** →
   click **Create repository**.
4. On the new repo's page, click **uploading an existing file** (or
   **Add file → Upload files**).
5. Drag in everything *inside* the `site` folder — `index.html`, the `css`
   folder, and the `challenges` folder — keeping the same folder structure.
   GitHub's uploader preserves folders if you drag the whole folder in, or
   you can use GitHub Desktop / git commands below if you prefer.
6. Scroll down, click **Commit changes**.

### Alternative: using git on your computer
```bash
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/policy-hackathon.git
git push -u origin main
```

## 2. Turn on GitHub Pages (this is what makes it a live website)

1. In your repo, click **Settings** (top menu).
2. In the left sidebar, click **Pages**.
3. Under "Build and deployment" → **Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose **main** and folder **/ (root)** → click **Save**.
5. Wait ~1 minute, refresh the page. GitHub will show a green box with your
   live URL, something like:
   `https://YOUR-USERNAME.github.io/policy-hackathon/`

That's it — no server, no hosting bill, updates automatically every time you
push a change to `main`.

## 3. Replace the placeholder links

Every page has a few links that currently point at placeholder addresses.
Search each file for `REPLACE_WITH` and swap in your real links:

- **Challenge Document** → a Google Doc per track (File → Share → "Anyone
  with the link can view")
- **Join the Discord** → your Discord server/channel invite link
  (`discord.gg/...`)
- **Submit Your Project** → a Google Form. Add a **file upload** question
  in the form if you want people to attach files directly (Google Forms
  supports this natively and saves uploads to a Drive folder tied to the
  form), or just collect a GitHub/Drive link as a short-answer question.
- **Email signup form** → currently points at a placeholder Formspree URL
  (`formspree.io/f/REPLACE_WITH_FORM_ID`). Formspree (formspree.io) is a
  free service that takes plain HTML `<form>` submissions and emails them
  to you — no backend code needed. Sign up, create a form, and paste your
  real endpoint into the `action="..."` attribute in each file (search for
  `email-form`).

## 4. Editing content later

Every challenge page was generated from `build_site.py` (not included here,
but keep asking if you want it) — but you don't need Python to make edits.
Each `challenges/track-X.html` is a normal HTML file: open it in any text
editor (VS Code is a good free one), find the section you want to change
(e.g. `<h2>Required Deliverables</h2>`), and edit the text inside the
`<li>` tags. Save, commit, push — GitHub Pages updates automatically.

## 5. Adding a 12th track / renaming things

- Copy any file in `challenges/` as a starting template.
- Add a matching `<article class="card">...</article>` block in
  `index.html` inside the `<div class="grid">` section, with an `<a>` tag
  pointing to your new file.
