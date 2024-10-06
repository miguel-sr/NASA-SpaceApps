import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai

key = os.environ['GEMINI_API_KEY']

genai.configure(api_key=key)

app = Flask(__name__)

twilio_account_sid = ''
twilio_auth_token = ''
twilio_whatsapp_number = ''

client = Client(twilio_account_sid, twilio_auth_token)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body')
    sender_number = request.form.get('From')

    response = MessagingResponse()
    response.message(f'Sua mensagem foi recebida: {incoming_msg}')

    resposta_ia = consultar_ia(incoming_msg)

    client.messages.create(
        from_=f'whatsapp:{twilio_whatsapp_number}',
        body=resposta_ia,
        to=sender_number
    )

    return str(response)

def consultar_ia(pergunta):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(pergunta)

    return response.text

if __name__ == '__main__':
    app.run(port=3000)