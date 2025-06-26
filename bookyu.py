import matplotlib.pyplot as plt


print('\nSeja Bem-Vinda ao Bookyu ^^')
nome = input('\nQual é o seu nome: ')
idade = int(input('\nQual é sua idade: '))
cidade = input('\nQual é a sua cidade: ')
estado = input('\nQual é o seu estado: ')

livros_dig = int(input('\nQuantos livros digitais você leu no ultimo ano: '))
livros_fis = int(input('\nQuantos livros fisicos você leu no ultimo ano: '))

while True:
    livro_prefer = ''
    escolha_prefer = input('\nQual é o seu formato preferido de leitura? Digite 1 = Fisico ou 2 = Digital: ')
    if escolha_prefer == '1':
        livro_prefer = 'Fisico'
        break
    elif escolha_prefer == '2':
        livro_prefer == 'Digital'
        break
    else:
        print('Opção invalida! Por favor selecione 1 ou 2!')

livros_study = int(input('\nQuantos livros você leu no ultimo ano por estudo: '))
livros_entertain = int(input('\nQuantos livros você leu no ultimo ano por entretenimento: '))

horas_study = int(input('\nQuantas horas por semana você dedica aos livros por estudo: '))
horas_entertain = int(input('\nQuantas horas por semana você dedica aos livros por entretenimento: '))

def mensagem():
    print(f'\n{nome} Seja muito bem vindo(a) ao Bookyu!!')
    dados = {
    # Regiao Norte
    "acre": "O Seringal - Miguel Jeronymo Ferrante",
    "amazonas": "Dois Irmãos - Milton Hatoum",
    "amapa": "Poemas do Homem do Cais - Alcy Araújo",
    "para": "Sumidouro - Olga Savary",
    "rondonia": "Cidade Morta - Otávio Afonso",
    "roraima": "Makunaimãtaani - Presente de Makunaimã - Kamuu Dan Wapichana",
    "tocantins": "Meu Primeiro Picolé - José Concesso",
    
    # Regiao Nordeste
    "alagoas": "Vidas Secas - Graciliano Ramos",
    "bahia": "Capitães da Areia - Jorge Amado",
    "ceara": "O Quinze - Rachel de Queiroz",
    "maranhao": "O Cortiço - Aluísio Azevedo",
    "paraiba": "O Auto da Compadecida - Ariano Suassuna",
    "pernambuco": "Morte e Vida Severina - João Cabral de Melo Neto",
    "piaui": "Os Últimos Dias de Paupéria - Torquato Neto",
    "rio_grande_do_norte": "Oiteiro: Memórias de uma sinhá-moça - Madalena Antunes",
    "sergipe": "Feijão de Cego - Vladimir Souza Carvalho",
    
    # Regiao Centro-Oeste
    "goias": "Poemas dos Becos de Goiás e Estórias - Cora Coralina",
    "mato_grosso": "Livro sobre Nada - Manoel de Barros",
    "mato_grosso_do_sul": "Jardim Fechado - Uma antologia poética - Raquel Naveira",
    "distrito_federal": "Faroeste Caboclo - Renato Russo",
    
    # Regiao Sudeste
    "espirito_santo": "50 Crônicas Escolhidas - Rubem Braga",
    "minas_gerais": "Grande Sertão: Veredas - João Guimarães Rosa",
    "rio_de_janeiro": "Dom Casmurro - Machado de Assis",
    "sao_paulo": "Macunaíma - Mário de Andrade",
    
    # Regiao Sul
    "parana": "O Vampiro de Curitiba - Dalton Trevisan",
    "rio_grande_do_sul": "O Tempo e o Vento - Érico Veríssimo",
    "santa_catarina": "Broquéis - Cruz e Sousa"}

    if estado in dados:
        print(f'Com base no seu estado {estado}, o Bookyu recomenda: {dados[estado]}')
    else:
        print('Houve um erro inesperado :(')


def mensagem_2(cidade):
    cidade_formatada = cidade.replace(" ", "+")
    maps_link = f'https://www.google.com/maps/search/livrarias+em+{cidade_formatada}'
    print(f'\nConfira algumas livrarias proximas de {cidade}: {maps_link}')



def estimativas():
    total_livros = livros_fis + livros_dig
    print(f'\n{nome} Você irá ler {total_livros * 5} livros em 5 anos, se continuar com a mesma frequência de leitura.')

    if livros_study >= 40:
        print(f'Você é um excelente leitor estudioso, se continuar no mesmo ritmo, você irá ler {livros_study * 5} livros de estudo em 5 anos. Parabens! Sua média de leitura é excelente! Continue assim.')
    elif livros_study >= 20:
        print(f'Você é um razoavel leitor estudioso, se continuar no mesmo ritmo, você irá ler {livros_study * 5} livros de estudo em 5 anos. Sua média de leitura é razoavel! Tente se desafiar a ser um excelente leitor, lendo 40 livros por ano!')
    elif livros_study >= 0:
        print(f'Você é um mal leitor estudioso, se continuar no mesmo ritmo, você irá ler apenas {livros_study * 5} livros de estudo em 5 anos. Sua média de leitura é baixa! Tente se desafiar a ler mais todos os dias, para ser um excelente leitor!')
    else:
        print('Ocorreu algum erro desconhecido :(')
        
    if livros_entertain >= 40:
        print(f'\nVocê é um excelente leitor de entretenimento, se continuar com a mesma frequencia, você irá ler {livros_entertain * 5} livros de entretenimento em 5 anos. Parabens! Sua média de leitura é excelente! Continue assim <3')
    elif livros_entertain >= 20:
        print(f'\nVocê é um razoavel leitor de entretenimento, se continuar com a mesma frequencia, você irá ler {livros_entertain * 5} livros de entretenimento em 5 anos. Sua média de leitura é razoavel! Tente se desafiar a ser um excelente leitor, lendo 40 livros por ano!')
    elif livros_entertain >= 0:
        print(f'\nVocê é um mal leitor de entretenimento, se continuar com a mesma frequencia, você irá ler apenas {livros_entertain * 5} livros de entretenimento em 5 anos. Sua média de leitura é baixa! Tente se desafiar a ler mais todos os dias, para ser um excelente leitor!')
    else:
        print('Ocorreu algum erro desconhecido :(')



def horas_ano():
    print(f"\nVocê se dedica aproximadamente: {horas_study * 52} horas de estudos por ano e {horas_entertain * 52} horas de leituras por entretenimento por ano!")



def grafico_meta():
    meta = int(input('\nQuantos livros você planeja ler neste ano: '))
    atual = int(input('\nQuantos livros você ja leu neste ano: '))
    progresso = atual / meta * 100
    restante = 100 - progresso

    plt.pie([progresso, restante], labels=['Livros Lidos', 'Livros Não Lidos'], autopct='%1.1f%%', startangle=90, colors=['purple', 'lightgray'])
    plt.title("Meta Anual de Leitura")
    plt.axis('equal')
    plt.show()


def desafio_leitura():
    if livros_dig + livros_fis < 15:
        print('\nDesafio Bookyu! Tente ler 1 livro por mês este ano, uma dica é começar por livros pequenos que abordam temas que você gosta :)')
    elif livros_dig + livros_fis < 30:
        print('\nDesafio Bookyu! Tente ler 2 livros por mês este ano, você consegue! :)')
    else:
        print('\nDesafio Bookyu! Experimente explorar um livro de um gênero novo!')


mensagem()
horas_ano()
mensagem_2(cidade)
estimativas()
desafio_leitura()
grafico_meta()