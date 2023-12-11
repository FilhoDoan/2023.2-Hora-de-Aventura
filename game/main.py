from Banco import * 
import game
from battle import *

personagem = Personagem()
pc = Pc()
lc=Local()

print_rapido("\033[31m            ⠀⠀⠀⠀⠀⠀⠀⠰⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n")
print_rapido("            ⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n")
print_rapido("            ⠀⠀⠀⠀⠀⢀⣀⣼⣿⣀⣹⣿⡆⠀⢤⡄⢤⣄⢤⡤⠀⢤⣤⣤⣤⣤⢤⣄⠀⢤⣤⡤⣤⣤⣤⢠⡄⠀⣤⢤⡤⢤⡠⣤⠤⣴⠀⠀⠀⠀     \n")
print_rapido("            ⠀⠀⠀⠀⠀⠈⢹⣿⡇⠉⠉⢿⣿⡄⢸⡇⠀⢹⡏⢿⣠⡟⢹⣿⠤⠄⢸⡿⣷⣼⡇⠀⣿⡇⠀⢸⡇⠀⡇⢸⡇⣎⠀⣿⠶⠌⠀⠀⠀⠀     \n")
print_rapido("            ⠀⠀⠀⠀⠀⡴⠾⠿⠀⠀⠀⠘⠿⠿⠾⠿⠴⠛⠁⠘⠏⠀⠼⠿⠦⠖⠸⠃⠀⠙⠇⠀⠿⠇⠀⠘⠷⠚⠇⠾⠇⠘⠿⠿⠶⠶⠀⠀⠀      \n") 
print_rapido("            ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⢠⣤⡤⠀⢲⣶⣶⡄⠀⠀⠀⣰⣶⣶⠖⠀⢲⣶⣶⠶⠶⢶⣶⠀⠀⠀⠀     \n") 
print_rapido("            ⢀⣀⠀⠀⠀⠀⠀⢀⣸⣿⣉⣀⠀⢟⡉⠉⡉⣿⣿⢉⣉⣙⣛⣘⣿⣇⣀⡀⣿⢿⣿⡄⠀⣼⡿⣿⣿⢠⣤⣬⣭⣭⣤⣤⣤⣬⣤⣤⣀⠀     \n")
print_rapido("            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⢇⣿⠰⠻⣿⣾⡿⠵⣿⣿⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠁     \n")
print_rapido("            ⠀⠀⠀⠀⠀⠀⠀⠉⢹⣿⣍⠁⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢰⣶⡆⠀⣼⣿⡆⠀⠹⡿⠁⠀⣿⣿⡀⠀⣸⣿⣿⣤⣤⣤⣤⡆⠀⠀⠀     \n")
print_rapido("            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠉⠀⠀⠀⠀⠀⠴⠟⠛⠂⠀⠀⠀⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠻⠋⠀        \033[0m\n")
print_rapido("                                                                                \n")
print_rapido("          ⣠⣴⠶⢶⣦⡀                                                              \n")
print_rapido("         ⣰⡟⠁⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀\033[93;1m⢀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m\n")
print_rapido("      ⠀⠀⢀⡟⠀⠀⠀⠀⠀⣿⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⣼⠋⠀⠀⠈⢻⡆\033[93;1m⠀⠀⢀⣠⣴⡶⠿⠛⠋⠉⠉⠉⠉⠉⠉⠉⠙⠛⠲⢤⣀⠀⠀⠀⠀⠀   \033[0m\n")
print_rapido("      ⠀⠀⣸⠁⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠳⢦⣼⠇⠀⠀⠀⠀⠈⣇\033[93;1m⣠⣶⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀   \033[0m\n")
print_rapido("      ⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀\033[93;1m⢠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠴⠶⠶⣶⣤⡀⠀⠀⠀⠀⠀⠙⢦⠀   \033[0m\n")
print_rapido("      ⠀⣼⠁⠀⠀⠀⠀⠀⢀⣀⡠⠤⠤⠤⠤⠤⠤⠄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[93;1m⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⠀⠀⠈⢻⣿⡄⠀⠀⠀⠀⠀⠈⣧   \033[0m\n")
print_rapido("      ⢠⡿⠀⠀⠀⢀⡴⠊⠉⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠈⠉⠒⢤⡀⠀⠀⠀⠀\033[93;1m⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠠⣀⡀⠀⣠⡿   \033[0m\n")
print_rapido("      ⣸⡇⠀⠀⢠⠋⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀\033[93;1m⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣀⠀⠀⢀⣠⣾⠟⠀⠀⠀⠘⣿⣿⠋⠀   \033[0m\n")
print_rapido("      ⣿⠇⠀⠀⡇⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠇⠀⠀⠘⡄3\033[93;1m⢀⡇⠠⠒⠉⠙⠛⣶⣄⠀⣠⠤⠒⠒⠚⠚⠛⠿⢿⡛⠋⠁⠀⠀⠀⠀⠀⠘⣿⡇⠀   \033[0m\n")
print_rapido("      ⣿⠀⠀⠀⡇⠀⠀⠀⠀⢀⣿⣿⡏⠂⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱\033[93;1m⠘⡇⠁⠀⠀⠀⠀⠈⣿⠋⠀⠀⢀⣀⣀⡀⠀⠀⠀⠈⠒⢄⠀⠀⠀⠀⠀⠀⣹⡇⠀   \033[0m\n")
print_rapido("      ⣿⠀⠀⠀⠘⡄⠀⠀⠀⠀⢿⣿⡿⢿⣿⣿⣄⣈⣯⣉⣉⡇⠀⠀⠀⠀⡜⠀\033[93;1m⠇⢆⠀⠀⠀⠀⣰⠇⠀⢀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢀⣿⠁⠀   \033[0m\n")
print_rapido("      ⢹⣇⠀⠀⠀⠈⠢⣄⠀⠀⠈⠻⣦⣀⠀⠈⠉⠻⣿⣿⡿⠁⠀⠀⠀⡰⠁⠀\033[93;1m⠘⡀⠑⠒⠒⠚⢻⠀⠀⠈⠛⡟⠛⠉⢀⠽⣦⣀⣀⣀⡠⠃⠀⠀⠀⢀⣾⠇⠀⠀   \033[0m\n")
print_rapido("      ⠀⢻⣦⠀⠀⠀⠀⠀⠙⠲⠤⣀⡀⠉⠛⠛⠛⠛⠉⠁⠀⢀⣠⠴⠊⠀⠀⠀⠀\033[93;1m⢱⡄⠀⠀⠀⠘⡀⠀⠀⠀⣿⣤⣦⡼⠊⠉⡹⠁⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀   \033[0m\n")
print_rapido("      ⠀⠀⠙⢷⣦⣀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠒⠒⠒⠒⠚⠉⠁⠀⠀⠀⠀⠀⠀⡠⠋\033[93;1m⠙⢦⡀⠀⠀⠐⠠⠀⠔⠁⠈⠛⠣⠄⠚⠁⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀⠀⠀   \033[0m\n")
print_rapido("      ⠀⠀⠀⠀⠉⠛⠿⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⠋⠀⠀⠀⠀\033[93;1m⠙⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀   \033[0m\n")
print_rapido("      ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠻⠷⠶⠶⠶⠶⠶⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[93;1m⠉⠛⠻⠷⠶⠶⠶⠶⠿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \033[0m\n")
print_rapido("                                                                   \n")
print_rapido("                             A aventura vai começar                \n")
print_rapido("                             Todos juntos vamos                    \n")
print_rapido("                             Visitar                               \n")
print_rapido("                             O mundo de Jake e seu amigo Finn      \n")
print_rapido("                             Diversão é aqui!                      \n")
print_rapido("                             Hora de aventura!                     \n")
    
while(True):
    print("\n\033[1;32m| Bem-vindo ao MUD Hora de Aventura |\033[0m\n")
    print("\033[0;36m|1| = Acessar Menu")
    print("|2| = Carregar Jogo")
    print("|3| = Fechar jogo\n")        
    print("\033[1;32mEscolha uma opção de 1 a 3:\033[0m\n")
    
    opcao = input()
    print("Opção escolhida: ", opcao)
    print("\n")
    
    match opcao:
        case '1':  
            print("\033[1;32mOpções de Menu:\033[0m")    
            print("\033[0;36m|1|= Opções de Jogador")
            print("\033[0;36m|2|= Voltar")
            
            opcoes = input()
            
            print("Opção escolhida: ", opcoes)
            print("\n")
    
            if(opcoes == '1'):
                game.menuJogador()
            if(opcoes == '2'):
                print("opcoes 2 ") 
                   
        case'2':
            game.CarregarJogo()

        
        case '3':
           print_devagar("\033[31;1;4mFinalizando o jogo.....\033[0m\n")
           break    

  
 
 