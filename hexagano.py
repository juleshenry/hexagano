import escritor
import lector
import asyncio

def parse_importante(response):
    prio = 1
    headlines = []
    for r in response.split("\n"):
        if r.startswith(f"{prio}. "):
            headlines.append(r.replace(f"{prio}. ", ""))
            prio += 1

    return headlines

def producir(edition):
    hl_dicc = asyncio.run(
        lector.leer(edition)
    )[0]['result']
    titulares = escritor.identifica_importante([entry['headline'] for entry in hl_dicc])
    articulos = [escritor.escribir_articulo(titular) for titular in titulares]
    return [{t:a} for t,a in zip(titulares, articulos)]

def export_as_json(produzed):
    import json
    with open("titulares.json", "w") as f:
        json.dump(produzed, f)
        
if __name__ == "__main__":
    tit_art = producir()
    export_as_json(tit_art)
    