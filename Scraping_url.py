'''
File for scraping the data off of the website
'''
import requests
from bs4 import BeautifulSoup

def scrape(url):
    import requests
    from bs4 import BeautifulSoup

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # check if the main tag exists
    main_content = soup.find("main")
    if main_content is not None:
        content = main_content
    else:
        content = soup.find("body")

    text_content = []
    for element in content.find_all(text=True):
        if element.parent.name not in ['script', 'style']:
            text_content.append(element.strip())

    # split the text into 500-word segments
    text_segments = [text_content[i:i+500] for i in range(0, len(text_content), 500)]

    # create a dictionary of text segments
    text_dict = {}
    for i, segment in enumerate(text_segments):
        key = 'p{}'.format(i+1)
        value = ' '.join(segment)
        text_dict[key] = value

    return text_dict









