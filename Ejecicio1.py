# ---------------------------------------------------------------------------- #
#                                  Ejercicio 1                                 #
# ---------------------------------------------------------------------------- #

# Hacer un prorama que simule un cajero automático con un saldo inicial de $1000
# Al iniciar el programa deberá pedir el siguiente pin: “1235” para autenticar.
# Si está mal, deberá pedirlo máximo 3 veces.
# Pasando esas 3 vez el pin no es correcto, el programa deberá terminarse.
# Si es correcto mostrará un mensaje de bienvenida con tu nombre.
# y que tenga el siguiente menú de opciones:

# 1.- Ingresar el dinero en la cuenta
# 2.- Retirar el dinero de la cuenta
# 3.- Mostrar el dinero de disponible
# 4.- Mostrar histórico de la cuenta
# 5.- Salir

# ----------------------------- Cajero automático ---------------------------- #

i = 1
password = 1235
saldo = 1000
historico = []

while i < 6:
  print("#=================================#")
  print("\t.::IDENTIFICACIÓN::.")
  print("Para continuar ingrese sus datos:")
  print("#=================================#")
  nombre = str(input("Nombre: "))
  apellido = str(input("Primer apellido: "))

  print("#=================================#")
  print("\t.::BIENVENIDO::.")
  print(f"Hola de nuevo {nombre} {apellido}")
  print("Para continuar digite su contraseña")
  print("#=================================#")
  print()

  login = int(input("Contraseña: "))
  print()

  if login == password:
      while True:
        print("\t.::MENU::.")
        print("1.- Ingresar el dinero en la cuenta")
        print("2.- Retirar el dinero de la cuenta")
        print("3.- Mostrar el dinero disponible")
        print("4.- Mostrar histórico de la cuenta")
        print("5.- Salir")

        print()

        opcion = int(input("Digite una opción de menú: "))
        print()

        if opcion == 1:
            extra = int(input("¿Cuánto dinero desea ingresar? -> "))
            saldo += extra
            print(f"Dinero en la cuenta: {saldo}")
            print()
        elif opcion == 2:
            retirar = int(input("¿Cuánto dinero desea retirar? -> "))
            print()
            if retirar > saldo:
              print("Disculpe, usted no tiene esa cantidad en su cuenta...")
              print()
            else:
              saldo -= retirar
              print(f"Dinero en la cuenta: {saldo}")
              print()
        elif opcion == 3:
            print(f"Dinero en la cuenta: {saldo}")
            print()
        elif opcion == 4:
            print("¡Ups! Función no disponible")
            print("Seguimos trabajando en ésta mejora")
            print("Por favor, disuculpe la molestia...")
            print()
        elif opcion == 5:
            print("!Hasta pronto!")
            print("Gracias por utilizar su cajero automático...")
            print()
            break
        else:
            print("!Ups! Esa opcion no esta en nuestro registro, por favor vuelva a intentarlo")
            print()

  # ------------------------------- Login success ------------------------------ #
  else:
    print("Lo sentimos, su contraseña es incorrecta. Por favor intente nuevamente...")
    print()
    if i == 3:
      print("¡Ups! Llegó al número máximo de intentos. Por favor, intente más tarde...")
      print()
      break
    i += 1
  # -------------------------------- Login Fail -------------------------------- #

  # ---------------------------------- Errores --------------------------------- #
  print(f'Número de intetos fallidos: {i}')
  print()
