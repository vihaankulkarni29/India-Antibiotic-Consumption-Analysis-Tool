import requests
from bs4 import BeautifulSoup

def get_article_text(url: str) -> str | None:
    """
    Fetches and returns the text content of a given URL.

    Args:
        url (str): The URL of the article to scrape.

    Returns:
        str | None: The text content of the article, or None if the request fails.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Define content areas for different sites to improve accuracy
        if 'pmc.ncbi.nlm.nih.gov' in url:
            content = soup.find('div', class_='j-body')
        elif 'cgdev.org' in url:
            content = soup.find('div', class_='article-body')
        else:
            content = soup.body

        if content:
            return content.get_text(separator=' ', strip=True)
        # Fallback for unexpected structures
        return soup.body.get_text(separator=' ', strip=True)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None
