import json

def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_json(diario):
    
    with open("diario.json" , "w") as diary:
        json.dump(
        diario,
        diary,
        indent=4,
        ensure_ascii=False
        )

def carregar_json():
    
    try:
        with open("diario.json", "r") as diary:
            diario = json.load(diary)
    except (FileNotFoundError, json.JSONDecodeError):
        diario = []
        
    return diario

