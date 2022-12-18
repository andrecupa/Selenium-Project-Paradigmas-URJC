from selenium.webdriver.common.by import By
from selenium import webdriver

def test(lGrados):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.urjc.es/intranet-urjc')
        
        estudios_button = driver.find_element(By.XPATH, "//*[@id='rt-header']/div/div[2]/div/ul/li[2]/a")
        estudios_button.click()

        ingenieria_button = driver.find_element(By.XPATH, "//*[@id='set-rl_sliders-1']/div[4]/div[1]/a")
        ingenieria_button.click()

        cookie_button = driver.find_element(By.XPATH, "//*[@id='cookiefirst-root']/div/div/div[2]/div[2]/div[2]/div[1]/button")
        cookie_button.click()

        for grado in lGrados:
            if (grado[0] != '3') and (grado[0] != '17'):
                xpath = "//*[@id='ingenieria-y-arquitectura']/div/ul/li[" + grado[0] + "]/a"
                grado_button = driver.find_element(By.XPATH, xpath)
                driver.implicitly_wait(10)
                grado_button.click()
                driver.implicitly_wait(10)
                titulo_grado = driver.find_element(By.ID, "i4t-id-11").text
                titulo = grado[1].replace('_',' ')
                assert titulo_grado == titulo
                driver.back()
                driver.implicitly_wait(10)
                isdisplay = driver.find_element(By.XPATH, xpath).is_displayed()
                if not isdisplay:
                    driver.find_element(By.XPATH, "//*[@id='set-rl_sliders-1']/div[4]/div[1]/a").click()

        driver.close()
        print("Test ok")
    except:
        print('Test not ok')

def cargarDatos():
    lGrados = []
    nombreFichero = "./project/grados.txt"
    with open(nombreFichero,'r',encoding='utf-8') as fichero:
        for linea in fichero:
            lGrados.append(linea.split())
    return lGrados

#--------------------------------------------------------------------
lGrados = cargarDatos()
test(lGrados)