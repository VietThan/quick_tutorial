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
#         self.assertEqual('Home View', response['page_title'])

# class TutorialFunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from tutorial import main
#         app = main({})
#         from webtest import TestApp

#         self.testapp = TestApp(app)

#     def test_home(self):
#         res = self.testapp.get('/', status=200)
#         self.assertIn(b'TutorialViews - Home View', res.body)

from pyramid import testing

class TestTutorial:

    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.home()
        assert 'Home View' == response['page_title']


class TestFunctional():
    from tutorial import main
    app = main({})
    from webtest import TestApp
    testapp = TestApp(app)

    def test_home_functional(self):
        res = self.testapp.get('/', status=200)
        assert b'TutorialViews - Home View' in res.body