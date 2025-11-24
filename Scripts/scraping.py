import requests
from bs4 import BeautifulSoup


url = "http://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    first_quote = soup.find("span", class_="text").get_text()
    print("première citation :", first_quote)
else:
    print("eerreur.. ", response.status_code)
