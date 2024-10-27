#this web scraper will get the Title, Time since posted, Views, Name of Channel, Likes, Number of subscribers, Number of comments in the given youtube video 
from selenium import webdriver

website = input("Enter the youtube video link: ")
driver = webdriver.Chrome()
driver.get(website)
driver.implicitly_wait(7)
Video_title = driver.find_elements(by="xpath", value='//div[@id="above-the-fold"]/div[@id="title"]/h1/yt-formatted-string')[0].text
Channel_name = driver.find_elements(by="xpath", value='//yt-formatted-string[@id="text"]/a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')[0].text
Channel_subscriber_count = driver.find_elements(by="xpath", value='//div[@id="upload-info"]/yt-formatted-string')[0].text
Time_posted = driver.find_elements(by="xpath", value='//div[@id="info-container"]/yt-formatted-string[@id="info"]/span')[2].text
views = driver.find_elements(by="xpath", value='//div[@id="info-container"]/yt-formatted-string[@id="info"]/span')[0].text
likes = driver.find_elements(by="xpath", value='//button[@class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start"]/div[@class="yt-spec-button-shape-next__button-text-content"]')[0].text
try: 
    num_comments = driver.find_elements(by="xpath", value='//h2[@id="count"]/yt-formatted-string[@class="count-text style-scope ytd-comments-header-renderer"]/span[@class="style-scope yt-formatted-string"]')[0].text
except IndexError:
    num_comments = "Comments are turned off."
data_dict = {"Title: ": Video_title,"Time Since Posted: ": Time_posted, "Views: ": views, "Name of Channel: ": Channel_name, "Likes: ": likes, "Number of comments: ": num_comments, "Subscribers on the channel: ": Channel_subscriber_count}
i = 1
for key, value in data_dict.items():
    print(i, key, value)
    i += 1