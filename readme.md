# Python KeyLogger

Este projeto consiste em um key logger básico que registra as teclas pressionadas pelo usuário e armazena essas informações em um arquivo CSV. O logger também registra o título da janela ativa no momento da pressionada de tecla.



## Como usar

1. Clone ou faça o download do repositório no seu computador.

2. Abra o terminal e navegue até o diretório onde o script está localizado.

3. Execute o script com o seguinte comando:


```shell
 python logger.py
```

_Para parar o script, segure o ESC por 5 segundos_

## Requisitos 

Python 3.x
As bibliotecas Python **keyboard** e **pygetwindow**. Você pode instalá-las executando:

```
pip install keyboard
pip install pygetwindow
```

ou

```
pip install requirements.txt
```

## Saídas

As saídas são duas, na pasta `/logs` serão salvos o log de teclas e código de janelas separados por dia. Já na pasta `/map` será salvo o mapeamento de janelas. 

- Exemplo log_15-04-2023.csv

```
window_code,key_code
37,15
37,15
37,15
49,15
37,15
83,35
80,15
```

- Exemplo windows_map.csv

```
code,title
1,logger.py - KeyLogger - Visual Studio Code
2,Spotify Premium
3,#🥤┃data | SouJunior - Discord

```

## Criando mapeamento de teclas

Tendo em vista a variedade de teclados que trabalhamos, o script `create_key_map.py` pode auxiliar na criação do mapeamento de teclas.


## Contribua

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Basta abrir uma issue ou enviar um pull request.

## EsmolaPill

Gostou do projeto? Você pode contribuir com uma ⭐️ aqui no repositório no repositório!


## Vamos conectar?

<div align="left">
  <a href="https://linkedin.com/in/moscarde" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-333333?style=flat&logo=linkedin&logoColor=0072b1" alt="Linkedin logo" height="30px" />
  </a>
  <a href="https://github.com/moscarde" target="_blank">
    <img src="https://img.shields.io/badge/-Github-333333?style=flat&logo=github&logoColor=00000"  alt="Github logo" height="30px"  />
  </a>
    
  
</div>