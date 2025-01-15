import time
import matplotlib.pyplot as plt

def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        return
    torres_de_hanoi(n - 1, origem, auxiliar, destino)
    torres_de_hanoi(n - 1, auxiliar, destino, origem)

def torres_de_hanoi_com_passos(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    torres_de_hanoi_com_passos(n - 1, origem, auxiliar, destino)
    print(f"Mover disco {n} de {origem} para {destino}")
    torres_de_hanoi_com_passos(n - 1, auxiliar, destino, origem)

def medir_tempo(n):
    if n <= 3:
        start_time = time.time()
        torres_de_hanoi_com_passos(n, 'A', 'C', 'B')
        end_time = time.time()
    else:
        start_time = time.time()
        torres_de_hanoi(n, 'A', 'C', 'B')
        end_time = time.time()
    tempo = end_time - start_time
    return tempo

tempos = []

discos = list(range(1, 31))
for d in discos:
    tempo = medir_tempo(d)
    tempos.append(tempo)
    print(f"Tempo necessário para {d} discos: {tempo:.6f} segundos")

plt.plot(discos, tempos)
plt.xlabel('Número de Discos')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução das Torres de Hanói')
plt.show()
