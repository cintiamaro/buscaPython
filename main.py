#cria o grafo com as arestas

arestas = [
  [1],#0
  [0,2],#1
  [1,3,4],#2
  [2,4,5],#3
  [2,3,5],#4
  [3,4,6],#5
  [5,7,8],#6
  [6],#7
  [6],#8
]

#define o inicio como o 2 (é )
inicial = 2

#cria os vetores auxiliares
#Vetor visitados com todos os valores marcados como False
visitados = [False] * len(arestas)

#cria a fila vazia
fila = []
#insere o valor inicial na fila
fila.append(inicial)

#setar o primeiro visitado como 0
visitados[inicial]=0

#enquanto houver vértices na fila, continua
while (len(fila) > 0):
  verticeAtual = fila[0]
  print("Vértice Atual:", verticeAtual)

# passa por todas as conexões do vertice atual (vizinhos) 
  for i in range(0, len(arestas[verticeAtual]), 1):
    #define o vizinho atual
    vizinho = arestas[verticeAtual][i]
    #verifica se o vizinho já foi visitado, se sim -> ignora
    if visitados[vizinho] is False:
      fila.append(vizinho)
      #adiciona a distancia do vertice e insere nos visitados
      visitados[vizinho] = visitados[verticeAtual] + 1
      
  fila.pop(0)
  print("Fila:")
  for i in range (0, len(fila), 1):
    print(fila[i])

print ("Resultado:")
for i in range (0, len(visitados), 1):
    print("[", i, "] -> ", visitados[i])