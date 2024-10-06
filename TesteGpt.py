import os
import google.generativeai as genai

# key = os.environ['GEMINI_API_KEY']
key = "AIzaSyAzI8GSjCuiKpGdRSLuA-OyDAUQckGTZPo"
genai.configure(api_key=key)

def consultar_ia(pergunta):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(pergunta)

    return response.text

if __name__ == "__main__":
    pergunta = input("Digite sua mensagem para o Gemini: ")
    ##if pergunta == "minha plantacao de tomate estragou, voce sabe o que pode ter sido?\n":
    pergunta = pergunta + "plantas com mancha\nproblema aconteceu hoje\ntem chovido pouco com muito calor\nsem praga\ntenho usado fertilizante"
    resposta = consultar_ia(pergunta)
    print(f"Gemini: {resposta}")
