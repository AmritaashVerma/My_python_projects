from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas
import os
import sys

#making a py an exe file
application_path = os.path.dirname(sys.executable)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
website = "https://www.thesun.co.uk/sport/football/"
path = r"\"C:\Users\amrit\Desktop\My programming folders\My_python_projects\python automation\chrome_driver\chromedriver.exe"

#headless mode
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(options=options)
driver.get(website)
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
titles = []
sub_titles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value="./a/h3").text
    sub_title = container.find_element(by="xpath", value="./a/p").text
    link = container.find_element(by="xpath", value="./a").get_attribute("href")
    titles.append(title)
    sub_titles.append(sub_title)
    links.append(link)

my_dict = {'titles': titles, 'subtitles': sub_titles, 'links': links}

df_headline = pandas.DataFrame(my_dict)
# df_headline.to_csv(r"\"C:\sers\amrit\Desktop\My programming-folders\My_python_projects\python automation\Project #2 web automation and scrapping\headline.csv")

driver.quit()
print(df_headline)
# pandas.options.display.max_columns = None
# pandas.options.display.max_rows = None
# data = pandas.read_csv(r'\'C:\Users\amrit\Desktop\My programming folders\My_python_projects\python automation\Project #2 web automation and scrapping\headline.csv')
# data.to_html(r"\"C:\Users\amrit\Desktop\My programming folders\My_python_projects\python automation\Project #2 web automation and scrapping\csv_html.html")
