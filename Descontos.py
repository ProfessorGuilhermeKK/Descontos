print('Bem vindo a loja do Guilherme Klein Klug')
Valortotal= float(input('Entre com o valor do Produto:'))
Quantidade= int(input('Entre com o valor da Quantidade:'))
Valorsemdesconto= float(Valortotal*Quantidade)
print('O valor sem desconto foi R${}'.format(Valorsemdesconto))
if 0<Quantidade<=4:
    desconto = (0) #desconto de 0%
    valorcomdesconto = (Valorsemdesconto-Valorsemdesconto*desconto)
    print('O valor com desconto foi: R${}'.format(valorcomdesconto))
elif 5 <= Quantidade < 20:
    desconto = (0.03) # desconto de 3%
    valorcomdesconto = Valorsemdesconto - Valorsemdesconto * desconto
    print('O valor com desconto foi: R${} '.format(valorcomdesconto))
elif 20 <= Quantidade < 100:
    desconto = (0.06) # desconto de 6%
    valorcomdesconto = Valorsemdesconto - Valorsemdesconto * desconto
    print('O valor com desconto foi: R${} '.format(valorcomdesconto))
elif Quantidade >= 100:
    desconto = (0.10)  #desconto de 10%
    valorcomdesconto = Valorsemdesconto - Valorsemdesconto * desconto
    print('O valor com desconto foi: R${} '.format(valorcomdesconto))
