# CINtra Game 🎮
Um jogo 2D desenvolvido em Python com Pygame, onde o jogador deve coletar itens enquanto desvia de obstáculos que caem do céu. O jogo tem o objetivo de aplicar conceitos de Programação Orientada a Objetos e conceitos de python. O objetivo é coletar três tipos de itens (Lanche, Arma e Crachá) para acumular pontos e vencer o jogo, enquanto desvia de obstáculos. O jogo inicialmente tinha a temática inspirada no Contra, um jogo Run and Gun, mas por conta da limitação de membros da equipe e na problemas no desenvolvimento do jogo, os quais não cabem ser pontuados aqui, resolvemos mudar 

# Sobre a Equipe:
 * Landson - Responsável pela lógica de tela de gameover, tela de vitória e as respectivas lógicas
 * Lucas Mateus - Responsável pela criação da HUD e dos slides
 * Luiz Taiguara de Oliveira Guimarães - Responsável pela arquitetura do código e ideação das classes bases, estruturação do game, player, itens coletaveis, tela inicial. Responsável pela gestão do Notion, bem como o versionamento no GIT e solução dos conflitos de versionamento. Responsável pelo READme.




## Breve introdução sobre o jogo e sua mecânica

### Como executar o jogo 

clone e mude pra pasta 

git clone https://github.com/TaiguaraOG/ipgame-group6.git
cd ipgame-group6

instale as dependências: 
pip install pygame

Rode o artigo principal:
pip main.py

### Objetivos do Jogo

Meta de Vitória: Alcançar 10 pontos
Itens Coletáveis:

  *  Lanche: 2 pontos
  *  Arma: 3 pontos
  *  Crachá: 5 pontos

Desafio: Desviar dos obstáculos que caem aleatoriamente

> Controles

  *  A / ← (Seta Esquerda): Mover para esquerda
  *  D / → (Seta Direita): Mover para direita
  *  Enter: Iniciar jogo / Reiniciar após vitória ou derrota
  *  ESC: Voltar ao menu / Sair do jogo

> Tecnologias Utilizadas

Python 
Pygame - Biblioteca para desenvolvimento de jogos

A estrutura do projeto foi a seguinte:

ipgame-group6/
│
├── src/

│   ├── game.py              
│   ├── player.py           
│   ├── collectible_itens.py
│   ├── obstaculos.py        
│   ├── init_screen.py     
│   ├── end_screen.py        
│   ├── game_over.py        
│   ├── settings.py          
│   ├── game_data.py         
│   └── icones.py            
│
├── assets/

│   ├── sprites/             
│   └── screens/             
│
└── main.py                 


# Galeria de Imagens 
## Tela Inicial 
<img width="797" height="680" alt="image" src="https://github.com/user-attachments/assets/69bea0f2-c95c-4cc5-b44f-d70e3728f0a4" />

## Tela durante o gameplay 
<img width="802" height="682" alt="image" src="https://github.com/user-attachments/assets/ab6dda34-e332-4bbd-94d1-4f857d9e6fdc" />

## Tela de Vitória 
<img width="798" height="682" alt="image" src="https://github.com/user-attachments/assets/fc8c243f-7445-4524-896f-7469568abbc5" />

## Tela de Derrota 
<img width="797" height="678" alt="image" src="https://github.com/user-attachments/assets/0378dfc1-fe9a-449b-be8b-7282579587c0" />


## Conceitos de programação aplicados no desenvolvimento do projeto 

  *  POO -> Herença, principalmente herdando os metódos do pygame.sprite.Sprite, e encapsulamento das funções através das classes. 
  *  Listas -> listas de tuplas na hora da posição
  *  Condicionais -> Muito usado dentro de eventos e update
  *  Laços de repetição -> O maior impacto foi o loop principal, também na parte de eventos, e Geração de Posições Aleatórias
  *  Dicionários e tuplas -> Fundamentais para lidar com a posição dos coletáveis, e tuplas foram especialmente relevantes para posições dentro do mapa
  *  Funções -> O maior destaque do uso de funções foi a standalone presente dentro do arquivo de coletaveis, para lidar com a posição dos itens. 
  *  Recursão -> Recursão não fora usado na construção do nosso código

## Erros, Desafios e Aprendizados 
### Erros 
O grupo deveria ter levado mais em consideração a divisão das tarefas e gestão do tempo, o que gerou uma dificuldade na gestão das expectativas, diminuindo muito o potencial do que o jogo poderia ter se tornado. Alguns erros de versionamento geraram a necessidade de cherrypick, o que consumiu muito tempo. A necessidade de gameficar o jogo ao máximo também levou a uma versão do jogo sucetível a bug. 

### Desafios 
Divisão igualitaria das atividades, entrega das tasks, uso do GIT, definição do objetivo do jogo e uso da plataforma de comunicação (Notion). Aprendizado do uso de POO e como correlacionar a ideia das classes com o que era necessário implementar. 

### Aprendizados 
Importância da comunicação e definição das responsabilidades, a relevância do versionamento e arquitetura foram enormes, principalmente considerando o contexto no qual o jogo foi desenvolvimento. O uso de pygame e POO. 




