from django.test import TestCase

class TestView(TestCase):
    def test_post_list(self):
        self.assertEqual(2, 3) # chapter TDD. 2와 3이 같은지 테스트
