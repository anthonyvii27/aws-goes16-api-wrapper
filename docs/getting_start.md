# Guia inicial
Aqui você verá como deve ser realizado a configuração inicial da AWS GOES16 API Wrapper.

## Sumário
* [Passos iniciais](#passos-iniciais)
  * [Forma programática](#instalacao-programatica)
  * [Via CLI](#instalacao-cli)
* [Autenticação](#autenticacao)

<a id="passos-iniciais"></a>
### Passos iniciais
A AWS GOES16 API Wrapper pode ser utilizado de duas maneiras distintas em seus projetos. A primeira é através da sua forma programática, ou seja, realizando a importação do módulo do projeto em um notebook por exemplo e utilizando de suas classes conforme a documentação. A segunda forma é através de uma CLI (Command Line Interface). Nessa forma, basta executar o processo de instalação e utilizar da CLI seguindo o que foi especificado na documentação.

Para cada uma das duas formas citadas acima é feito um processo de instalação próprio. Abaixo você pode conferir como realizar o processo de instalação das duas formas:

<a id="instalacao-programatica"></a>
#### Forma programática
Primeiro, faça o clone do repositório do projeto mais recente para seu ambiente local:

```shell
git clone https://github.com/anthonyvii27/aws-goes16-api-wrapper.git
cd aws-goes16-api-wrapper
pip install -r requirements.txt
```

Feito isso, insira o projeto dentro do seu ambiente de trabalho e faça as importações necessárias para utilizar das classes e métodos do goes16 dentro do seu projeto.

Você pode encontrar exemplos de como utilizar da AWS GOES16 API Wrapper nos exemplos presentes dentro da pasta [docs](https://github.com/anthonyvii27/aws-goes16-api-wrapper/tree/master/docs)

<a id="instalacao-cli"></a>
### Via CLI

Para utilizar o projeto via CLI o processo inicial é o mesmo da forma programática. Primeiramente, realize o clone do repositório do projeto para seu ambiente local:

```shell
git clone https://github.com/anthonyvii27/aws-goes16-api-wrapper.git
cd aws-goes16-api-wrapper
pip install -r requirements.txt
```

Após isso, dentro pasta do projeto, rode o comando abaixo para instalar a CLI no seu ambiente:

```shell
make install
```

Feito isso, é possível acessar a CLI diretamente no seu terminal utilizando do comando `awsgoes16`. Para testar se tudo está funcionando perfeitamente, rode o comando abaixo:

```shell
awsgoes16 --help
```

### Autenticação
É possível realizar as operações de download e visualização dos arquivos presentes nos buckets de forma anônima (default) e autenticada. Para o uso com o NOAA GOES16 não é necessário estar identificado, ou seja, não é necessário realizar nenhum tipo de configuração para o uso. Porém, caso por exemplo, o usuário deseja ver o conteúdo do seu bucket privado que possui arquivos do NOAA GOES16 previamente baixados e upados no S3. Para isso, é necessário estar autenticado. Abaixo está apresentado como realizar essa autenticação.

#### Via importação
```python
api_goes.authenticate(access_key='AWS_ACCESS_KEY', secret_key='AWS_SECRET_KEY')
```

| Parâmetro  | Descrição      | Required |
|------------|----------------|----------|
| access_key | AWS Access Key | Sim      |
| secret_key | AWS Secret Key | Sim      |

#### Via CLI
```shell
awsgoes16 authenticate --access_key AWS_ACCESS_KEY --secret_key AWS_SECRET_KEY
#or
awsgoes16 authenticate -ak AWS_ACCESS_KEY -sk AWS_SECRET_KEY
```

| Parâmetro    | Abreviação | Descrição      | Required  |
|--------------|------------|----------------|-----------|
| --access_key | -ak        | AWS Access Key | Sim       |
| --secret_key | -sk        | AWS Secret Key | Sim       |
