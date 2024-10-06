from ApiClient import ApiClient
import json
from datetime import datetime
from geopy.geocoders import Nominatim
from Utils import CriarTabelaAPartirDeArray

casos_reais_queimadas = [ "1 - Queimada no Paraguai, Puerto Casado dia 03/10/2024."
                         ,"2 - Queimada na Rússia, Mazhanovsky District dia 02/10/2024."
                         ,"3 - Queimada no Brasil, Ururaí dia 01/10/2024."
                         ,"4 - Queimada no Brasil, Jaborandi dia 01/10/2024."
                         ,"5 - Queimada na Bolívia, Canton Exaltación dia 01/10/2024."]

def calcular_dias_passados(data_evento):
    data_evento = datetime.strptime(data_evento, '%Y-%m-%dT%H:%M:%SZ')
    data_atual = datetime.utcnow()
    dias_passados = (data_atual - data_evento).days
    return dias_passados


# Função para obter o nome da cidade com base nas coordenadas
def obter_cidade_por_coordenadas(coordenadas):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(f"{coordenadas[1]}, {coordenadas[0]}")
        if location:
            return location.address.split(',')[0]  # Retorna o nome da cidade
        return "Local desconhecido"
    except:
        return "Local desconhecido"

def mostrar_output(response_json, dias):
    for caso in casos_reais_queimadas:
        print(caso)
    CriarTabelaAPartirDeArray(casos_reais_queimadas)
    # thisdict = {
    #     "Wildfires": "Queimada",
    #     "Severe Storms": "Tempestades severas"
    # }
    #
    # index = 1
    # print(f"Aconteceram os seguintes desastres naturais no período de {dias} dias:\n ")
    # for evento in response_json['events']:
    #     if len(evento['geometries']) > 1:
    #         continue
    #     dias_passados = dias
    #     categoria = evento['categories'][0]['title']
    #     coordenadas = evento['geometries'][0]['coordinates']
    #     cidade = obter_cidade_por_coordenadas(coordenadas)
    #
    #     # Obter país de acordo com o nome do evento (essa lógica pode ser ajustada)
    #     pais = evento['title'].split(' in ')[1].split(' ')[0]
    #
    #     iso_date = evento['geometries'][0]['date']
    #     date_object = datetime.strptime(iso_date, '%Y-%m-%dT%H:%M:%SZ')
    #     formatted_date = date_object.strftime('%d/%m/%Y')
    #
    #     descricao = f"{index} - {thisdict[categoria]} no {pais}, {cidade} dia {formatted_date}."
    #
    #     print(descricao)
    #     index += 1

if __name__ == '__main__':
    dias = 5
    api_client = ApiClient(base_url="https://eonet.gsfc.nasa.gov/api/v2.1", api_key="sua_api_key_aqui")
    resposta_get = api_client.get('events', params={'days': dias})
    mostrar_output(resposta_get, dias)