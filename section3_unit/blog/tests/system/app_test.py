from unittest import TestCase
from unittest.mock import patch
from app import *   # import the names from the file
import app  # import the file - executes the file at first import
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test" : blog}  # mapping of blog name to blog object (repr method),
                                    # so that the object contains this single blog

        # komplicirano je testirati sto se printa na konzolu (i print je builtin funkcija pa valjda radi),
        # a testirana metoda nema return
        # zato mockamo print i provjeravamo je li print metoda pozvana s ispravnom vrijednosti

        with patch('builtins.print') as mocked_print:   # patch trazi i modul uz naziv funkcije
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')  # repr u blog.py

    # TODO - AssertionError: Calls not found.
    # def test_print_two_blogs(self):
    #     blog1 = Blog("Test1", "Test Author1")
    #     blog2 = Blog("Test2", "Test Author2")
    #     app.blogs = {"Test1" : blog1, "Test2" : blog2}
    #     print_calls = ['- Test1 by Test Author1 (0 posts)', '- Test2 by Test Author2 (0 posts)']
    #     # app.print_blogs()     # printa na konzolu jedan po jedan
    #     with patch('builtins.print') as mocked_print:
    #         for blog in app.blogs:
    #             app.print_blogs()
    #             mocked_print.assert_has_calls(print_calls)

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()
            self.assertIsNone(app.blogs.get("Test"))

    def test_ask_read_post(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}

        with patch('builtins.input', return_value='Test'):
            # 2 checks possible: 1) if print_posts was called; 2) if print was called
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.asssert_called_with(blog)

    def test_print_posts(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("Test Post", "Test Content")
        app.blogs = {"Test": blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts()
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected_print = '''
--- {} ---
    
{}
    
'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)
