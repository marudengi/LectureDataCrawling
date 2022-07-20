## 셀레니움

### 너무 빠른 입력 대응책(아직 미적용 이슈 발생시 적용 예정)

pyautogui → ‘ctrl’ + ‘v’ 기능 수행

pyperclip → 클립보드에 저장

## 패키지

selenium

pytube

## 코드 흐름

### 클래스

selenium_crawling.py

- webdriver의 초기화 및 작업 수행
- `driver.find_element()`
    - `By.CLASS_NAME` 으로 어떤 태그로 접근할지 설정
    - 해당 태그의 속성
    - 반환값은 오브젝트형태이므로 결과적으로 `driver.find_element(By.CLASS_NAME, attribute_name).text` 처럼 text로 반환시켜야 사용 가능
- `driver.find_elements()`
    - `driver.find_element()` 와 사용법 동일
    - 일치하는 태그의 속성값들 정보를 모두 수집
    - 따라서 반환값은 오브젝트들을 리스트에 담은 형태
    - 반복문으로 text로 변환시켜줘야 사용 가능

parser.py

- get(), set() 메서드를 통해 webdriver 작업 수행
- get() 메서드로 받아온 데이터 파싱
- pytube로 유튜브 영상 및 thumbnail 이미지 받아오기
- 이미지 저장시 이름을 강의 제목으로 지정
    - 문자열 중 특수기호 `\ / : * ? " < > |` 예외 처리
    - 파일 경로 예외처리
        - `./image` 경로에 저장
        - 없으면 만들기
- 영상 저장시 강의 제목으로 지정
    - 파일 경로 예외처리
        - `./video` 경로에 저장
        - 없으면 만들기

## 유튜브 영상 받아오기

[https://vincinotes.com/파이썬-pytube로-유튜브-영상과-음원-추출하기/](https://vincinotes.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-pytube%EB%A1%9C-%EC%9C%A0%ED%8A%9C%EB%B8%8C-%EC%98%81%EC%83%81%EA%B3%BC-%EC%9D%8C%EC%9B%90-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0/)

[https://marinelifeirony.tistory.com/146](https://marinelifeirony.tistory.com/146)

```python
try:
        yt = YouTube(sub_title)
    except exceptions.VideoUnavailable:
        print(f'Video {sub_title} is unavaialable, skipping.')
    else:
        print(f'Downloading video: {sub_title}')
        print(yt.streams.filter(resolution='360p',file_extension='mp4',progressive=True))
        yt.streams.get_by_itag(18).download(video_down_dir)
```

## 썸네일 이미지 받아오기

pytube로 썸네일 url 받아오기

[https://www.codegrepper.com/code-examples/whatever/how+to+download+thumbnails+pytube](https://www.codegrepper.com/code-examples/whatever/how+to+download+thumbnails+pytube)

url을 이미지로 저장하기

[https://soyoung-new-challenge.tistory.com/92](https://soyoung-new-challenge.tistory.com/92)

```python
ategory_thumbnail = YouTube(sub_title).thumbnail_url
filename = YouTube(sub_title).title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','')
try:
    os.system('curl '+ category_thumbnail + ' > ./image/'+ ''.join(filename.split()) + '.jpg')
except OSError:
    print(exceptions)
```

## 구조적 개편

태그별로 crawler 클래스에서 webdriver로 받아오는 방식으로 진행하였으나 인프런과 유튜브의 구조적 차이점으로 한번에 모든 문자열을 읽어서 가져온 후 parser클래스에서 문자열 파싱을 진행

→ 유튜브 영상이 규격화되어있지 않으므로 예외상황 발생 가능성 농후 이에대한 대책 필요
