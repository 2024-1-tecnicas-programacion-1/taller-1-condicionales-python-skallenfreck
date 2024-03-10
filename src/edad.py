def evaluar(dia, mes, anno):
    from time import localtime
    t=localtime()
    diaactual= t.tm_mday
    mesactual= t.tm_mon
    annoactual= t.tm_year
    if mes<mesactual:
        return "Usted tiene "+(annoactual-anno)+" años"
    elif mes==mesactual and dia<diaactual:
        return "Usted tiene "+(annoactual-anno)+" años"
    else:
        return "Usted tiene "+ (annoactual-anno-1)+" años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
