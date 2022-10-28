from seleniumbase import BaseCase

class HomePage(BaseCase):
    access_to_blog = "/html/body/div[2]/footer/div[1]/div/div/div/div[2]/div[1]/nav/ul/li[6]/a"
    
    def open_page(self):
        self.open("https://www.cesar.school/")

    def access_blog(self):
        self.click(self.access_to_blog)
        
