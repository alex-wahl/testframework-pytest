import allure
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from libs.helper import SingletonMeta


class BasePage(metaclass=SingletonMeta):
    TITLE = "head > title"
    TAG_NAME = "body"

    def __init__(self, setup, url):
        self.driver = setup
        self.driver.get(url)

    def get_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, self.TAG_NAME))
        )
        return self.driver.execute_script(f"return document.querySelector('{self.TITLE}').textContent;")

    def make_screenshot(self, filename="screenshot.png"):
        # Calculate the total height of the web page and set the window size
        total_height = self.driver.execute_script("return document.body.parentNode.scrollHeight")
        self.driver.set_window_size(1920, total_height)  # Width is set to 1920px
        self.driver.save_screenshot(filename)  # Take a screenshot of the entire page

        # Open the screenshot, convert it to RGB if necessary, and save as JPEG
        with Image.open(filename) as img:
            if img.mode == 'RGBA':
                img = img.convert('RGB')  # Assign the converted image to img
            # Save the converted image as JPEG
            img.save(filename.replace('.png', '.jpg'), "JPEG", optimize=True, quality=80)

        # Attach the screenshot to Allure report as JPEG
        with open(filename.replace('.png', '.jpg'), 'rb') as file:
            allure.attach(file.read(), name="Full Page Screenshot", attachment_type=allure.attachment_type.JPG)