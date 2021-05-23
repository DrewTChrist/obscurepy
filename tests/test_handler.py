import unittest
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.handlers.handler import Handler


class TestHandler(Handler):
    pass


class HandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = TestHandler()
        self.classdef_handler = ClassDefHandler()

    def test_get_next(self):
        self.fixture.set_next(self.classdef_handler)
        handler = self.fixture.get_next()
        self.assertEqual(type(handler), ClassDefHandler)

    def test_get_next_none(self):
        handler = self.fixture.get_next()
        self.assertEqual(handler, None)
