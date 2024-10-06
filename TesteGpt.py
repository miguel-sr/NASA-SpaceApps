import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai

# key = os.environ['GEMINI_API_KEY']
genai.configure(api_key="")

app = Flask(__name__)

twilio_account_sid = ''
twilio_auth_token = ''
twilio_whatsapp_number = ''

client = Client(twilio_account_sid, twilio_auth_token)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # incoming_msg = request.values.get('Body', '')
    incoming_msg = request.form.get('Body')
    sender_number = request.form.get('From')

    response = MessagingResponse()
    ##response.message(consultar_ia(incoming_msg))
    from main import mostrar_output
    response.message(mostrar_output())
    ##msg.message("Dados transformados em uma tabela no formato png: ")
    # msg.media("https://github.com/miguel-sr/NASA-SpaceApps/blob/main/img.png")
    # resposta_ia = consultar_ia(incoming_msg)
    #
    # client.messages.create(
    #     from_=f'{twilio_whatsapp_number}',
    #     body=resposta_ia,
    #     to=sender_number
    # )

    return str(response)

@app.route('/')
def index():
    return "É isso aqui x 3!"

def consultar_ia(pergunta):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(pergunta)

    return response.text

# if __name__ == "__main__":
#     pergunta = input("Digite sua mensagem para o Gemini: ")
    ##if pergunta == "minha plantacao de tomate estragou, voce sabe o que pode ter sido?\n":
    # pergunta = pergunta + "plantas com mancha\nproblema aconteceu hoje\ntem chovido pouco com muito calor\nsem praga\ntenho usado fertilizante"
    # resposta = consultar_ia(pergunta)
    # print(f"Gemini: {resposta}")

if __name__ == '__main__':
    app.run(port=3000)
