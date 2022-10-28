from page_objects.home_page import HomePage
from page_objects.blog_page import BlogPage

class HomeTest(HomePage, BlogPage):
    def test_task2(self):
        self.open_page()
        self.access_blog()
        self.get_elements()
        self.show()