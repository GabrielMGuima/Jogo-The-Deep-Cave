vida = 250
Soldados_de_Aizen = 50
esqueletos = 75
Monstro_Marinho = 100
boss_final = 250


from time import sleep
import sys
import random

def verifica_vida(vida):
 if vida <=0: sys.exit(print('Gamer Over'))
 
def slowprint(texto, atraso=0.0001): 
     for c in texto:
        print(c, end='', flush=True)
        sleep(atraso)

slowprint("""
______________________________________________________________________________________________
                            
                                         The Deep Cave
______________________________________________________________________________________________          
\n \n \n""")

slowprint(f'''  Há muito tempo, em uma terra repleta de mistérios e perigos, existia uma caverna conhecida como a Caverna Profunda.\n Diziam que ela era habitada por criaturas sombrias, tesouros esquecidos e segredos antigos.\n Aventureiros corajosos se aventuravam em suas profundezas, mas nenhum de voltou de lá.       
          ''')

nome = input('\n Digite Seu Nome =>')

slowprint(f'''
 Nosso herói(na), um(a) jovem chamado(a) {nome}, sonhava em se tornar um grande guerreiro(a).
 Ele ouvia histórias sobre a Caverna Profunda desde a infância e estava determinado a explorá-la.
 Com sua espada enferrujada e uma tocha, ele entrou na escuridão.
 As paredes da caverna eram úmidas e gotejantes. O ar cheirava a mofo e medo.
 Mesmo assim o(a) corajoso(a) {nome} avançou
 As Aranhas Gigantes te atacam o que você faz ?
         ''')

menu = """
[1] Atacar
[2] Tentar Fugir
=> """

while True:
  
 opcao = int(input(menu))
 if opcao == 1: 
     atacar = random.randint(5,20)
     if atacar >= 0: 
         Soldados_de_Aizen -= atacar 
         dano = random.randint(5,10)
         vida -= dano
         
         if Soldados_de_Aizen >= 1:
            slowprint(f'\n Você atacou os soldados e eles ainda tem {Soldados_de_Aizen} de vida, eles revidaram e você está com {vida} de vida. \n O que você fará?')
         
         if Soldados_de_Aizen <= 0:
            slowprint(f'Você conseguiu derrotar os soldados de! ')
            break
         if vida <=0:
            slowprint(f'Você foi derrotado pelos soldados ! ')
            break

 if opcao == 2: 
   fuga = random.randint(0,10)
   if fuga >5: slowprint('\n Você conseguiu escapar')
   if fuga >5:break
   if fuga <=5: slowprint('\n Os soldados de aizen o acertou enquanto você tentava fugir')
   if fuga <=5: print('\n\n Gamer Over')
   sys.exit()
 

slowprint(f'\nApós passar pelos soldados, {nome} consegue adentrar mais profundo na Caverna... \nVocê está explorando e ouve barulho de ossos se chocando, ao se virar para o local de onde vem o som, percebe que os esqueletos estão próximos de você \n\nQuando de repente.....\n\nEsqueletos vivos te atacam!!! ')

while True:
   opcao = int(input(menu))
   if opcao == 1: 
     atacar = random.randint(5,20)
     if atacar >= 0: 
         esqueletos -= atacar 
         dano = random.randint(4,30)
         vida -= dano
         if esqueletos >= 1: slowprint(f'\n Você atacou os Esqueletos e eles ainda tem {esqueletos} de vida, eles revidaram e você está com {vida} de vida. \n O que você fará?')
         if esqueletos <=0:
            slowprint(f'Você conseguiu derrotar os Esqueletos! ')
            break
         if vida <=0:
            slowprint(f'Você foi derrotado pelos Esqueletos! ')
            break
   if opcao == 2: 
    fuga = random.randint(0,10)
    if fuga >=4:slowprint('\n Você conseguiu escapar')
    if fuga >=4:break
    if fuga <=3: slowprint('\n Os Esqueletos te mataram enquanto você tentava fugir')       
    if fuga <=3: print('\n\n Gamer Over')
    sys.exit()
  
                  
