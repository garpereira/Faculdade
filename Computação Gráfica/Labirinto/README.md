# Repositório de Computação Gráfica - Trabalho Final

Bem-vindo ao repositório de Computação Gráfica da Universidade Federal de São Paulo - Campus São José dos Campos. Este repositório foi criado para armazenar e compartilhar o trabalho final da disciplina de Computação Gráfica, que consiste em um jogo 3D de labirinto.

## Descrição do Projeto

Neste repositório, você encontrará o projeto desenvolvido como parte da matéria de Computação Gráfica. O projeto é um jogo 3D que envolve a movimentação em perspectiva em um labirinto procurando alvos em um ambiente virtual. Os alunos se empenharam em aplicar conceitos de computação gráfica, modelagem 3D, animação e interatividade para criar este jogo emocionante.

## Como Compilar

Como foi utilizada a API SOIL para poder carregar as texturas, então será necessária sua instalação, claro que, subentende-se que o usuário já possua o GLUT instalado na sua máquina.

```
sudo apt-get install libsoil-dev
gcc labirinto.c -o labirinto -lglut -lGL -lGLU -lm -lSOIL

```

Para executar

```
./labirinto

```


## Tecnologias Utilizadas

O jogo foi produzido utilizando a linguagem C com a API do OpenGL.

## Como Utilizar Este Repositório

- **Recursos 3D**: Todos os recursos 3D, como modelos, texturas e animações, estão armazenados na pasta `Texturas/`.

## Contribuições

Este repositório está aberto a contribuições. Se você é um aluno da matéria de Computação Gráfica na UNIFESP - Campus São José dos Campos ou se deseja contribuir de alguma forma, fique à vontade para enviar pull requests, relatar problemas ou fazer sugestões para melhorar o projeto.

## Autores

- Gabriel Almeida
  - [GitHub](https://github.com/garpereira)

- André Silva
  - [GitHub](https://github.com/andreqsilva)

- Gabriel de Mello Cambuy
  - [GitHub](https://github.com/gacambuy)
 
## Referência de Implementação

- André Backes
  - [Youtube](https://youtube.com.br/progdescomplicada)

Este projeto foi desenvolvido como parte da disciplina de Computação Gráfica na UNIFESP - Campus São José dos Campos.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

Agradecemos por visitar o nosso repositório e esperamos que este projeto de Computação Gráfica lhe seja útil e inspirador!
