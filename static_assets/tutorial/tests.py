# import unittest

# from pyramid import testing


# class TutorialViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()

#     def tearDown(self):
#         testing.tearDown()

#     def test_home(self):
#         from .views import TutorialViews

#         request = testing.DummyRequest()
#         inst = TutorialViews(request)
#         response = inst.home()
#         self.assertEqual('Home View', response['name'])

#     def test_hello(self):
#         from .views import TutorialViews

#         request = testing.DummyRequest()
#         inst = TutorialViews(request)
#         response = inst.hello()
#         self.assertEqual('Hello View', response['name'])


# class TutorialFunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from tutorial import main
#         app = main({})
#         from webtest import TestApp

#         self.testapp = TestApp(app)

#     def test_home(self):
#         res = self.testapp.get('/', status=200)
#         self.assertIn(b'<h1>Hi Home View', res.body)

#     def test_hello(self):
#         res = self.testapp.get('/howdy', status=200)
#         self.assertIn(b'<h1>Hi Hello View', res.body)

from pyramid import testing

def test_home():
    from .views import TutorialViews

    request = testing.DummyRequest()
    inst = TutorialViews(request)
    response = inst.home()
    assert 'Home View' == response['name']

def test_hello():
    from .views import TutorialViews

    request = testing.DummyRequest()
    inst = TutorialViews(request)
    response = inst.hello()
    assert 'Hello View' == response['name']


class TestFunctional():
    from tutorial import main
    app = main({})
    from webtest import TestApp
    testapp = TestApp(app)

    def test_home_functional(self):
        res = self.testapp.get('/', status=200)
        assert b'<h1>Hi Home View' in res.body

    def test_hello_functional(self):
        res = self.testapp.get('/howdy', status=200)
        assert b'<h1>Hi Hello View' in res.body