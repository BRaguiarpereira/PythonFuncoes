'''
Funcoes
subprograma (rotina,metodo,etc)que executa uma tarefa ,
normalmente dentro de um programa maior.

No Python
def nomedafuncao(parametros):
 instrucoes

'''
def saudacao():
    nome = input('Qual seu nome?')
    print('ola,{}, boa noite'.format(nome))
    
'''
O programa sem a funcao da erro

print('aula de ipe')
saudacao()

Uma funcao pode receber um parametro ,ou seja,um valor de entrada

'''
'''
Return
uma funcao pode retornar um valor
(no caso do python,mais de um , na forma de uma tupla)
'''
#funcao tabuada
def tabuada(n):
    for i in range(0,11):
        x = n*i
        print('{}X{}={}'.format(n,i,x))
tabuada(3)

#calcula  e retorna o fatarial de um numero

def fatorial(n):
    fat = 1
    for i in range(1,n+1):
        fat=fat*i
    return fat
f=fatorial(4)
print(f)

# funcao de combinacao

def combin (n,p):
    c=fatorial(n)/(fatorial(p)*fatorial(n-p))
    return c
a = int(input('N de ele :'))
b = int(input('N de sub :'))
c = combin(a,b)
print(c)


        
