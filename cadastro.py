import json
import os

ARQUIVO_DADOS = "dados.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_dados(usuarios):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)

def proximo_id(usuarios):
    if not usuarios:
        return 1
    return max(u["id"] for u in usuarios) + 1

def cadastrar_usuario(usuarios):
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()

    if not nome or not email:
        print("❌ Nome e email não podem ficar vazios.")
        return

    for u in usuarios:
        if u["email"].lower() == email.lower():
            print("❌ Já existe um usuário com esse email.")
            return

    novo = {"id": proximo_id(usuarios), "nome": nome, "email": email}
    usuarios.append(novo)
    salvar_dados(usuarios)
    print("✅ Usuário cadastrado com sucesso!")

def listar_usuarios(usuarios):
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
        return

    print("\n=== Usuários cadastrados ===")
    for u in usuarios:
        print(f'ID: {u["id"]} | Nome: {u["nome"]} | Email: {u["email"]}')

def buscar_usuario(usuarios):
    termo = input("Buscar por (nome, email ou id): ").strip()

    if not termo:
        print("❌ Você precisa digitar algo para buscar.")
        return

    if termo.isdigit():
        tid = int(termo)
        resultados = [u for u in usuarios if u["id"] == tid]
    else:
        t = termo.lower()
        resultados = [u for u in usuarios if t in u["nome"].lower() or t in u["email"].lower()]

    if not resultados:
        print("🔎 Nenhum resultado encontrado.")
        return

    print("\n=== Resultados ===")
    for u in resultados:
        print(f'ID: {u["id"]} | Nome: {u["nome"]} | Email: {u["email"]}')

def remover_usuario(usuarios):
    if not usuarios:
        print("📭 Nenhum usuário para remover.")
        return

    termo = input("Digite o ID do usuário para remover: ").strip()
    if not termo.isdigit():
        print("❌ Digite um ID válido (número).")
        return

    tid = int(termo)
    for u in usuarios:
        if u["id"] == tid:
            usuarios.remove(u)
            salvar_dados(usuarios)
            print("🗑️ Usuário removido com sucesso!")
            return

    print("❌ ID não encontrado.")
