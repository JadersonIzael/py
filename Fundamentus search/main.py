from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

setor_selecionado = "Consumo Cíclico"
codigo_acao = "cple4"
dy_minimo = "100"
dy_maximo = "2500"
pl_minimo = "0000"
pl_maximo = "0500"
pvp_minimo = "0000"
pvp_maximo = "0200"
roe_minimo = "1500"

#função de repeticao
def preencher_campo(campo, valor):
    for i in range(15):
        campo.send_keys(Keys.BACK_SPACE)
    campo.send_keys(valor)

#entrar em um site:

driver = webdriver.Chrome()
driver.get('https://www.fundamentus.com.br/buscaavancada.php')
driver.maximize_window()

sleep(15)

pyautogui.click(1237,250, duration=1.5)
pyautogui.click(618,515, duration=1.5)
pyautogui.click(355,710, duration=1.5)

# Digitar
campo_dy0 = driver.find_element(By.XPATH,"//input[@name='dy|0']")
campo_dy1 = driver.find_element(By.XPATH,"//input[@name='dy|1']")
campo_pl0 = driver.find_element(By.XPATH,"//input[@name='p_l|0']")
campo_pl1 = driver.find_element(By.XPATH,"//input[@name='p_l|1']")
campo_pvp0 = driver.find_element(By.XPATH,"//input[@name='p_vp|0']")
campo_pvp1 = driver.find_element(By.XPATH,"//input[@name='p_vp|1']")
campo_roe0 = driver.find_element(By.XPATH,"//input[@name='roe|0']")
preencher_campo(campo_dy0, dy_minimo)
preencher_campo(campo_dy1, dy_maximo)
preencher_campo(campo_pl0, pl_minimo)
preencher_campo(campo_pl1, pl_maximo)
preencher_campo(campo_pvp0, pvp_minimo)
preencher_campo(campo_pvp1, pvp_maximo)
preencher_campo(campo_roe0, roe_minimo)

apertar_botao = driver.find_element(By.XPATH,"//*[@id='main-2']/div[3]/div/div/div/button[2]")
ActionChains(driver).click(apertar_botao).perform()

pyautogui.click(1712,308, duration=1.5)

sleep(300)