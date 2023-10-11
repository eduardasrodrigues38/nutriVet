def calcular_imc(peso, comprimento):
    peso_kg = float(peso)
    comprimento_m = float(comprimento) / 100 
    imc = peso_kg / (comprimento_m ** 2)
    return imc

with open('dados_NutriVet.txt', 'r') as arquivo:
    pets = []
    for linha in arquivo:
        partes = linha.strip().split(', ')
        dados = {}
        for parte in partes:
            chave, valor = parte.split(': ')
            dados[chave] = valor
        pets.append(dados)

for pet in pets:
    imc = calcular_imc(pet['Peso'], pet['Comprimento'])
    pet['IMC'] = imc

with open('dados_NutriVet.txt', 'w') as arquivo:
    for pet in pets:
        arquivo.write(f"Tutor: {pet['Tutor']}, E-mail: {pet['E-mail']}, Senha: {pet['Senha']}, Nome: {pet['Nome']}, Idade: {pet['Idade']}, Peso: {pet['Peso']}, Comprimento: {pet['Comprimento']}, Raca: {pet['Raca']}, IMC: {pet['IMC']},\n")
