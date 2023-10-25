from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

cooldown = 10
link = ""
pathToUserProfile = os.getenv("LOCALAPPDATA")+"/Google/Chrome/User Data/"

setup = open('setup.txt', encoding='utf8')
link = setup.readline()
cooldown = int(setup.readline())+1
setup.close()

PATH = "./chromedriver.exe"

options = webdriver.ChromeOptions()

options.add_argument("--user-data-dir=" + pathToUserProfile) #if you have many profiles just add it it will be profile {#} where {#} is your proflie number
driver = webdriver.Chrome(PATH)

driver.get(link)

for i in range(4):
    print(i)
    time.sleep(1)

iframe = driver.find_element(By.XPATH, '//iframe[@id="chatframe"]')
driver.switch_to.frame("chatframe")
commentBox = driver.find_element(By.XPATH, '//div[@id="input"]')

poem = open('poem.txt', encoding='utf8')
while True:
    line = poem.readline()
    if not line:
        break
    print(line)
    commentBox.send_keys(line)
    time.sleep(1)
    commentBox.send_keys(Keys.RETURN)
    for i in range(cooldown):
        print(i)
        time.sleep(1)
poem.close()
print("End of file")
