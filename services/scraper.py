import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Fetches and extracts text content from the given website URL."""
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract meaningful text
        text = " ".join(soup.stripped_strings)
        return text

    except requests.RequestException as e:
        return f"Error fetching website: {str(e)}"
