import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Задержки в секундах
MICRO_DELAY = 1
SHORT_DELAY = 2
LONG_DELAY = 4


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def login(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(SHORT_DELAY)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(SHORT_DELAY)


def checkout_process(driver):
    driver.find_element(By.ID, "checkout").click()
    time.sleep(SHORT_DELAY)
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Smith")
    driver.find_element(By.ID, "postal-code").send_keys("01234")
    driver.find_element(By.ID, "continue").click()
    time.sleep(SHORT_DELAY)
    driver.find_element(By.ID, "finish").click()
    time.sleep(SHORT_DELAY)


def verify_order_completion(driver):
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert "Thank you for your order!" in success_message.text
    time.sleep(LONG_DELAY)


@pytest.mark.parametrize("product_name", [
    "Test.allTheThings() T-Shirt (Red)"
])
def test_purchase_flow(driver, product_name):
    login(driver)

    # Выбор товара
    product_xpath = f"//div[text()='{
        product_name}']/ancestor::div[@class='inventory_item']//button"
    driver.find_element(By.XPATH, product_xpath).click()
    time.sleep(MICRO_DELAY)

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(SHORT_DELAY)

    # Проверка наличия товара в корзине
    assert product_name in driver.page_source
    time.sleep(MICRO_DELAY)

    # Оформление покупки
    checkout_process(driver)

    # Проверка успешного завершения покупки
    verify_order_completion(driver)

    print(f"Тест успешно завершен для товара: {product_name}")


def test_empty_cart_purchase(driver):
    login(driver)

    # Переход в пустую корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(SHORT_DELAY)

    # Проверка, что корзина пуста
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "Корзина не пуста"

    # Попытка оформления покупки из пустой корзины
    checkout_process(driver)

    # Проверка успешного завершения покупки
    verify_order_completion(driver)

    print("Тест успешно завершен для заказа из пустой корзины")
