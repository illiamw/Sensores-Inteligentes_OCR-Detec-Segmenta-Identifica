# Proposta
### DETECÇÃO
O trabalho consiste em detectar uma placa, sempre definida por uma borda, usualmente preta, que define o entorno do texto a ser reconhecido.

### SEGMENTAÇÃO
Uma vez detectada a placa, esta deve ser separada do fundo, através de uma segmentação da placa. A segmentação é o processo onde se separa o item de interesse (placa) do fundo.

### RECONHECIMENTO DO TEXTO (OCR)
Implementar um reconhecedor de caracteres (OCR - Optical Character Recognizer).
O reconhecedor deve identificar a sequência de caracteres que estão dispostos na placa. No caso, pode ser implementado um reconhecimento por uma "janela deslizante" aplicando o reconhecedor já implementado anteriormente.

### PASTA PLACA+FUNDO
O trabalho "padrão" irá realizar o reconhecimento de uma placa, que possui um entorno em preto, que circunda a placa, um fundo branco, e o texto em letras brancas. A placa padrão é a placa neste formato com os dizeres "Entrada Proibida". Esta placa está à disposição dos alunos caso queiram gerar mais imagens e fotos da mesma. As fotos foram batidas em diferentes situações, onde o fundo apresenta diferentes texturas e cores, onde a iluminação também pode variar, e onde espera-se que pelo menos 3 situações diferentes de fundo+placa possam ser reconhecidas (3 fundos diferentes). Não é necessário reconhecer todas as imagens desta pasta, porém deve-se buscar reconhecer a placa e o seu texto corretamente, pelo menos para algumas cenas diferentes.

### PASTA FUNDO-APENAS
Esta pasta contém fotos onde não existe a placa, apenas o fundo do cenário. O detector e reconhecedor de placas deve ser capaz de identificar SE EXISTE, OU NÃO, uma placa na cena. No caso das imagens de FUNDO-APENAS o reconhecedor deve indicar que não existe uma placa na cena. Estes fundos de cena podem ser usados para inserir sobre eles novas e diferentes placas. A pasta PLACA contém alguns exemplos de placas (só a placa, isolada/segmentada - ver informações da pasta PLACA abaixo), e que podem ser colocadas junto ao fundo.

### PASTA PLACA:
Existem exemplos com a placa isoladas, inicialmente com a placa padrão: fundo branco, entorno preto,e letras pretas com os dizeres "Entrada Proibida".
Existem, também, "placas alternativas" que podem ser consideradas como um desafio adicional (opcional), em que varia a cor do fundo, a cor da borda e do texto. Não é obrigatório reconhecer estas outras placas, mas quem quiser pode tentar fazer um algoritmo mais genérico que aceite também placas diferentes.
Estas placas podem ser usadas para serem inseridas em diferentes cenários, como foi feito nos arquivos da pasta PLACAS+EDITADAS.

### PASTA PLACAS-EDITADAS:
Esta pasta contém imagens que foram geradas através da edição, usando o "Microsoft PAINT", para unir uma placa da pasta PLACA com um fundo da pasta FUNDO-APENAS, gerando assim uma PLACA-EDITADA (não é uma foto real, mas uma imagem editada e manipulada com um editor de imagens).
As placas desta pasta podem ser usadas no trabalho, mas são imagens OPCIONAIS para uso no trabalho, uma vez que as placas seguem diferentes padrões (placas alternativas são opcionais).

# Execução
Para execurtar esse projeto precisa-se prepara seu ambiente para execução.

## Instalando pacotes
No diretório Projeto

Instalando o OCR fornecido pelo Google
```
pip3 install pytesseract 
```
Instando Darknet

```
make
```
## Predição
Para identificar o texto contido nas imagens, basta executar o camando
```
python3 run.py [imagem]	
```
* onde [imagem] corresponde ao caminho onde encontra-se a imagem, exemplo:

```
python3 run.py ./data/Todos-Dados/20191110_192833.jpg
```

```
output: Nao foi encontrado nenhuma palavra
```
