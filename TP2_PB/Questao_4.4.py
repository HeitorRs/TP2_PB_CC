import time
import matplotlib.pyplot as plt

def permutar_string(s, prefixo="", resultado=None):
    if resultado is None:
        resultado = set()

    if len(s) == 0:
        resultado.add(prefixo)
    else:
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            permutar_string(s[:i] + s[i+1:], prefixo + s[i], resultado)

    return resultado

def gerar_permutacoes(s):
    return permutar_string(s)

def medir_tempo(s):
    start_time = time.time()
    gerar_permutacoes(s)
    end_time = time.time()
    return end_time - start_time

tamanhos = list(range(1, 16))
tempos = []

for n in tamanhos:
    input_str = 'aaabaaabbcaaaabbbccdaaaaabbbbcccdde'[:n]
    tempo = medir_tempo(input_str)
    tempos.append(tempo)
    print(f"Tempo necessário para string de {n} caracteres: {tempo:.6f} segundos")

plt.plot(tamanhos, tempos, marker='o')
plt.xlabel('Tamanho da String')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução para Gerar Permutações de String Progressivas')
plt.grid(True)
plt.show()


