def inverter_string(s):
    resultado = ""
    for caractere in s:
        resultado = caractere + resultado
    return resultado

entrada = input("Digite uma string para inverter: ")
string_invertida = inverter_string(entrada)
print(f"String original: {entrada}")
print(f"String invertida: {string_invertida}")
