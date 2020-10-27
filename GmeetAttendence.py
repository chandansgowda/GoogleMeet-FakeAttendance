from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pyautogui

#get user details [INPUT]
email = str(input("Email/Mob. No.  >>   "))
password = str(input("Password  >>   "))
meeting_id = str(input("Enter meeting id  >>   "))
message = str(input("Type your message"))

#[OUTPUT]
print("Your job is going on.Please wait..   :)")

#loading webdriver for chrome
driver = webdriver.Chrome("chromedriver.exe") #supports only chrome browser
wait = WebDriverWait(driver, 1000)  #waiting for expected conditions

#main function starts
driver.get("https://meta.stackexchange.com/users/login?returnurl=https%3a%2f%2fstackexchange.com%2fusers%2flogin-or-signup%2fdelegated%3freturnurl%3dhttps%253a%252f%252fstackexchange.com%253f_%253d998711021&cdl=1")

driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[1]").click()

driver.find_element_by_id("identifierId").send_keys(f"{email}") #email

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click() #next

#waiting until the element is visible in order to prevent errors
wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")))

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(f"{password}")


driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()

time.sleep(4)

driver.get(f"https://meet.google.com/{meeting_id}")

wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")))

driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span").click() #dismiss

wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span/span")))

driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span/span").click()  #asktojoin

wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span")))

driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span").click()
#chat open  

wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea")))

driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea").send_keys(f"{message}")
#chat text area 

wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span")))

driver.find_element_by_xpath(" /html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span").click()
#chat enter  

time.sleep(10)
 
#saving screenshot using pyautogui for future reference
screenshot = pyautogui.screenshot()
screenshot.save("attended.png")

# Programmed By Chandan S Gowda
# Visit www.chandansgowda.blogspot.com and know me better
