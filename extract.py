import requests
from bs4 import BeautifulSoup


def extract_title_content(url):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Error reading text")
    page = r.text
    soup = BeautifulSoup(page, "lxml")
    title = soup.find("title").get_text().strip()
    ps = soup.find_all("p")
    content = extract_text(ps)
    return title, content


def extract_text(p_tags):
    # may need different rule for different site
    ps_text = [t.text for t in p_tags]
    text = " ".join(ps_text)
    return text
