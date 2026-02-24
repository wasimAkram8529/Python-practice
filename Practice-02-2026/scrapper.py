import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)


html = """
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div>
      <header>Sample Header</header>
      <section>
        Sample Section
        <div>
          <p>From para</p>
          <span>From span</span>
        </div>
      </section>
      <footer>Sample Footer</footer>
  </div>
  <div>
      <header>Sample Header</header>
      <section>
        Sample Section
        <div>
          <p>From para</p>
          <span>From span</span>
        </div>
      </section>
      <footer>Sample Footer</footer>
  </div>
</body>
</html>
"""

# soup = BeautifulSoup(html, "html.parser")
# print(soup.div.text)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# for quote, author in zip(quotes, authors):
#   print(quote.text)

for link in soup.find_all('a'):
  print(link.get('href'))
