import requests
from bs4 import BeautifulSoup

# Hardcoded footer data with social media links
FOOTER_CONTENT = """
Contact Information:
- Location: Electronic City, Bangalore
- Email: alphaesai@gmail.com
- Phone: +91 8220850596
- Social Media:
  - YouTube: https://www.youtube.com/@alphaesai
  - LinkedIn: https://www.linkedin.com/company/alphaesai
  - Instagram: https://www.instagram.com/alphaesai
"""

def scrape_website(url):  
    """Fetches and extracts text content from the given website URL, with hardcoded footer details."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract meaningful text from the website
        text = " ".join(soup.stripped_strings)

        # Append hardcoded footer content
        full_content = text + "\n\n" + FOOTER_CONTENT

        return full_content

    except requests.RequestException as e:
        return f"Error fetching website: {str(e)}"
