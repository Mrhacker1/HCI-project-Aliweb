import os
import re

def replace_html_code(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    filedata = f.read()
                
                # Define the old and new HTML code
                old_code = r'<div class="header">\s*<img src="logo.png" alt="Aliweb Logo" class="logo">\s*</div>'
                new_code = '<header class="header">\n        <a href="../aliweb.html">\n            <img src="logo.png" alt="Aliweb Logo" class="logo">\n        </a>\n    </header>'
                
                # Use regex to replace the old HTML code with the new one
                new_filedata = re.sub(old_code, new_code, filedata, flags=re.DOTALL)
                
                # Write the new HTML code to the file
                with open(filepath, 'w') as f:
                    f.write(new_filedata)

# Call the function on your directory
replace_html_code(r'C:\Users\meetf\OneDrive\Desktop\University of Oklahoma\HCI\project\https---github.com-DemiladeJooda-aliweb')
