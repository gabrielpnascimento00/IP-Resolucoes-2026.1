# Definir variaveis para as qte de diamantes e para o tempo da competicao
# Comparar todos os valores obtidos
# (Como printar o maior sem IF???)

Rend_Art = int(input())
Rend_Luiz = int(input())
Rend_Pedro = int(input())
Tempo_Compet = int(input())

Qte_Art = (Rend_Art * Tempo_Compet)
Qte_Luiz = (Rend_Luiz * Tempo_Compet)
Qte_Pedro = (Rend_Pedro * Tempo_Compet)

comp_1 = int((Qte_Art + Qte_Luiz + abs(Qte_Art - Qte_Luiz))/ 2)

comp_2 = int((comp_1 + Qte_Pedro + abs(comp_1 - Qte_Pedro))/ 2)

print(comp_2)