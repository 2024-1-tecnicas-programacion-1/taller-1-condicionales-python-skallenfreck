from unicodedata import numeric


def evaluar(num_victorias_a, num_victorias_b):
    
    if num_victorias_b > 7  or num_victorias_a > 7:
        return "Resultado Inválido"
    elif (num_victorias_a == 7 or num_victorias_b == 7) and (abs(num_victorias_b-num_victorias_a)>2 or abs(num_victorias_b-num_victorias_a)==0):
        return "Resultado Inválido" 
    elif (num_victorias_a == 6 or num_victorias_b == 6) and abs(num_victorias_a-num_victorias_b)>=2:
        if num_victorias_a-num_victorias_b>0:
            return "Ganó A"
        elif num_victorias_b-num_victorias_a>0:
            return "Ganó B"
    elif num_victorias_a == 7 or num_victorias_b == 7:
        if num_victorias_a==7:
            return "Ganó A"
        elif num_victorias_b ==7:
            return "Ganó B"
    else:
        return "Aún no termina"


if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)


