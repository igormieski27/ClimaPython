import requests

def obter_localizacao_por_ip():
    url = 'https://ipinfo.io/json'
    response = requests.get(url)
    data = response.json()
    cidade = data.get('city', '')
    return cidade

def obter_clima(cidade):
    api_key = 'SUA_CHAVE_DE_API'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}'

    response = requests.get(url)
    dados = response.json()

    if dados['cod'] == 200:
        descricao_clima = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']

        print(f"Clima em {cidade}: {descricao_clima}")
        print(f"Temperatura: {temperatura} K")
        print(f"Umidade: {umidade}%")
    else:
        print(f"Erro: {dados['message']}")
