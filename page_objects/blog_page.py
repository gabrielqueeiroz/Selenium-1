from seleniumbase import BaseCase

class BlogPage(BaseCase):
    last_element = "/html/body/div[2]/footer/div[2]/div/div/div/div/div"
    access_to_second_page = "/html/body/div[2]/div/div/div/div/nav/div/a[5]"
    articles = "/html/body/div[2]/div/div"
    publications = []
    content = {}
    address = ".onde > p:nth-child(2)"

    def get_to_second_page(self):
        print(self.find_elements(self.address)[0].text)
       
    def organizator(self, operator):
        if operator == 0:
            return "mes"
        elif operator == 1:
            return "dia"
        elif operator == 2:
            return "ano"
        elif operator == 3:
            return "titulo"
        elif operator == 4:
            return "autor"
        elif operator == 5:
            return "descricao1"
        elif operator == 6:
            return "descricao2"
        elif operator == 7:
            return None

    def get_elements(self):
        self.school_address = self.find_element(self.address).text.split("\n")

        elements = self.find_elements(self.articles)[0].text.split("\n")
      
        for line in range(len(elements) - 2):
            component = self.organizator(line % 8)
            if component != None:
                self.content[component] = elements[line]
            else:
                self.publications.append(self.content)
                self.content = {}
        
    def show(self):
        print(f"Título do segundo post: {self.publications[1]['titulo']}")
        print(f"Data do segundo post: {self.publications[1]['dia']}/{self.publications[1]['mes']}/{self.publications[1]['ano']}")
        print(f"Título do terceito post: {self.publications[2]['titulo']}")
        print(f"Autor do terceito post: {self.publications[2]['autor']}")
        print(f"Endereço do School: {self.school_address[0]}")
