from database import jogadores, times, campeonatos 

def novo_jogador(nome, posicao, nacionalidade, time):
    novo_jogador =  {"id": len(jogadores) + 1, 'nome': nome, "posição": posicao, "nacionalidade": nacionalidade, "time": time}
    jogadores.append(novo_jogador)

def ver_jogadores():
    return jogadores

def apagar_jogador(jogador_id):
    jogadores[:] = [jogador for jogador in jogadores if jogador["id"] != jogador_id]

def atualizar_jogador(jogador_id, novo_nome, nova_posicao, nova_nacionalidade):
    for jogador in jogadores:
        if jogador["id"] == jogador_id:
            jogador["nome"] = novo_nome
            jogador["posicao"] = nova_posicao
            jogador["nacionalidade"] = nova_nacionalidade
            break

def trocar_jogador(jogador_id, novo_time):
    for jogador in jogadores:
        if jogador["id"] == jogador_id:
            jogador["time"] = novo_time

def time_novo(nome, pais, ano):
    time_novo =  {"id": len(times) + 1, 'nome': nome, "país": pais, "ano de fundação": ano}
    times.append(time_novo)

def atualizar_time(time_id, novo_nome, novo_pais, novo_ano):
    for time in times:
        if time["id"] == time_id:
            time["nome"] = novo_nome
            time["país"] = novo_pais
            time["ano de fundacao"] = novo_ano
            break

def ver_times():
    return times

def novo_campeonato(nome, ano, pais, tipo):
    novo_campeonato =  {"id": len(campeonatos) + 1, 'nome': nome, "ano": ano, "país": pais, "tipo": tipo}
    campeonatos.append(novo_campeonato)

def atualizar_campeonato(campeonato_id, camp_nome, camp_ano, camp_pais, camp_tipo):
     for campeonato in campeonatos:
        if campeonato["id"] == campeonato_id:
            campeonato["nome"] = camp_nome
            campeonato["ano"] = camp_ano
            campeonato["país"] = camp_pais
            campeonato["tipo"] = camp_tipo
            break

def ver_campeonatos():
    return campeonatos