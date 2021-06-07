from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

class TestView(TestCase):
    # testcase 내 기본적으로 설정되어야 하는 내용 정의
    def setUp(self):
        self.client = Client() # setUp 함수 내에 Client()를 사용하겠다는 내용

    # 포스트 목록 페이지 테스트
    def test_post_list(self):
        # 1.1 포스트 목록 페이지 가져오기
        # client라는 가상의 사용자가 웹에 '127.0.0.1:8000/blog/'를 입력하면 열리는 웹 페이지 정보를 response에 저장
        response = self.client.get('/blog/')
        # 1.2 페이지 로드
        # 실패하면 404를 response, 성공하면 200을 response
        self.assertEqual(response.status_code, 200)
        # 1.3 페이지 타이틀 'Blog'인지
        # parsing된 html의 title이 Blog인지 확인
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')
        # 1.4 네비게이션 바 존재 여부
        # soup에 담긴 요소 중 nav 요소만 navbar에 저장
        navbar = soup.nav
        # 1.5 Blog, About Me가 네비게이션 바에 있음
        # navbar 요소 중, Blog와 About Me가 있는지 확인
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)
        # 2.1 메인 영역에 게시물이 하나도 없다면
        # 작성된 포스트가 0개인지 확인
        self.assertEqual(Post.objects.count(), 0)
        # 2.2 '아직 게시물이 없습니다.'라는 문구 출력
        # id가 main_area인 요소를 찾아 main_area에 저장
        # main_area가 해당 텍스트인지 확인
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        # 3.1 게시물이 2개 있다면
        # 가상의 게시물 2개 생성
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World'
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트입니다.',
            content='Goodbye World'
        )
        # 2개가 생성되었는지 확인
        self.assertEqual(Post.objects.count(), 2)

        # 3.2 포스트 목록 페이지를 새로고침했을 때
        # 새로고침하기 위해 1.1~1.3을 반복
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재
        # 포스트 2개가 잘 생성되었는지 확인
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # 3.4 '아직 게시물이 없습니다.'문구 삭제됨
        # 게시물이 없다는 문구가 출력되지 않음을 확인
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

    # 포스트 상세 페이지 테스트
    def test_post_detail(self):
        # 1.1 포스트가 하나 있다
        # 가상의 포스트 생성
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = '와ㅓㅏㅇ나뫈어ㅏㄹ머ㅏㅓ'
        )
        # 1.2 그 포스트의 url은 '/blog/1/'이다.
        # 만들어진 가상의 포스트 pk와 url 확인
        self.assertEqual(post_001.get_absolute_url(), '/blog/1/')

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1 첫 번째 포스트의 url로 접근하면 정상적으로 작동한다. (status code : 200)
        # response code 성공인지 확인
        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 2.2 포스트 목록 페이지와 똑같은 내비게이션 바가 있다
        # 내비게이션 바의 텍스트가 포스트 ''목록'' 페이지의 텍스트와 같은지 확인
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)
        # 2.3 첫 번째 포스트의 제목이 웹 브라우저 탭 타이틀에 들어있다.
        # 해당 포스트의 title 필드 값이 웹 브라우저 탭의 타이틀에 있는지 확인
        self.assertIn(post_001.title, soup.title.text)
        # 2.4 첫 번째 포스트의 제목이 포스트 영역에 있다.
        # 메인 영역에서 포스트 영역만 불러와 post_area에 담고 title이 포스트 영역 안에 있는지 확인
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(post_001.title, post_area.text)
        # 2.5 첫 번째 포스트의 작성자가 포스트 영역에 있다.
        # 아직 구현 불가?
        # 2.6 첫 번째 포스트의 내용이 포스트 영역에 있다.
        self.assertIn(post_001, post_area.text)

