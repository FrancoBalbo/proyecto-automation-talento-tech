import pytest
from selenium import webdriver.common.by import By
# pyrefly: ignore [missing-import]
from  selenium.web

def test_login_exitoso():
    driver = webdriver.Chrome()

    try: 
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID, "user-name")
        contraseña = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton_login.click()

        assert "/inventory.html" in driver.current_url
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

        # Validacion de texto
        logo = driver.find_element(By.CLASS_NAME, "app_logo").text
        assert logo == "Swag Labs"
        
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test == title]").text
        assert titulo == "Products" 
    finally:
        driver.quit()
