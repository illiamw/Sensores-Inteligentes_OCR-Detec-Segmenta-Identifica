import sys
import subprocess
import os
import shutil

from PIL import Image

import pytesseract

def rotateImage(file, degree):
    img = Image.open(file)
    img = img.rotate(degree)
    img.save('predictions.jpg')

def cutImage(left, top, right, bot):
    img = Image.open('predictions.jpg')
    img = img.crop((left, top, right, bot))
    img = img.save('cutted.jpg')

def ocr():
    texto = pytesseract.image_to_string(Image.open('cutted.jpg'))
    return texto

command = sys.argv
isWord = False
havePlate = False
degree = 0
text = 'Nao foi encontrado nenhuma palavra'

if len(command) == 2:
    if 'help' in command[1]:
        print('Para executar basta digitar: python3 run.py <imagem>\nSubstituindo <imagem> pelo caminho e nome completo da imagem')
    else:
        try:
            file = command[1]
            shutil.copy(file, 'predictions.jpg')

            while not (isWord and havePlate) and degree < 360:
                rotateImage(file, degree)
                degree += 30
                output = subprocess.check_output('./darknet detector test cfg/coco.data darknet-yolov3.cfg lapi.weights predictions.jpg', shell=True)

                if 'Placa:' in output.decode('utf-8'):
                    havePlate = True
                    strTmp = (output.decode('utf-8')).split('\n')
                    for i in strTmp:
                        if 'Bounding Box:' in i:
                            coordenadas = []
                            tmp = i.split(',')
                            for j in tmp:
                                _, coord = j.split('=')
                                coordenadas.append(int(coord))
                            cutImage(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3])
                            text = ocr()
                            text = text.strip()

                            if len(text) > 0:
                                isWord = True
                                rotateImage('cutted.jpg', 180)
                                shutil.copy('predictions.jpg', 'cutted.jpg')
                                text = 'Possibilidade 1:' + text + '\nPossibilidade 2:' + ocr()
                            else:
                                isWord = False
                                havePlate = False


            print(text)
        except:
            print('Arquivo nao encontrado')
else:
    print('ERRO: Parâmetros incorretos\nDigite python3 run.py --help para ajuda')
