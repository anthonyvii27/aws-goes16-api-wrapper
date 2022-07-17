# AWS GOES16 - API Wrapper
[AWS GOES16 API Wrapper](https://anthonyvii27.github.io/aws-goes16-api-wrapper/) é uma API Wrapper desenvolvida para facilitar o acesso e download aos dados dos diferentes produtos do satélite NOAA GOES 16 presentes na storage da AWS (S3) que pode ser utilizada a partir de importação de seu módulo em um notebook por exemplo, ou via CLI. 

## Sumário
* [Guia Inicial](#guia-inicial)
  * [Instalação](#instalacao)
    * [Uso via importação](#instalacao-programatica)
    * [Uso via CLI](#instalacao-cli)
  * [Exemplos](#exemplos)
* [Documentação](#documentacao)
* [Contribuição](#contribuicao)
* [Código de conduta](#codigo-conduta)
* [Guia de contribuição](#guia-contribuicao)
* [Good First Issue](#good-first-issue)
* [License](#license)

<a id="guia-inicial"></a>
## Guia inicial
A AWS GOES16 API Wrapper pode ser utilizado de duas maneiras distintas em seus projetos. A primeira é através da sua forma programática, ou seja, realizando a importação do módulo do projeto em um notebook por exemplo e utilizando de suas classes conforme a documentação. A segunda forma é através de uma CLI (Command Line Interface). Nessa forma, basta executar o processo de instalação e utilizar da CLI seguindo o que foi especificado na documentação.

Para cada uma das duas formas citadas acima é feito um processo de instalação próprio. Abaixo você pode conferir como realizar o processo de instalação das duas formas:

<a id="instalacao"></a>
### Instalação

<a id="instalacao-programatica"></a>
#### Forma programática
Primeiro, faça o clone do repositório do projeto mais recente para seu ambiente local:

```shell
    git clone https://github.com/anthonyvii27/aws-goes16-api-wrapper.git
    cd aws-goes16-api-wrapper
```

Feito isso, insira o projeto dentro do seu ambiente de trabalho e faça as importações necessárias para utilizar das classes e métodos do goes16 dentro do seu projeto.

Você pode encontrar exemplos de como utilizar da AWS GOES16 API Wrapper nos exemplos presentes dentro da pasta [docs](https://github.com/anthonyvii27/aws-goes16-api-wrapper/tree/master/docs)

<a id="instalacao-cli"></a>
#### Via CLI

Para utilizar o projeto via CLI o processo inicial é o mesmo da forma programática. Primeiramente, realize o clone do repositório do projeto para seu ambiente local:

```shell
    git clone https://github.com/anthonyvii27/aws-goes16-api-wrapper.git
    cd aws-goes16-api-wrapper
```

Após isso, dentro pasta do projeto, rode o comando abaixo para instalar a CLI no seu ambiente:

```shell
    make install
```

Feito isso, é possível acessar a CLI diretamente no seu terminal utilizando do comando `awsgoes16`. Para testar se tudo está funcionando perfeitamente, rode o comando abaixo:

```shell
    awsgoes16 --help
```

<a id="exemplos"></a>
### Exemplos
Coming soon

<a id="documentacao"></a>
## Documentação
Coming soon

<a id="contribuicao"></a>
## Contribuição
Coming soon

<a id="codigo-conduta"></a>
### [Código de Conduta](#)

<a id="guia-contribuicao"></a>
### [Guia de Contribuição](#)

<a id="good-first-issue"></a>
### Good First Issue

<a id="license"></a>
### License