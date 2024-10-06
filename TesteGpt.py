import openai
from openai import models

def consultar_chatgpt(pergunta):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pergunta},
        ],
        temperature=1,
        max_tokens=200
    )
    return completion.choices[0].message['content']

if __name__ == "__main__":
    pergunta = input("Digite sua mensagem para o ChatGPT: ")
    resposta = consultar_chatgpt(pergunta)
    print(f"ChatGPT: {resposta}")
