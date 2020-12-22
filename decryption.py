from urllib.request import urlopen
import hashlib
from requests.exceptions import ConnectionError
import os
import time
import random
import platform
import sys
import argparse
from hashlib import algorithms_available
from time import sleep as sl

if platform.system() != 'Linux':
    print("Solo se puede ejecutar en Linux !")
    sys.exit()
else:
    pass

print("")
colores = {
        "M" :  "\033[1;31m",
        "H" :  "\033[1;32m",
        "K" :  "\033[1;33m",
        "U" :  "\033[1;34m",
        "P" :  "\033[1;35m",
        "C" :  "\033[1;36m",
        "W":  "\033[1;37m",
        "A" :  "\033[90m",
}

os.system("clear")

def clear():
    os.system("clear")

#passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")

class Banner:
    def __str__(self):
        return colores["C"]+"""

  /$$$$$$                               /$$       /$$
 /$$__  $$                             | $$      |__/
| $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$ /$$ /$$$$$$$   /$$$$$$
| $$       /$$__  $$|____  $$ /$$_____/| $$  /$$/| $$| $$__  $$ /$$__  $$
| $$      | $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$| $$  \ $$| $$  \ $$
| $$    $$| $$      /$$__  $$| $$      | $$_  $$ | $$| $$  | $$| $$  | $$
|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$| $$| $$  | $$|  $$$$$$$
 \______/ |__/      \_______/ \_______/|__/  \__/|__/|__/  |__/ \____  $$
                                                                /$$  \ $$
                                                               |  $$$$$$/
                                                                \______/
"""

h = Banner()
clear()
print(h)
sl(0.7)
clear()
sl(0.3)
print(h)
sl(0.3)
clear()
sl(0.3)
print(h)
sl(0.3)
clear()
sl(0.3)
print(h)
sl(1.5)

class users:
    def __init__(self):
        pass
    def agents(self):
        list_agent = [
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 1.0.5)",
                "curl/7.7.2 (powerpc-apple-darwin6.0) libcurl 7.7.2 (OpenSSL 0.9.6b)",
                "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
                "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
                "Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
                "Opera/9.80 (X11; Linux i686; U; pl) Presto/2.6.30 Version/10.61"
                ]
        random_agent = random.choice(list_agent)
        user_agent = {'User-Agent' : random_agent}

def analise():
    os.system("clear")
    os.system("python3 analizer/hash-id.py ")

def arguments():
    parser = argparse.ArgumentParser()
    parser.description = 'HashCrack es una herramienta que te permitra crackear muchas familias de algoritmos con sus respectivas versiones. Entre los cuales se encuentran: MD5, SHA (1, 224, 256, 384, 512), SHA-3 (224, 256, 384, 512), blake2b'
    primary = parser.add_argument_group('Argumentos principales')
    parser.description = "   -a   --analyze   Analiza un has / Analyze a hash"
    args = parser.parse_args()

def sha1():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-20.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            x = hashlib.sha1(bytes(password, "utf-8")).hexdigest()
            if x == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
                print("[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def md5():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            y = hashlib.md5(bytes(password, "utf-8")).hexdigest()
            if y == hashes:
                    print(colores["H"]+"[+] La contraseña es: " + str(password))
                    exit()
            else:
                    print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha224():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            z = hashlib.sha224(bytes(password, "utf-8")).hexdigest()
            if z == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha256():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            m = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
            if m == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha512():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            a = hashlib.sha512(bytes(password, "utf-8")).hexdigest()
            if a == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha3_256():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            d = hashlib.sha3_256(bytes(password, "utf-8")).hexdigest()
            if d == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha384():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            b = hashlib.sha384(bytes(password, "utf-8")).hexdigest()
            if b == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def blake2b():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            w = hashlib.blake2b(bytes(password, "utf-8")).hexdigest()
            if w == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def blake2s():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            t = hashlib.blake2s(bytes(password, "utf-8")).hexdigest()
            if t == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
        pass
    except KeyboardInterrupt:
        print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
        print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def ripemd160():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            e = hashlib.new('ripemd160')(bytes(password, "utf-8")).hexdigest()
            if e == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha3_512():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            k = hashlib.sha3_512(bytes(password, "utf-8")).hexdigest()
            if k == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha3_224():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            s = hashlib.sha3_224(bytes(password, "utf-8")).hexdigest()
            if s == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha3_256():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            l = hashlib.sha3_256(bytes(password, "utf-8")).hexdigest()
            if l == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
            pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def sha3_384():
    try:
        hashes = input(colores["P"]+"Ingresa el texto encriptado: ")
        passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), "utf-8")
        for password in passwords.split("\n"):
            n = hashlib.sha3_384(bytes(password, "utf-8")).hexdigest()
            if n == hashes:
                print(colores["H"]+"[+] La contraseña es: " + str(password))
                exit()
            else:
                print(colores["M"]+"[+] Contraseña: " + str(password) + " no es la contraseña,probando con la siguiente...")
        print("\nLa contraseña no esta en este diccionario")
    except AttributeError:
        pass
    except KeyboardInterrupt:
            print("\n[+]Proceso detenido por el usuario")
    except ConnectionResetError:
            print("No se han podido leer las lineas del diccionario,verifica tu conexión a internet")

