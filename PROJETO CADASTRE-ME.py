from datetime import datetime
import random 


print("Bem-Vindo a Empresa MAGIC")
print("Preencha o formulario a baixo para fazer cadastro na empresa")

Nome = input("Digite seu nome completo: ")
Idade = int(input("Digite sua Idade: "))
Aniversario = input("Digite sua data de aniversario: ")


dia_do_Registro = datetime.now()
print('Parabéns você se cadastrou no dia', dia_do_Registro)

print('você receberá um dos cartoes aleatoriamente por ter se cadastrado na empresa')
cartoes = ['R$50,00','R$250,00','R$120,00']
print(cartoes)


print(f'Olá', Nome , 'seu registro foi concluído com sucesso no dia', dia_do_Registro)
print("Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de: ", random.choice(cartoes))
