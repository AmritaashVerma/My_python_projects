from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas


website = "https://www.youtube.com"
path = "E:\Amritaash\pythonProject\python automation\chrome_driver\chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
div_elements = driver.find_elements(by="xpath", value='//div[@class="style-scope ytd-rich-grid-media" and @id="meta"]')
views = []
titles = []

for element in div_elements:
    view = element.find_element(by="xpath", value='.//div[@class="style-scope ytd-video-meta-block"]/ytd-badge').text
    title = element.find_element(by="xpath", value="./h3").text
    views.append(view)
    titles.append(title)

my_dict = {"Title": titles, "Views": views}
data_frame = pandas.DataFrame(my_dict)
data_frame.to_csv('E:\Amritaash\pythonProject\python automation\Project #2 web automation and scrapping\YT_views.csv')
data = pandas.read_csv('E:\Amritaash\pythonProject\python automation\Project #2 web automation and scrapping\YT_views.csv')
data.to_html('E:\Amritaash\pythonProject\python automation\Project #2 web automation and scrapping\YT_views.html')
