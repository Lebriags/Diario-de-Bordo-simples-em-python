'''
    Projeto de sistema para diario de bordo.
    Ou pode se chamar de bloco de notas mas com algumas limitações...
    
    Arquitetura do Projeto: 
        - utilitarios.py > diario.py > menus.py > main.py
        - diario.json (definir isso como banco de dados) > diario.py
        
    O que o usuario poderá fazer:
        - Criar anotações
        - Listar anotações
        - Buscar por uma anotação
        - Excluir uma anotação 
        - Estatisticas do sistema (acho meio meh, mas a atividade pede, então ja sabe :/)
        - Sair do sistema
        
    Funções do programa: 
        - menu()
        - nova_anotacao()
        - listar_anotacoes()
        - buscar_anotacoes()
        - excluir_anotacao()
        - estatisticas() (me pergunto o pra que disso...)
        - salvar_json()
        - carregar_json()
        
        agora as funções mais gerais do programa:
        
        - limpar()  
    
    Como cada função vai funcionar:
    Se conseguir executar, só vai. 
    Se não conseguir executar o código, avisa sobre o erro e eu que resolvo.
'''

from menus import menu_principal

menu_principal()