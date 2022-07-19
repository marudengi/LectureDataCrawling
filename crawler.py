from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#chrome driver auto update
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import pyperclip

class Crawler:

    def __init__(self):
        service = Service(executable_path=ChromeDriverManager().install())

        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--log-level=1')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        print('-----------------------driver init-----------------------')
    
    def __del__(self):
        self.driver.close()
        print("-------------------driver closed-------------------")

    def setCrawler(self,LectureName):
        print('-------------------------set crawler-------------------------')
        self.driver.get(LectureName)
        time.sleep(2)

    ##################### category url ###################################

    def get_category_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'course_title').get_attribute('innerText')

    def get_category_intro(self):
        return self.driver.find_element(By.CLASS_NAME, 'course_description').get_attribute('innerText')

    def get_category_thumbnail(self):
        return self.driver.find_element(By.TAG_NAME, 'img').get_attribute('src')

    def get_category_difficulty(self):
        return self.driver.find_element(By.CLASS_NAME, 'course_level').get_attribute('innerText')

    def get_category_tag(self):
        return self.driver.find_element(By.CLASS_NAME, '').get_attribute('')

    def get_category_for_recommend(self):
        return self.driver.find_element(By.CLASS_NAME, '').get_attribute('')

    def get_category_paid(self):
        return self.driver.find_element(By.CLASS_NAME, '').get_attribute('')

    def get_category_teacher(self):
        return self.driver.find_element(By.CLASS_NAME, 'instructor').get_attribute('innerText')

    ####################### lecture url #####################################

    def get_lecture_url(self):
        return self.driver.find_element(By.CLASS_NAME, 'course_card_front').get_attribute('href')

    def get_lecture_review(self):
        return self.driver.find_element(By.CLASS_NAME, 'review-list__content').get_attribute('innerText')

    def get_lecture_body(self):
        return self.driver.find_element(By.CLASS_NAME, 'cd-body').get_attribute('innerText')
    
    def get_lecture_pay_div(self):
        return self.driver.find_element(By.CLASS_NAME, 'course_card_front').get_attribute('innerText')

    def get_lecture_curriculum_summary(self):
        return self.driver.find_element(By.CLASS_NAME, 'cd-curriculum').get_attribute('innerText')

    ######################## contents url ###################################

    def get_content_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'css-1pqj6dl').get_attribute('innerText')

    def get_content_order(self):
        return self.driver.find_element(By.CLASS_NAME, '').get_attribute('')

    def get_content_type(self):
        return self.driver.find_element(By.CLASS_NAME, 'css-1pqj6dl').get_attribute('innerText')

    def get_content_data_url(self):
        return self.driver.find_element(By.CLASS_NAME, 'css-w1atjl shaka-video').get_attribute('currentSrc')

    def get_content_data_body(self):
        return self.driver.find_element(By.CLASS_NAME, '').get_attribute('')

    def get_content_data_description(self):
        return self.driver.find_element(By.CLASS_NAME, '').get_attribute('')