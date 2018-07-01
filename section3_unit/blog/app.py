import blog


MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post , "q" to quit: '
POST_TEMPLATE = '''
--- {} ---
    
{}
    
'''

blogs = dict()  # take the blogs from some db and put them in a dictionary;
                # [(blog_name, Blog), (blog_name, Blog)]
                # mapping blog_name to blog object


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():     # [(blog_name, Blog), (blog_name, Blog)]
        # print(blog)   # neformatirano
        print('- {}'.format(blog))  # list of bulletpoints

def ask_create_blog():
    title = input("What is the blog title? ")
    author = input("Who is the author? ")
    # save user input in the blogs dic with the key [title];
    # if the key doesn't exist yet, it is created automatically
    blogs[title] = blog.Blog(title, author)

def ask_read_blog():
    title = input("Which blog title you want to read? ")
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    pass # ask title, ...


