#imprimir el menú
def imprimir_menu():
    print("Menu:")
    print("1. Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")

#Bucle 
while True:
    imprimir_menu()  #Imprimir el menú
    opcion = input("Seleccione una opción: ")  

    if opcion == '1':
        print("Hola, has presionado la opción Personas")
    elif opcion == '2':
        print("Hola, has presionado la opción Vehiculos")
    elif opcion == '3':
        print("Hola, has presionado la opción Universidades")
    elif opcion == '4':
        print("Hola, has presionado la opción Notas")
    elif opcion == '5':
        print("Saliendo del programa...")
        break  # Salir del bucle
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
