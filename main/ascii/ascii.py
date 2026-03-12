import subprocess
import os

def mostrar_ascii(pasta_ascii, nome_arquivo):
    caminho_txt = os.path.join(pasta_ascii, nome_arquivo)

    codigo = f"""
import time

with open(r'{caminho_txt}', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

for linha in linhas:
    print(linha, end='')
    time.sleep(0.01)

time.sleep(1)
"""

    script_temp = os.path.join(pasta_ascii, "temp_ascii.py")

    with open(script_temp, "w", encoding="utf-8") as f:
        f.write(codigo)

    subprocess.Popen(f'start cmd /c python "{script_temp}"', shell=True)