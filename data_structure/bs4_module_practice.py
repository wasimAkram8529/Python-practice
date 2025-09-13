from bs4 import BeautifulSoup
import requests as rq

BASE_URL = "https://quotes.toscrape.com/"
response = rq.get(BASE_URL)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
all_a = soup.find_all("a")
for link in all_a:
  print(f"{link.get("href")}")
# print(all_a)



# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>Document</title>
# </head>
# <body>
#   <p>Hii Wasim</p>
#   <p>Hello Wasim</p>
#   <h1>How are you buddy</h1>
#   <h1>How are you my friend</h1>
#   <div class="container">
#     <div class="left-item">
#       <ul>
#         <li>List 1 from left portion</li>
#         <li>List 2 from left portion</li>
#       </ul>
#     </div>
#     <div class="right-item">
#       <ul>
#         <li>List 1</li>
#         <li>List 2</li>
#         <li>List 3</li>
#         <li>List 4</li>
#         <li>List 5</li>
#       </ul>
#     </div>
#   </div>
# </body>
# </html>
# """

# soup = BeautifulSoup(html, "html.parser")
# h1 = soup.find_all("h1")
# print("Title content: ", h1)