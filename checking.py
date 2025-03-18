# checking footer.html

import requests

footer_url = "https://alphaesai.com/footer.html"  # Adjust the URL if needed
response = requests.get(footer_url)

if response.status_code == 200:
    print(response.text)  # Check if footer content is retrieved
else:
    print("Failed to fetch footer")
