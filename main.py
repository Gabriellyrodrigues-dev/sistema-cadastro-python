from cadastro import (
    carregar_dados,
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    remover_usuario
)

def menu():
    print("\n=== Sistema de Cadastro ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Remover usuário")
    print("0 - Sair")

def main():
    usuarios = carregar_dados()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            buscar_usuario(usuarios)
        elif opcao == "4":
            remover_usuario(usuarios)
        elif opcao == "0":
            print("👋 Saindo... Até mais!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
