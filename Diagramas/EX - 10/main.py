salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
total_vendido = float(input("Digite o total vendido no mês: R$ "))

comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao

print("Comissão: R$", comissao)
print("Salário total: R$", salario_total)