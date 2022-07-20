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

    category_title = 'style-scope ytd-watch-metadata' # 강좌명
    category_sub_title = "" #부-강좌명
    category_intro = "" #강의 소개
    category_thumbnail = 'style-scope yt-img-shadow' #썸네일
    category_difficulty = "" #난이도
    category_tag = "" # 태그
    category_for_recommend = "" # ??? 강의 소개
    category_paid = "" # 가격?
    category_teacher = 'yt-simple-endpoint style-scope yt-formatted-string' # 강의자

    category_url = 'style-scope ytd-playlist-panel-renderer' #해당 강의 카테고리 url

    category_review = 'style-scope ytd-comment-renderer' # 수강평
    category_body = '' # 강의 소개
    category_pay_div = False # ??? 강의 난이도 boolean
    category_curriculum_summary = 'style-scope ytd-playlist-panel-video-renderer' # 커리큘럼

    content_url = 'style-scope ytd-playlist-panel-renderer' #해당 카테고리내의 개별 강의 url

    content_title = 'style-scope ytd-watch-metadata' # 컨텐츠명
    content_order = '' # 컨텐츠 순서(컨텐츠명에서 떼오면 될듯)
    content_type = '' # ??? 컨텐츠
    content_data_url = '' # 강의 영상 링크
    content_data_body = 'style-scope yt-formatted-string' # ??? 내용
    content_data_description = "yt-simple-endpoint style-scope yt-formatted-string" # ??? 학습 목표 및 부가 정보

    def __init__(self):
        service = Service(executable_path=ChromeDriverManager().install())

        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--log-level=1')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        print('-----------------------driver init-----------------------')
    
    def __del__(self):
        self.driver.close()
        print("-------------------driver closed-------------------")

    def setCrawler(self,url):
        print('-------------------------set crawler-------------------------')
        self.driver.get(url)
        time.sleep(2)

    ##################### category url ###################################

    def get_category_title(self):
        print(Crawler.category_title)
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_title).text

    def get_category_sub_title(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_sub_title).text

    def get_category_intro(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_intro).get_attribute('innerText')

    def get_category_thumbnail(self):
        return self.driver.find_element(By.TAG_NAME, Crawler.category_thumbnail).get_attribute('src')

    def get_category_difficulty(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_difficulty).get_attribute('innerText')

    def get_category_tag(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_tag).get_attribute('')

    def get_category_for_recommend(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_for_recommend).get_attribute('')

    def get_category_paid(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_paid).get_attribute('')

    def get_category_teacher(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_teacher).get_attribute('innerText')

    def get_category_url(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_url).get_attribute('href')

    def get_category_review(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_review).get_attribute('innerText')

    def get_category_body(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_body).get_attribute('innerText')
    
    def get_category_pay_div(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.category_pay_div).get_attribute('innerText')

    def get_category_curriculum_summary(self):
        arr = []
        for temp in self.driver.find_elements(By.CLASS_NAME, Crawler.category_curriculum_summary):
            arr.append(temp.text)
        return arr

    ######################## contents url ###################################

    def get_content_url(self):
        arr = []
        for temp in self.driver.find_elements(By.CLASS_NAME, Crawler.content_url):
            arr.append(temp.get_attribute('href'))
        return arr

    def get_content_title(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.content_title).get_attribute('innerText')

    def get_content_order(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.content_order).get_attribute('')

    def get_content_type(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.content_type).get_attribute('innerText')

    def get_content_data_url(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.content_data_url).get_attribute('href')

    def get_content_data_body(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.content_data_body).get_attribute('')

    def get_content_data_description(self):
        return self.driver.find_element(By.CLASS_NAME, Crawler.content_data_description).get_attribute('')