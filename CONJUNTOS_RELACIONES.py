
# 1. NOTACIÓN DE CONJUNTOS
def notacion_conjuntos():
    # La notación de conjuntos puede expresarse de dos formas:
    # por extensión (listando los elementos) o por comprensión (usando una propiedad).
    # Ejemplo matematico: A = {1, 2, 3, 4} 
    A = set([1, 2, 3, 4])
    print("Conjunto A:", A)

    # COMPRESION
    # Definición: SE ENCARGA DE IMPRIMIR LOS NUMEROS PARES en CONJUNTOS
    # Ejemplo matematico: B={x∈N∣x es par}
    B = set(x for x in range(1, 21) if x % 2 == 0)
    print("Conjunto B de numeros pares:", B)


# 2. CARDINALIDAD
def cardinalidad():
    # Definición: ESTA ENCARGADO DE DEFINIR CUANTOS ELEMENTOS TIENE CADA CONJUNTO
    # Ejemplo matematico : |A| = 4
    A = {1, 2, 3, 4}
    print(f"Cardinalidad de A: {len(A)}")

    # Conjunto infinito (simulación primeros 100 naturales)
    # Definición: Este programa genera un conjunto con los números del 1 al 100 
    # Ejemplo matematico : 100
    n = set(range(1, 101))
    print("100 primeros numeros:", n)


# 3. OPERACIONES CONJUNTISTAS
def operaciones_conjuntos():
    # Conjuntos base
    A = {1, 2, 3}
    B = {3, 4, 5}

    # UNIÓN
    # Definición: A ∪ B = conjunto de elementos que están en A, en B o en ambos.
    print(f"A ∪ B = {A.union(B)}") 

    # INTERSECCIÓN
    # Definición: A ∩ B = conjunto de elementos que están tanto en A como en B.
    print(f"A ∩ B = {A.intersection(B)}")  

    # DIFERENCIA
    # Definición: A - B = conjunto de elementos que están en A pero no en B.
    print(f"A - B = {A.difference(B)}") 

    # DIFERENCIA SIMÉTRICA
    # Definición: A ^ B = elementos que están en A o en B, pero no en ambos.
    print(f"A ^ B = {A.symmetric_difference(B)}") 

    # COMPLEMENTO
    # Universo: todos los elementos posibles
    # Definición: EL COMPLEMENTO DEL CONJUNTO A RESPECTO A UN UNIVERSO U
    U = {1, 2, 3, 4, 5}
    complemento = U - A
    print(f"Complemento de A (U - A): {complemento}")  

    # PRODUCTO CARTESIANO
    # Definición: El producto cartesiano A × B es el conjunto de todos los pares ordenados (a, b),
    # donde 'a' pertenece al conjunto A y 'b' pertenece al conjunto B.
    cartesiano = {(a, b) for a in A for b in B}
    print(f"Producto cartesiano A × B: {cartesiano}")


# 4. RELACIONES
def relaciones():
    # Reflexiva
    # Definición: define los conjuntos y la relación entre sí
    # Ejemplo matemático: A={1,2,3}, R={(1,1),(2,2),(3,3)}
    A = {1, 2, 3}
    R = {(1,1), (2,2), (3,3)}
    reflexiva = all((a,a) in R for a in A)
    print("Relacion reflexiva:", reflexiva)

    # Simétrica
    # Definición: una relación es simétrica si (a,b) implica (b,a)
    # Ejemplo matemático: R={(1,2),(2,1),(3,3)}
    R = {(1,2), (2,1), (3,3)}
    simetrica = all(((b,a) in R) for (a,b) in R)
    print("Relacion simetrica:", simetrica)

    # Antisimétrica
    # Definición: se relaciona antisimétrica si (a,b) y (b,a) implican a=b
    # Ejemplo matemático: R={(1,2),(2,2)}
    R = {(1,2), (2,2)}
    antisimetrica = all((b,a) not in R or a==b for (a,b) in R)
    print("Relacion antisimetrica:", antisimetrica)

    # Transitiva
    # Definición: se puede deducir (a,c) si existen (a,b) y (b,c)
    # Ejemplo matemático: R={(1,2),(2,3),(1,3)}
    R = {(1,2),(2,3),(1,3)}
    transitiva = all(((a,d) in R) for (a,b) in R for (c,d) in R if b==c)
    print("Relacion transitiva:", transitiva)

    # Relación de equivalencia
    # Definición: es equivalencia cuando cumple reflexiva, simétrica y transitiva
    A = {1,2,3}
    R = {(1,1),(2,2),(3,3),(1,2),(2,1)}
    reflexiva = all((a,a) in R for a in A)
    simetrica = all(((b,a) in R) for (a,b) in R)
    transitiva = all(((a,d) in R) for (a,b) in R for (c,d) in R if b==c)
    print("Equivalencia:", reflexiva and simetrica and transitiva)

    # Relación de orden
    # Definición: es cuando la relación es reflexiva, antisimétrica y transitiva
    # Ejemplo matemático: A={1,2,3}, R={(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)}
    A = {1,2,3}
    R = {(a,b) for a in A for b in A if a <= b}
    reflexiva = all((a,a) in R for a in A)
    antisimetrica = all((b,a) not in R or a==b for (a,b) in R)
    transitiva = all(((a,d) in R) for (a,b) in R for (c,d) in R if b==c)
    print("Relacion de orden:", reflexiva and antisimetrica and transitiva)


