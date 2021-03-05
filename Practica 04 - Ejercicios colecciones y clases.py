'''print('1. Un programa que almacene en una lista el número de días que tiene cada mes (supondremos que es un año no bisiesto), pida al usuario que le indique un mes (1=enero, 12=diciembre) y muestre en pantalla el número de días que tiene ese mes. \n')

meses_del_año = {'1' : 'enero tiene un total de 31', '2' : 'febrero tiene un total de 28', '3': 'marzo tiene un total de 31', '4' : 'abril tiene un total de 30 dia', '5': 'mayo tiene un total de 31 dias', '6' : 'junio tiene un total de 30 dias',
                 '7': 'julio tiene un total de 31 dias', '8': 'agosto tiene un total de 31 dias' , '9': 'septiembre tiene un total de 30 dias', '10' : 'octubre tiene un total de 31 dias', '11' : 'novembre tiene un total de 30 dias', '12' : 'diciembre tiene un total de 31 dias'}

print(meses_del_año['1'])'''





'''print('2.Crear y cargar una lista con 10 enteros por teclado. Crear un programa que identifique el valor mas pequeño de la lista y la posición donde se encuentra. Mostrar en pantalla el resultado.\n')

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

uno = int (input('introduzca el primer entero : '))
dos = int (input('introduzca el segundo entero: '))
tres = int (input('introduzca el tercero entero: '))
cuatros = int (input('introduzca el cuarto entero: '))
cinco = int (input('introduzca el quinto entero: '))
seis = int (input('introduzca el sexto entero: '))
siete = int (input('introduzca el septimo entero: '))
ocho = int (input('introduzca el octavo entero: '))
nueve = int (input('introduzca el noveno entero: '))
diez = int (input('introduzca el  decimo entero: '))

if uno < dos and uno < tres and uno < cuatros and uno < cinco and uno < seis and uno < siete and uno < ocho and uno < nueve and uno < diez:
    print('el numero : ', uno , 'es el mas pequeño de la lista y esta en la posicion numero 0')

elif dos < uno and dos < tres and dos < cuatros and dos < cinco and dos < seis and dos < siete and dos < ocho and dos < nueve and dos < diez:
    print('el numero : ', dos , 'es el mas pequeño de la lista y esta en la posicion numero 1')

elif tres < uno and tres < dos and tres < cuatros and tres < cinco and tres < seis and tres < siete and tres < ocho and tres< nueve and tres < diez:
    print('el numero : ', tres , 'es el mas pequeño de la lista y esta en la posicion numero 2')

elif cuatros < uno and cuatros < dos and cuatros < tres and cuatros < cinco and cuatros< seis and cuatros < siete and cuatros < ocho and cuatros< nueve and cuatros < diez:
    print('el numero : ',cuatros , 'es el mas pequeño de la lista y esta en la posicion numero 3')

elif cinco < uno and cinco < dos and cinco< tres and cinco < cuatros and cinco < seis and cinco < siete and cinco < ocho and cinco < nueve and cinco < diez:
    print('el numero : ',cinco , 'es el mas pequeño de la lista y esta en la posicion numero 4')

elif seis < uno and seis< dos and seis < tres and seis < cuatros and seis < cinco and seis < siete and seis < ocho and seis < nueve and seis < diez:
    print('el numero : ',seis , 'es el mas pequeño de la lista y esta en la posicion numero 5')

elif siete < uno and siete < dos and siete < tres and siete < cuatros and siete < cinco and siete < seis and siete < ocho and siete < nueve and siete < diez:
    print('el numero : ',siete , 'es el mas pequeño de la lista y esta en la posicion numero 6')

elif ocho < uno and ocho < dos and ocho < tres and ocho < cuatros and ocho < cinco and ocho < seis and ocho < siete and ocho < nueve and ocho < diez:
    print('el numero : ',ocho, 'es el mas pequeño de la lista y esta en la posicion numero 7')

elif nueve < uno and nueve < dos and nueve < tres and nueve < cuatros and nueve < cinco and nueve < seis and nueve < siete and nueve < ocho and nueve < diez:
    print('el numero : ',nueve , 'es el mas pequeño de la lista y esta en la posicion numero 8')

elif diez < uno and diez < dos and diez < tres and diez < cuatros and diez < cinco and diez < seis and diez < siete and diez < ocho and diez < nueve:
    print('el numero : ',nueve , 'es el mas pequeño de la lista y esta en la posicion numero 9')
'''







''''print('3.Crear una lista. La lista tiene que tener 3 elementos. Cada elemento debe ser una lista de 5 enteros. Calcular y mostrar la suma de cada lista contenida en la lista principal.')

suma = [10 + 10 + 10 + 10 + 10  ]
suma1 = [20 + 20 + 20 + 20 +20]
suma2 = [30 + 30 + 30 + 30 + 30 ]

lista = suma + suma1 + suma2

print(lista)
'''






