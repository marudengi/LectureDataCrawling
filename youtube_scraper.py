from pytube import YouTube, exceptions, Playlist
import json
import os
from unicodedata import normalize


programming_sub_category = {
    "BasicProgramming" : "https://www.youtube.com/watch?v=-3DHpwy498o&list=PLuHgQVnccGMDtnr4nTSFfmocHL5FeH1xR&index=1"
    , "WebProgramming" : "https://www.youtube.com/watch?v=tZooW6PritE&list=PLuHgQVnccGMDZP7FJ_ZsUrdCGH68ppvPb"
    , "DevOps": "https://www.youtube.com/watch?v=Ps8HDIAyPD0&list=PLuHgQVnccGMDeMJsGq2O-55Ymtx0IdKWf"
    , "AI": "https://www.youtube.com/watch?v=LPqmPfhnR1o&list=PLuHgQVnccGMDy5oF7G5WYxLF3NCYhB9H9"
    , "DB": "https://www.youtube.com/watch?v=h_XDmyz--0w&list=PLuHgQVnccGMCgrP_9HL3dAcvdt8qOZxjW"
    , "Algorithm": "https://www.youtube.com/watch?v=bj2F0hTiTtw&list=PLuHgQVnccGMDsWOOn_P0EmAWB8DArS3Fk"
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

category_title = "" # 강좌명 required
category_sub_title = "" #부-강좌명
category_intro = "" #강의 소개 
category_thumbnail = "" #썸네일 
category_difficulty = '중' #난이도
category_tag = [] # 태그
category_for_recommend = [] # 수강 추천 대상
category_paid = 0 # 가격
category_review = [] # 수강평
category_body = "" # 강의 소개
category_pay_div = "유료" # 유무료 여부
category_teacher = "" # 강의자 required
category_curriculum_summary = [] # 커리큘럼
content_title = '' # 컨텐츠명 required
content_order = 0 # 컨텐츠 순서
content_type = 'video' # 컨텐츠 타입(영상, 문서, ...) required
content_data_url = '' # 강의 영상 링크
content_data_body = '' # 강의 설명
content_data_description = '' # 강의 상세 설명

# image_down_dir = './image/'


if not os.path.exists('./jsonfile/'):
    os.mkdir('./jsonfile/')

if not os.path.exists('./video/'):
    os.mkdir('./video/')

################################## 카테고리 ###################################
for category_name, category  in categories.items():
    ################################## 부-카테고리 #####################################
    for sub_category_name, sub_category_url in category.items():
        print(sub_category_url) 

        ############################# 이미지 다운로드 #############################
        # category_thumbnail = YouTube(sub_category_url).thumbnail_url
        # filename = YouTube(sub_category_url).title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','')
        # try:
        #     os.system('curl '+ category_thumbnail + ' > ' + image_down_dir + ''.join(filename.split()) + '.jpg')
        # except OSError:
        #     print(exceptions)

        pl = Playlist(sub_category_url)
        
        category_title = pl.title
        category_teacher = pl.owner
        
        if not os.path.exists('./jsonfile/' + sub_category_name):
            os.mkdir('./jsonfile/' + sub_category_name)

        video_down_dir = './video/' + sub_category_name+'/'

        if not os.path.exists('./video/'+sub_category_name+'/'):
            os.mkdir('./video/' + sub_category_name+'/')
        ######################################## 개별 컨텐츠 작업 ############################################
        for order, content in enumerate(pl.video_urls):
            print(content)
            
            ############################## 영상 다운로드 ##############################
            try:
                yt = YouTube(content)
                title = yt.title.replace('\\',' ').replace('/',' ').replace(':','-').replace('*',' ').replace('?',' ').replace('"',"'").replace('<','[').replace('>',']').replace('|',' ')
                title = normalize('NFC',title)
            except exceptions.VideoUnavailable:
                print(f'Video {content} is unavaialable, skipping.')
            else:
                print(f'Downloading video: {content}')
                yt.streams.filter(resolution='360p',file_extension='mp4',progressive=True)
                yt.streams.get_by_itag(18).download(output_path=video_down_dir, filename=title+'.mp4')

            
            # print('video id : ' + yt.video_id)
            describe = yt.description.split('\n')
            content_data_body = describe[0]
            content_data_description = ' '.join(describe[1:])
            category_curriculum_summary.append(title)
            #################### 개별 영상에서 받아올 수 있는 부분 #######################
            ContentSchema = {
                "title": title , #{ type: String, required: true },// 컨텐츠명
                "order" : order , #{ type: Number, default: 0 },// 콘텐츠 순서
                "type" : content_type , #{ type: String, required: true }, // 콘텐츠 타입
           		"lecture_id": "",#{ type: ObjectId , required: true, ref: "Lecture" }
                "data" : {
                    "url" : content, #{ type: String, default:"" }, // 영상 및 자료 링크
                    "body" : content_data_body, #{ type: String, default:""  }, // 내용
                    "description" : content_data_description #{ type: String, default:""  }, // 학습 목표 및 부가 정보
                }
            }
            
            ########################## content -> json 파일로 저장 #########################
            with open('./jsonfile/' + sub_category_name + '/' + title +'.json', 'w', encoding='UTF-8') as f:
                json.dump(ContentSchema, f, indent=2, ensure_ascii=False)
        ##################### 재생 목록에서 받아올 수 있는 부분 #######################
        LectureSchema = {
            "category" : category_name , #{ type: String, required: true }, // 카테고리
            "sub_category" : sub_category_name , #{ type: String, default:"" }, //카테고리 -부
            "title" :  category_title, #{ type: String, required: true }, // 강좌명
            "sub_title" : category_sub_title, # { type: String, default:"" }, // 부 제목
            "intro" : category_intro, #{ type: String, default:"" }, // 강의 소개
            "thumbnail" : category_thumbnail, #{ type: Array, default:[] }, // 강의 소개
            "difficulty" : category_difficulty, #{ type: String, default:"중" }, // 강의 소개
            "tag" : category_tag, #{ type: Array, default:[] }, // 강의 소개
            "for_recommend" : category_for_recommend, #{ type: Array, default:[] }, // 강의 대상
            "paid" : category_paid, #{ type: Number, default:0 }, // 가격
            "body" : category_body, #{ type: String, default:"" }, // 강의 요약 정보
            "pay_div" : category_pay_div, #{ type: Boolean, default:"중" }, // 강의 유무료 여부
            "teacher" : category_teacher, #[{ type: ObjectId , required: true, ref: "teacher" }], // 강의자
            "curriculum_summary" :  category_curriculum_summary#{ type: Array, default:[] } // 신청 강좌 주차 요약 정보
        }
        ############################## category -> json 파일로 저장 ##########################
        with open('./jsonfile/' + sub_category_name + '/' + sub_category_name +'.json', 'w', encoding='UTF-8') as f:
          json.dump(LectureSchema, f, indent=2, ensure_ascii=False)
        