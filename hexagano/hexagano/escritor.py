import ollama

def escribir_articulo(headline):
    response = ollama.chat(model='llama3:latest', messages=[
        {
            'role': 'user',
            'content': f'''You are a reporter for One World Gazette, "What's Going Down on Planet Earth Right Now."™
            Your first assignment is to write a 250 word article on {headline}. Use all information, 
            historical context and global politics and your own knowledge to write a compelling article.
            ''',
        },
    ])
    return response['message']['content']

