from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas

website = "https://www.wikipedia.org/wiki/States_and_union_territories_of_India"
path = "E:\Amritaash\pythonProject\python automation\chrome_driver\chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
hatnote_elements = driver.find_elements(by="xpath", value='//div[@class="hatnote navigation-not-searchable"]')
links = []
texts = []

for element in hatnote_elements:
    link = element.find_element(by="xpath", value='.//a').get_attribute("href")
    text = element.find_element(by="xpath", value='.//a').text
    links.append(link)
    texts.append(text)

p_elements = driver.find_elements(by="xpath", value='//div[@class="vector-body ve-init-mw-desktopArticleTarget-targetContainer"and @id="bodyContent"]/div[@class="mw-body-content mw-content-ltr" and @id="mw-content-text"]/div[@class="mw-parser-output"]')

for p_tag_link in p_elements:
    p_link = p_tag_link.find_element(by="xpath", value='.//p//a').get_attribute("href")
    p_text = p_tag_link.find_element(by="xpath", value='.//p//a').text
    links.append(p_link)
    texts.append(p_text)

my_dict = {'Links': links, 'Text in links': texts}
data_frame = pandas.DataFrame(my_dict)
data_frame.to_csv('E:\Amritaash\pythonProject\python automation\Project #2 web automation and scrapping\states.csv')
data = pandas.read_csv('E:\Amritaash\pythonProject\python automation\Project #2 web automation and scrapping\states.csv')
data.to_html('E:\Amritaash\pythonProject\python automation\Project #2 web automation and scrapping\states_csv_html.html')

