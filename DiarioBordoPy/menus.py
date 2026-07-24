from utilitarios import limpar
from diario import criar_anotacao, listar_anotacoes, buscar_anotacoes, excluir_anotacao, estatisticas

def menu_criar_anotacao():

    while True: 
        
        limpar()
        
        print("Adicionar uma anotação.\n")
        
        criar_anotacao()
        
        print("\nAnotação adicionada!")
        input("Pressione ENTER para retornar ao menu... ")
        break
        
def menu_listar_anotacoes():
    
    while True: 
        
        limpar()
        
        print("Todas as anotações disponiveis!\n")
        
        listar_anotacoes()
        
        input("\nDigite ENTER para retornar ao menu...")
        break

def menu_buscar_anotacoes():
    
    while True: 
        
        limpar()
        
        print("Buscar por uma anotação.\n")
        
        buscar_anotacoes()
        
        input("\nPressione ENTER para retornar ao menu... ")
        break

def menu_excluir_anotacao():
    
    while True:
        
        limpar()
        
        print("Excluir uma anotação.\n")
        
        excluir_anotacao()
        
        input("\nPressione ENTER para retornar ao menu... ")
        break

def menu_estatisticas():
    
    while True:
        
        limpar()
        
        print("Estatisticas do sistema.\n")
        
        estatisticas()
        
        input("\nPressione ENTER para retornar ao menu... ")
        break

def menu_principal():

    while True:
        
        limpar()
        
        print("Bem vindo ao Diario de Bordo Py!\n")
        
        print("[1] - Criar anotação.")
        print("[2] - Listar anotações.")
        print("[3] - Buscar anotações.")
        print("[4] - Excluir anotação.")
        print("[5] - Estatisticas.")
        print("[0] - Fechar programa.\n")
        
        escolha = input("Selecione uma opção pelo seu número: ")
        
        if escolha == "1":
            menu_criar_anotacao()
        
        elif escolha == "2":
            menu_listar_anotacoes()
        
        elif escolha == "3":
            menu_buscar_anotacoes()
            
        elif escolha == "4":
            menu_excluir_anotacao()
        
        elif escolha == "5":
            menu_estatisticas()
        
        elif escolha == "0":
            limpar()
            print("\nObrigado por anotar!")
            break
        
        else:
            limpar()
            print("Digite uma opção valida!\n")
            input("Press ENTER... ")