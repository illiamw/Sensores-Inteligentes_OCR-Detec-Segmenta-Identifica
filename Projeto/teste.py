import subprocess
import os
import shutil

diretorio = 'data/Todos-Dados'
count = 0

for r, d, f in os.walk(diretorio):
    for file in f:
        if '.jpg' in file:
            output = subprocess.check_output('python run.py ' + diretorio + '/' +  file, shell=True)

            if 'Nao foi encontrado nenhuma palavra' not in output.decode('utf-8'):
                count += 1
                shutil.copy('cutted.jpg', 'results/' + str(count) + '.jpg')

                with open('results/' + str(count) + '.txt', 'w') as fp:
                    fp.write(output.decode('utf-8'))

print(str((count / 84) * 100) + '%')