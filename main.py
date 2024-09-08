import canillita, beomju
from hexagano import producir
import json
import sys


def shell_main():
    print("Calling Hexagano with edition: ", sys.argv[1])
    # Uncomment when in production
    # main(edition=sys.argv[1])


def main(edition=1):
    papelerito = canillita.Canillita("press_release")
    headlines = {}
    HEADS = []
    head_art = producir(edition)
    print(head_art)
    sort_by_headlines = sorted(
        [
            (
                list(h.keys())[0],
                list(h.values())[0],
            )
            for h in head_art
        ],
        key=lambda x: x[0],
    )
    # fmt: off
    headlines, articles = [x[0] for x in sort_by_headlines], [y[1] for y in sort_by_headlines]
    # fmt: on
    formatted_headlines = [
        "-".join(h.split(" ")[:10])
        .replace("'", "")
        .replace("´", "")
        .replace(",", "")
        .replace("(", "")
        .replace(")", "")
        for h in headlines
    ]
    path = f"e{edition}"
    papelerito.make_articles_routes(path=path, headlines=formatted_headlines)
    papelerito.make_pages(path=path, headlines=headlines, articles=articles)
    papelerito.make_home_page(formatted_headlines, edition)


if __name__ == "__main__":
    main(edition=1)
