# :newspaper: Descrição do Projeto
<p align="justify ">Fiz esse jogo por sugestão de um amigo. Infelizmente, devido às limitações da biblioteca usada, não consegui fazer uma animação para o movimento dos números, 
por conta disso, eles se movem de forma "instantânea" e isso faz com que o jogo fique diferente do jogo original. Tirando isso, acredito que é parecido com o jogo original.</p>
<br>
<details>
 <summary>Vídeo de demonstração</summary>
 <br>
 <p>:tv: Esse vídeo foi feito de forma simples, apenas para mostrar como o jogo funciona:
 <a href="https://www.youtube.com/watch?v=EGHH-litfPk&ab_channel=Romulo" target="blank">Vídeo no Youtube</a></p>
</details>
<br>

# :mag_right: Visão Geral
<p align="justify">Assim como feito no projeto do <a href="https://github.com/romulodm/Pac-Man">Pac-Man</a>, utilizei matriz neste jogo.
Desta vez foi uma matriz de tamanho 4x4, usada para inserir os números, que dentro da interface gráfica viram as células, com cores e tudo mais.</p>
<br>
<p align="center">

 <img src="https://github.com/romulodm/2048-Game/blob/main/demo.png">
 
</p>
<br>
<p align="justify">Vale salientar que é a partir dessa matriz que fazemos a compressão dos números, a união entre dois valores iguais e a checagem, tanto de derrota quanto de vitória.</p>
<br>
<details>
  <summary>Matriz inicial do jogo</summary>
  <br>

  ```
  self.board = [[None,None,None,None],
                [None,None,None,None],
                [None,None,None,None],
                [None,None,None,None]]
  ```

</details>

<details>
  <summary>Movimentação das células</summary>
  <br>
  
  ```
  def moveUp(self, move):       
      self.compressUp()
      #Merge cells:
      for row in range(1, 4):
          for column in range(0, 4):
              if self.board[row][column] == self.board[row - 1][column] and self.board[row][column] != None:
                  self.board[row - 1][column] = self.board[row][column] * 2
                  self.updateScore(self.board[row][column] * 2)
                  self.board[row][column] = None
    
      self.compressUp()
      self.generateRandomPiece()
    
      self.lastMove = move
      return True
  
  def compressUp(self):
      emptyBoard = self.generateEmptyBoard()
      for column in range(0, 4):
          count = 0
          for row in range(0, 4):
              if self.board[row][column] != None:
                  emptyBoard[count][column] = self.board[row][column]
                  count += 1
      
      self.board = emptyBoard
      return True 
  ```

</details>


# :hammer_and_wrench: Rodar o Projeto
* ```Ter 'python' instalado```
* ```Baixar a biblioteca``` <a href="https://docs.python.org/3/library/random.html">```Random```</a> ```'pip install random'```
* ```Rodar o arquivo main.py```

