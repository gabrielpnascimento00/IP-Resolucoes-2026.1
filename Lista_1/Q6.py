robin_disp = input()
estelar_disp = input()
ciborgue_disp = input()
ravena_disp = input()
mutano_disp = input()

qte_candidatos = 0
if robin_disp == 'S':
    qte_candidatos += 1

if estelar_disp == 'S':
    qte_candidatos += 1

if ciborgue_disp == 'S':
    qte_candidatos += 1

if ravena_disp == 'S':
    qte_candidatos += 1

if mutano_disp == 'S':
    qte_candidatos += 1

amor_no_ar_robin = robin_disp == 'S' and estelar_disp == 'S' and ciborgue_disp == 'N' and ravena_disp == 'N' and mutano_disp == 'N'
amor_no_ar_ravena = ravena_disp == 'S' and mutano_disp == 'S' and ciborgue_disp == 'N' and robin_disp == 'N' and estelar_disp == 'N'
disputa_tofu = mutano_disp == 'S' and ciborgue_disp == 'S' and robin_disp == 'N' and estelar_disp == 'N' and ravena_disp == 'N'
solo = qte_candidatos == 1

if robin_disp == 'S' and estelar_disp == 'S' and ciborgue_disp == 'S' and ravena_disp == 'S' and mutano_disp == 'S':
    print('Em toda a vida do Batman, ele nunca viu um lugar tão caótico quanto a torre dos titãns depois da notícia, nem mesmo Gotham, com isso ele percebe que não seria ali o local ideal para encontrar o novo salvador da terra!')
    print('Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT.')
    print('Que bom que tudo deu certo, sem dificuldades!')

else:
    if robin_disp == 'N' and estelar_disp == 'N' and ciborgue_disp == 'N' and ravena_disp == 'N' and mutano_disp == 'N':
        print('Parece que ninguém quer participar da Liga da Justiça, o Batman vai ter que ouvir um Super-Esculacho do Super-Homem por não ter conseguido ninguém super forte!')
        print('Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT.')
        print('Que bom que tudo deu certo, sem dificuldades!')

    
    if solo == True:
        if robin_disp == 'S' and estelar_disp == 'N' and ciborgue_disp == 'N' and ravena_disp == 'N' and mutano_disp == 'N':
            selecionado = 'Robin'
            print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
            print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
            print('Que bom que tudo deu certo, sem dificuldades!')

        elif ravena_disp == 'S' and robin_disp == 'N' and estelar_disp == 'N' and ciborgue_disp == 'N' and mutano_disp == 'N':
            selecionado = 'Ravena'
            print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
            print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
            print('Que bom que tudo deu certo, sem dificuldades!')

        elif estelar_disp == 'S' and robin_disp == 'N' and ciborgue_disp == 'N' and mutano_disp == 'N' and ravena_disp == 'N':
            selecionado = 'Estelar'
            print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
            print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
            print('Que bom que tudo deu certo, sem dificuldades!')

        elif ciborgue_disp == 'S' and robin_disp == 'N' and estelar_disp == 'N' and mutano_disp == 'N' and ravena_disp == 'N':
            selecionado = 'Ciborgue'
            print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
            print('BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...')
            print('Que bom que tudo deu certo, sem dificuldades!')

        elif mutano_disp == 'S' and robin_disp == 'N' and estelar_disp == 'N' and ciborgue_disp == 'N' and ravena_disp == 'N':
            selecionado = 'Mutano'
            print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
            print('O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!')
            print('Que bom que tudo deu certo, sem dificuldades!')


    # Casos especiais
    # Caso Amor no Ar
    if amor_no_ar_robin == True:
        selecionado = 'Estelar'
        print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
        print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
        print('Parece que o cavalherismo ainda não morreu não é mesmo?')

    elif amor_no_ar_ravena == True:
        selecionado = 'Ravena'
        print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
        print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
        print('Parece que o cavalherismo ainda não morreu não é mesmo?')

    # Caso disputa de Tofu
    elif disputa_tofu == True:
        qte_mutano = int(input())
        qte_ciborgue = int(input())
        if qte_mutano > qte_ciborgue:
            selecionado = 'Mutano'
            print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
            print(f'O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!')
        elif qte_ciborgue > qte_mutano:
            selecionado = 'Ciborgue'
            print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
            print('BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...')
        else:
            escolhido = input()
            if escolhido == 'Mutano':
                selecionado = 'Mutano'
                print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
                print('O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!')
            else:
                selecionado = 'Ciborgue'
                print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
                print('BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...')
        print('Nem uma competição árdua assim pode abalar a amizade desses caras!')
    elif qte_candidatos > 2 and qte_candidatos < 5:
        if robin_disp == 'S':
            selecionado = 'Robin'
            print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
            print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
            print('Que bom que tudo deu certo, sem dificuldades!')
        elif ravena_disp == 'S':
            selecionado = 'Ravena'
            print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
            print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
            print('Que bom que tudo deu certo, sem dificuldades!')
        elif ravena_disp == 'N':
            selecionado = 'Ravena'
            print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
            print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
            print('O Batman não iria perder a chance de ter um dos seres mais poderosos do Universo DC no time, o preparo dele não permite isso!')
    else:
        if qte_candidatos == 2 and amor_no_ar_ravena == False and amor_no_ar_robin == False and disputa_tofu == False:
            if robin_disp == 'S':
                selecionado = 'Robin'
                print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
                print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
                print('Que bom que tudo deu certo, sem dificuldades!')
            elif ravena_disp == 'S':
                selecionado = 'Ravena'
                print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
                print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
                print('Que bom que tudo deu certo, sem dificuldades!')
            elif estelar_disp == 'S':
                selecionado = 'Estelar'
                print(f'Mesmo com {qte_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
                print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
                print('Que bom que tudo deu certo, sem dificuldades!')