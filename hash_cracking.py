import decryption
from sys import argv
from argparse import ArgumentParser

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


if len(argv) != 1:
    if argv[1] == "-a":
        decryption.analise()
    else:
        parse = ArgumentParser()
        parse.description = "   -a   --analyze   Analiza un has / Analyze a hash"
        parse.add_argument("-eje1", "--ejemplo1", help="ejemplo1")
        parse = parse.parse_args()
        print(ejemplo1, ' ', ejemplo2)
else:
    pass

print(colores["K"]+"""

Elige el tipo de hash a desencriptar / Choose the type of hash to decrypt


        [1] SHA1
        [2] MD5                             [50] Convertir y desconvertir texto Unicode(Decimal)
        [3] SHA224                             /  Convert and Unconvert Unicode (Decimal) Text   
        [4] SHA256
        [5] SHA512
        [6] SHA3_256
        [7] SHA384                          [99] Analizar un hash / Analyze a hash
        [8] BLAKE2B_512
        [9] BLAKE2S_256
        [10] RIPEMD160
        [11] SHA3_512
        [12] SHA3_224
        [13] SHA3_256
        [14] SHA3_384
        [15] Salir / exit


        """)

o = int(input(colores["K"]+"\nEscoge una opción / Choose an option: "))

if o == 1:
    decryption.sha1()
elif o == 2:
    decryption.md5()
elif o == 3:
    decryption.sha224()
elif o == 4:
    decryption.sha256()
elif o == 5:
    decryption.sha512()
elif o == 6:
    decryption.sha3_256()
elif o == 7:
    decryption.sha384()
elif o == 8:
    decryption.blake2b()
elif o == 9:
    decryption.blake2s()
elif o == 10:
    decryption.ripemd160()
elif o == 11:
    decryption.sha3_512()
elif o == 12:
    decryption.sha3_224()
elif o == 13:
    decryption.sha3_256()
elif o == 14:
    decryption.sha3_384()
elif o == 15:
    decryption.exit()
elif o == 50:
    decryption.unicode()
elif o == 99:
    decryption.hash_analyzer()
else:
    print("La opción que has elegido no existe / The option you have chosen does not exist")

