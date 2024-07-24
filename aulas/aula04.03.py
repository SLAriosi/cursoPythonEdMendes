# Serve para podermos utilizar o .until de maneira mais correta
from selenium.webdriver.support import expected_conditions as EC
# Serve para poder usar o WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

def find_by_text(browser, tag, text):
    # Aguarda até que o elemento que eu pedi esteja presente no site;
    # Porque de usar o parâmetro (driver):
    #    Quando você define uma função personalizada para until, como element_with_text_present, essa função é chamada repetidamente pelo WebDriverWait 
    #    até que retorne algo que não seja False ou None. Para realizar essas chamadas, o Selenium precisa passar o driver para a função, para que ela 
    #    possa usar o driver para buscar os elementos na página. E quando usamos uma função já pré settada 
    #    como wait.until(EC.presence_of_element_located((By.ID, "elementEmail")), o próprio Selenium já passa o driver para a função.
    
    def element_with_text_present(driver):
      nav = browser.find_element(By.ID, 'nav-xshop')
      elementos = nav.find_elements(By.TAG_NAME, tag)
      for elemento in elementos:
         if elemento.text == text:
            return elemento
      return False

    elemento = wait.until(element_with_text_present)
    return elemento


browser = Chrome()
wait = WebDriverWait(browser, 5)
url = ('https://www.amazon.com.br/ref=nav_logo')

browser.get(url)
nome_itens_navbar = ["Livros", "Música", "Eletrônicos", "Casa"]

for nome in nome_itens_navbar:
   find_by_text(browser, 'a', nome).click()
   
# Depois disso é só usar o browser.back() ou browser.forward() para voltar ou avançar na página.
# Teste
for nome in nome_itens_navbar:
   browser.back()

for nome in nome_itens_navbar:
   browser.forward()

# Essa aula era pra aprender a usar o browser.back() e browser.forward(), fiz uma validação a mais para que o selenium esperasse até que meus itens aparecessem depois da tela carregar;