# import selenium_crawling as sc
from crawler import Crawler as sc
# from selenium_crawling import 

if __name__ == "__main__":
    title = ["Programming","Business","Design"]
    programming_sub_title = {
        "BasicProgramming" :"https://www.inflearn.com/courses/it-programming/programming-lang"
        # "WebProgramming" :"https://www.inflearn.com/courses/it-programming/web-dev?skill=web-dev",
        # "DevOps":"https://www.inflearn.com/courses/it-programming/devops-infra?skill=devops",
        # "AI":"https://www.inflearn.com/courses/data-science/artificial-intelligence?skill=ai",
        # "DB":"https://www.inflearn.com/courses/it-programming/database-dev?skill=database",
        # "Algorithm":"https://www.inflearn.com/courses/it-programming/algorithm?skill=algorithm"
        }

    category_title = [] # 강좌명
    category_sub_title = [] #부-강좌명
    category_intro = [] #강의 소개
    category_thumbnail = [] #썸네일
    category_difficulty = [] #난이도
    category_tag = [] # 태그
    category_for_recommend = [] # ??? 강의 소개
    category_paid = [] # 가격?
    lecture_review = [] # 수강평
    lecture_body = [] # 강의 소개
    lecture_pay_div = [] # ??? 강의 난이도 boolean
    lecture_teacher = [] # 강의자
    lecture_curriculum_summary = [] # 커리큘럼
    content_title = [] # 컨텐츠명
    content_order = [] # 컨텐츠 순서(컨텐츠명에서 떼오면 될듯)
    content_type = [] # ??? 컨텐츠
    content_data_url = [] # 강의 영상 링크
    content_data_body = [] # ??? 내용
    content_data_description = [] # ??? 학습 목표 및 부가 정보

    for sub_title in programming_sub_title.values():
        print(sub_title)
        crawler = sc()
        crawler.setCrawler(sub_title)
        print(crawler.get_category_title())
        print(crawler.get_category_difficulty())
        print(crawler.get_category_intro())
        print(crawler.get_category_thumbnail())
        print(crawler.get_category_teacher())
        crawler.setCrawler(crawler.get_lecture_url())
        print(crawler.get_lecture_review())
        print(crawler.get_lecture_curriculum_summary())
        crawler.setCrawler()
        
        # print(driver)

        # for element in elements:
        # print(element.get_attribute('innerText'))
        # print(element.get_attribute(''))
        #     print(element.get_attribute('innerText'))
            # print(element.get_attribute('title'))
            # print(element.get_attribute('href'))
        
        