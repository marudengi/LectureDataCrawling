## 패키지

pytube

## 코드 흐름

`youtube_scraper.py`

- pytube로 유튜브 영상 및 정보 받아오기
- 파일 경로 지정
    - 파일 경로 예외처리
            - `./video` 경로 유무 확인
            - 없으면 생성
            - `./jsonfile` 경로 유무 확인
            - 없으면 생성
- category와 playlist, video 순으로 정보 받아오기
- playlist 정보(영상 제목, 채널 소유자) 저장
- jsonfile, video 경로 뒤에 playlist 제목으로 경로 생성(ex> jsonfile/AI)
- playlist안의 video 정보 받기
- video 정보를 받아 제목과 파일 존재 여부에 대한 예외처리
- 영상 다운로드
- 개별 영상에 대한 정보 받아오기(ContentSchema 정보 json 형식으로 저장)
- 개별 영상 정보 모두 받은 후 playlist 전체에 대한 정보 받아오기(LectureSchema 정보 json 형식으로 저장)

## 유튜브 영상 받아오기

[https://vincinotes.com/파이썬-pytube로-유튜브-영상과-음원-추출하기/](https://vincinotes.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-pytube%EB%A1%9C-%EC%9C%A0%ED%8A%9C%EB%B8%8C-%EC%98%81%EC%83%81%EA%B3%BC-%EC%9D%8C%EC%9B%90-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0/)

[https://marinelifeirony.tistory.com/146](https://marinelifeirony.tistory.com/146)

- 영상은 유튜브 생활코딩 채널에서 받아왔습니다.

> https://www.youtube.com/watch?v=-3DHpwy498o&list=PLuHgQVnccGMDtnr4nTSFfmocHL5FeH1xR&index=1

> https://www.youtube.com/watch?v=tZooW6PritE&list=PLuHgQVnccGMDZP7FJ_ZsUrdCGH68ppvPb

> https://www.youtube.com/watch?v=Ps8HDIAyPD0&list=PLuHgQVnccGMDeMJsGq2O-55Ymtx0IdKWf

> https://www.youtube.com/watch?v=LPqmPfhnR1o&list=PLuHgQVnccGMDy5oF7G5WYxLF3NCYhB9H9

> https://www.youtube.com/watch?v=h_XDmyz--0w&list=PLuHgQVnccGMCgrP_9HL3dAcvdt8qOZxjW

> https://www.youtube.com/watch?v=bj2F0hTiTtw&list=PLuHgQVnccGMDsWOOn_P0EmAWB8DArS3Fk

```python
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
```
- 영상 제목에 대한 예외처리(파일 이름에 \/:*?"<>|가 들어갈 수 없다)
- 영상 제목이 깨지는 경우에 대한 예외처리(정규화 정준 결합(자음 모음 결합))
- 영상 정보가 없는 경우에 대한 예외처리
- 영상 해상도는 360p, 확장자는 mp4로 설정
- 저장 경로는 기존에 생성한 'video/'에 저장, 파일 이름은 앞서 예외처리한 영상 제목

## 유튜브 정보 json 파일로 받아오기

```python
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

with open('./jsonfile/' + sub_category_name + '/' + title +'.json', 'w', encoding='UTF-8') as f:
    json.dump(ContentSchema, f, indent=2, ensure_ascii=False)

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

with open('./jsonfile/' + sub_category_name + '/' + sub_category_name +'.json', 'w', encoding='UTF-8') as f:
    json.dump(LectureSchema, f, indent=2, ensure_ascii=False)

```
- json 형식으로 저장할 때 UTF-8로 지정 후 저장할 대 ensure_ascii=False를 해줘야 한글이 깨지지 않고 제목 정상 출력

## ~~썸네일 이미지 받아오기~~

~~pytube로 썸네일 url 받아오기~~

[https://www.codegrepper.com/code-examples/whatever/how+to+download+thumbnails+pytube](https://www.codegrepper.com/code-examples/whatever/how+to+download+thumbnails+pytube)

~~url을 이미지로 저장하기~~

[https://soyoung-new-challenge.tistory.com/92](https://soyoung-new-challenge.tistory.com/92)

- 썸네일은 CDN에서 뽑아오기로 결정, 기능 제거