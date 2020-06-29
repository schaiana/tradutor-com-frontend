# Tradutor

Esta aplicação transforma algarismos no intervalo [-99999, 99999] em números por extenso.

Ela foi desenvolvida utilizando Python e Flask.


**Dependências**:

É necessário possuir os seguintes programas previamente instalados:

* Docker
* Make


 **Para manipular a aplicação, foi criado um Makefile, que contém a seguinte estrutura:**

* *build*: responsável por criar uma imagem da aplicação;

* *run*: responsável por executar a aplicação de maneira acoplada ao terminal;

* *test*: responsável por executar os testes automatizados da aplicação;

* *start*: responsável por executar a aplicação de maneira desacoplada ao terminal (cria um processo à parte);

* *stop*: responsável por parar o contêiner da aplicação.

  
**Para executar o servidor, utilize um dos seguintes comandos:**
  
  `make run`
  
  `make start`
  
**Para rodar os testes automatizados, execute:**
  
  `make test`
    
**Para parar o contêiner da aplicação, execute:**
  
  `make stop`
  
  **OBS.1:** Todos os comandos devem ser executados no diretório onde estiver o arquivo Makefile;
  
  
  **OBS.2:** Toda a nomeclatura do código está em português para ficar condizente com o exemplo passado: ("extenso: ").
 

