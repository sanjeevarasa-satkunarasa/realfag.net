from bs4 import BeautifulSoup

def replace_src_with_url_for(html_file_path, output_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Replace src attributes
    for tag in soup.find_all(src=True):
        src_value = tag['src']
        if 'static/' in src_value:
            new_src_value = "{{ url_for('static', filename='" + src_value.split('static/')[-1] + "') }}"
            tag['src'] = new_src_value

    # Replace href attributes
    for tag in soup.find_all(href=True):
        href_value = tag['href']
        if 'static/' in href_value or 'eksamensoppgaver/' in href_value or 'ZIP/' in href_value or 'templates/' in href_value:
            new_href_value = "{{ url_for('static', filename='" + href_value.split('static/')[-1] + "') }}"
            tag['href'] = new_href_value

    # Replace src attributes in script tags
    for tag in soup.find_all('script', src=True):
        src_value = tag['src']
        if 'static/' in src_value or 'script/' in src_value:
            new_src_value = "{{ url_for('static', filename='" + src_value.split('static/')[-1] + "') }}"
            tag['src'] = new_src_value

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

# Example usage
replace_src_with_url_for('input.html', 'output.html')
