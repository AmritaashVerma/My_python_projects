from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas

website = "https://en.wikipedia.org/wiki/Olympic_Games"
path = r'\'C:\Users\amrit\Desktop\My programming folders\My_python_projects\python automation\chrome_driver'

service = Service(executable_path=path)
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
data_frame.to_csv('python automation\Project #2 web automation and scrapping\links.csv', index=False)
data = pandas.read_csv("python automation\Project #2 web automation and scrapping\links.csv")
data.to_html("python automation\Project #2 web automation and scrapping\wiki_links.html")

