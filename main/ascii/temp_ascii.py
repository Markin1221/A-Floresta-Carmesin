
import time

with open(r'C:\Users\marki\OneDrive\Documentos\GitHub\A-Floresta-Carmezin\main\ascii\arte.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

for linha in linhas:
    print(linha, end='')
    time.sleep(0.01)

time.sleep(1)
