from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test author")

        self.assertEqual("Test", b.title, "title not equal")
        self.assertEqual("Test author", b.author, "author not equal")
        self.assertListEqual([], b.posts, "lists not equal")
        # ILI: self.assertEqual(len([]), len(b.posts), "lists not equal")
        # ILI: self.assertEqual(0, len(b.posts), "lists not equal")

    def test_repr(self):
        b = Blog("Test", "Test author")
        b2 = Blog("My day", "Rolf")

        self.assertEqual(b.__repr__(), "Test by Test author (0 posts)")
        self.assertEqual(b2.__repr__(), "My day by Rolf (0 posts)")

    def test_repr_multiple_posts(self):
        b = Blog("Test", "Test author")
        b.posts = ["test"]
        b2 = Blog("My day", "Rolf")
        b2.posts = ["test", "another"]

        self.assertEqual(b.__repr__(), "Test by Test author (1 post)")
        self.assertEqual(b2.__repr__(), "My day by Rolf (2 posts)")

