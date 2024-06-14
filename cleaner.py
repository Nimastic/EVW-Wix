from bs4 import BeautifulSoup

# Function to remove inline CSS
def remove_inline_css(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup.find_all(True):
        if tag.has_attr('style'):
            del tag['style']
    return str(soup)

# Read the original HTML file
with open('original.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Remove inline CSS
cleaned_html = remove_inline_css(html_content)

# Write the cleaned HTML to a new file
with open('cleaned.html', 'w', encoding='utf-8') as file:
    file.write(cleaned_html)

print("Inline CSS removed and cleaned HTML saved to 'cleaned.html'")
