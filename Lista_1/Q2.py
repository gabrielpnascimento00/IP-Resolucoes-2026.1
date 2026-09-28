veloc_IJ = int(input())
veloc_LR = int(input())
dific_inimigos = int(input())

pontuação = (veloc_IJ * veloc_LR) / dific_inimigos

if pontuação > 153000:
    print('IMPOSSÍVEL!!! A DUPLA IMPLACÁVEL FOI CAPAZ DE QUEBRAR O RECORDE INALCANÇÁVEL DO JOREL!')

elif pontuação > 99000 or pontuação == 153000:
    print('SENSACIONAL!! Os jogadores conseguiram alcançar o pódio do jogo ao lado das outras pontuações do Jorel.')

elif pontuação > 65000 or pontuação == 99000:
    print('INCRÍVEL! A dupla conseguiu alcançar o top 10 nas pontuações do jogo.')

else:
    print('BRUTAL! Ninguém jamais conseguiu alcançar as pontuações fantásticas do Jorel.')