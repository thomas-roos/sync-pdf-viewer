# PDF Sync for GitHub Pages

**✅ Now with PeerJS for reliable real-time connections!**

## Quick Setup

1. **Fork or create a new repository**
2. **Upload the HTML file** as `index.html`
3. **Enable GitHub Pages** in repository settings
4. **Access your app** at `https://yourusername.github.io/your-repo-name`

## 🚀 New Features

- ✅ **Real-time peer-to-peer connections** using PeerJS
- ✅ **Multiple viewers support** - unlimited concurrent connections
- ✅ **Reliable data synchronization** - no more connection issues
- ✅ **Navigation controls** with keyboard shortcuts
- ✅ **Connection status monitoring** with debug info
- ✅ **Automatic reconnection** handling

## File Structure

```
your-repo/
├── index.html (the QR PDF sync app)
├── example-pdfs/
│   ├── 1_1.pdf
│   ├── 1_2.pdf
│   ├── 3_15.pdf
│   ├── 14_20.pdf
│   └── ... (all PDFs from 1_1 to 14_20)
└── README.md
```

## Usage

1. **Presenter device**: Open the GitHub Pages URL
2. **Select section (1-14) and page (1-20)** using the dropdown menus
3. **Generate QR code**
4. **Viewer devices**: Scan QR code
5. **Enter local folder name** on each device (e.g., "pdfs", "documents", "my-folder")
6. **PDF loads automatically** - each device loads the same numbered PDF from their specified folder

## Example
- Presenter selects: Section 3, Page 15
- QR code is generated
- Viewers scan QR code
- Viewer 1 enters folder: "pdfs" → loads: `pdfs/3_15.pdf`
- Viewer 2 enters folder: "documents" → loads: `documents/3_15.pdf`
- All devices show the same content from their own folders!

## Benefits

- ✅ No registration required
- ✅ Works on any device with a browser
- ✅ Free hosting on GitHub Pages
- ✅ HTTPS enabled by default
- ✅ Global CDN for fast loading
- ✅ Perfect for presentations and meetings
- ✅ Flexible folder structure - users choose their own folder names
