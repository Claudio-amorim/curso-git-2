salário = float(input('Qual o seu salário? R$ '))
novo = salário + (salário * 15 / 100)
print('Seu salario era R${:.2f}e com aumento de 15% é R${:.2f}'.format(salário, novo))