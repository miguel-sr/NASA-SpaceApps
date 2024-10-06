import os
import google.generativeai as genai

key = os.environ['GEMINI_API_KEY']

genai.configure(api_key=key)

def consultar_ia(pergunta):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(pergunta)

    return response.text

if __name__ == "__main__":
    pergunta = input("Digite sua mensagem para o Gemini: ")
    resposta = consultar_ia(pergunta)
    print(f"Gemini: {resposta}")
