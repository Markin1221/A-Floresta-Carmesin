import subprocess
import os

pasta = os.path.dirname(__file__)
arquivo_ascii = os.path.join(pasta, "arte.txt")
script_temp = os.path.join(pasta, "mostrar_ascii.py")

codigo = f"""
import time

with open(r'{arquivo_ascii}', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

for linha in linhas:
    print(linha, end='')
    time.sleep(0.01)

time.sleep(4)
"""

# cria script temporário
with open(script_temp, "w", encoding="utf-8") as f:
    f.write(codigo)

# abre um novo cmd rodando o script
subprocess.Popen(f'start cmd /k python "{script_temp}"', shell=True)