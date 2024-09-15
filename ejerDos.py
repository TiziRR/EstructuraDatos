# 1)
def mayorDeTres(n1:int, n2:int, n3:int):
    mayor = 0
    if (n1 == n2 == n3):
        print('Error: valores iguales')
    elif n1 > mayor:
        mayor = n1
        print(mayor)
    elif n2 > mayor:
        mayor = n2
        print(mayor)
    elif n3 > mayor:
        mayor = n3
        print(mayor)
    else:
        return '-'
    
mayorDeTres(6,6,6)

# 2)
def fechaValida(n1, n2, n3):
    dia = list(range(1,31))
    mes = list(range(1,12))
    print(f'{True}: La fecha {n1}/{n2}/{n3} es válida') if n1 in dia and n2 in mes and n3 <= 2024 else print(f'{False}: fecha no válida')

fechaValida(12,1,2024)

# 3)
def cambioCaja(totalCompra:int, dineroRecibido:int):
    if dineroRecibido < totalCompra:
        return print('Error: dinero insuficiente')
    cambio = dineroRecibido - totalCompra
    print(f'Su cambio es de: ${cambio}')
    
    digitos = list(range(10))
    digitos_str = str(digitos)

    cambio_str = str(cambio)
    
    if len(cambio_str) == 1:
        if cambio_str < '5':
            print(f'{cambio_str} billete de $1') if cambio_str == '1' else print(f'{cambio_str} billetes de $1')
        
        if cambio_str == '5':
            print('1 billete de $5')
            
        if cambio_str > '5':
            cambio_un_digito = int(cambio_str) - 5
            print('1 billete de $5')
            print(f'{cambio_un_digito} billete de $1') if cambio_un_digito == 1 else print(f'{cambio_un_digito} billetes de $1')
        
    if len(cambio_str) == 2:
        for digito in digitos_str:
            if digito in cambio_str[0]:
                if digito < '5':
                    print(f'{digito} billete de $10') if digito == '1' else print(f'{digito} billetes de $10')
                    
                if digito == '5':
                    print('1 billete de $50')
                
                if digito > '5':
                    billetes_diez_dos = int(digito) - 5
                    print('1 billete de $50')
                    print(f'{billetes_diez_dos} billete de $10') if billetes_diez_dos == 1 else print(f'{billetes_diez_dos} billestes de $10')

            if digito in cambio_str[-1]:
                if digito < '5':
                    print(f'{digito} billete de $1') if digito == '1' else print(f'{digito} billetes de $1')
                
                if digito == '5':
                    print('1 billete de $5')
                    
                if digito > '5':
                    billetes_uno_dos = int(digito) - 5
                    print('1 billete de $50')
                    print(f'{billetes_uno_dos} billete de $1') if billetes_uno_dos == 1 else print(f'{billetes_uno_dos} billetes de $1')
    
    if len(cambio_str) == 3:
        for digito in digitos_str:
            
            if digito in cambio_str[0]:
                print(f'{digito} billete de $100') if digito == '1' else print(f'{digito} billetes de $100')
                
            if digito in cambio_str[1]:
                if digito < '5':
                    print('{digito} billete de $10') if digito == '1' else print(f'{digito} billetes de $10')
                
                if digito == '5':
                    print('1 billete de $50')
                    
                if digito > '5':
                    billetes_diez = int(digito) - 5
                    print('1 billete de $50')
                    print(f'{billetes_diez} billete de $10') if billetes_diez == 1 else print(f'{billetes_diez} billetes de $10')
            
            if digito in cambio_str[-1]:
                if int(digito) < 5:
                    print(f'{digito} billete de $1') if digito == 1 else print(f'{digito} billetes de $1')
                    
                if int(digito) == 5:
                    print('1 billete de $5')
                
                if int(digito) > 5 and int(digito) < 10:
                    billetes_uno = int(digito) - 5
                    print(f'{digito} billete de $1') if billetes_uno == 1 else print(f'{digito} billetes de $1')

cambioCaja(317, 500)

# 4)
def ventaZapallos(cant:str, divisa:int):
    moneda = {
        'dolares':0.05,
        'yenes':0.15,
        'guaranies':0.20,
        'pesos':0.10
    }
    if divisa in moneda.keys():
        print(f'La cantidad de zapallos que desea es de: {cant}. Usted por pagar en {divisa} tiene un descuento del {moneda[divisa] * 100}%, por lo tanto el total le quedaría en: {(cant * 1000) - ((cant * 1000) * moneda[divisa])}')
    else:
        print(f'La cantidad de zapallos que desea es de: {cant}. Usted por pagar en {divisa} tiene un aumento del 10%, por lo tanto el total le quedaría en: ${((cant * 1000) * 1.10)}')

ventaZapallos(2, 'franco suizo')