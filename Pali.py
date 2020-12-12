def pa(texto):
    ig = 0
    au = 0
    for i in reversed(range(0, len(texto))):
        if texto[i].lower() == texto[au].lower():
            ig += 1
        au += 1
    
    lista = []
    text = open("wordlist.txt", "r")
    text = text.read().splitlines()
    for i in text:
        lista.append(i)
    
    if len(texto) == ig:
        print("Palindromo")
        if texto in lista:
            print("Y en lista")
            return texto
        else:
            print("No esta")
    else:
        print("no palindromo")
