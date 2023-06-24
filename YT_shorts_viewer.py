from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
from pytube import YouTube 
import time

print("Go to your web browser and open up youtube shorts. I give you 8 seconds to do this")
time.sleep(5)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), executable_path='<C:\Program Files\Google\Chrome\Application\chrome.exe>', options=options)
link = driver.current_url
#this project has failed but will come back to it later 