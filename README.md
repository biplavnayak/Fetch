# Fetch Landing Page

Clean, minimal landing page for Fetch - the smart file organization tool.

## Features

- Black & white line art design
- Notion-style minimal aesthetic
- Waitlist email collection
- Responsive layout
- SVG illustrations

## Local Development

```bash
cd landing-page
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:5001

## Deploy to Vercel

1. Create new Vercel project
2. Import this `landing-page` folder
3. Deploy!

Vercel will auto-detect Flask and deploy.

## Structure

```
landing-page/
├── app.py              # Flask app
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel config
├── templates/
│   └── landing.html   # Landing page HTML
└── static/
    ├── landing.css    # Styles
    ├── hero_lineart.png  # Hero illustration
    └── logo.png       # Fetch logo
```

## Tech Stack

- Flask (Python backend)
- Vanilla HTML/CSS/JavaScript
- Black & white line art design
- No frameworks

---

© 2025 BartLabs. All rights reserved.
