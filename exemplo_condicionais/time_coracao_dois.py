time_coracao = input("Digite o time do coração: ")

time_coracao = time_coracao.strip().upper()

match time_coracao:
    case "GREMIO":
        print("Gremista")
    case "INTER":
        print("Colorado")
    case "JUVENTUDE":
        print("Juventista")
    case _:
        print("Seleciona o time ai mano!")