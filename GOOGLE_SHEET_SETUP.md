# Setup Apps Script for Your Google Sheet

## Step-by-Step Instructions

### Step 1: Open Your Sheet
Go to: https://docs.google.com/spreadsheets/d/1IdsCdU6jiCru6-OVXcEwH7yentfx2S7vF8pCKr67Isc/edit

### Step 2: Open Apps Script
1. Click **Extensions** → **Apps Script**
2. Delete any existing code
3. Paste this code:

```javascript
function doPost(e) {
  try {
    // Get the active sheet
    const sheet = SpreadsheetApp.openById('1IdsCdU6jiCru6-OVXcEwH7yentfx2S7vF8pCKr67Isc').getActiveSheet();
    
    // Parse the incoming data
    const data = JSON.parse(e.postData.contents);
    
    // Add new row with timestamp, email, and source
    sheet.appendRow([
      new Date().toISOString(),
      data.email,
      data.source || 'Fetch Landing Page'
    ]);
    
    // Send email notification
    MailApp.sendEmail({
      to: 'people@bartlabs.in',
      subject: 'Fetch App - New Waitlist Signup',
      body: 'New waitlist signup!\n\nEmail: ' + data.email + '\nTimestamp: ' + new Date().toISOString() + '\nSource: ' + (data.source || 'Fetch Landing Page')
    });
    
    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      message: 'Email added to waitlist'
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput('Fetch Waitlist API is running');
}
```

4. Click **Save** (💾 icon)
5. Name it: "Fetch Waitlist API"

### Step 3: Deploy as Web App
1. Click **Deploy** → **New deployment**
2. Click the ⚙️ (gear) icon next to "Select type"
3. Choose **Web app**
4. Configure:
   - **Description**: Fetch Waitlist Collector
   - **Execute as**: Me (your email)
   - **Who has access**: Anyone
5. Click **Deploy**
6. Click **Authorize access**
7. Choose your Google account
8. Click **Advanced** → **Go to Fetch Waitlist API (unsafe)**
9. Click **Allow**
10. **COPY THE WEB APP URL** - it looks like:
    `https://script.google.com/macros/s/AKfycby...../exec`

### Step 4: Send Me the URL
Once you copy the URL, send it to me and I'll update the landing page code!

---

## What This Does:
- ✅ Adds each email to your Google Sheet
- ✅ Sends notification to people@bartlabs.in
- ✅ Records timestamp
- ✅ Tracks source (Landing Page)

## Your Sheet Format:
Make sure Row 1 has these headers:
- Column A: **Timestamp**
- Column B: **Email**  
- Column C: **Source**
