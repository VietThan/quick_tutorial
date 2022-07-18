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
#         request.matchdict['first'] = 'First'
#         request.matchdict['last'] = 'Last'
#         inst = TutorialViews(request)
#         response = inst.home()
#         self.assertEqual(response['first'], 'First')
#         self.assertEqual(response['last'], 'Last')


# class TutorialFunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from tutorial import main
#         app = main({})
#         from webtest import TestApp

#         self.testapp = TestApp(app)

#     def test_home(self):
#         res = self.testapp.get('/howdy/Jane/Doe', status=200)
#         self.assertIn(b'Jane', res.body)
#         self.assertIn(b'Doe', res.body)

from pyramid import testing

class TestTutorial():
    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        request.matchdict['first'] = 'Viet'
        request.matchdict['last'] = 'Than'
        inst = TutorialViews(request)
        response = inst.home()
        assert response['first'] == 'Viet'
        assert response['last'] == 'Than'


class TestFunctional():
    from tutorial import main
    app = main({})
    from webtest import TestApp
    testapp = TestApp(app)

    def test_home_functional(self):
        res = self.testapp.get('/howdy/Jane/Doe', status=200)
        assert b'Jane' in res.body
        assert b'Doe' in res.body