def atualizar_dados(pet, campo, novo_valor):
    campos_validos = {
        'Nome': 'Nome',
        'Peso': 'Peso',
        'Comprimento': 'Comprimento',
        'Idade': 'Idade',
        'Email': 'Email',
        'Senha': 'Senha',
        'Tutor': 'Tutor',
        'Raca': 'Raca'
    }

    if campo in campos_validos:
        pet[campos_validos[campo]] = novo_valor

quant = int(input("Digite a quantidade de Pets que tem na lista: "))
pets = []

for x in range(quant):
    nome_tutor = input("Digite o seu nome: ")
    email_tutor = input("Digite o seu e-mail: ") 
    senha_tutor = input("Defina a sua senha de acesso: ")
    nome = input("Digite o nome do seu Pet: ")
    idade = input("Digite a idade do seu Pet: ")
    comprimento = input("Digite o comprimento do seu Pet: ")
    raca = input("Digite a raça do seu Pet: ")   
    massa = input("Digite o peso do seu Pet (ex: 8.100): ") 

    pets_info = {
        'Nome': nome,
        'Idade': idade,
        'Comprimento': comprimento,
        'Raca': raca,
        'Peso': massa,
        'Tutor': nome_tutor,
        'Email': email_tutor,
        'Senha': senha_tutor
        }
    
    pets.append(pets_info)

with open('dados_NutriVet.txt', 'a') as arquivo:
    for pet in pets:     
        arquivo.write(f"Tutor: {pet['Tutor']} , Email: {pet['Email']} , Senha: {pet['Senha']} , Nome: {pet['Nome']} , Idade: {pet['Idade']} , Peso: {pet['Peso']} , Comprimento: {pet['Comprimento']} , Raca: {pet['Raca']}\n")

with open('dados_NutriVet.txt', 'r') as arquiv:
    conteudo = arquiv.read()
    print(conteudo)

nome_para_atualizar = input("Digite o nome do tutor que você deseja atualizar os dados da conta: ")
encontrado = False

for pet in pets:
    if pet['Tutor'] == nome_para_atualizar:
        encontrado = True
        break

if encontrado:
    campo_para_atualizar = input(f"Digite o campo que você deseja atualizar para {nome_para_atualizar}: ").capitalize()

    if campo_para_atualizar in pets_info:
        novo_valor = input(f"Digite o novo valor para {campo_para_atualizar}: ")
        atualizar_dados(pet, campo_para_atualizar, novo_valor)

        with open('dados_NutriVet.txt', 'w') as arquivo:
            for e in pets:
                arquivo.write(f"Tutor: {e['Tutor']} , Email: {e['Email']} , Senha: {e['Senha']} , Nome: {e['Nome']} , Idade: {e['Idade']} , Peso: {e['Peso']} , Comprimento: {e['Comprimento']} , Raca: {e['Raca']}\n")

        print(f"{campo_para_atualizar} de {nome_para_atualizar} foi atualizado com sucesso!")
    else:
        print("Campo inválido. Por favor, digite um campo válido.")
else:
    print(f"{nome_para_atualizar} não foi encontrado na lista de contatos.")
