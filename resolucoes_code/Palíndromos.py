# 6 - Verificando Palíndromos
palavra = input("Digite uma palavra: ")

# Normalizando (opcional): removendo espaços e deixando tudo minúsculo
normalizada = palavra.replace(" ", "").lower()

if normalizada == normalizada[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
