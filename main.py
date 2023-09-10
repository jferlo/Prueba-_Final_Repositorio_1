from selenium import webdriver
from selenium.webdriver.common.by import By
#from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://www.remax.com.ec/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#searchbar-input")
search_box.send_keys("Pinar Alto")
search_button = driver.find_element(by=By.CSS_SELECTOR, value="#button-search")
search_button.click()

house_cards = driver.find_elements(By.CSS_SELECTOR,"#wrapper")

for card in house_cards:
    titulo= card.find_element(By.CSS_SELECTOR,"div.mat-ripple.info > div > h2").text
    precio= card.find_element(By.CSS_SELECTOR,"#price-expenses").text
    features= card.find_element(By.CSS_SELECTOR,"div.mat-ripple.info > div > div.features").text
    print (titulo)
    print(f'$ {precio}')
    print(features)
    print("----------------------------------------------------")
    grabar= {
        'titulo':titulo,
        'precio':precio,
        'features':features
    }
    db.



driver.close()