# Criar uma variavel para a qte de diamantes que Tantan precisa
# Comparar essa variavel com as qtes oferecidas pelos amigos usando condicionais

qte_dima = int(input())

qte_art = 10
qte_luiz = 30
qte_pedro = 100

if qte_dima <= qte_art:
    print('Arthur')

if qte_dima <= qte_luiz and qte_dima > qte_art:
    print('Luiz')

if qte_dima <= qte_pedro and qte_dima > qte_luiz:
    print('Pedro')

if qte_dima > qte_pedro:
    print('Nenhum')