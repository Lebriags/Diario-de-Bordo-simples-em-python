from utilitarios import salvar_json, carregar_json
from datetime import datetime
from zoneinfo import ZoneInfo

def criar_anotacao():
    
    diario = carregar_json()
    
    titulo = input("Digite um titulo para a anotação: ").strip()

    if not titulo:
        print("O título não pode ficar vazio.")
        return

    texto = input("Escreva sua anotação... ").strip()

    if not texto:
        print("O texto não pode ficar vazio.")
        return
    data = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).strftime("%d/%m/%Y %H:%M:%S")
    novo_id = len(diario) + 1
    
    nova_anotacao = {
        "id" : novo_id,
        "titulo" : titulo,
        "texto" : texto,
        "data" : data
    }
    
    diario.append(nova_anotacao)
    salvar_json(diario)


def listar_anotacoes():
    
    diario = carregar_json()

    if not diario:
        print("Nenhuma anotação cadastrada.")
        return

    for anotacao in diario:
        print("-" * 40)
        print(f"ID: {anotacao['id']}")
        print(f"Título: {anotacao['titulo']}")
        print(f"Texto: {anotacao['texto']}")
        print(f"Data: {anotacao['data']}")

def buscar_anotacoes():
    
    diario = carregar_json()

    if not diario:
        print("Não existem anotações.")
        return

    try:
        buscar = int(input("Digite o ID da anotação que deseja buscar: "))
    except ValueError:
        print("Digite apenas números.")
        return

    for anotacao in diario:
        if anotacao["id"] == buscar:
            print("-" * 40)
            print(f"ID: {anotacao['id']}")
            print(f"Título: {anotacao['titulo']}")
            print(f"Texto: {anotacao['texto']}")
            print(f"Data: {anotacao['data']}")
            return

    print("Anotação não encontrada.")

def excluir_anotacao():
    
    diario = carregar_json()

    if not diario:
        print("Não existem anotações.")
        return

    try:
        excluir = int(input("Digite o ID da anotação que deseja excluir: "))
    except ValueError:
        print("Digite apenas números.")
        return

    for anotacao in diario:
        if anotacao["id"] == excluir:

            diario.remove(anotacao)

            # Reorganiza os IDs
            for indice, anotacao in enumerate(diario, start=1):
                anotacao["id"] = indice

            salvar_json(diario)

            print("Anotação excluída.")
            return

    print("ID não encontrado.")

def estatisticas():

    diario = carregar_json()

    if not diario:
        print("Nenhuma anotação cadastrada.")
        return

    quantidade = len(diario)

    maior_titulo = max(diario, key=lambda anotacao: len(anotacao["titulo"]))
    menor_titulo = min(diario, key=lambda anotacao: len(anotacao["titulo"]))

    total_caracteres = sum(len(anotacao["texto"]) for anotacao in diario)

    print(f"Quantidade de anotações: {quantidade}")
    print(f"Maior título: {maior_titulo['titulo']}")
    print(f"Menor título: {menor_titulo['titulo']}")
    print(f"Total de caracteres escritos: {total_caracteres}")
    
    