from django.test import Client, TestCase


class TestApiURLs(TestCase):
    def setUp(self):
        self.client = Client()

    def test_echo_res(self):
        response = self.client.get('/api/v1/echo?msg=hello')
        self.assertEqual(eval(response.content.decode('utf-8')), {"msg": "hello"})

    def test_echo_404(self):
        response = self.client.get('/api/v1/echo?hello=hello')
        self.assertEqual(response.status_code, 404)
