# Deploy Landing Page to fetch.bartlabs.in

## ✅ Local Testing Complete

The separated landing page is working at: **http://127.0.0.1:5001**

## 📁 Project Structure

```
landing-page/           # Standalone landing page (NEW)
├── app.py             # Flask app for landing
├── requirements.txt   # Dependencies
├── vercel.json       # Vercel config
├── templates/
│   └── landing.html  # Landing page
└── static/
    ├── landing.css   # B&W styles
    ├── hero_lineart.png
    └── logo.png

02 Raw separator/      # Main app (UNCHANGED)
├── app.py            # Desktop app backend
├── templates/
│   └── index.html   # App interface
└── ...
```

## 🚀 Deployment Steps

### Step 1: Initialize Git in Landing Page Folder

```bash
cd "/Volumes/SSD 2/Projects/01 SAAS/02 Raw separator/landing-page"
git init
git add .
git commit -m "Initial commit: Fetch landing page with B&W line art"
```

### Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `fetch-landing`
3. Make it **Public**
4. **DO NOT** initialize with README
5. Click "Create repository"

### Step 3: Push to GitHub

```bash
cd "/Volumes/SSD 2/Projects/01 SAAS/02 Raw separator/landing-page"

# Add your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/fetch-landing.git
git branch -M main
git push -u origin main
```

### Step 4: Deploy to Vercel

**Option A: Vercel Web Interface (Recommended)**

1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Select `fetch-landing` repository
4. **Project Settings:**
   - Framework Preset: `Other`
   - Root Directory: `./` (leave as is)
5. Click **"Deploy"**

**Option B: Vercel CLI**

```bash
cd "/Volumes/SSD 2/Projects/01 SAAS/02 Raw separator/landing-page"
npm install -g vercel
vercel --prod
```

### Step 5: Configure Custom Domain

After deployment:

1. Go to Vercel project settings
2. Navigate to "Domains"
3. Add custom domain: `fetch.bartlabs.in`
4. Follow Vercel's DNS instructions
5. Update your DNS settings at your domain provider

## ✅ After Deployment

Your landing page will be live at:
- **Production**: https://fetch.bartlabs.in/
- **Vercel URL**: https://your-project.vercel.app/

## 🧪 Testing Checklist

After deployment, verify:

- [ ] Landing page loads at https://fetch.bartlabs.in/
- [ ] All images load (hero, logo)
- [ ] Black & white line art renders correctly
- [ ] Step numbers are B&W
- [ ] Workflow diagram is B&W
- [ ] Feature icons are B&W
- [ ] Waitlist form works
- [ ] Toast notifications appear
- [ ] Responsive on mobile
- [ ] No console errors

## 📝 Important Notes

### Two Separate Projects

1. **Landing Page** (`landing-page/`)
   - Deployed to: https://fetch.bartlabs.in/
   - Purpose: Marketing/waitlist
   - Standalone Flask app

2. **Main App** (`02 Raw separator/`)
   - Desktop application backend
   - NOT deployed to web
   - Used by Electron app

### No Conflicts

- Landing page is completely separate
- Main app remains unchanged
- Desktop app continues to work
- Clean separation of concerns

## 🔧 Troubleshooting

### If deployment fails:

1. Check `vercel.json` is in root of `landing-page/`
2. Verify `requirements.txt` exists
3. Check Vercel build logs
4. Ensure Flask version is 3.0.0

### If images don't load:

1. Check file paths in `landing.html`
2. Verify images are in `static/` folder
3. Check Vercel static file serving

---

**Status**: ✅ Ready to Deploy
**Tested Locally**: http://127.0.0.1:5001 ✅
**Next**: Push to GitHub → Deploy to Vercel → Configure Domain
