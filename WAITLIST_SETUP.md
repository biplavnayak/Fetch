# Fetch Waitlist - Google Sheets Backend Setup

## Overview

The waitlist form collects emails and stores them in a Google Sheet accessible to people@bartlabs.in

## Setup Instructions

### Step 1: Create Google Sheet

1. Go to https://sheets.google.com
2. Create a new spreadsheet
3. Name it: "Fetch Waitlist"
4. Add headers in Row 1:
   - A1: `Timestamp`
   - B1: `Email`
   - C1: `Source`

### Step 2: Create Google Apps Script

1. In your Google Sheet, click **Extensions** → **Apps Script**
2. Delete any existing code
3. Paste this code:

```javascript
function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = JSON.parse(e.postData.contents);
    
    // Add row with timestamp, email, and source
    sheet.appendRow([
      data.timestamp || new Date().toISOString(),
      data.email,
      data.source || 'Unknown'
    ]);
    
    // Send email notification to people@bartlabs.in
    MailApp.sendEmail({
      to: 'people@bartlabs.in',
      subject: 'Fetch App - New Waitlist Signup',
      body: `New waitlist signup:\n\nEmail: ${data.email}\nTimestamp: ${data.timestamp}\nSource: ${data.source}`
    });
    
    return ContentService.createTextOutput(JSON.stringify({
      success: true
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
```

4. Click **Save** (disk icon)
5. Name the project: "Fetch Waitlist API"

### Step 3: Deploy as Web App

1. Click **Deploy** → **New deployment**
2. Click gear icon → Select **Web app**
3. Settings:
   - **Description**: Fetch Waitlist Collector
   - **Execute as**: Me (your@email.com)
   - **Who has access**: Anyone
4. Click **Deploy**
5. **Copy the Web App URL** (looks like: `https://script.google.com/macros/s/...`)

### Step 4: Update Landing Page

1. Open `/Volumes/SSD 2/Projects/01 SAAS/02 Raw separator/landing-page/index.html`
2. Find line with `const SCRIPT_URL =`
3. Replace the URL with your copied Web App URL
4. Save the file

### Step 5: Share Sheet with Team

1. Click **Share** button in Google Sheet
2. Add `people@bartlabs.in` with **Editor** access
3. Now the team can view all waitlist signups

## How It Works

1. User enters email on landing page
2. JavaScript sends email to Google Apps Script
3. Script adds row to Google Sheet
4. Script sends notification email to people@bartlabs.in
5. User sees success message

## Features

✅ **Automatic Collection**: All emails saved to Google Sheet
✅ **Email Notifications**: Instant email to people@bartlabs.in for each signup
✅ **Timestamp**: Records exact time of signup
✅ **Source Tracking**: Tracks where signup came from
✅ **Accessible**: Sheet accessible to entire team
✅ **Export**: Easy to export to CSV for email campaigns

## Viewing Waitlist

Access the Google Sheet anytime to see all signups:
- Timestamp of signup
- Email address
- Source (Landing Page)

## Backup: Formspree

The form also tries to send via Formspree as a backup notification method.

## Testing

After setup, test by:
1. Opening landing page
2. Entering test email
3. Clicking "Join Waitlist"
4. Check Google Sheet for new row
5. Check people@bartlabs.in for notification email

---

**Status**: Ready to deploy once Google Apps Script is set up
**Time to Setup**: ~5 minutes
**Cost**: Free (Google Sheets/Apps Script)
