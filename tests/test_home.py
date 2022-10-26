from page_objects.home_page import HomePage
import pytest

class HomeTest(HomePage):
    def test_task1(self):
        self.open_page()
        self.printer()