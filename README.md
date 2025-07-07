# PDF Sync for GitHub Pages

## Quick Setup

1. **Fork or create a new repository**
2. **Upload the HTML file** as `index.html`
3. **Enable GitHub Pages** in repository settings
4. **Access your app** at `https://yourusername.github.io/your-repo-name`

## File Structure

```
your-repo/
├── index.html (the QR PDF sync app)
├── mobile1/
│   ├── 1_1.pdf
│   ├── 1_2.pdf
│   ├── 3_15.pdf
│   ├── 14_20.pdf
│   └── ... (all PDFs from 1_1 to 14_20)
├── mobile2/
│   ├── 1_1.pdf
│   ├── 1_2.pdf
│   ├── 3_15.pdf
│   ├── 14_20.pdf
│   └── ... (all PDFs from 1_1 to 14_20)
└── README.md
```

## Usage

1. **Presenter device**: Open the GitHub Pages URL
2. **Select chapter (1-14) and verse (1-20)** using the dropdown menus
3. **Generate QR code**
4. **Viewer devices**: Scan QR code
5. **Select local folder** on each device (mobile1, mobile2, etc.)
6. **PDF loads automatically** - each device loads the same numbered PDF from their local folder

## Example
- Presenter selects: Chapter 3, Verse 15
- QR code is generated
- Viewers scan QR code
- Device 1 loads: `mobile1/3_15.pdf`
- Device 2 loads: `mobile2/3_15.pdf`
- All devices show the same content!

## Benefits

- ✅ No registration required
- ✅ Works on any device with a browser
- ✅ Free hosting on GitHub Pages
- ✅ HTTPS enabled by default
- ✅ Global CDN for fast loading
- ✅ Perfect for presentations and meetings
