#hacer un cuadrado magico que en todas las filas sume lo mismo y si suma lo mismo es cudrado magico.
def es_cuadrado_magico_(matriz):
  n = len(matriz)
  if n == 0:
      return False
  suma_magica = sum(matriz[0])
  numeros_vistos = set()
  for fila in matriz:
      for numero in fila:
          if numero in numeros_vistos:
              return False
          numeros_vistos.add(numero)
  sumas = []
  # Filas
  sumas.extend([sum(fila) for fila in matriz])
  # Columnas
  sumas.extend([sum(col) for col in zip(*matriz)])
  sumas.append(sum(matriz[i][i] for i in range(n)))
  sumas.append(sum(matriz[i][n-1-i] for i in range(n)))
  return all(suma == suma_magica for suma in sumas)
if __name__ == "__main__":
  print("Ingrese la matriz cuadrada bidimensional(separada por espacios y cada fila en una línea): ")
  matriz = []
  for _ in range(int(input())):
      fila = list(map(int, input().split()))
      matriz.append(fila)
  if es_cuadrado_magico_(matriz):
      print("La matriz ingresada es un cuadrado mágico.")
  else:
      print("La matriz ingresada no es un cuadrado mágico.")
