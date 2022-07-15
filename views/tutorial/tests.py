# import unittest
# 
# from pyramid import testing
# 
# 
# class TutorialViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
# 
#     def tearDown(self):
#         testing.tearDown()
# 
#     def test_home(self):
#         from .views import home
# 
#         request = testing.DummyRequest()
#         response = home(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'Visit', response.body)
# 
#     def test_hello(self):
#         from .views import hello
# 
#         request = testing.DummyRequest()
#         response = hello(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'Go back', response.body)
# 
# 
# class TutorialFunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from tutorial import main
#         app = main({})
#         from webtest import TestApp
# 
#         self.testapp = TestApp(app)
# 
#     def test_home(self):
#         res = self.testapp.get('/', status=200)
#         self.assertIn(b'<body>Visit', res.body)
# 
#     def test_hello(self):
#         res = self.testapp.get('/howdy', status=200)
#         self.assertIn(b'<body>Go back', res.body)

from pyramid import testing

def test_home():
    from .views import home

    request = testing.DummyRequest()
    response = home(request)
    assert response.status_code == 200
    assert b'Visit' in response.body

def test_hello():
    from .views import hello

    request = testing.DummyRequest()
    response = hello(request)
    assert response.status_code == 200
    assert b'Go back' in response.body


class TestFunctional():
    from tutorial import main
    app = main({})
    from webtest import TestApp
    testapp = TestApp(app)

    def test_home_functional(self):
        res = self.testapp.get('/', status=200)
        assert b'<body>Visit' in res.body

    def test_hello_functional(self):
        res = self.testapp.get('/howdy', status=200)
        assert b'<body>Go back' in res.body