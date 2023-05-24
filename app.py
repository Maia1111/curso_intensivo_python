idade = 37.5 
print(type(idade))

dado = 1 
print(type(dado))


dado2 = True
print(type(dado2))


dado3 = "37.5"
print(type(dado3))


dado4 = "37"
print(type(dado4))

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


print(f" Meu nome é {nome} e minha idade é {idade} anos")

print("Meu nome é {} e minha idade é {} anos".format(nome, idade))


if idade > 18:
    print("Maior de idade")
else:
    print("Menor de idade")



print(False and False)