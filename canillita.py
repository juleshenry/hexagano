import os
from beomju import Beomju
import shutil
from make_article_page import make_article_page

class Canillita:

    def __init__(self, beomju):
        self.beomju = beomju
    
    def make_all_encompassing_routes(self, path):
        os.makedirs(path, exist_ok=True)
        for beomju in sorted(self.beomju.categories)[:4]:
            beomju_path = os.path.join(path, beomju)
            os.makedirs(beomju_path, exist_ok=True)
            for cou in sorted(self.beomju.countries)[:4]:
                cou_path = os.path.join(beomju_path, cou)
                os.makedirs(cou_path, exist_ok=True)
    
    def make_articles_routes(self, path, headlines):
        os.makedirs(path, exist_ok=True)
        for h in headlines:
            os.makedirs(os.path.join(path, h), exist_ok=True)

    def rm_folders(self, path):
        shutil.rmtree(path)

    def make_pages(self, path, headlines, articles):
        assert len(headlines) == len(articles)
        for h,a in zip(headlines, articles):
            print('**'*10)
            print(h)
            print('**'*10)
            print('^^^^^^'*10)
            print(a)
            print('^^^^^^'*10)
        sorted_ha = sorted(zip(headlines, articles), key=lambda x: x[0])
        for ha,folder in zip(sorted_ha, sorted(os.listdir(path))):
            # bug mismatches articles due to alphabeticazlication 
            h, a = ha
            print('>>>',h,'|||' ,folder)
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path):
                page_path = os.path.join(folder_path, "page.jsx")
                with open(page_path, "w") as file:
                    file.write(make_article_page(h, a))

if __name__ == "__main__":
    papelerito = Canillita(Beomju())
    path = "e1"
    headlines = ["h1", "h2", "h3"]
    papelerito.make_articles_routes(path, headlines=headlines)
    # papelerito.rm_folders(path)