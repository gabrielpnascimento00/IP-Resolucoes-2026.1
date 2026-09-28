energia_danny = input()
tipo_fantasma = input() #Comum, raro, chefe ou tipo desconhecido
energia_fantasma = input()
nome_fantasma = input()
nome_fantasma = nome_fantasma.lower()
portal_instavel = input() #Sim ou não

print('CInFantasma - Defesa Sobrenatural do CIn!')

if energia_danny.isdigit() and energia_fantasma.isdigit():
    energia_fantasma = int(energia_fantasma)
    energia_danny = int(energia_danny)
if 'king' in nome_fantasma or 'lord' in nome_fantasma:
    print('O Scanner detectou um possível fantasma de elite!')

    if len(nome_fantasma) > 12:
        print('O nome do fantasma é assustadoramente longo...')

    if portal_instavel == 'sim':
        print('O portal da Zona Fantasma continua instável!')

    else:
        print('O portal parece estar temporariamente estável.')

    if tipo_fantasma != 'comum' and tipo_fantasma != 'raro' and tipo_fantasma != 'chefe' and energia_fantasma >= 70:
        print('Um fantasma misterioso apareceu no CIn!')

    if tipo_fantasma == 'chefe' and energia_fantasma >= 80 and energia_danny >= energia_fantasma:
        print('Danny ativou o Modo Fantasma Total!')

    elif tipo_fantasma == 'raro' and energia_fantasma >= 50 and energia_danny >= energia_fantasma:
        print('Danny capturou o fantasma com o Fenton Thermos!')

    elif energia_fantasma < 20:
        print('Danny decidiu apenas observar o fantasma.')

    elif energia_fantasma > energia_danny:
        print('Danny percebeu que o fantasma é forte demais e decidiu recuar!')

    else:
        print('Danny enfrentou o fantasma normalmente!')

else:
    print('Erro no Scanner Fenton: nível de energia inválido!') 