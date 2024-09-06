import os

# Read version from environment or a VERSION file
version = os.getenv("VERSION", "1.0.0")  # Fallback version

# Get the correct path to index.html
html_file_path = os.path.join(os.path.dirname(__file__), "index.html")

# Read the HTML template
with open(html_file_path, "r") as file:
    html_content = file.read()

# Replace the placeholder {{VERSION}} with the actual version number
updated_html = html_content.replace("{{VERSION}}", version)

# Write the updated HTML back to the file
with open(html_file_path, "w") as file:
    file.write(updated_html)
