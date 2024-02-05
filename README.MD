# Processo Seletivo RoboForge - Equipe 3ML

Este repositório contém todos os arquivos e documentações relacionados ao processo seletivo da RoboForge, desenvolvidos pela equipe 3ML. A equipe é composta por estudantes universitários dedicados a aplicar seus conhecimentos teóricos em desafios práticos, visando a inovação e excelência técnica.

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

- `main.py` - Arquivo principal do Desafio Prático realizado em 03/02.
- `/desafios-programacao` - Pasta contendo os códigos dos desafios de programação propostos pela equipe RoboForge.
    - `/python` - Desafios de Introdução ao Python.
        - `nivel0.py`  -  Solução para Desafios PS 00.
        - `nivel01.py` -  Solução para Desafios PS 01.
        - `nivel02.py` -  Solução para Desafios PS 02.

    - `/eve3` - Desafios envolvendo sensores com o EV3 MicroPython.
        - `sensores.py` - Solução para o Desafio de Sensores.
        - `movimentacao.py` - Solução para o Desafio de Movimentação.


## Projetos

Descrição breve dos projetos incluídos neste repositório:

## `Python`

1. **Solução Desafios PS 00 - Introdução ao Python** - Desenvolva uma função em Python que aceite como entrada um único número inteiro. A função deve analisar o número fornecido e retornar uma string específica com base nas seguintes condições: se o número for divisível por 3, a função deve retornar a string "Fizz"; se for divisível por 5, deve retornar "Buzz". Nos casos em que o número for divisível tanto por 3 quanto por 5 simultaneamente, a função deve retornar "FizzBuzz".

2. **Solução Desafios PS 01 - Introdução ao Python** - Crie uma função em Python destinada a determinar se um número fornecido é primo. Para um número ser considerado primo, ele deve ser divisível apenas por 1 e por si mesmo, sem outros divisores. Além disso, desenvolva uma segunda função cujo propósito é gerar uma lista contendo 10 números aleatórios dentro de um intervalo especificado pelo usuário. A tarefa seguinte envolve a utilização dessas duas funções em conjunto: percorra a lista gerada pela segunda função e identifique quais números são primos com a ajuda da primeira função. Por fim, calcule o produto de todos os números primos encontrados na lista e retorne esse resultado.

3. **Solução Desafios PS 02 - Introdução ao Python** - Desenvolva um programa em Python que, a partir de três pontos cartesianos (x, y) fornecidos, execute uma série de cálculos geométricos para determinar os comprimentos dos lados, os ângulos internos, o perímetro e a área do triângulo formado. Adicionalmente, o programa deve classificar o triângulo quanto ao tipo de seus lados (equilátero, isósceles ou escaleno) e quanto ao tipo de seus ângulos (acutângulo, retângulo ou obtusângulo). Para isso, você pode utilizar livremente as funções da biblioteca math do Python e recorrer à internet para pesquisar fórmulas e verificar cálculos. Este exercício visa aferir habilidades em geometria analítica, trigonometria e programação, além de estimular a pesquisa e aplicação de recursos matemáticos em soluções de software.

## `EVE3`

1. **Solução Desafios SENSORES - Desafios Motores e Sensores** - Desenvolva um código que permita a um robô, equipado com a capacidade de utilizar até quatro sensores simultaneamente conforme a configuração dos sensores EV3, seguir um conjunto específico de regras de movimentação e interação com o ambiente. O algoritmo deve ser projetado para que o robô mantenha um movimento paralelo em relação à parede, mantendo-se a uma distância fixa dela. Durante sua locomoção, o robô deve ser capaz de reconhecer cores específicas no chão e reagir a elas da seguinte maneira: ao detectar a cor vermelha, o robô deve realizar uma curva de 90 graus e prosseguir com seu trajeto ao longo da parede. Se identificar a cor amarela, deve pausar e aguardar por um comando de um usuário antes de retomar sua rotina normal de movimentação. Por fim, ao encontrar a cor verde, o robô deve cessar todos os movimentos e parar completamente.


2. **Solução Desafios MOVIMENTAÇÃO - Desafios Motores e Sensores** - Analíse o código fornecido pela equipe Robo Forge e crie um código mais idiomático e bem estruturado respeitando as especificidades da linguágem Python


## Como Usar

Siga as instruções abaixo para clonar, configurar e executar os projetos:

```sh
# Clone o repositório
git clone https://github.com/marcosawe/seletivo-roboforge.git
```

Execute os seguintes comandos de acordo com seu sistema operacional para preparar o ambiente de desenvolvimento:

```sh
# Para Linux
python3 -m venv venv
source venv/bin/activate
pip install pybricks
```
```sh
# Para Windows
python3 -m venv venv
.\venv\Scripts\Activate.ps1
pip install pybricks
```
## Contribuições

A equipe 3ML incentiva contribuições. Se você tem sugestões de melhorias, por favor, abra uma issue ou envie um pull request.

## Contato

Para dúvidas ou sugestões, entre em contato conosco através do e-mail <marcos.domingues@ufu.br> ou abra uma issue neste repositório.

