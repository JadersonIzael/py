from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

#entrar em um site:

driver = webdriver.Chrome()
driver.get('https://open.spotify.com/intl-pt')
driver.maximize_window()

sleep(10)

# Digitar
musicas_curtidas = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div/section[1]/div[2]/div[1]/div/div[3]')
ActionChains(driver).click(musicas_curtidas).perform()

for i in range(1, 800):
    pyautogui.click(1864,610, duration=1.5)
    pyautogui.moveTo(1731,653, duration=1.5)
    pyautogui.moveTo(1633,654, duration=1.5)
    pyautogui.click(1423,293, duration=1.5)
    pyautogui.click(267,995, duration=1.5)

sleep(300)