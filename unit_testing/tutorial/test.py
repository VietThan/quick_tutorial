# import unittest

# from pyramid import testing


# class TutorialViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()

#     def tearDown(self):
#         testing.tearDown()

#     def test_hello_world(self):
#         from tutorial import hello_world

#         request = testing.DummyRequest()
#         response = hello_world(request)
#         self.assertEqual(response.status_code, 200)

from pyramid import testing

def test_hello_world():
    from tutorial import hello_world
    request = testing.DummyRequest()
    response = hello_world(request)
    assert '200' in response.status