from Banco import *

pc = Pc()
personagem = Personagem()
possuiHab = PossuiHab()
lc=Local()
instanciaItem = Instanciaitem()
inventario = Inventario()

def CarregarJogo():
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.getPC(Save)
    return jogador[0]

def EncontrarSalas(pos, Id):
    Quadrado=2
    Oeste=lc.getLocal(pos-1)
    Norte=lc.getLocal(pos-Quadrado)
    Leste=lc.getLocal(pos+1)
    Sul=lc.getLocal(pos+Quadrado)
    salas_disponiveis = []

    print("\033[1;32mSuas opções de viajem são:\033[0m\n")

    if Oeste is not None and ((pos)%Quadrado):
        print(f"\033[0;36mOeste = {Oeste[0][2]} / Cordenada {Oeste[0][0]}\033[0m\n")
        salas_disponiveis.append(Oeste[0][0])

    if Norte is not None:
        print(f"\033[0;36mNorte = {Norte[0][2]} / Cordenada {Norte[0][0]}\033[0m\n")
        salas_disponiveis.append(Norte[0][0])

    if Leste is not None and (((pos+1)%Quadrado) != 0):
        print(f"\033[0;36mLeste = {Leste[0][2]} / Cordenada {Leste[0][0]}\033[0m\n")
        salas_disponiveis.append(Leste[0][0])

    if Sul is not None:
        print(f"\033[0;36mSul = {Sul[0][2]} / Cordenada {Sul[0][0]}\033[0m\n")
        salas_disponiveis.append(Sul[0][0])

    mudar=int(input("\033[1;32mPara qual sala deseja viajar? Digite -1 para Sair: \033[0m"))

    for i in salas_disponiveis:
        if(i==mudar):
            print("")
            pc.updatePcLocal(Id, mudar)


        
def inserirInventarioPersonagem(pcID):
    IDinv+=1
    inventario.inserirInventario(IDinv,1,pcID)    

def ListarHabilidadePersonagem(pcID):    
    habilidade = possuiHab.consultarPossuiHabPersonagem(pcID)
    tuplasHabilidade =[f"|Habilidades que possui\n|Nome Habilidade:| {y[1]}\n\n" for y in habilidade]
    for x in tuplasHabilidade:
        print(x)       
    
def definirHabilidadePersonagem(pcEspecie,pcID):
    possuiHab = PossuiHab()       
    match pcEspecie:
        case 'Humano':
            possuiHab.inserirPossuiHab(pcID,1)
        
        case 'Povo fogo':
            possuiHab.inserirPossuiHab(pcID,2)
        
        case 'Povo crystal':
            possuiHab.inserirPossuiHab(pcID,3)
                
        case 'Vampiro':
            possuiHab.inserirPossuiHab(pcID,4)
    
def deletarJogador(pcID):
    criarPC = Pc()
    criarPC.deletarPC(pcID)
    
def verJogadorOp(NomedoJogador,pcID):
    jogador = pc.consultarPCNome(NomedoJogador)
    tuplas = [f"|Caracteristicas personagem\n| ID:{x[0]} | Nome: {x[1]} | LVL:{x[4]}| Especie:{x[6]}|\n\n" for x in jogador]
    for y in tuplas:
        print(y)
    ListarHabilidadePersonagem(pcID)
    menuJogador()
            
def atualizarJogador(pcID,pcNome):
    pc.updatePc(pcID,pcNome)
    menuJogador()

def criarJogador(pcID,pcNome,pcEspecie):
    criarPC = Pc()
    personagem.criarPersonagem(pcID, True) 
    criarPC.criarPc(pcID,pcNome,0,100,0,0,pcEspecie,5,0,0)
    definirHabilidadePersonagem(pcEspecie, pcID)
    inserirInventarioPersonagem(pcID)
    menuJogador()

def menuJogador():
    print("\033[1;32m Opções de Jogador")
    print("\033[0;36m|1| = Criar personagem")
    print("|2| = Ver jogador")
    print("|3| = Atualizar jogador")
    print("|4| = Deletar jogador")
    print("|5| = Voltar\n")
    
    OpçaoJogador = input()            
    
    match OpçaoJogador:
        case '1':
            pcID = input("ID do jogador :")
            pcNome = input("Nome do jogador :")
            pcEspecie = input("|Especies: |\n|Humano|\n|Povo Fogo|\n|Povo crystal|\n|Vampiro|:\n")
            criarJogador(pcID,pcNome,pcEspecie)
        case '2':
            pcID = input("ID do jogador :")
            NomedoJogador = input("Digite o Nome do jogador(es) que busca:")
            verJogadorOp(NomedoJogador,pcID)                
        case '3':
            NomedoJogador = input("Digite seu Nome")
            pcID = input("ID do jogador que você deseja atualizar o Nome:")
            pcNome = input("Novo Nome do jogador :")
            atualizarJogador(NomedoJogador,pcID,pcNome)
        case '4':
            pcID = input("ID do jogador que deseja deletar :")
            deletarJogador(pcID)
