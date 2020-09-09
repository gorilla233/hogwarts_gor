from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(5)  #隐式等待

    def teardown(self):
        time.sleep(3)  #强制等待
        self.driver.quit()

    def test_hogwarts(self):
        category_name = (By.XPATH, "/html/body/section/div/div[2]/div[5]/div[2]/div/div/div/div/div[1]/table/tbody/tr[12]/td[1]/h3/a/div/span")
        print(category_name)
        self.driver.find_element_by_link_text("所有分类").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(category_name))
        self.driver.find_element(*category_name).click()
