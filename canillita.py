import os
from beomju import Beomju
import shutil
from maker.make_article_page import make_article_page
from maker.make_home_page import make_home_page

class Canillita:

    def __init__(self, root = "press_release"):
        self.root = root

    def make_all_encompassing_routes(self, path, beomju):
        os.makedirs(path, exist_ok=True)
        for beomju in sorted(beomju.categories)[:4]:
            beomju_path = os.path.join(path, beomju)
            os.makedirs(beomju_path, exist_ok=True)
            for cou in sorted(self.beomju.countries)[:4]:
                cou_path = os.path.join(beomju_path, cou)
                os.makedirs(cou_path, exist_ok=True)

    def make_articles_routes(self, path, headlines):
        path = os.path.join(self.root, path)
        print("routes",path)
        os.makedirs(path, exist_ok=True)
        print(headlines)
        for h in headlines:
            print("proposed path",os.path.join(path, h))
            os.makedirs(os.path.join(path, h), exist_ok=True)

    def rm_folders(self):
        shutil.rmtree(self.root)

    def make_pages(self, path, headlines, articles, debug=False):
        assert len(headlines) == len(articles)
        path = os.path.join(self.root, path)
        if debug:
            for h, a in zip(headlines, articles):
                print(
                    sepp := "**" * 10 + "\n",
                    h,
                    sepp,
                    sepp2 := "^^^^^^" * 10 + "\n",
                    a,
                    sepp2,
                )
        for ha, folder in zip(
            sorted(zip(headlines, articles), key=lambda x: x[0]),
            sorted(os.listdir(path)),
        ):
            h, a = ha
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path):
                page_path = os.path.join(folder_path, "page.jsx")
                with open(page_path, "w") as file:
                    file.write(make_article_page(h, a))

    def make_home_page(self, HEADS, edition):
        path = os.path.join(self.root, "page.jsx")
        with open(path, "w") as f:
            f.write(make_home_page(HEADS, edition))

if __name__ == "__main__":
    papelerito = Canillita("press_release")
    path = "e1"
    headlines = ["h1", "h2", "h3"]
    papelerito.make_articles_routes(path, headlines=headlines)
    # papelerito.rm_folders(path)
