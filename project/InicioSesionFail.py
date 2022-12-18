from selenium import webdriver
from selenium.webdriver.common.by import By

Error_text = "Acceso inválido. Por favor, inténtelo otra vez."

user_name = "Fake Name"
passw = "Fake"

XPATH_AulaVirtual_Button = "//*[@id='rt-mainbody']/div/article/div/div/div[3]/div/div/div[2]/a"
XPATH_Access_Denied = "//*[@id='loginerror']/div"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.urjc.es/intranet-urjc")

driver.implicitly_wait(10)
AV_button = driver.find_element(By.XPATH, XPATH_AulaVirtual_Button)
AV_button.click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

driver.implicitly_wait(10)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(user_name)
pass_field = driver.find_element(By.ID, "password")
pass_field.send_keys(passw)

login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

driver.implicitly_wait(10)
Denied_Panel_text = driver.find_element(By.XPATH, XPATH_Access_Denied).text

if (Denied_Panel_text == Error_text):
    print("Test OK. msg error is: ", Error_text)
else:
    print("Test NOT ok")

driver.close()


