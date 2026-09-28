
nome_maq1 = input()
qte_peças1 = int(input())
reacao_1 = input()

# Pontuação inicial 1
pontuacao_1 = len(nome_maq1) + qte_peças1

if 'i' in nome_maq1 and 'n' in nome_maq1 and 'a' in nome_maq1 and 't' in nome_maq1 and 'o' in nome_maq1 and 'r' in nome_maq1:
    pontuacao_1 -= 50
if 'Perry' in nome_maq1:
    pontuacao_1 += 20

# Reações
if reacao_1 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_1 += 30
elif reacao_1 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_1 += 20
elif reacao_1 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_1 += 10
elif reacao_1 == 'SÉRIO? SÓ ISSO?':
    pontuacao_1 -= 5
elif reacao_1 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_1 -= 10
elif reacao_1 == 'AH, ESQUECE…':
    pontuacao_1 -= 15

if nome_maq1 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_1 *= 2

if nome_maq1 == 'MáquinaDeBanhoForçado':
    pontuacao_1 -= 20

#=======================================================================

nome_maq2 = input()
qte_peças2 = int(input())
reacao_2 = input()

# Pontuação inicial 2
pontuacao_2 = len(nome_maq2) + qte_peças2
if 'i' in nome_maq2 and 'n' in nome_maq2 and 'a' in nome_maq2 and 't' in nome_maq2 and 'o' in nome_maq2 and 'r' in nome_maq2:
    pontuacao_2 -= 50
if 'Perry' in nome_maq2:
    pontuacao_2 += 20

# Reações
if reacao_2 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_2 += 30
elif reacao_2 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_2 += 20
elif reacao_2 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_2 += 10
elif reacao_2 == 'SÉRIO? SÓ ISSO?':
    pontuacao_2 -= 5
elif reacao_2 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_2 -= 10
elif reacao_2 == 'AH, ESQUECE…':
    pontuacao_2 -= 15

if nome_maq2 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_2 *= 2

if nome_maq2 == 'MáquinaDeBanhoForçado':
    pontuacao_2 -= 20

#=======================================================================

nome_maq3 = input()
qte_peças3 = int(input())
reacao_3 = input()

# Pontuação inicial 3
pontuacao_3 = len(nome_maq3) + qte_peças3
if 'i' in nome_maq3 and 'n' in nome_maq3 and 'a' in nome_maq3 and 't' in nome_maq3 and 'o' in nome_maq3 and 'r' in nome_maq3:
    pontuacao_3 -= 50
if 'Perry' in nome_maq3:
    pontuacao_3 += 20

# Reações
if reacao_3 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_3 += 30
elif reacao_3 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_3 += 20
elif reacao_3 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_3 += 10
elif reacao_3 == 'SÉRIO? SÓ ISSO?':
    pontuacao_3 -= 5
elif reacao_3 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_3 -= 10
elif reacao_3 == 'AH, ESQUECE…':
    pontuacao_3 -= 15

if nome_maq3 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_3 *= 2

if nome_maq3 == 'MáquinaDeBanhoForçado':
    pontuacao_3 -= 20

#=======================================================================

nome_maq4 = input()
qte_peças4 = int(input())
reacao_4 = input()

# Pontuação inicial 4
pontuacao_4 = len(nome_maq4) + qte_peças4
if 'i' in nome_maq4 and 'n' in nome_maq4 and 'a' in nome_maq4 and 't' in nome_maq4 and 'o' in nome_maq4 and 'r' in nome_maq4:
    pontuacao_4 -= 50
if 'Perry' in nome_maq4:
    pontuacao_4 += 20

# Reações
if reacao_4 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_4 += 30
elif reacao_4 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_4 += 20
elif reacao_4 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_4 += 10
elif reacao_4 == 'SÉRIO? SÓ ISSO?':
    pontuacao_4 -= 5
elif reacao_4 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_4 -= 10
elif reacao_4 == 'AH, ESQUECE…':
    pontuacao_4 -= 15

if nome_maq4 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_4 *= 2

if nome_maq4 == 'MáquinaDeBanhoForçado':
    pontuacao_4 -= 20


# Ordenando no placar

pos_1 = pontuacao_1
maq_1 = nome_maq1

pos_2 = pontuacao_2
maq_2 = nome_maq2

pos_3 = pontuacao_3
maq_3 = nome_maq3

pos_4 = pontuacao_4
maq_4 = nome_maq4

# Critérios de desempate

desempate1 = 0
desempate2 = 0
desempate3 = 0
desempate4 = 0

if (len(maq_1) > 15):
    desempate1 += 1
if (len(maq_2) > 15):
    desempate2 += 1
if (len(maq_3) > 15):
    desempate3 += 1
if (len(maq_4) > 15):
    desempate4 += 1
if (qte_peças1 > 25):
    desempate1 += 1
