def po(texto):
    igual = 0
    aux = 0
    for i in reversed(range(0, len(texto))):
        if texto[i].lower() == texto[aux].lower():
            igual += 1
        aux +=1
    
    lista = []
    text = open("wordlist.txt", "r")
    text = text.read().splitlines()
    for i in text:
        lista.append(i)
    
    if len(texto) == igual:
        if texto in lista:
            return texto
    else:
        return igual