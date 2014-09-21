import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15) # 15 seconds
        self.base_url = "http://gimepmobile.weebly.com/"

    def test_contact_form(self):
        driver = self.driver
        driver.get(self.base_url + "contact.html")        
        self.assertIn("Contact - Arduino Domotic Control",driver.title)
        elem = driver.find_element_by_id("input-443138284781667233")
        elem.send_keys("Pablo")
        elem_lastName = driver.find_element_by_id("input-443138284781667233-1")
        elem_lastName.send_keys("Gimenez")
        elem_email = driver.find_element_by_id("input-651478021189180441")
        elem_email.send_keys("test-at@hotmail.com")
        elem_comment = driver.find_element_by_id("input-611364065981515057")
        elem_comment.send_keys("This is a text")        
        elem_btn = driver.find_element_by_css_selector("#form-851191180248929463 > div:nth-child(3) > a > span")
        elem_btn.click()        
        self.assertTrue(self.is_text_present("Thanks. Your information has been sent."))

    def test_download(self):
        driver = self.driver
        driver.get(self.base_url + "download.html")
        link = self.driver.find_element_by_link_text('ArduinoDomoticControl v2.0')
        href = link.get_attribute('href')
        download = self.driver.get(href)
        print download

    def is_text_present(self, text):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "851191180248929463-msg"))
            )
            print element.text
        except NoSuchElementException, e:
            return False        
        return text in element.text
   
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
