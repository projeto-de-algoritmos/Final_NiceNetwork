from random import sample, randint

class Graph:

    def __init__(self, name):
        self.graph = self.new_graph()
        self.name = self.change_user(name)
        self.suggestion = self.suggestion_update()


    def new_graph(self):
        """ Gera um grafo de 10000 vertices """
        def randomNames(name, names):
            """ Retorna uma lista de 10 a 500 pessoas em names, com name nao incluso """
            k = randint(11, 500)
            followed_peoples = sample(names, k = k)
            if name in followed_peoples:
                followed_peoples.remove(name)
            return followed_peoples

        
        graph = {}
        file_pointer = open('nicenetwork/utils/nomes.txt')
        names = file_pointer.read().split('\n')
        while True:
            if not names[-1]:
                names.pop()
            else:
                break
        for name in names:
            graph[name] = randomNames(name, names)
        file_pointer.close()
        return graph

    def reverse_graph(self):
        graphREverse = {key: [] for key in self.graph}
        for name in self.graph:
            for follow in self.graph[name]:
                graphREverse[follow].append(name)
        return graphREverse


    def reverse_graph_count(self):
        """ Retorna um dicionario com o valor de cada grau no grafo reverso {nome: grau no grafo reverso}"""
        graphRcount = {}
        for value in self.graph.values():
            for name in value:
                if graphRcount.get(name):
                    graphRcount[name] = graphRcount[name] + 1
                else:
                    graphRcount[name] = 1
        return graphRcount


    def suggestion_update(self, user=False):
        """ atualiza a lista de sugestoes """
        if not user:
            user = self.name
        if len(self.graph[user]) == 0:
            suggestion = self.reverse_graph_count()
            self.suggestion = suggestion
        else:
            suggestion = {nome: 0 for nome in self.graph}
            for following in self.graph[user]:
                for name in self.graph[following]:
                    suggestion[name] = suggestion[name] + 1
            del suggestion[user]
            self.suggestion = suggestion
        return suggestion


    def insert_edge(self, v, w):
        """ Insere uma nova aresta no grafo atualizando as sugestões """
        #caso v já seja um vertice do grafo
        if self.graph.get(v):
            self.graph[v].append(w)
            self.suggestion_update()
        else:
            self.graph[v] = [w]
            self.suggestion_update()


    def insert_verice(self, name):
        """ insercao de usuario no grafo """
        self.graph[name] = []
    

    def change_user(self, newUser):
        """ troca de usuario """
        self.name = newUser
        if not self.graph.get(newUser):
            self.insert_verice(newUser)
        self.suggestion = self.suggestion_update(user=newUser)
        return newUser