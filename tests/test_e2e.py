import pytest
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self, setup):

        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            # print(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CLASS_NAME, "checkbox").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(success_message)
        assert "Success! Thank you!" in success_message
