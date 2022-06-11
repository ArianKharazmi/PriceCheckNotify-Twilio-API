from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

# Amazon product you want
url = 'https://www.amazon.com/MSI-RTX-3080-LHR-10G/dp/B09FSWGS7L/ref=sr_1_2?crid=3NKWMC4XDVNJ&keywords=3080&qid=1654958938&sprefix=3080%2Caps%2C91&sr=8-2'

# Request the webpage
response = Request(url, headers = headers)

# Open and parse the response
webpage = urlopen(response).read()
html = soup(webpage, "html.parser")

# Get product name
product = html.find(id="productTitle").get_text().strip()

# Get and convert price to float
price = float((html.find("span", class_ = "a-offscreen").get_text()).replace('$', ''))
