from selenium import webdriver
import pandas

website = "https://en.wikipedia.org/wiki/Stock_market"

driver = webdriver.Chrome()
driver.get(website)
hatnote_elements = driver.find_elements(by="xpath", value='//div[@class="mw-content-ltr mw-parser-output"]/p/a')
links = []
texts = []

for element in hatnote_elements:
    link = element.get_attribute("href")
    text = element.text
    links.append(link)
    texts.append(text)

my_dict = {'Links': links, 'Text in links': texts}
data_frame = pandas.DataFrame(my_dict)
print(data_frame)
data_frame.to_csv('links.csv', index=False)
data = pandas.read_csv("links.csv")
data.to_html("wiki_links.html")

