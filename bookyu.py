import matplotlib.pyplot as plt
import tkinter as tk
import webbrowser
import io
import contextlib

print('\nSeja Bem-Vindo(a) ao Bookyu ^^')
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
        livro_prefer = 'Digital'
        break
    else:
        print('Opção invalida! Por favor selecione 1 ou 2!')

livros_study = int(input('\nQuantos livros você leu no ultimo ano por estudo: '))
livros_entertain = int(input('\nQuantos livros você leu no ultimo ano por entretenimento: '))

horas_study = int(input('\nQuantas horas por semana você dedica aos livros por estudo: '))
horas_entertain = int(input('\nQuantas horas por semana você dedica aos livros por entretenimento: '))

def mensagem():
    print(f'\n{nome.capitalize()} seja muito bem vindo(a) ao Bookyu!!')
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

    estado_formatado = estado.lower().replace(' ', '_')
    if estado_formatado in dados:
        print(f'Com base no seu estado {estado}, o Bookyu recomenda: {dados[estado_formatado]}')
    else:
        print('Houve um erro inesperado :(')


def mensagem_2(cidade):
    cidade_formatada = cidade.replace(" ", "+")
    maps_link = f'https://www.google.com/maps/search/livrarias+em+{cidade_formatada}'
    print(f'\nConfira algumas livrarias proximas de {cidade}: {maps_link}')



def estimativas():
    total_livros = livros_fis + livros_dig
    print(f'\n{nome.capitalize()}, se você mantiver essa frequência de leitura, irá ler {total_livros * 5} livros nos próximos 5 anos!')

    if livros_study >= 40:
        print(f'\n**Parabéns! Você é um(a) leitor(a) dedicado(a) aos estudos!** Com esse ritmo, você lerá aproximadamente {livros_study * 5} livros de estudo em 5 anos. \nSua média é excelente! Continue explorando e aprendendo!')
    elif livros_study >= 20:
        print(f'\nVocê tem um bom ritmo de leitura para estudos! Ao continuar assim, você lerá cerca de {livros_study * 5} livros de estudo em 5 anos. \nQue tal um pequeno desafio para se tornar um(a) leitor(a) ainda mais voraz? Tente alcançar 40 livros por ano!')
    elif livros_study >= 0:
        print(f'\nSua jornada de leitura para estudos está apenas começando! Se continuar nesse ritmo, você lerá cerca de {livros_study * 5} livros de estudo em 5 anos. \nCada página conta! Que tal definir uma meta para ler um pouco mais a cada dia e descobrir o quanto você pode aprender?')

        
    if livros_entertain >= 40:
        print(f'\n**Excelente! Você é um(a) leitor(a) de entretenimento superengajado(a)!** Mantendo essa frequência, você desfrutará de {livros_entertain * 5} livros de entretenimento em 5 anos. \nQue maravilha! Continue se divertindo e explorando novas histórias!')
    elif livros_entertain >= 20:
        print(f'\nVocê tem um bom hábito de leitura para entretenimento! Se mantiver o ritmo, lerá aproximadamente {livros_entertain * 5} livros de entretenimento em 5 anos. \nPara turbinar ainda mais sua leitura, que tal se desafiar a descobrir 40 livros novos por ano?')
    elif livros_entertain >= 0:
        print(f'\nPara suas leituras de entretenimento, se continuar nesse ritmo, você lerá cerca de {livros_entertain * 5} livros em 5 anos. \nLembre-se, o importante é começar! Pequenas leituras diárias podem te levar a grandes aventuras. Que tal explorar um novo gênero?')
    else:
        print('Ocorreu algum erro desconhecido :(')



def horas_ano():
    print(f"\nVocê se dedica aproximadamente: {horas_study * 52} horas de estudos por ano e {horas_entertain * 52} horas de leituras de entretenimento por ano!")



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
        print('\nDesafio Bookyu! Experimente explorar um livro de um gênero novo! ')



def capturar_saida(func):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        func()
    return buffer.getvalue()

def mostrar_janela():

    saida_mensagem = capturar_saida(mensagem)
    saida_horas = capturar_saida(horas_ano)
    saida_estimativas = capturar_saida(estimativas)
    saida_desafio = capturar_saida(desafio_leitura)


    cidade_formatada = cidade.replace(" ", "+")
    link_maps = f'https://www.google.com/maps/search/livrarias+em+{cidade_formatada}'

    def abrir_link(event):
        webbrowser.open_new(link_maps)


    root = tk.Tk()
    root.title("Resumo Bookyu")

    texto_total = (
        saida_mensagem +
        saida_horas +
        saida_estimativas +
        saida_desafio
    )

    label = tk.Label(root, text=texto_total, justify="left", wraplength=500)
    label.pack(padx=10, pady=10)

    link_label = tk.Label(root, text=f"Livrarias próximas de {cidade}", fg="blue", cursor="hand2")
    link_label.pack()
    link_label.bind("<Button-1>", abrir_link)

    tk.Button(root, text="Fechar", command=root.destroy).pack(pady=10)
    root.mainloop()


mostrar_janela()
grafico_meta()