import urllib.request
from bs4 import BeautifulSoup
import ssl

def main():
    url = input("Enter a url: ")
    visited = set()
    to_visit = set([url])
    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue
        visited.add(current_url)
        print(f"Visiting: {current_url}")
        links = goto(current_url)
        for link in links:
            print(link)
            if link not in visited:
                to_visit.add(link)

def goto(url):
    links = set()
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={'User-Agent': 'Chrome/35.0.1916.47'})
        page = urllib.request.urlopen(req, context=ctx)
        strPage = page.read().decode("UTF-8")
        soup = BeautifulSoup(strPage, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):
                links.add(href)
    except Exception as e:
        print(f"Error: {e}")
    return links

if __name__ == "__main__":
    main()
