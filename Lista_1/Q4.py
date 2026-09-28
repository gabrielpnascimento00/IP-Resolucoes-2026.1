carne_misteriosa = float(input())
qjo_radioativo = float(input())
molho_especial = float(input())

if carne_misteriosa <= 0 or qjo_radioativo <= 0 or molho_especial <= 0:
    print('Vocês destruíram o parque! ESTÃO DESPEDIDOS!')

else:
    print('A receita não explodiu!')

    if carne_misteriosa == qjo_radioativo == molho_especial:
        print('Todas as medidas são iguais. Vocês criaram o Hambúrguer Supremo do Caos!')
    
    if carne_misteriosa > qjo_radioativo and carne_misteriosa > molho_especial:
        print('Havia muita carne! O Musculoso vai adorar esse Bifão de Dinossauro!')
    
    if qjo_radioativo > carne_misteriosa and qjo_radioativo > molho_especial:
        print('Tem queijo pra todo lado! Criamos uma Lasanha Dimensional!')
    
    if molho_especial > carne_misteriosa and molho_especial > qjo_radioativo:
        print('Panela cheia de molho e sorriso no rosto, criamos o Strogonoff da Paz!')
    
    if molho_especial == carne_misteriosa != qjo_radioativo or molho_especial == qjo_radioativo != carne_misteriosa or carne_misteriosa == qjo_radioativo != molho_especial:
        print('Tá tudo girando! Acabamos de criar um Buraco Negro Culinário!')
    
    print('OOOOOOOH! Mandaram bem, caras!')