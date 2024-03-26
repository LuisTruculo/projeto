from docs.lib.funcoes import *

while True:
    print("\nMenu:")
    print("1. Cadastrar novos jogadores")
    print("2. Consultar jogadores")
    print("3. Apagar")
    print("4. Atualizar")
    print("5. Trocar jogador de time")
    print("6. Cadastrar novo time")
    print("7. Atualizar novo time")
    print("8. Consultar times")
    print("9. Cadastrar novo campeonato")
    print("10. Atualizar novo campeonato")
    print("11. Consultar campeonatos")
    print("12. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = input("Digite o nome do jogador: ")
        posicao = input("Digite a posição do jogador: ")
        nacionalidade = input("Digite a nacionalidade do jogador: ")
        time = input("Digite o time do jogador: ")
        novo_jogador(nome, posicao, nacionalidade, time)

    elif escolha == 2:
        print(ver_jogadores())

    elif escolha == 3:
        jogador_id = int(input("Digite o ID do jogador que deseja apagar: "))
        apagar_jogador(jogador_id)

    elif escolha == 4:
        jogador_id = int(input("Digite o ID do jogador que deseja atualizar: "))
        novo_nome = input("Digite o novo nome do jogador: ")
        nova_posicao = input("Digite a nova posição: ")
        nova_nacionalidade = input("Digite a nova nacionalidade: ")
        atualizar_jogador(jogador_id, novo_nome, nova_posicao, nova_nacionalidade)

    elif escolha == 5:
        jogador_id= int(input("Digite o ID do jogador que deseja trocar de time: "))
        novo_time = input("Digite o novo time do jogador: ")
        trocar_jogador(jogador_id, novo_time)

    elif escolha == 6:
        nome = input("Digite o nome do time: ")
        pais = input("Digite o país do time: ")
        ano = int(input("Digite o ano de fundação do time: "))
        time_novo(nome, pais, ano)

    elif escolha == 7:
        time_id = int(input("Digite o ID do time que deseja atualizar: "))
        novo_nome = input("Digite o novo nome do time: ")
        novo_pais = input("Digite o país do time: ")
        novo_ano = int(input("Digite o ano de fundação do time: "))
        atualizar_time(time_id, novo_nome, novo_pais, novo_ano)
    
    elif escolha ==8:
        print(ver_times())

    elif escolha == 9:
        nome = input("Digite o nome do campeonato: ")
        ano = int(input("Digite o ano que vai acontecer esse campeonato: "))
        pais = input("Digite o país que acontece o campeonato: ")
        tipo = input("O campeonato é nacional, regional ou internacional: ")
        novo_campeonato(nome, ano, pais, tipo)

    elif escolha == 10:
        campeonato_id = int(input("Digite o ID do campeonato que deseja atualizar: "))
        camp_nome = input("Digite o novo nome do campeonato: ")
        camp_ano = int(input("Digite o novo ano: "))
        camp_pais = input("Digite o novo país: ")
        camp_tipo = input("Digite se é nacional, regional ou internacional: ")
        atualizar_campeonato(campeonato_id, camp_nome, camp_ano, camp_pais, camp_tipo)
    
    elif escolha == 11:
         print(ver_campeonatos())
    
    elif escolha == 12:
        break
    else:
        print("Opção inválida. Tente novamente.")