# 5. FUNCIONES
def funciones():
    # Inyectiva
    # Definición: si los elementos de A se asignan a elementos distintos en B
    # Ejemplo matemático: A={1,2,3}, B={2,4,6}, f(1)=2, f(2)=4, f(3)=6
    A = {1,2,3}
    B = {2,4,6}
    f = {1:2, 2:4, 3:6}
    inyectiva = len(set(f.values())) == len(f.values())
    print("Funcion inyectiva:", inyectiva)

    # Sobreyectiva
    # Definición: cada elemento de B es imagen de al menos un elemento de A
    # Ejemplo matemático: A={0,1,2}, B={0,1,2}, f(x)=x
    A = {0,1,2}
    B = {0,1,2}
    f = {0:0, 1:1, 2:2}
    sobreyectiva = all(b in f.values() for b in B)
    print("Funcion sobreyectiva:", sobreyectiva)

    # Biyectiva
    # Definición: es inyectiva y sobreyectiva a la vez
    # Ejemplo matemático: A={1,2,3}, B={2,3,4}, f(x)=x+1
    A = {1,2,3}
    B = {2,3,4}
    f = {1:2, 2:3, 3:4}
    inyectiva = len(set(f.values())) == len(f.values())
    sobreyectiva = all(b in f.values() for b in B)
    print("Funcion biyectiva:", inyectiva and sobreyectiva)


# 6. CLAUSURAS
def clausuras():
    # Clausura reflexiva
    # Definición: añadir los pares (a,a) que falten
    # Ejemplo: A={1,2,3}, R={(1,2)} -> {(1,1),(2,2),(3,3),(1,2)}
    A = {1,2,3}
    R = {(1,2)}
    for a in A:
        R.add((a,a))
    print("Clausura reflexiva:", R)

    # Clausura simétrica
    # Definición: si (a,b) está en R, añadir (b,a)
    # Ejemplo: R={(1,2)} -> {(1,2),(2,1)}
    R = {(1,2)}
    for (a,b) in list(R):
        R.add((b,a))
    print("Clausura simetrica:", R)

    # Clausura transitiva
    # Definición: si (a,b) y (b,c) están en R, añadir (a,c)
    # Ejemplo: R={(1,2),(2,3)} -> {(1,2),(2,3),(1,3)}
    R = {(1,2),(2,3)}
    agregado = True
    while agregado:
        agregado = False
        for (a,b) in list(R):
            for (c,d) in list(R):
                if b==c and (a,d) not in R:
                    R.add((a,d))
                    agregado = True
    print("Clausura transitiva:", R)

    # Clausura de equivalencia
    # Definición: combinación de reflexiva, simétrica y transitiva
    # Ejemplo: A={1,2,3}, R={(1,2)} -> R_clausura con reflexiva+simétrica+transitiva
    A = {1,2,3}
    R = {(1,2)}
    for a in A:
        R.add((a,a))
    for (a,b) in list(R):
        R.add((b,a))
    agregado = True
    while agregado:
        agregado = False
        for (a,b) in list(R):
            for (c,d) in list(R):
                if b==c and (a,d) not in R:
                    R.add((a,d))
                    agregado = True
    print("Clausura de equivalencia:", R)


# === MENU PRINCIPAL  ===
def menu():
    while True:
        print("\n MENU PRINCIPAL")
        print("1. Notación de conjuntos")
        print("2. Cardinalidad")
        print("3. Operaciones conjuntistas")
        print("4. Relaciones")
        print("5. Funciones")
        print("6. Clausuras")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                notacion_conjuntos()
            case "2":
                cardinalidad()
            case "3":
                operaciones_conjuntos()
            case "4":
                relaciones()
            case "5":
                funciones()
            case "6":
                clausuras()
            case "7":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida, intente de nuevo.")

# Ejecutar el menu
menu()
