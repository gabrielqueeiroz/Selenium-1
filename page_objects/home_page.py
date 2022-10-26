from seleniumbase import BaseCase

class HomePage(BaseCase):
    tab_to_demo = "/html/body/header[1]/div/nav/div/ul/li[5]/a"
    demo = "/html/body/header[1]/div/nav/div/ul/li[5]/ul/li[2]/a"
    lock_components = "/html/body/section/div/div[2]/div[2]/div[5]/div[2]/div/div/div[2]/table/tbody/tr[34]/td[1]/span/div"
    
    def open_page(self):
        self.open("https://www.discourse.org/")

    def printer(self):
        self.click(self.tab_to_demo)
        self.click(self.demo)
        self.scroll_to_bottom()
        elements = self.find_elements(self.lock_components)
        print(elements)
        for element in elements:
            print(element.text)
        