'''print('4.Crear una aplicación que se ingrese por teclado el nombre de 5 empleados, sueldo cobrado por cada empleado en los ultimos 3 meses. Mostrar en pantalla el total pagado a cada empleado en los ultimos 3 meses obtener y mostrar cual fue el empleado de mayor ingreso.\n')



empleado1 =  input('digite el nombre del empleado: ' )
empleado2 =  input('digite el nombre del segundo empleado: ')
empleado3 =  input('digite el nombre del tercer empleado: ')
empleado4 =  input('digite el nombre del cuarto empleado: ')
empleado5 =  input('digite el nombre del quinto empleado: ')


sueldos = (10000 , 20000 , 300000,  40000 ,  50000)

sueldo1, sueldo2 , sueldo3 , sueldo4,sueldo5 = sueldos

if sueldo1 > sueldo2  and sueldo1 > sueldo3  and sueldo1 > sueldo4 and sueldo1 > sueldo5:
    print(empleado1 , ' logro obtener un total de ',  sueldo1 , 'en los ultimos tres meses y fue el que mas gano' )

elif sueldo2 > sueldo1  and sueldo2 > sueldo3  and sueldo2 > sueldo4 and sueldo1 > sueldo5:
    print(empleado2, ' logro obtener un total de ', sueldo2, 'en los ultimos tres meses y fue el que mas gano')

elif  sueldo3 > sueldo1  and sueldo3 > sueldo2  and sueldo3 > sueldo4 and sueldo3 > sueldo5:
    print(empleado3, ' logro obtener un total de ', sueldo3, 'en los ultimos tres meses y fue el que mas gano\n')

elif sueldo4 > sueldo1  and sueldo4 > sueldo2  and sueldo4 > sueldo3 and sueldo4 > sueldo5:
    print(empleado4, ' logro obtener un total de ', sueldo4, 'en los ultimos tres meses y fue el que mas gano')

elif  sueldo5 > sueldo1  and sueldo5 > sueldo2  and sueldo5 > sueldo3 and sueldo5 > sueldo4:
    print(empleado5, ' logro obtener un total de ', sueldo5, 'en los ultimos tres meses y fue el que mas gano')

print('sueldo obtenido de cada uno en general \n')

print('********************')
print('********************\n')
print(empleado1, sueldo1)
print(empleado2, sueldo2)
print(empleado3, sueldo3)
print(empleado4, sueldo4)
print(empleado5, sueldo5)
print('********************')
print('********************')
'''






'''print('5.Crear una función que le enviemos como parámetros dos enteros y nos retorne el mayor.')

def entero (num1, num2):
    if num1 >= num2:
        return 10

    elif num1 <= num2:
        return 5

print( entero(10, 5 ))
'''






'''print('6.Crear una lista y almacenar 20 enteros pedidos por teclado. Eliminar todos los elementos que sean pares.')

numeros = [25,15,27,9,21,1,3,5,7,9,10,2,4,6,20,100,12,60,30,16]
print(numeros, '\n')
print(numeros[0:10])
'''






'''print("7.Un programa que pida al usuario 4 "
      "números, los memorice (utilizando una coleccion), calcule su media "
      "aritmética y después muestre en pantalla la media y los datos ingresado.")

valor1,valor2,valor3,valor4 =(0,0,0,0)

valor1 = int(input("Ingrese el primer numero: "))
valor2 = int(input("Ingrese el segundo numero: "))
valor3 = int(input("Ingrese el tercer numero: "))
valor4 = int(input("Ingrese el cuarto numero: "))

total = round (valor1+valor2+valor3+valor4/4)

print("Sus numeros ingresados fueron",valor1,",",valor2,",",valor3,"y",valor4,"y la media aritmetica calculada es",total,)'''





'''print("8.Crear una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18.")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
def edad (edad1, edad2):
    if edad1 >= 18:
        return edad1
    elif edad2 >= 17:
        return edad2
print(edad(18, 17))
'''





'''print('9.Crear un programa que defina una lista de 5 elementos de tipo reales que representen las alturas de 5 personas, '
      'Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.')


estaturas = [5.7, 5.8, 5.9, 6.1, 6.3]
Altura_promedio = (estaturas[0] + estaturas[1] + estaturas[2] + estaturas[3] + estaturas[4]) / 5
personas_altas = 0
personas_bajas = 0

for i in range(len(estaturas)):
    if float(estaturas[i]) > Altura_promedio:
        personas_altas += 1
    elif float(estaturas[i]) < Altura_promedio:
        personas_bajas += 1
        
        
print('\n******************************************')
print('******************************************')

print("\nLa altura promedio es:", Altura_promedio)
print("\nHay", personas_altas, " mas altas que el promedio")
print("\nHay", personas_bajas, " mas bajas que el promedio")

print('******************************************')
print('******************************************')
'''









'''print('10. Crear una clase que permita ingresar valores enteros por teclado y nos muestre la tabla de multiplicar de dicho valor.'
      ' Finalizar el programa al ingresar el -1.')

def tabla_de_multiplicacion():
    valor = 1
    for x in range(10):
        print(entrada, " x", valor, " =", entrada * valor)
        valor += 1


valor = int(input("Ingresa un numero entero: "))

while valor != -1:
    tabla_de_multiplicacion()
    entrada = int(input("\nIngresa un numero entero: "))

else:
    print("gracias por ver mi programa")
'''
