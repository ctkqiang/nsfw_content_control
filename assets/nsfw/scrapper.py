# scrapy scrapper.py
url = 'https://www.pornhub.com/video?o=ht&cc=gb'
fetch(url)
view(response)
print(response.text)
response.css(".categoryName::text").extract()
