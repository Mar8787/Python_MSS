# 5. Programa que muestre en líneas separadas lo siguiente:
# ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
# WXVUTSRQPONMLKJIHGFEDCBA, ..., DCBA, CBA, BA, A

letras = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
print(letras)
for i in range(1, len(letras)):
    print(letras[i:])