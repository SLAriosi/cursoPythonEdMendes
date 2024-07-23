from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html/'
navegador = Chrome()
navegador.get(url)

sleep(1)

a = navegador.find_element(By.TAG_NAME, "a")

for click in range(1, 10+1):     
   a.click()
   p = navegador.find_elements(By.TAG_NAME, "p")
   texto_paragrafo = p[click].text
   
   print(f'Valor de p {texto_paragrafo} valor do click: {click}')
   print(f'Os valores são iguais {texto_paragrafo == str(click)}')
