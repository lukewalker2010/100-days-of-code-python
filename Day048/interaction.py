from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # print(article_count.text)
# # article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

FIRST_NAME = "Luke"
LAST_NAME = "SkyWalker"
EMAIL = "LUKE.SKY.WALKER@EMAIL.COM"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first = driver.find_element(By.NAME, value="fName")
first.send_keys(FIRST_NAME)
last = driver.find_element(By.NAME, value="lName")
last.send_keys(LAST_NAME)
form_email = driver.find_element(By.NAME, value="email")
form_email.send_keys(EMAIL)

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()
