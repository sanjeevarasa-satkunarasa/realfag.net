import os
from bs4 import BeautifulSoup

# Define the subject variable
subject = "Rettslære_2"  # You can change this to any subject you want

html_content = """
<li>
          <h3>H2023</h3>
        </li>
        <li><a href="/eksamensoppgaver\Rettslære 2/sam3023-rettslaere-2-e-h23_removed.pdf" target="_blank" download>
            Oppgave </a></li>
        <li>
          <h3>V2016</h3>
        </li>
        <li><a href="/eksamensoppgaver\Rettslære 2/SAM3023 Rettslære 2 eksamen v16 oppg.pdf" target="_blank" download>
            Forberedelsesdel </a></li>
        <li><a href="/eksamensoppgaver\Rettslære 2/Forberedelsesdel SAM3023 Rettslære 2 v16.pdf" target="_blank"
            download> Oppgave </a></li>
        <li>
          <h3>V2011</h3>
        </li>
        <li><a href="/eksamensoppgaver\Rettslære 2/Rettslære_2_oppgave_v11.pdf" target="_blank" download> Oppgave </a>
        </li>
        <li>
          <h3>H2007</h3>
        </li>
        <li><a href="/eksamensoppgaver\Rettslære 2/Eksamensoppgaver Rettslære H07 - Udir.no.pdf" target="_blank"
            download> Oppgave </a></li>
        <li>
"""

base_path = r"G:\My Drive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder"

soup = BeautifulSoup(html_content, 'html.parser')
result = {}

# Parse the HTML content and create the dictionary
for h3 in soup.find_all('h3'):
    if len(h3.text) == 5:
        anchor = h3.find_next('a', href=True)
        if anchor and '/eksamensoppgaver/' in anchor['href']:
            full_path = base_path + anchor['href'].replace('/', '\\')
            full_path = full_path.replace('\\\\', '\\').replace('\\', '/')
            result[h3.text] = full_path

# Rename the files according to the specified format and update the HTML content
for key, path in result.items():
    # Extract the directory and the file extension
    directory, old_filename = os.path.split(path)
    file_extension = os.path.splitext(old_filename)[1]
    
    # Create the new filename
    new_filename = f"Eksamen_{subject}_{key}{file_extension}"
    
    # Create the full path for the new filename
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file, ignoring case sensitivity
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower() == old_filename.lower():
                os.rename(os.path.join(root, file), new_path)
                print(f"Renamed '{os.path.join(root, file)}' to '{new_path}'")
                break
    
    # Update the anchor tag in the HTML content
    for anchor in soup.find_all('a', href=True):
        if anchor['href'].lower().endswith(old_filename.lower()):
            anchor['href'] = anchor['href'].replace(old_filename, new_filename)

# Write the updated HTML content to a text file
updated_html_content = soup.prettify()
with open("updated_html_content.txt", "w", encoding="utf-8") as file:
    file.write(updated_html_content)

print("Updated HTML content has been written to 'updated_html_content.txt'")
