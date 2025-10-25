import markdown
from weasyprint import HTML, CSS
from markdown.extensions import codehilite

# Read the markdown report
with open('MovieLens_Analysis_Report.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(markdown_content, extensions=['tables', 'codehilite'])

# Add CSS styling
css_style = """
<style>
body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
h2 { color: #34495e; border-bottom: 1px solid #bdc3c7; padding-bottom: 5px; }
h3 { color: #7f8c8d; }
table { border-collapse: collapse; width: 100%; margin: 20px 0; }
th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
th { background-color: #f2f2f2; font-weight: bold; }
code { background-color: #f8f9fa; padding: 2px 4px; border-radius: 3px; }
.highlight { background-color: #fff3cd; padding: 10px; border-left: 4px solid #ffc107; }
</style>
"""

# Combine CSS and HTML
full_html = f"<!DOCTYPE html><html><head>{css_style}</head><body>{html_content}</body></html>"

# Save as HTML first
with open('MovieLens_Analysis_Report.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Report converted to HTML: MovieLens_Analysis_Report.html")
print("You can now:")
print("1. Open the HTML file in your browser")
print("2. Print to PDF using Ctrl+P -> Save as PDF")
print("3. Or use an online HTML to PDF converter")