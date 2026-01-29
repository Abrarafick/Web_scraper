import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    # safer title extraction
    title_tag = soup.find('h1')
    if title_tag:
        title = title_tag.text.strip()
    else:
        title = "Title not found"

    # safer paragraph extraction
    paragraphs = soup.find_all('p')
    first_para = "Paragraph not found"

    for p in paragraphs:
        if p.text.strip():
            first_para = p.text.strip()
            break

    print("Title:")
    print(title)

    print("\nFirst Paragraph:")
    print(first_para)


scrape_wikipedia("https://en.wikipedia.org/wiki/Python_(programming_language)")
