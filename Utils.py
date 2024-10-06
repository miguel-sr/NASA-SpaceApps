import pandas as pd
import matplotlib.pyplot as plt

casos_reais_queimadas = [ "1 - Queimada no Paraguai, Puerto Casado dia 03/10/2024."
                         ,"2 - Queimada na Rússia, Mazhanovsky District dia 02/10/2024."
                         ,"3 - Queimada no Brasil, Ururaí dia 01/10/2024."
                         ,"4 - Queimada no Brasil, Jaborandi dia 01/10/2024."
                         ,"5 - Queimada na Bolívia, Canton Exaltación dia 01/10/2024."]
def CriarTabelaAPartirDeArray(array):
    # Exemplo de dados em um array
    data = [
        ['Tipo do Desastre', 'País', 'Cidade', 'Data do Ocorrido'],
        ['Queimada', "Paraguai", 'Puerto Casado', "03/10/2024"],
        ['Queimada', "Rússia", 'Mazhanovsky District', "02/10/2024"],
        ['Queimada', "Brasil", 'Ururaí', "01/10/2024"],
        ['Queimada', "Brasil", 'Jaborandi', "01/10/2024"],
        ['Queimada', "Bolívia", 'Canton Exaltación', "01/10/2024"]
    ]

    # Criando um DataFrame a partir do array
    df = pd.DataFrame(data[1:], columns=data[0])  # Usa a primeira linha como cabeçalho

    # Criando uma figura e um eixo
    fig, ax = plt.subplots()

    # Removendo os eixos
    ax.axis('tight')
    ax.axis('off')

    # Criando a tabela
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc = 'center', loc='center')

    # Ajustando a tabela
    table.auto_set_font_size(False)  # Não ajustar automaticamente o tamanho da fonte
    table.set_fontsize(14)  # Definindo um tamanho de fonte fixo
    table.scale(1.2, 1.2)  # Ajustando a escala da tabela

    for (i, j), cell in table.get_celld().items():
        if i == 0:  # Cabeçalho
            cell.set_facecolor('green')  # Verde para o cabeçalho
            cell.set_text_props(color='white')  # Texto branco no cabeçalho
        else:  # Linhas de dados
            if i % 2 == 0:  # Linhas pares
                cell.set_facecolor('lightblue')  # Azul claro para linhas pares
            else:  # Linhas ímpares
                cell.set_facecolor('lightgray')  # Cinza claro para linhas ímpares
           ## cell.set_text_props(color='white')  # Texto branco

    # Salvando a imagem da tabela
    plt.savefig('tabela.png', bbox_inches='tight')  # Salva a imagem no formato PNG
    plt.show()  # Exibe a tabela