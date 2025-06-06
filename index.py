import random

def escolher_palavra_por_tema():
    temas = {
        "1": ("Heróis", [
            "superman", "batman", "homemaranha", "mulhermaravilha", "wolverine",
            "capitaomarvel", "homemdeferro", "panteranegra", "flash", "thor"
        ]),
        "2": ("Filmes", [
            "titanic", "avatar", "interestelar", "vingadores", "matrix",
            "inception", "gladiador", "godzilla", "frozen", "topgun"
        ]),
        "3": ("Séries", [
            "breakingbad", "strangerthings", "theoffice", "got", "lupin",
            "dark", "vikings", "friends", "theboys", "you"
        ]),
        "4": ("Comida", [
            "pizza", "hamburguer", "lasanha", "sushi", "chocolate",
            "bolo", "pastel", "coxinha", "brigadeiro", "macarrao"
        ]),
        "5": ("Animais", [
            "cachorro", "gato", "elefante", "girafa", "leao",
            "tigre", "zebra", "jacare", "urso", "pinguim"
        ])
    }

    print("🎯 Escolha um tema:")
    for k, (nome, _) in temas.items():
        print(f"{k} - {nome}")

    escolha = ""
    while escolha not in temas:
        escolha = input("Digite o número do tema desejado: ")

    nome_tema, palavras = temas[escolha]
    palavra_escolhida = random.choice(palavras).lower()
    print(f"\nTema escolhido: {nome_tema}\n")
    return palavra_escolhida

def exibir_palavra(palavra, letras_corretas):
    exibida = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibida += letra + " "
        else:
            exibida += "_ "
    return exibida.strip()

def desenhar_forca(tentativas):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    print(estagios[tentativas])
