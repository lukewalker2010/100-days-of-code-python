from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://appbrewery.github.io/instant_pot/")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price is ${price_dollar.text}.{price_cents.text}")


# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org")
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li a")
# for name in event_names:
#     print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text,
    }

print(events)




# driver.close()
driver.quit()