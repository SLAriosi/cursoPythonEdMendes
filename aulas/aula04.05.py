"""
1. Pegar todos os itens da navbar menu;
2. Navegar até a página de produtos de música depois disso;
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
   
browser = Chrome()
wait = WebDriverWait(browser, 5)
url = ('https://www.amazon.com.br/ref=nav_logo')
browser.get(url)

nav_bar_menu = browser.find_element(By.ID, 'nav-xshop')
itens_nav_bar = nav_bar_menu.find_elements(By.TAG_NAME, 'a')

print(itens_nav_bar.text)
# nome_itens = [itens_nav_bar.text]

# for item in itens_nav_bar:
#    if item.text != '':
#       sleep(1)
#       print(item.text)
# Funcionou E Dropei o Curso fui ver um gringo, defasado em pontos importantes!!