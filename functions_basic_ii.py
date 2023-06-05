#1 Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 

def Cuenta_regresiva(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
print(Cuenta_regresiva(10))

# Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.

def imprimir_devolver(list):
    a = list[0]
    b = list [1]
    print(a)
    return b
print(imprimir_devolver([1,2]))

# 3. Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.

def Primero_mas_longitud(list):
    a = list[0]
    b = len(list)
    
    return a+b
print(Primero_mas_longitud([1,2,3,4,5]))

# 4. Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False

def Valores_mayores_que_el_segundo(list):
   
    if len(list) < 2:
        return False
    segundo_valor = list[1]
   
    newlist= [valor for valor in list if valor > segundo_valor]
    
    lennewlist = len(newlist)
    print("nueva cantidad de la lista", lennewlist )

    return newlist
print(Valores_mayores_que_el_segundo([5,2,3,2,1,4]))

# 5. Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.

def Esta_longitud_ese_valor(a,b):


    list = []
    for i in range(a, 0, -1):
        list.append(b)
    return list
print(Esta_longitud_ese_valor(4,7))
print(Esta_longitud_ese_valor(6,2))

