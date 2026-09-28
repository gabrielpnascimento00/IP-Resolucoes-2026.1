# Definir uma variavel para o input
# Dividir o valor de packs por 3 e usar função int() para obter o número inteiro e não o decimal e defini-lo como V
# Multiplicar o resultado obtido por 3 e subtrair do total a fim de descobrir o resto dessa divisão e defini-lo como F
# Printar ambos os resultados

P = int(input())
V = int(P/3)
F = int(P - V*3)
print(V)
print(F)