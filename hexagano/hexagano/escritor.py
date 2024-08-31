import ollama


def escribir_articulo(headline):
    response = ollama.chat(
        model="llama3:latest",
        messages=[
            {
                "role": "user",
                "content": f"""You are a reporter for One World Gazette, "What's Going Down on Planet Earth Right Now."™
            Your first assignment is to write a 250 word article on {headline}. Use all information, 
            historical context and global politics and your own knowledge to write a compelling article.
            """,
            },
        ],
    )
    # Parse response
    articulo_final = ""
    for line in response["message"]["content"].split('\n'):
        if '*'in line:
            continue
        else:
            articulo_final += line + "\n"
    return articulo_final


def identifica_importante(headlines):
    response = ollama.chat(
        model="llama3:latest",
        messages=[
            {
                "role": "user",
                "content": f"Order these headlines by most important {headlines}. Strictly use one list, ordinal 1,2,3",
            }
        ],
    )
    # Parse response
    i, importantes = 1, []
    for line in response["message"]["content"].split('\n'):
        if line.startswith(f"{i}. "):
            importantes.append(line.replace(f"{i}. ", "").replace('"', '').replace("'", ""))
            i += 1
    return importantes

