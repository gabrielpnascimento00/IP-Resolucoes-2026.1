# Definir variaveis para a qte de casas das vilas, a qte de dias, o tempo gasto, a qte de ticks e a qte total de hrs de jogo
# Multiplicar a qte de dias pelas 3 horas diarias p/ descobrir a qte de horas totais de jogo
# Dividir a qte total de horas pelos 20 min e multiplicar esse valor pelos 24000 ticks p descobrir ticks totais
# Dividir o valor de ticks totais por 2 para isolar os ticks diurnos e depois dividir pela qte de casas das vilas

dias_jogo = int(input())
qte_casas = int(input())

ticks_dia_m = 24000
tempo_dia_m_min = 20

min_jogo = (dias_jogo * (3*60))
dias_no_jogo = (min_jogo / 20)
ticks_totais = (dias_no_jogo * ticks_dia_m)

ticks_constr_casa = int((ticks_totais / 2) / qte_casas)

print(ticks_constr_casa)