from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"


def _login(driver, wait):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory.html"))


def test_flujo_completo_de_compra(driver, wait):
    _login(driver, wait)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))

    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    driver.find_element(By.ID, "first-name").send_keys("Jorge")
    driver.find_element(By.ID, "last-name").send_keys("Lopez")
    driver.find_element(By.ID, "postal-code").send_keys("00000")
    driver.find_element(By.ID, "continue").click()

    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()

    mensaje = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    assert "Thank you for your order" in mensaje.text


def test_carrito_vacio_no_permite_checkout(driver, wait):
    _login(driver, wait)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    botones_checkout = driver.find_elements(By.ID, "checkout")
    items_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(items_en_carrito) == 0
    assert len(botones_checkout) == 1
