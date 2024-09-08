import canillita, beomju
import json

if __name__ == "__main__":
    edition = 1
    papelerito = canillita.Canillita(beomju.Beomju())
    headlines = {}
    HEADS = []
    with open("titulares.json", "r") as f:
        head_art = json.load(f)
        sort_by_headlines = sorted([(list(h.keys())[0],list(h.values())[0],) for h in head_art],key=lambda x:x[0])
        headlines = [x[0] for x in sort_by_headlines]
        articles = [y[1] for y in sort_by_headlines]
        # print(headlines)
        HEADS = ['-'.join(h.split(' ')[:10]).replace("'",'').replace('´','').replace(',','').replace('(','').replace(')','') for h in headlines]
        # print(HEADS)
    papelerito.make_articles_routes(path=f"e{edition}", headlines=HEADS)
    papelerito.make_pages(f"e{edition}", headlines, articles)
    papelerito.make_home_page(HEADS, edition)