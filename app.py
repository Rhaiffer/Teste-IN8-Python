from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
import re


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--start-maximized")
options.add_argument('--disable-infobars')
driver = webdriver.Chrome(options=options, executable_path= r"D:\Lenovo\chromedriver\chromedriver.exe")


driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")


def scroll() -> None:
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
    

def get_index() -> list:
    lista_produtos = []
    driver.implicitly_wait(7)
    scroll()
    get_urls_produtos = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div')
    get_links = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/div/div[1]/h4[2]/a')
    cont = 0
    for urls in get_urls_produtos:
        dict_produtos = {}

        dict_produtos[urls.text] = get_links[cont].get_attribute("title") + '\n'
        if re.search('lenovo', get_links[cont].get_attribute("title"), re.IGNORECASE):
            lista_produtos.append(dict_produtos)
        cont+=1

    return lista_produtos
produtos_lenovo = get_index()
print(produtos_lenovo)

