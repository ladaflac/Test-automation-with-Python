# test suite = class
# always inherits from TestCase
# TestCase is part of unittest library

from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        # create new post object
        p = Post("Test", "Test content")

        # TestCase = self object because it is inherited
        # this test will fail when init method in post.py is changed
        self.assertEqual("Test", p.title, "title should be equal but is not")
        self.assertEqual("Test content", p.content, "content should be equal but is not")

    def test_json(self):
        p = Post("Test", "Test content")
        expected = {"title": "Test", "content": "Test content"}
        
        self.assertDictEqual(expected, p.json(), "dict not as expected")
