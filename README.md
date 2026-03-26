# Programação Orientada a Objetos ⚽⚾🏀
<img src="https://raw.githubusercontent.com/GabrielMascavo75/POO/bc05d75db8797a927124b1bfd02ee4be8b7f6335/bolas_diferentes.jpg" width="500">
  
É um paradigma da programação que organiza códigos em torno de objetos, entidades que combinam atributos e métodos. A POO promove a reutilização, organização e modularidade do código, sendo amplamente usada em sistemas complexos.
Nesse repositório será exposto conceitos como:

__Classe:__ Modelo abstrato que define a estrutura e o comportamento de um objeto, agrupando atributos (características) e métodos (ações).  
__Objeto:__ Instância concreta de uma classe, representando uma entidade do mundo real ou abstrata que combina dados (atributos) e comportamentos (métodos).  
__Atributos:__ Características ou propriedades do objeto (ex: cor, nome).  
__Métodos:__ Ações que o objeto pode realizar (ex: andar, calcular).  

---
# 1.Adivinhação RPG 
 O código do jogo de adivinhação demonstra uma aplicação consistente dos principais conceitos da Programação Orientada a Objetos (POO), como abstração, encapsulamento, herança e polimorfismo. A estrutura foi organizada de forma modular, favorecendo a reutilização, manutenção e expansão do sistema. A classe abstrata `Jogo` estabelece um modelo genérico ao definir os métodos `iniciar` e `jogar`, garantindo que qualquer classe derivada implemente essas funcionalidades. Esse uso evidencia o conceito de abstração, permitindo a criação de diferentes tipos de jogos seguindo uma mesma estrutura base.
 
 A classe `Jogador` representa uma entidade do sistema, encapsulando atributos como nome e pontuação. Já a classe `JogoAdivinhacao`, que herda de `Jogo`, demonstra o uso de herança e polimorfismo ao implementar de forma específica os métodos definidos na classe base. Além disso, o uso de atributos privados, como `__tentativas` e `__limite`, reforça o encapsulamento, protegendo o estado interno do objeto. A lógica de definição de dificuldade no construtor mostra flexibilidade na configuração do jogo, ajustando limites de tentativas e intervalos de números conforme a escolha do usuário. O sistema de pontuação e ranking contribui para uma experiência mais interativa, enquanto a separação de funções auxiliares melhora a organização do código.
 
 Por fim, o tratamento de exceções durante a entrada de dados aumenta a robustez do sistema, evitando falhas por entradas inválidas. Assim, o código evidencia um bom domínio dos fundamentos de POO, aliado a práticas que tornam o software mais organizado, seguro e eficiente.

---
