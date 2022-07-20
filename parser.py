from crawler import Crawler as sc 
from pytube import YouTube, exceptions, metadata, Playlist
import json
import os


programming_sub_category = {
    "BasicProgramming" :"https://www.youtube.com/watch?v=-3DHpwy498o&list=PLuHgQVnccGMDtnr4nTSFfmocHL5FeH1xR&index=1"
    # ,"WebProgramming" : "https://www.youtube.com/watch?v=tZooW6PritE&list=PLuHgQVnccGMDZP7FJ_ZsUrdCGH68ppvPb"
    # ,"DevOps":"https://www.youtube.com/watch?v=Ps8HDIAyPD0&list=PLuHgQVnccGMDeMJsGq2O-55Ymtx0IdKWf"
    # ,"AI":"https://www.youtube.com/watch?v=LPqmPfhnR1o&list=PLuHgQVnccGMDy5oF7G5WYxLF3NCYhB9H9"
    # ,"DB":"https://www.youtube.com/watch?v=h_XDmyz--0w&list=PLuHgQVnccGMCgrP_9HL3dAcvdt8qOZxjW"
    # ,"Algorithm":"https://www.youtube.com/watch?v=bj2F0hTiTtw&list=PLuHgQVnccGMDsWOOn_P0EmAWB8DArS3Fk"
    }

business_sub_category = {

}

design_sub_category = {

}

categories = {
    "Programming" : programming_sub_category
#    ,"Business" : business_sub_category
#    ,"Design" : design_sub_category
}

category_title = "" # 강좌명
category_sub_title = "" #부-강좌명
category_intro = "" #강의 소개
category_thumbnail = [] #썸네일
category_difficulty = '중' #난이도
category_tag = [] # 태그
category_for_recommend = [] # ??? 강의 소개
category_paid = 0 # 가격?
category_review = [] # 수강평
category_body = "" # 강의 소개
category_pay_div = True # ??? 강의 난이도 boolean
category_teacher = "" # 강의자
category_curriculum_summary = [] # 커리큘럼
content_title = '' # 컨텐츠명
content_order = 0 # 컨텐츠 순서(컨텐츠명에서 떼오면 될듯)
content_type = 'video' # ??? 컨텐츠
content_data_url = '' # 강의 영상 링크
content_data_body = '' # ??? 내용
content_data_description = '' # ??? 학습 목표 및 부가 정보

video_down_dir = './video'
image_down_dir = './image/'

if not os.path.exists('./image/'):
    os.mkdir('./image/')
if not os.path.exists('./video/'):
    os.mkdir('./video/')


crawler = sc()

for category_name, category  in categories.items():
    for sub_category_name, sub_category_url in category.items():
        print(sub_category_url) 

        ############################# 이미지 다운로드 #############################
        category_thumbnail = YouTube(sub_category_url).thumbnail_url
        filename = YouTube(sub_category_url).title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','')
        try:
            os.system('curl '+ category_thumbnail + ' > ' + image_down_dir + ''.join(filename.split()) + '.jpg')
        except OSError:
            print(exceptions)
        
        crawler.setCrawler(sub_category_url)
        print("강좌명")
        temp = crawler.get_category_title().split('\n')
        t = temp[0].split(':')
        print(t)
        category_title = t[0]
        category_sub_title = t[-1]

        ############################# LectureSchema 저장 ################################
        # print("난이도")
        # print(crawler.get_category_difficulty())
        # print("강의 소개")
        # print(crawler.get_category_intro())
        print("썸네일")
        print(category_thumbnail)
        # print(crawler.get_category_thumbnail())
        # print("강의자")
        # print(crawler.get_category_teacher())
        # crawler.setCrawler(crawler.get_category_url())
        # print("수강평")
        # print(crawler.get_category_review())
        print("커리큘럼")
        category_curriculum_summary.append(crawler.get_category_curriculum_summary())
        # print("영상 링크")
        # print(crawler.get_content_data_url())
        
        # print(driver)
    
        print(category_title)
        print(category_sub_title)
        print(category_curriculum_summary)

        ##################### 재생 목록에서 받아올 수 있는 부분 #######################
        # LectureSchema = {
        #     "category" : category_name , #{ type: String, required: true }, // 카테고리
        #     "sub_category" : sub_category_name , #{ type: String, default:"" }, //카테고리 -부
        #     "title" : , #{ type: String, required: true }, // 강좌명
        #     "sub_title" : , # { type: String, default:"" }, // 부 제목
        #     "intro" : , #{ type: String, default:"" }, // 강의 소개
        #     "thumbnail" : , #{ type: Array, default:[] }, // 강의 소개
        #     "difficulty" : , #{ type: String, default:"중" }, // 강의 소개
        #     "tag" : , #{ type: Array, default:[] }, // 강의 소개
        #     "for_recommend" : , #{ type: Array, default:[] }, // 강의 대상
        #     "paid" : , #{ type: Number, default:0 }, // 가격
        #     "review" : , #[{ type: ObjectId , ref: "review" }], // 신청 강좌 정보(댓글)
        #     "body" : , #{ type: String, default:"" }, // 강의 요약 정보
        #     "pay_div" : , #{ type: Boolean, default:"중" }, // 강의 유무료 여부
        #     "teacher" : , #[{ type: ObjectId , required: true, ref: "teacher" }], // 강의자
        #     "curriculum_summary" :  #{ type: Array, default:[] } // 신청 강좌 주차 요약 정보
        # }
        # contents_url = crawler.get_content_url()
        # print(contents_url)
        pl = Playlist(sub_category_url)
        
        for order, content in enumerate(pl.video_urls):
            print(content)
            crawler.setCrawler(content)

            ############################## 영상 다운로드 ##############################
            try:
                yt = YouTube(content)
                title = yt.title
            except exceptions.VideoUnavailable:
                print(f'Video {title} is unavaialable, skipping.')
            else:
                print(f'Downloading video: {title}')
                print(yt.streams.filter(resolution='360p',file_extension='mp4',progressive=True))
                yt.streams.get_by_itag(18).download(video_down_dir)

            

            ##################### 개별 영상에서 받아올 수 있는 부분 #######################
            # ContentSchema = {
            #     "title": title , #{ type: String, required: true },// 컨텐츠명
            #     "order" : order , #{ type: Number, default: 0 },// 콘텐츠 순서
            #     "type" : content_type , #{ type: String, required: true }, // 콘텐츠 타입
            #     "data" : {
            #         "url" : content, #{ type: String, default:"" }, // 영상 및 자료 링크
            #         "body" : content_data_body, #{ type: String, default:""  }, // 내용
            #         "description" : content_data_description #{ type: String, default:""  }, // 학습 목표 및 부가 정보
            #     }
            # }
            ########################## content -> json 파일로 저장 #########################
            #with open('./' + filename +'.json', 'w') as f:
            #json.dump(ContentSchema, f, indent=2)
        ############################## category -> json 파일로 저장 ##########################
        #with open('./' + sub_category_name +'.json', 'w') as f:
        #   json.dump(LectureSchema, f, indent=2)
        