slowprint(f'''
 \n\n Após o ocorrido {nome} encontrou escritas antigas nas paredes, revelando pistas sobre o no coração da caverna \n Adentrando mais na caverna em uma câmara profunda, {nome} descobriu um lago subterrâneo\n Sua superfície era calma e lá {nome} para e cuida dos seus ferimentos.''')
sleep(2)
cuidado = random.randint(50,100)
vida += cuidado

slowprint(f'\n\n Recuperando {cuidado} de sua vida que agora está {vida}\n Quando inesperadamente algo se moveu abaixo do lago subterrâneo e {nome} olha com curiosidade\n Mergulhando então nosso herói(ina) {nome} a vista uma cidade submersa habitada por criaturas aquáticas\n Olhando mais atentamente, {nome} a vista um Monstro Marinho que estava ameaçando a cidade \n Bravemente nosso herói(ina) brande sua espada e parte para cima do monstro!\n\n')

while True:
   opcao = int(input(menu))
   if opcao == 1: 
      atacar = random.randint(5,20)
      if atacar >= 0: 
       Monstro_Marinho -= atacar 
       dano = random.randint(4,30)
       vida -= dano
       if Monstro_Marinho >= 1: slowprint(f'\n Você atacou o Monstro Marinho e ele ainda tem {Monstro_Marinho} de vida, ele revidou com um ataque e você está com {vida} de vida \n O que você fará?')
       if Monstro_Marinho <=0: break
   if vida <=0: break
   if opcao == 2:
      slowprint(' \nNão tem como fugir Agora! \n Nosso herói está determinado a defender a cidade')
   #continue

slowprint(f'\n\n Após a dura Batalha\n os Habitantes recebem {nome} com desconfiança \n Mas {nome} Provou sua coragem e honra ao Enfrentar O Temido Monstro Marinho' )

slowprint(f'\nDepois de descansar em uma das hospedagens da cidade\n Os cidadões lhe presenteiam com equipamentos novos e poderosos \n é{nome} Segue seu caminho pela caverna \n Encontrando duas Rotas')

slowprint(f'\n O da Esquerda era calmo e silencioso so emitindo um calmo som de vento \n E o da Direita se escutava um som de goteira é um cheiro de madeira velha')
rota = input('\nQual Caminho Você Escolhe o da [1] Direita  Ou o [2] da Esquerda: ')

if rota == '1':
 slowprint(f'''
 \n\n Segue o caminho da esquerda e então {nome} Encontra um velho Sábio \n Que conta sobre um poderoso guardião \n Uma criatura ancestral que protegia um Grandioso Tesouro chamado de A Pedra da Eternídade: dízia-se que quem a possuísse teria poderes inimagináveis.
 hahahahaha você tem muita sorte! está no caminho certo! siga em frente que você irá direto ao guardião.
                                     ''')

elif rota == '2':
 slowprint(f'''\n 
 {nome} avança pelo caminho da direita e cai em uma armadinha e encontra alguns monstros de níveis inferiores.
 Já com os sua experiência das batalhas anteriores, os derrota de maneira fácil.
 então ele pergunta para um dos monstros que aibda estava vivo.''')

 slowprint(f'''
 {nome} : Qual é o segredo desse caverna que tanto falam?
 
 Monstro ferido : Eu não sei'
 
 {nome} : Desembucha logo maldito, não sou tão piedoso assim'
 
 Monstro ferido : Eu não sei muito sobre, mas há um guardião que possui a pedra da eternidade. Dizem que quem adquiri-la irá obter um poder grandioso. 
 
 {nome} : Como eu faço para ir até ele?
 
 Monstro ferido : Você tem deve ir seguir esse caminho, assim possivelmente encontrará o guardião

 {nome} : Se a informação não foi verdadeira, eu volto aqui e acabo com vida!

 {nome} foi de encontro até o Guardião
         ''')

