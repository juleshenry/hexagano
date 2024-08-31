import escritor
import lector
import asyncio
import pprint

def parse_importante(response):
    prio = 1
    headlines = []
    for r in response.split("\n"):
        if r.startswith(f"{prio}. "):
            headlines.append(r.replace(f"{prio}. ", ""))
            prio += 1

    return headlines

def producir():
    hl_dicc = asyncio.run(
        lector.leer()
    )[0]['result']
    titulares = escritor.identifica_importante([entry['headline'] for entry in hl_dicc])
    articulos = [escritor.escribir_articulo(titular) for titular in titulares]
    return [(t,a,) for t,a in zip(titulares, articulos)]

if __name__ == "__main__":
    tit_art = producir()
    import pprint
    pprint.pprint(tit_art)