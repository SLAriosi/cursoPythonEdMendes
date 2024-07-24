from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

browser = Chrome()

url = ('https://www.amazon.com.br/ref=nav_logo')
browser.get(url)

url_parseada = urlparse(browser.current_url)