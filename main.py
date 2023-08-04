from welcome import display_welcome_message
from weather import obter_localizacao_por_ip, obter_clima

if __name__ == "__main__":
    display_welcome_message()

    cidade_usuario = obter_localizacao_por_ip()
    print(f"Localização detectada: {cidade_usuario}")

    resposta_correta = input("Essa é a localização correta? (sim/não): ").lower()
    while resposta_correta != 'sim':
        cidade_usuario = input("Digite o nome da cidade correta: ")
        resposta_correta = input("Essa é a localização correta? (sim/não): ").lower()

    obter_clima(cidade_usuario)
