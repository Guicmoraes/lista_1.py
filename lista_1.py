# Definição da classe Mago 

#1. Adicione mais 2 atributos e 2 métodos à classe Mago. 

class Mago:
    # Atributos de classe
    possuiMagia = True
    #Novos atributos:
    vida = 50 
    possui_artefato = True

    # Método construtor
    def __init__(self, nome, idade, escola):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola 
        print('Mago ', self.nome, ' foi criado!')

    # Outros métodos    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def cumprimentar(self,nome):
        print('Ola, ', nome)
    
    #Novos métodos:
    def bicar(self):
        print('quack!!!')
    
    def dormir(self):
        print('ZZZZzzzz...')
    
    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 
        
#2. Instancie 3 objetos da classe mago e invoque seus métodos.         
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts')
gd = Mago('Gandalf', 2000, 'Magia Cinza')
#Novos objetos
pt = Mago('Patolino', 3000, 'Pato')
ml = Mago('Merlin',100000,'Tavola Redonda' )
de = Mago('Estranho',47, 'Vingadores')
#Acessando atributos públicos
print(hp.nome)
print(hp.idade)
print(hp.escola)

#Invocando métodos
hp.andar()
hp.falar()
hp.invocarMagia()
hp.cumprimentar("Rossana")

gd.falar()
gd.cumprimentar("Gabriel")

#Invocação dos novos métodos:
pt.falar()
pt.andar()
ml.cumprimentar(pt.nome)
ml.andar()
de.falar()
de.andar()
ml.invocarMagia()
pt.bicar()
ml.dormir()

del hp
del gd
del pt
del ml
del de

#3.Exercício Data:
class Data:
    #Atributo da classe
    nomesMeses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    #Método construtor
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprimirData(self):
        print(self.dia,'/',self.mes,'/',self.ano)

    def imprimirDataPorExtenso(self,cidade):

        strmes = self.nomesMeses[int(self.mes)-1]

        if self.mes == 1:
            strmes = 'Janeiro'
        elif self.mes == 2:
            strmes = 'Fevereiro'
        elif self.mes == 3:
            strmes = 'Marco'
        elif self.mes == 4:
            strmes = 'Abril'
        elif self.mes == 5:
            strmes = 'Maio'
        elif self.mes == 6:
            strmes = 'Junho'
        elif self.mes == 7:
            strmes = 'Julho'
        elif self.mes == 8:
            strmes = 'Agosto'
        elif self.mes == 9:
            strmes = 'Setembro'
        elif self.mes == 10:
            strmes = 'Outubro'
        elif self.mes == 11:
            strmes = 'Novembro'
        elif self.mes == 12:
            strmes = 'Dezembro'
        print(cidade,' , ',self.dia, ' de ', strmes, ' de ', self.ano)    

data = Data(24,8,2023)

data.imprimirData()
data.imprimirDataPorExtenso('Porto Alegre')
#4.Adaptação do exercício de revisão:
class Musica:  #Classe
    def __init__(self,titulo,artista,genero,ano,duracao): #Método constrututor com atributos
        
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.ano = ano
        self.duracao = duracao
    
    def infomusic(self,name):
        if self.titulo == name:
            print('Título = ',self.titulo,'\n','Artista = ',self.artista,'\n','Gênero = ',self.genero,'\n','Ano = ',self.ano,'\n','Duração =',self.duracao)
            return True
        else:
            return False
    
    def verificação(self,newsong):
        if newsong == self.titulo and newsong not in(newlist):
            newlist.append(newsong)
            print("Música adicionada na playlist com sucesso")
        elif newsong == self.titulo and newsong in(newlist):
            print("música já adicionada a playlist") 
    def visualizarplaylist(self):
        for self in newlist:
            print(self)   
    

def menu():
    print('[ APP MÚSICA ]\n[1]-Pesquisar música\n[2]-adicionar música na playlist\n[3]-visualizar playlist\n[4]-Sair')
    escolha = int(input('Informe o serviço desejado: '))
    return escolha

#Banco de dados com músicas e informações
database = [
    ['Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
    [ 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
    [ 'Rock and Rolo', 'The Buns','Rock',	1984, '4:01' ],
    [ 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ],
    ['Outra musica', 'Anira', 'Funk', 2019, '3:05']
]

lista = []

newlist = []



#atribuição das instâncias dos objetos
for l in range(len(database)):
    titulo = database[l][0]
    artista = database[l][1]
    genero = database[l][2]
    ano = database[l][3]
    duracao = database[l][4]
    music = Musica(titulo,artista,genero,ano,duracao)
    lista.append(music)  #Armazenamento dos novos objetos

choice = menu()
while choice!=4:
    if choice==1:
        name = input('informe o nome da música: ')
        for l in range(len(lista)):
            music = lista[l]           
            info = music.infomusic(name)
            if info == True:
                break
        else:
            print('Musica não encontrada no banco de dados')
        print('')
        choice = menu()
    elif choice==2:
        newsong = input('informe o nome da música que deseja adicionar na sua playlist, se quiser retornar ao menu, digite 0: ')
        while newsong!='0':    
            for l in range(len(lista)):
                music = lista[l]
                verificacao=music.verificação(newsong)    
            newsong = input('informe o nome da música que deseja adicionar na sua playlist, se quiser retornar ao menu, digite 0: ')
        else:
            choice = menu()
    elif choice == 3:
        music.visualizarplaylist()
        choice = menu()
    else:
        print('opção inválida, faça outra solicitação: ')
        choice = menu()
else:
    print('saindo do programa')
    del music