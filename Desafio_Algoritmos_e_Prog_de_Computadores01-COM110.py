dados = []

# Variável para marcar uma alteração na dados
alterada = False

tipos_de_notas = ["algoritmos" ,"calculo1", "introducao"]


def pede_nome(padrão=""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return(nome)

def pede_disciplina(padrão=""):
    disciplina = input("Nota: ")
    if disciplina == "":
        disciplina = padrão
    return disciplina

def pede_tipo_disciplina(padrão=""):
    while True:
        tipo = input("Disciplina: [%s]: " % ",".join(tipos_de_notas)).lower()
        if tipo == "":
            tipo = padrão
        for t in tipos_de_notas:
            if t.startswith(tipo):
                return t # Retorna o nome completo
        else:
            print("Tipo de disciplina inválido!")

def pede_rg(padrão=""):
    rg = input("RG: ")
    if rg == "":
        rg = padrão
    return(rg)

def pede_aniversário(padrão=""):
    aniversário = input("Data de aniversário: ")
    if aniversário == "":
        aniversário = padrão
    return(aniversário)


def mostra_dados(nome, disciplinas, rg, aniversário):
    print("Nome: %s" % nome.capitalize())
    print("RG: %s\nAniversário: %s\n" % (rg, aniversário))
    print("disciplina(s):")
    for disciplina in disciplinas:
        print("\tNota: %15s Disciplina: %s" % (disciplina[0], disciplina[1].capitalize()))

def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(dados):
         if e[0].lower() == mnome:
               return p
     return None

def novo():
     global dados, alterada
     nome = pede_nome()
     if pesquisa(nome) != None:
        print("Nome já existe!")
        return
     rg = pede_rg()
     aniversário = pede_aniversário()
     disciplinas = []
     while True:
        numero = pede_disciplina()
        tipo = pede_tipo_disciplina()
        disciplinas.append( [numero, tipo] )
        if confirma("que deseja cadastrar outra disciplina") == "N":
            break
     dados.append([nome, disciplinas, rg, aniversário])
     alterada = True

def confirma(operação):
    while True:
        opção = input("Confirma %s (S/N)? " % operação).upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
     global dados, alterada
     nome = pede_nome()
     p = pesquisa(nome)
     if p != None:
        if confirma("apagamento") == "S":
            del dados[p]
            alterada = True
     else:
         print("Nome não encontrado.")

def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p != None:
        nome, disciplinas, rg, aniversário = dados[p]
        print("Encontrado:")
        mostra_dados(nome, disciplinas, rg, aniversário)
        nome = pede_nome(nome) # Se nada for digitado, mantém o valor
        rg = pede_rg(rg)
        aniversário = pede_aniversário(aniversário)        
        for disciplina in disciplinas:
            numero, tipo = disciplina
            disciplina[0] = pede_disciplina(numero)
            disciplina[1] = pede_tipo_disciplina(tipo)
        if confirma("alteração") == "S":
            dados[p] = [nome, disciplinas, rg, aniversário]
            alterada = True
    else:
        print("Nome não encontrado.")

def lista():
     print("\ndados\n\n------")
     # Usamos a função enumerate para obter a posição na dados
     for posição, e in enumerate(dados):
         # Imprimimos a posição
         print("\nPosição: %d" % posição)
         mostra_dados(e[0], e[1], e[2], e[3])
     print("------\n")


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                   return(valor)
        except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista   

   0 - Sai
""")
     print("\nNomes na dados: %d Alterada: %s\n" % (len(dados), alterada))
     return valida_faixa_inteiro("Escolha uma opção: ",0,5)


while True:
     opção = menu()
     if opção == 0:
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         altera()
     elif opção == 3:
         apaga()
     elif opção == 4:
         lista()
         
