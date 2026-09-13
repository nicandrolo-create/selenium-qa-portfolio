from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"


def _login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def test_flujo_completo_de_compra(driver):
    _login(driver)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Jorge")
    driver.find_element(By.ID, "last-name").send_keys("Lopez")
    driver.find_element(By.ID, "postal-code").send_keys("00000")
    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    mensaje = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order" in mensaje.text


def test_carrito_vacio_no_permite_checkout(driver):
    _login(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    botones_checkout = driver.find_elements(By.ID, "checkout")
    items_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(items_en_carrito) == 0
    assert len(botones_checkout) == 1
