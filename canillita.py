import os
from beomju import Beomju
import shutil


class Canillita:

    def __init__(self, beomju):
        self.beomju = beomju
    
    def make_folders(self, path):
        os.makedirs(path, exist_ok=True)
        for beomju in sorted(self.beomju.categories)[:4]:
            beomju_path = os.path.join(path, beomju)
            os.makedirs(beomju_path, exist_ok=True)
            for cou in sorted(self.beomju.countries)[:4]:
                cou_path = os.path.join(beomju_path, cou)
                os.makedirs(cou_path, exist_ok=True)

    def rm_folders(self, path):
        shutil.rmtree(path)

    def make_page(self, path):
        pass

if __name__ == "__main__":
    papelerito = Canillita(Beomju())
    path = "test"
    # papelerito.make_folders(path)
    papelerito.rm_folders(path)