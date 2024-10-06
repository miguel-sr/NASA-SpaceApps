import os

import openai
from flask import Flask, request
from pyexpat.errors import messages
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import geocoder

app = Flask(__name__)

openai.api_key = os.environ['OPENAI_API_KEY']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_whatsapp_number = os.environ['TWILIO_WHATSAPP_NUMBER']

client = Client(twilio_account_sid, twilio_auth_token)

historico = []

dadosIniciaisNaoForamAdicionados = True

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()

    resposta_ia = consultar_ia(incoming_msg)

    response.message(resposta_ia)

    return str(response)

@app.route('/')
def index():
    return "Ping Pong!"

def consultar_ia(pergunta):
    global dadosIniciaisNaoForamAdicionados
    g = geocoder.ip('me')

    if dadosIniciaisNaoForamAdicionados:
        historico.extend([
            {"role": "system", "content": "Você um assistente de agricultura"},
            {"role": "assistant", "content": f"Segue localização da requisição: {g.current_result.address}. Você não pode exceder o limite de 1400 caracteres na resposta!"}
        ])
        dadosIniciaisNaoForamAdicionados = False

    historico.append({"role": "user", "content": pergunta})

    completion = openai.chat.completions.create(
        model="gpt-4o",
        messages=historico,
    )

    retorno = completion.choices[0].message.content

    # if len(retorno) > 1599:
    #     completion = openai.chat.completions.create(
    #         model="gpt-3.5-turbo",
    #         messages=[
    #             {"role": "system", "content": "Você um assistente de agricultura"},
    #             {"role": "user", "content": f"Resuma o texto para que tenha no máximo 1500 caracteres: {retorno}"}
    #         ],
    #     )
    #
    #     retorno = completion.choices[0].message.content

    if len(retorno) > 1599:
        retorno = retorno[0, 1559]

    historico.append({"role": "system", "content": retorno})

    return retorno

if __name__ == '__main__':
    app.run(port=3000)
