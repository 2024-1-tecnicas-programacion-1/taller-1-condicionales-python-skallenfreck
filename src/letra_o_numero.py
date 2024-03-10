def evaluar(caracter):
    if ord('A')<= ord(caracter)<=ord('Z') or ord(caracter)==ord('Ñ'):
        return "Es letra mayúscula"
    elif ord('a')<=ord(caracter)<=ord('z') or ord(caracter)==ord('ñ'):
        return "Es letra minúscula"
    elif ord('0')<=ord(caracter)<=ord('9'):
        return "Es número"
    else:
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
    