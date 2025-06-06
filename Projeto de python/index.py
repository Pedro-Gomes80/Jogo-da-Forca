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
    
def jogar():
    palavra = escolher_palavra_por_tema()
    letras_corretas = []
    letras_erradas = []
    tentativas = 0
    max_tentativas = 6

    print("🎮 Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra secreta.\n")

    while tentativas <= max_tentativas:
        print(exibir_palavra(palavra, letras_corretas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        tentativa = input("Digite uma letra ou tente adivinhar a palavra inteira: ").lower()

        if not tentativa.isalpha():
            print("❗Digite apenas letras.\n")
            continue
        if len(tentativa) > 1:
            if tentativa == palavra:
                print(f"\n🎉 Parabéns! Você acertou a palavra inteira: {palavra}")
                break
            else:
                tentativas += 1
                print(f"❌ Palavra incorreta! Você perdeu uma tentativa.")
                desenhar_forca(tentativas)
        else:
            if tentativa in letras_corretas or tentativa in letras_erradas:
                print("⚠️ Você já tentou essa letra.\n")
                continue

            if tentativa in palavra:
                letras_corretas.append(tentativa)
                print("✅ Letra correta!\n")
            else:
                letras_erradas.append(tentativa)
                tentativas += 1
                print("❌ Letra errada.")
                desenhar_forca(tentativas)
                print()

        if all(l in letras_corretas for l in palavra):
            print(f"\n🎉 Parabéns! Você completou a palavra: {palavra}")
            break

        if tentativas == max_tentativas:
            print(f"\n💀 Você perdeu! A palavra era: {palavra}")
            break

if __name__ == "__main__":
    jogar()