def hash_analyzer():
    os.system("clear")
    system = input("¿Esta en una distribución Linux como Kali o Parrot? [Y]|[N] / Is it on a Linux distribution like Kali or Parrot? [Y]|[N] >>> ")
    system_LOW = system.lower()
    if system_LOW == "y":
        os.system("python3 analizer/hash-id.py")
    elif system_LOW =="n":
        os.system("apt install pip")
        os.system("pip install requests")
        os.system("python3 analizer/hash-id.py")
def unicode():
#NOTE: No pude conseguir la forma de poner todo esto en un bucle while o for intente hacerlo pero no pude :(
# Por favor no se enoje si no logra conseguir decodificar o codificar por completo su texto a decimal Unicode 
#NOTE: Puede codificar y decodificar texto libremente y de una manera más fácil en: https://cryptii.com/pipes/text-decimal
    true_false = str(input("Quieres convertir texto en Unicode decimal? [y] / [n]: "))
    if true_false == "y":
        message = str(input("Ingresa una palabra: "))
        lon = int(input("Cuántas letras tiene tu mensaje(debe considerar los espacios): "))
        message = message.lower()
        try:
            if lon == 1:
                a = message[0]
                a = ord(a)
                print(a)
            elif lon == 2:
                a, b = message[0], message[1]
                a, b = ord(a), ord(b)
                print(a, b)
            elif lon == 3:
                a, b, c = message[0], message[1], message[2]
                a, b, c = ord(a), ord(b), ord(c)
                print(a, b, c)
            elif lon == 4:
                a, b, c, d = message[0], message[1], message[2], message[3]
                a, b, c, d = ord(a), ord(b), ord(c), ord(d)
                print(a, b, c, d)
            elif lon == 5:
                a, b, c, d, e = message[0], message[1], message[2], message[3], message[4]
                a, b, c, d, e = ord(a), ord(b), ord(c), ord(d), ord(e)
                print(a, b, c, d, e)
            elif lon == 6:
                a, b, c, d, e, f = message[0], message[1], message[2], message[3], message[4], message[5]
                a, b, c, d, e, f = ord(a), ord(b), ord(c), ord(d), ord(e), ord(f)
                print(a, b, c, d, e, f)
            elif lon == 7:
                a, b, c, d, e, f, g = message[0], message[1], message[2], message[3], message[4], message[5], message[6]
                a, b, c, d, e, f, g = ord(a), ord(b), ord(c), ord(d), ord(e), ord(f), ord(g)
                print(a, b, c, d, e, f, g)
            elif lon == 8:
                a, b, c, d, e, f, g, h = message[0], message[1], message[2], message[3], message[4], message[5], message[6], message[7]
                a, b, c, d, e, f, g, h= ord(a), ord(b), ord(c), ord(d), ord(e), ord(f), ord(g), ord(h)
                print(a, b, c, d, e, f, g, h)
            elif lon == 9:
                a, b, c, d, e, f, g, h, i = message[0], message[1], message[2], message[3], message[4], message[5], message[6], message[7], message[8]
                a, b, c, d, e, f, g, h, i = ord(a), ord(b), ord(c), ord(d), ord(e), ord(f), ord(g), ord(h), ord(i)
                print(a, b, c, d, e, f, g, h, i)
            elif lon == 10:
                a, b, c, d, e, f, g, h, i, j = message[0], message[1], message[2], message[3], message[4], message[5], message[6], message[7], message[8], message[9]
                a, b, c, d, e, f, g, h, i, j = ord(a), ord(b), ord(c), ord(d), ord(e), ord(f), ord(g), ord(h), ord(i), ord(j)
                print(a, b, c, d, e, f, g, h, i, j)
            else:
                pass
        except AttributeError:
            pass
    elif true_false == "n":
        question = str(input("Quieres hacer la desconversion de caracteres Unicode? [y] / [n]: "))
        if question == "y":
            lon_2 = int(input("Cuántas letras tiene tu mensaje(debe conaiderar los espacios): "))
            if lon_2 == 1:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    a = chr(a)
                    print("La palabra o texto en unicode decimal es: ", a)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 2:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    a, b = chr(a), chr(b)
                    print("La palabra o texto en unicode decimal es: ", a, b)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 3:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    a, b, c = chr(a), chr(b), chr(c)
                    print("La palabra o texto en unicode decimal es: ", a, b, c)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 4:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    a, b, c, d = chr(a), chr(b), chr(c), chr(d)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 5:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    e = int(input("Ingresa el quinto párrafo: "))
                    a, b, c, d, e = chr(a), chr(b), chr(c), chr(d), chr(e)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d, e)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 6:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    e = int(input("Ingresa el quinto párrafo del numero: "))
                    f = int(input("Ingresa el sexto párrafo del numero: "))
                    a, b, c, d, e, f = chr(a), chr(b), chr(c), chr(d), chr(e), chr(f)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d, e, f )
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 7:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    e = int(input("Ingresa el quinto párrafo del numero: "))
                    f = int(input("Ingresa el sexto párrafo del numero: "))
                    g = int(input("Ingresa el septimo párrafo del numero: "))
                    a, b, c, d, e, f, g = chr(a), chr(b), chr(c), chr(d), chr(e), chr(f), chr(g)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d, e, f, g)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 8:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    e = int(input("Ingresa el quinto párrafo del numero: "))
                    f = int(input("Ingresa el sexto párrafo del numero: "))
                    g = int(input("Ingresa el septimo párrafo del numero: "))
                    h = int(input("Ingresa el octavo párrafo del numero: "))
                    a, b, c, d, e, f, g, h = chr(a), chr(b), chr(c), chr(d), chr(e), chr(f), chr(g), chr(h)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d, e, f, g, h)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 9:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    e = int(input("Ingresa el quinto párrafo del numero: "))
                    f = int(input("Ingresa el sexto párrafo del numero: "))
                    g = int(input("Ingresa el septimo párrafo del numero: "))
                    h = int(input("Ingresa el octavo párrafo del numero: "))
                    i = int(input("Ingresa el noveno párrafo del numero: "))
                    a, b, c, d, e, f, g, h, i = chr(a), chr(b), chr(c), chr(d), chr(e), chr(f), chr(g), chr(h), chr(i)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d, e, f, g, h, i)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 10:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    e = int(input("Ingresa el quinto párrafo del numero: "))
                    f = int(input("Ingresa el sexto párrafo del numero: "))
                    g = int(input("Ingresa el septimo párrafo del numero: "))
                    h = int(input("Ingresa el octavo párrafo del numero: "))
                    i = int(input("Ingresa el noveno párrafo del numero: "))
                    j = int(input("Ingresa el decimo párrafo del numero: "))
                    a, b, c, d, e, f, g, h, i, j = chr(a), chr(b), chr(c), chr(d), chr(e), chr(f), chr(g), chr(h), chr(i), chr(j)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d, e, f, g, h, i, j)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            elif lon_2 == 11:
                try:
                    a = int(input("Ingresa el primer parrafo del número: "))
                    b = int(input("Ingresa el segundo parrafo del numero: "))
                    c = int(input("Ingresa el tercer parrafo del numero: "))
                    d = int(input("Ingresa el cuarto párrafo del numero: "))
                    e = int(input("Ingresa el quinto párrafo del numero: "))
                    f = int(input("Ingresa el sexto párrafo del numero: "))
                    g = int(input("Ingresa el septimo párrafo del numero: "))
                    h = int(input("Ingresa el octavo párrafo del numero: "))
                    i = int(input("Ingresa el noveno párrafo del numero: "))
                    j = int(input("Ingresa el decimo párrafo del numero: "))
                    k = int(input("Ingresa el onceavo párrafo del numero: "))
                    a, b, c, d, e, f, g, h, i, j = chr(a), chr(b), chr(c), chr(d), chr(e), chr(f), chr(g), chr(h), chr(i), chr(j), chr(k)
                    print("La palabra o texto en unicode decimal es: ", a, b, c, d, e, f, g, h, i, j, k)
                except ValueError:
                    print("[+] Debes ingresar números enteros correspondientes al cifrado decimal Unicode")
            else:
                print("Tu palabra tiene demasiadas letras, por favor visita la siguiente página en donde puedes hacer la desconversion de cualquier texto sin ningún problema ----> https://cryptii.com/pipes/text-decimal")
        else:
            print("Has elegido que no, adiós")
            exit()
    else:
        print("Opción incorrecta,solo puede poner <y> o <n>")
        exit()

def exit():
    print("\t\nGoodbye :)\n")
    sys.exit(1)

# ESPERO QUE LES SIRVA ESTA PEQUEÑA TOOL :)
# SI MODIFICAS ALGO AÑADE MI NOMBRE EN EL SCRIPT XD