slowprint(f''' Chegando no habitat que o Guardião vive já é questionado pelo próprio:
 
 Guardião: Quem é você? 
           
 {nome}: Meu nome é {nome}!
  
 Guardião: O que você quer comigo???

 {nome}: Ouvi dizer que você tem uma tal de Pedra da Eternidade que pode conceder poder a quem a obtêm!

 Guardião:.......

 Guardião: Certamente! e para que você deseja poder?

 {nome}: Para virar o maior aventureiro de todos!

 Guardião: Já que o que eu ouço é verdade e posso ver com meus olhos os sentimentos das pessoas, lhe concederei A Pedra da Eternidade! 

 Guardião: Entretanto você terá que responder 3 perguntas para que eu a entregue!

 {nome}: Ok! Estou pronto pode vir!

                ''')

tentativa = 5
erro =1


def verifica_vida(tentativa):
 if tentativa <=0: sys.exit(print('Gamer Over'))

while True:
    resposta_1 = input('O que é o que é: quanto mais eu tiro, mais eu tenho?')
    tentativa -= erro
    if resposta_1 == 'Fotografia' or resposta_1 == 'fotografia' or resposta_1 == 'Fotos' or resposta_1 == 'fotos':
        slowprint
        ('\n certa resposta')
        break
    
    if resposta_1  != 'Fotografia' or resposta_1 == 'fotografia' or resposta_1 == 'Buraco' or resposta_1 == 'buraco' or resposta_1 == 'Fotos' or resposta_1 == 'fotos':
        if tentativa == 0: sys.exit(print("game over"))
        slowprint(f'\n voce tem {tentativa} chances para acertar!')
        slowprint('*DICA* Serve para solidificar memorias.')
slowprint('\nGuardião: Proxima charada, essa é um pouco mais dificil, quero ver voce acertar')

while True:
    resposta_2 = input('O que é o que é: Quanto mais seca, mais fica molhada? :')
    tentativa -= erro
    if resposta_2 == 'A toalha' or resposta_2 =='a Toalha' or resposta_2 == 'A Toalha' or resposta_2 == 'a toalha' or resposta_2 == 'toalha' or resposta_2 == 'Toalha':
       slowprint('\nCerta resposta!')
       break
    
    if resposta_2 != 'A toalha' or resposta_2 =='a Toalha' or resposta_2 == 'A Toalha' or resposta_2 == 'a tolha' or resposta_2 == 'toalha' or resposta_2 == 'Toalha':
        if tentativa == 0: sys.exit(print("game over"))
        slowprint(f'\n voce tem {tentativa} chances para acertar!')
        slowprint('\n*DICA* Tem no banheiro ')

slowprint('Parabéns você adquiriu a Pedra da Eternidade e agora obteve mais poder!')
cuidado = random.randint(100,250)
vida += cuidado
slowprint('Você está no caminho de volta e se depara com um homem suspeito que diz para você o entregar a Pedra!!!')

menu = """
[1] ATACAR
[2] DEFENDER
=> """

while True:
  
 opcao = int(input(menu))
 if opcao == 1: 
     atacar = random.randint(20, 50)
     if atacar >= 0: 
         boss_final -= atacar 
         dano = random.randint(15,30)
         vida -= dano
         if vida <=0: sys.exit(print('Gamer Over'))
         if boss_final >= 1:
            slowprint(f'\n Você atacou o homem  \n Ele ainda tem {boss_final} de vida\n Ele Revidou \n E você está com {vida} de vida \n o que Você fará?')
         
         if boss_final<= 0: 
            slowprint('Você venceu jogo! e se torno um aventureiro lendário :D')
            break
         if vida <=0: 
            slowprint('Você morreu! muito fraquinho XD')
            break
 
 if opcao == 2:
    defesa = random.randint(0,10)
    if defesa >= 0:
       vida -= defesa
       if boss_final <= 0: break
       if vida <=0: sys.exit(print('Gamer Over'))
       slowprint(f'defesa de {defesa} sua vida é de {vida}')
