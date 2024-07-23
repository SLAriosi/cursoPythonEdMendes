from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://sociorei.com/'
driver = Chrome()
driver.get(url)

botao_entrar = driver.find_element(By.XPATH, '//*[@id="wrapper"]/header/div/div[2]/div/div[2]/div[1]/div/a[1]').click()
email = driver.find_element(By.XPATH, '//*[@id="UserLogin"]').send_keys("ariosilucas@gmail.com")
senha = driver.find_element(By.XPATH, '//*[@id="inputPasswordStore"]').send_keys("NwvXuWU7aG@J-E8")
enviar = driver.find_element(By.XPATH, '//*[@id="frmLogin"]/div[3]/div/button').click()
dados_pessoais = driver.find_element(By.XPATH, '//*[@id="btnFan"]').click()
nome_usuario = driver.find_elements(By.XPATH, '//*[@id="frmFan"]/fieldset[1]/div/div[2]/div/div[2]/div[2]')

salvar = driver.find_element(By.ID, 'btnSaveFan')

print(f'Qual valor está vindo aqui no salvar: {salvar}')