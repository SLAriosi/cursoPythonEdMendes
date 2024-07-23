from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

browser = Chrome()

browser.get('https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=155790195778&hvpone=&hvptwo=&hvadid=677606588104&hvpos=&hvnetw=g&hvrand=15534914578032587065&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9102207&hvtargid=kwd-10573980&hydadcr=26346_11691057&gad_source=1')

# Esse trecho de código abaixo de mim, funciona na segunda linha, não é necessário fazer essa 3° 

lista_nao_ordenada = browser.find_element(By.TAG_NAME, 'ul')
listasN = lista_nao_ordenada.find_elements(By.TAG_NAME, 'li')
listasN[0].find_element(By.TAG_NAME, 'a').text

print (listasN[0].find_element(By.TAG_NAME, 'a').text)