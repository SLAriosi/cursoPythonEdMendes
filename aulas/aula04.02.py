from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


def find_by_text(browser, tag, text):
   # 
   # Para que serve:
   #    Encontrar o elemento com o texto 'text';
      
   # Argumentos:
   #    - browser = Instância do browser [firefox, chrome, ...];
   #    - texto = Conteúdo que deve estar na tag;
   #    - tag = tag onde o texto será procurado.
   # 
   elementos = browser.find_elements(By.TAG_NAME, tag) # em formato de lista;
   
   # Para cada Elemento que estiver dentro da minha lista de elementos, no caso na linha 16;
   for elemento in elementos:
      if elemento.text == text:
         return elemento

def find_by_href(browser, link):
   # 
   # Para que serve:
   #    Encontrar o elemento `a` com o link 'link';
      
   # Argumentos:
   #    - browser = Instância do browser [firefox, chrome, ...];
   #    - link = link que será procurado em todas as tags `a`.
   # 
   elementos = browser.find_elements(By.TAG_NAME, 'a')
   
   # Para cada Elemento que estiver dentro da minha lista de elementos, no caso na linha 16;
   for elemento in elementos:
        if link in elemento.get_attribute("href"):
            return elemento


browser = Chrome()
browser.get('https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=155790195778&hvpone=&hvptwo=&hvadid=677606588104&hvpos=&hvnetw=g&hvrand=15534914578032587065&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9102207&hvtargid=kwd-10573980&hydadcr=26346_11691057&gad_source=1')

# elemento_amazon_cuki = find_by_text(browser, "li", "Cookies")
elemento_amazon = find_by_href(browser, "amazon")