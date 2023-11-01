def fatorial(n,show=''): # Função que mostra o fatorial de um número e se show==true a conta é mostrada.
    f=1
    for c in range(n,0,-1):
        if show==True:
            print(f'{c}', end=' ')
            if c>1:
                print(f'*',end=' ')
            else:
                print('=',end=' ')
        f*=c
    print(f'{f}')
    return f


fatorial(4,show=True)

