from selenium import webdriver

#extracted all the jokes from a website
website = "https://parade.com/968634/parade/jokes-for-kids/"
driver = webdriver.Chrome()
driver.get(website)
paragraph_elements = driver.find_elements(by="xpath", value='//div[@class="m-detail--body"]/p')
array_of_p_elements = []
for element in paragraph_elements:
    text = element.text
    array_of_p_elements.append(text)

array_of_p_elements.pop(0)
print(''.join(array_of_p_elements))

