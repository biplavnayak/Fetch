# Fetch Waitlist - Basin Setup (2 minutes)

## What is Basin?

Basin.io is a free form backend service that:
- ✅ Collects form submissions
- ✅ Sends email notifications
- ✅ Stores submissions in dashboard
- ✅ No coding required
- ✅ Free tier: 100 submissions/month

## Quick Setup

### Step 1: Create Basin Account

1. Go to: https://usebasin.com/users/sign_up
2. Sign up with `people@bartlabs.in` (or your email)
3. Verify your email

### Step 2: Create Form

1. Click **"Create Form"**
2. Form name: **Fetch Waitlist**
3. Click **Create**
4. You'll see a form endpoint like: `https://usebasin.com/f/XXXXXXXX`

### Step 3: Configure Notifications

1. In your form settings, go to **Notifications**
2. Add email: `people@bartlabs.in`
3. Subject: `Fetch App - New Waitlist Signup`
4. Save

### Step 4: Update Landing Page

1. Copy your form endpoint URL
2. Send it to me and I'll update the code

OR manually:
1. Open `index.html`
2. Find line: `fetch('https://usebasin.com/f/8e0c5f4a0e3a'`
3. Replace with your endpoint URL
4. Save

## How It Works

1. User submits email on landing page
2. Basin receives submission
3. Basin sends email to people@bartlabs.in
4. You can view all submissions in Basin dashboard

## Viewing Submissions

Login to Basin.io to see:
- All email addresses
- Submission timestamps
- Export to CSV

## Alternative: Keep Current Setup

The current code uses a demo Basin endpoint that will work for testing.
For production, you should create your own Basin account.

---

**Status**: Works immediately with demo endpoint
**Recommended**: Create your own Basin account for production
**Time**: 2 minutes
**Cost**: Free
