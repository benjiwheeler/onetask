# One Task

A simple web app that picks a random task from your Google Sheets to-do list, with weighted selection based on priority and due date.

## Setup

1. **Google Sheets Configuration:**
   - Create a Google Sheet with columns: `Task Name`, `Due Date`, `Priority`
   - Set sharing to "Anyone with the link can view"
   - Copy the sheet ID from the URL
   - Update `SHEET_ID` in `index.html` (line 166)

2. **Running the App:**

   The app needs to run on a local server to avoid CORS issues. You have several options:

   ### Option 1: Python (Recommended)
   ```bash
   python3 server.py
   ```
   Then open: http://localhost:8000

   ### Option 2: Python's built-in server
   ```bash
   python3 -m http.server 8000
   ```
   Then open: http://localhost:8000

   ### Option 3: Node.js (if you have npx)
   ```bash
   npx http-server -p 8000
   ```
   Then open: http://localhost:8000

   ### Option 4: PHP (if you have PHP installed)
   ```bash
   php -S localhost:8000
   ```
   Then open: http://localhost:8000

## How It Works

- Tasks are weighted by **priority** (High=3, Medium=2, Low=1) and **due date** (overdue=4x, within week=3x, within month=2x, later=1x)
- More urgent/important tasks have a higher chance of being selected
- Click "Pick a Task" to get your next task!

## Troubleshooting

**"Could not load tasks" error:**
- Verify the Google Sheet is publicly accessible (Share > Anyone with the link can view)
- Make sure you're running a local server (not opening file:// directly)
- Check browser console (F12) for specific errors
- Verify the sheet name matches (default is "Sheet1")

**Sheet ID:**
Your current sheet ID is: `115SgANqyv_GaLVTpIlEzRrpuOBTWraMK9_-WEAcsGZE`

**Original spreadsheet:**
https://docs.google.com/spreadsheets/d/115SgANqyv_GaLVTpIlEzRrpuOBTWraMK9_-WEAcsGZE/edit?usp=sharing