if (qte_peças2 > 25):
    desempate2 += 1
if (qte_peças3 > 25):
    desempate3 += 1
if (qte_peças4 > 25):
    desempate4 += 1

# Primeiro lugar 
if pos_1 < pos_2:
    pos_1, pos_2 = pos_2, pos_1
    maq_1, maq_2 = maq_2, maq_1
elif pos_1 == pos_2:
    if desempate1 < desempate2:
        pos_1, pos_2 = pos_2, pos_1
        maq_1, maq_2 = maq_2, maq_1
    if desempate1 == desempate2:
        if qte_peças1 < qte_peças2:
            pos_1, pos_2 = pos_2, pos_1
            maq_1, maq_2 = maq_2, maq_1
        elif qte_peças1 == qte_peças2:
            if len(maq_1) < len(maq_2):
                pos_1, pos_2 = pos_2, pos_1
                maq_1, maq_2 = maq_2, maq_1



if pos_1 < pos_3:
    pos_1, pos_3 = pos_3, pos_1
    maq_1, maq_3 = maq_3, maq_1

elif pos_1 == pos_3:
    if desempate1 < desempate3:
        pos_1, pos_3 = pos_3, pos_1
        maq_1, maq_3 = maq_3, maq_1
    if desempate1 == desempate3:
        if qte_peças1 < qte_peças3:
            pos_1, pos_3 = pos_3, pos_1
            maq_1, maq_3 = maq_3, maq_1
        elif qte_peças1 == qte_peças3:
            if len(maq_1) < len(maq_3):
                pos_1, pos_3 = pos_3, pos_1
                maq_1, maq_3 = maq_3, maq_1

if pos_1 < pos_4:
    pos_1, pos_4 = pos_4, pos_1
    maq_1, maq_4 = maq_4, maq_1

elif pos_1 == pos_4:
    if desempate1 < desempate4:
        pos_1, pos_4 = pos_4, pos_1
        maq_1, maq_4 = maq_4, maq_1
    if desempate1 == desempate4:
        if qte_peças1 < qte_peças4:
            pos_1, pos_4 = pos_4, pos_1
            maq_1, maq_4 = maq_4, maq_1
        elif qte_peças1 == qte_peças4:
            if len(maq_1) < len(maq_4):
                pos_1, pos_4 = pos_4, pos_1
                maq_1, maq_4 = maq_4, maq_1


# Segundo lugar
if pos_2 < pos_3:
    pos_2, pos_3 = pos_3, pos_2
    maq_2, maq_3 = maq_3, maq_2

elif pos_2 == pos_3:
    if desempate2 < desempate3:
        pos_2, pos_3 = pos_3, pos_2
        maq_2, maq_3 = maq_3, maq_2
    if desempate2 == desempate3:
        if qte_peças2 < qte_peças3:
            pos_2, pos_3 = pos_3, pos_2
            maq_2, maq_3 = maq_3, maq_2
        elif qte_peças2 == qte_peças3:
            if len(maq_2) < len(maq_3):
                pos_2, pos_3 = pos_3, pos_2
                maq_2, maq_3 = maq_3, maq_2

if pos_2 < pos_4:
    pos_2, pos_4 = pos_4, pos_2
    maq_2, maq_4 = maq_4, maq_2

elif pos_2 == pos_4:
    if desempate2 < desempate4:
        pos_2, pos_4 = pos_4, pos_2
        maq_2, maq_4 = maq_4, maq_2
    if desempate2 == desempate4:
        if qte_peças2 < qte_peças4:
            pos_2, pos_4 = pos_4, pos_2
            maq_2, maq_4 = maq_4, maq_2
        elif qte_peças2 == qte_peças4:
            if len(maq_2) < len(maq_4):
                pos_2, pos_4 = pos_4, pos_2
                maq_2, maq_4 = maq_4, maq_2

# Terceiro Lugar
if pos_3 < pos_4:
    pos_3, pos_4 = pos_4, pos_3
    maq_3, maq_4 = maq_4, maq_3

elif pos_3 == pos_4:
    if desempate3 < desempate4:
        pos_3, pos_4 = pos_4, pos_3
        maq_3, maq_4 = maq_4, maq_3
    if desempate3 == desempate4:
        if qte_peças3 < qte_peças4:
            pos_3, pos_4 = pos_4, pos_3
            maq_3, maq_4 = maq_4, maq_3
        elif qte_peças3 == qte_peças4:
            if len(maq_3) < len(maq_4):
                pos_3, pos_4 = pos_4, pos_3
                maq_3, maq_4 = maq_4, maq_3

print(f'1º lugar - {maq_1} : {pos_1} pontos')
print(f'2º lugar - {maq_2} : {pos_2} pontos')
print(f'3º lugar - {maq_3} : {pos_3} pontos')
print(f'4º lugar - {maq_4} : {pos_4} pontos')