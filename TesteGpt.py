import os

import openai
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import geocoder
from Utils import obter_cidade_por_coordenadas

app = Flask(__name__)

openai.api_key = os.environ['OPENAI_API_KEY']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_whatsapp_number = os.environ['TWILIO_WHATSAPP_NUMBER']

client = Client(twilio_account_sid, twilio_auth_token)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()

    resposta_ia = consultar_ia(incoming_msg)

    response.message(resposta_ia)

    # from main import mostrar_output
    # response.message(mostrar_output())

    #msg.message("Dados transformados em uma tabela no formato png: ")
    # msg.media("https://github.com/miguel-sr/NASA-SpaceApps/blob/main/img.png")

    return str(response)

@app.route('/')
def index():
    return "Ping Pong!"

def consultar_ia(pergunta):
    g = geocoder.ip('me')

    completion = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pergunta},
            {"role": "assistant", "content": f"Segue localização da requisição: {g.current_result.address}. Resuma o máximo possível, não excendo o limite de 1500 caracteres."}
        ]
    )

    return completion.choices[0].message.content

if __name__ == '__main__':
    app.run(port=3000)
