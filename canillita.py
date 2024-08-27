import os
from beomju import Beomju

class Canillita:

    def __init__(self, beomju):
        self.beomju = beomju

    def remove_dir(self, path):
        try:
            os.rmdir(path)
        except OSError as e:
            print(f"Error: {e}")
    
    def make_1wg_routes(self, path):
        for beomju in sorted(self.beomju.categories):
            print(beomju)
            for cou in sorted(self.beomju.countries):
                print('\t-'+cou)

Canillita(Beomju()).make_1wg_routes("test")