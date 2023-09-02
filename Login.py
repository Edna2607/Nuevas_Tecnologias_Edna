#REGISTRO BASICO

correct_name = "Edna"
correct_password = 123
captcha = 100

print("Bienvenido - al inicio de sesión")
user = input("Ingrese con su nombre ó Numero de Celular = ")
password = int(input("Ingrese su contraseña = "))
captcha = int(input("Cuando es el valor de: 48+52 = "))

if (correct_name == user or user == "3013059673") and password == correct_password and captcha == 100:
    input("------Inicio de Sesion exitoso -------")
else: print("No puede Ingresar, los datos son erroneos")

#-----------------------------------------------------------------------------------
#REGISTRO BASICO 2

"""class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age

# Base de datos ficticia de usuarios
database = [
    User("tulip2607@hotmail.com", "miclave123", 36),
    User("3013059673", "miclave123", 36)
]

def login():
    print("Bienvenido - inicio de sesión")
    username = input("Ingresa tu correo electrónico o número de celular: ")
    password = input("Ingresa tu contraseña: ")
    name = input("Ingresa tu nombre : ")
    age = input("Ingresar tu edad : ")

    for user in database:
    
        if (user.username == username or user.username == password) and user.password == password:
            print(f" ----------  Inicio de sesión exitoso. ------------- ")
            print(f"¡Hola, {name}!")
            print(f"Tu edad registrada es: {age}")
            return
    print("------- Informacion incorrecta. Por favor, verifica tus datos. --------- ")

login()
"""

