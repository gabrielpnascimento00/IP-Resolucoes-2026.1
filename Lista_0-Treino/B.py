# Definir variaveis para o valor de X e Z de Tantan
# Definir variaveis para os valores de X e Z das vilas
# Definir a variavel Dist_Vila como a expressão de distancia euclidiana e realizar isso com todas as vilas
# Arredondar os valores com a formatação :.2f
# Printar todos os resultados

X_Tantan = int(input())
Z_Tantan = int(input())

X_Hogs = 34
Z_Hogs = 220

X_Kaka = 0
Z_Kaka = 0

X_Soli = 140
Z_Soli = 456

Dist_Hogs = ((X_Hogs - X_Tantan)**2 + (Z_Hogs - Z_Tantan)**2)**(1/2)

Dist_Kaka = ((X_Kaka - X_Tantan)**2 + (Z_Kaka - Z_Tantan)**2)**(1/2)

Dist_Soli = ((X_Soli - X_Tantan)**2 + (Z_Soli - Z_Tantan)**2)**(1/2)

print(f'Distancia para Hogsmeade: {Dist_Hogs:.2f}')
print(f'Distancia para Kakariko: {Dist_Kaka:.2f}')
print(f'Distancia para Solitude: {Dist_Soli:.2f}')