#!/usr/bin/env python3
"""
Create test PDF files for the PDF sync app
"""

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    import os
    
    def create_test_pdf(filename, section, page):
        """Create a simple test PDF with section and page info"""
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        
        # Title
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width/2, height-100, f"PDF Sync Test")
        
        # Section and Page
        c.setFont("Helvetica-Bold", 36)
        c.drawCentredString(width/2, height/2 + 50, f"Section {section}")
        c.drawCentredString(width/2, height/2, f"Page {page}")
        
        # Additional info
        c.setFont("Helvetica", 12)
        c.drawCentredString(width/2, height/2 - 100, f"Filename: {filename}")
        c.drawCentredString(width/2, height/2 - 120, "This is a test PDF for the sync app")
        
        c.save()
        print(f"Created: {filename}")
    
    # Create example-pdfs directory
    os.makedirs("example-pdfs", exist_ok=True)
    
    # Create some test PDFs
    test_files = [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3),
        (3, 15), (14, 20)  # Some specific examples
    ]
    
    for section, page in test_files:
        filename = f"example-pdfs/{section}_{page}.pdf"
        create_test_pdf(filename, section, page)
    
    print(f"\n✅ Created {len(test_files)} test PDF files in example-pdfs/")
    print("You can now test the PDF sync app with these files!")
    
except ImportError:
    print("❌ ReportLab not available. Creating simple HTML files instead...")
    
    # Create HTML files as fallback
    os.makedirs("example-pdfs", exist_ok=True)
    
    test_files = [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3),
        (3, 15), (14, 20)
    ]
    
    for section, page in test_files:
        filename = f"example-pdfs/{section}_{page}.html"
        with open(filename, 'w') as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>Section {section}, Page {page}</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            height: 100vh; 
            margin: 0; 
            background: #f0f0f0;
        }}
        .section {{ font-size: 48px; color: #333; margin: 20px; }}
        .page {{ font-size: 36px; color: #666; margin: 20px; }}
        .info {{ font-size: 14px; color: #999; margin: 20px; }}
    </style>
</head>
<body>
    <div class="section">Section {section}</div>
    <div class="page">Page {page}</div>
    <div class="info">Test file: {section}_{page}.html</div>
    <div class="info">PDF Sync App Test Content</div>
</body>
</html>""")
        print(f"Created: {filename}")
    
    print(f"\n✅ Created {len(test_files)} test HTML files in example-pdfs/")
    print("These can be used to test the sync functionality!")
