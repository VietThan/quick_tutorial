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
#         self.assertEqual(response.status, '302 Found')

#     def test_plain_without_name(self):
#         from .views import TutorialViews

#         request = testing.DummyRequest()
#         inst = TutorialViews(request)
#         response = inst.plain()
#         self.assertIn(b'No Name Provided', response.body)

#     def test_plain_with_name(self):
#         from .views import TutorialViews

#         request = testing.DummyRequest()
#         request.GET['name'] = 'Jane Doe'
#         inst = TutorialViews(request)
#         response = inst.plain()
#         self.assertIn(b'Jane Doe', response.body)


# class TutorialFunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from tutorial import main

#         app = main({})
#         from webtest import TestApp

#         self.testapp = TestApp(app)

#     def test_plain_without_name(self):
#         res = self.testapp.get('/plain', status=200)
#         self.assertIn(b'No Name Provided', res.body)

#     def test_plain_with_name(self):
#         res = self.testapp.get('/plain?name=Jane%20Doe', status=200)
#         self.assertIn(b'Jane Doe', res.body)

from pyramid import testing


class TestTutorial:


    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.home()
        assert response.status == '302 Found'

    def test_plain_without_name(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.plain()
        assert b'No Name Provided' in response.body

    def test_plain_with_name(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        request.GET['name'] = 'Jane Doe'
        inst = TutorialViews(request)
        response = inst.plain()
        assert b'Jane Doe' in response.body


class TestFunctional():
    from tutorial import main
    app = main({})
    from webtest import TestApp
    testapp = TestApp(app)

    def test_plain_without_name(self):
        res = self.testapp.get('/plain', status=200)
        assert b'No Name Provided' in res.body

    def test_hello_functional(self):
        res = self.testapp.get('/plain?name=Jane%20Doe', status=200)
        assert b'Jane Doe' in res.body