# AWS GOES16 - API Wrapper
[AWS GOES16 API Wrapper](https://anthonyvii27.github.io/aws-goes16-api-wrapper/) é uma API Wrapper desenvolvida para facilitar o acesso e download aos dados dos diferentes produtos do satélite NOAA GOES 16 presentes na storage da AWS (S3) que pode ser utilizada a partir de importação de seu módulo em um notebook por exemplo, ou via CLI. 

## Sumário
* [Guia Inicial](#guia-inicial)
  * [Instalação](#instalacao)
    * [Uso via importação](#instalacao-programatica)
    * [Uso via CLI](#instalacao-cli)
  * [Exemplos](#exemplos)
* [Documentação](#documentacao)
  * [Autenticação](#autenticacao)
  * [Configuração de parâmetros](#parameters)
  * [Métodos](#methods)

<a id="guia-inicial"></a>
## Guia inicial
A AWS GOES16 API Wrapper pode ser utilizado de duas maneiras distintas em seus projetos. A primeira é através da sua forma programática, ou seja, realizando a importação do módulo do projeto em um notebook por exemplo e utilizando de suas classes conforme a documentação. A segunda forma é através de uma CLI (Command Line Interface). Nessa forma, basta executar o processo de instalação e utilizar da CLI seguindo o que foi especificado na documentação.

Para cada uma das duas formas citadas acima é feito um processo de instalação próprio. Abaixo você pode conferir como realizar o processo de instalação das duas formas:

<a id="instalacao"></a>
### Instalação

<a id="instalacao-programatica"></a>
### Forma programática
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

<a id="exemplos"></a>
### Exemplos - Via importação
Abaixo estão alguns exemplos de como utilizar a API Wrapper do NOAA GOES16 de forma programática. Todos os exemplos podem ser encontrados na pasta [examples](https://github.com/anthonyvii27/aws-goes16-api-wrapper/tree/master/docs/examples) presente dentro da pasta docs.

#### Criando a instância da awsgoes16
```python
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

api_goes = AwsS3ApiGoes16()
```

#### Listando os arquivos presentes em um bucket (local e remoto)
```python
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16
api_goes = AwsS3ApiGoes16()

# USING THE LOCAL BUCKET ALIAS = 'local'
api_goes.list_bucket_files(bucket_name='local')

# REMOTE BUCKET
api_goes.list_bucket_files()
```

#### Definindo os parâmetros de coordenadas (latitude e longitude) para filtragem dos dados dos arquivos
```python
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16
api_goes = AwsS3ApiGoes16()

api_goes.lat_long_coords = {'n_lat': -22.5, 's_lat': -24.0, 'w_lon': -43.8, 'e_lon': -43.0}
```

#### Fazendo o download de um arquivo específico
```python
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16
api_goes = AwsS3ApiGoes16()

api_goes.get_file(datetime='2019-04-08 18', filename='OR_GLM-L2-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc')
```

#### Realizando o download de todos os arquivos presentes em uma data específica
```python
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16
api_goes = AwsS3ApiGoes16()

api_goes.get_all_files_one_day('2019-04-08')
```

### Exemplos - Via CLI

#### Listando os arquivos presentes em um bucket (local e remoto)
```shell
# LOCAL BUCKET
awsgoes16 list_bucket_files --bucket_name local

# REMOTE BUCKET
awsgoes16 list_bucket_files --bucket_name noaa-goes16
```

#### Definindo os parâmetros de coordenadas (latitude e longitude) para filtragem dos dados dos arquivos
```shell
awsgoes16 coords --n_lat -22.5 --s_lat -24.0 --w_lon -43.8 --e_lon -43.0
# or
awsgoes16 coords -nl -22.5 -sl -24.0 -wl -43.8 -el -43.0
```

#### Fazendo o download de um arquivo específico
```shell
awsgoes16 get_file --filename OR_GLM-L2-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc --date 2019-04-08 --time 18
# or
awsgoes16 get_file -fn OR_GLM-L2-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc -d 2019-04-08 -t 18
```

#### Realizando o download de todos os arquivos presentes em uma data específica
```shell
awsgoes16 get_all_files_one_day --date 2019-04-08 --logs False
# or
awsgoes16 get_all_files_one_day -d 2019-04-08 -l False
```

<a id="documentacao"></a>
## Documentação

<a id="autenticacao"></a>
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

<a id="parameters"></a>
## Configuração dos parâmetros
A [AWS GOES16 API Wrapper](https://anthonyvii27.github.io/aws-goes16-api-wrapper/) possui diversos parâmetros que devem ser definidos para realizar o download dos arquivos de forma correta. Abaixo está a listagem de todos os parâmetros que podem ser definidos e sua documentação de como realizar a operação pela forma programática e via CLI.

Antes de tudo, vale ressaltar que para utilizar este projeto de forma programática, é necessário realizar a instanciação da classe principal. Ela será necessária para todas as operações que vão vir. Abaixo está o código para instanciação.

```python
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

api_goes = AwsS3ApiGoes16()
```

Caso queira mais detalhes sobre as configurações iniciais do projeto, [clique aqui](https://github.com/anthonyvii27/aws-goes16-api-wrapper/blob/master/docs/getting_start.md).

## Sumário
* [Local Bucket](#local-bucket)
* [Remote Bucket](#remote-bucket)

<a id="local-bucket"></a>
### Local Bucket
O local bucket é a pasta do seu computador definida para salvar os arquivos baixados. Por padrão, caso esse valor não seja definido, o programa utilizará da pasta root do projeto. Abaixo está a forma de uso via CLI e importação.

#### Via importação
A forma mais básica de se definir o local bucket é passando o path da pasta que salvará os arquivos baixados conforme mostrado abaixo. 
```python
api_goes.local_bucket = '/Users/username/www/example'
```

Além disso, caso seja necessário definir o local bucket como o path da pasta root do projeto, basta passar o caractere `/`. Esse valor é um alias para o valor do pwd da pasta que o projeto está sendo executada.
```python
api_goes.local_bucket = '/'
```

#### Via CLI
Pela CLI é bem semelhante a forma via importação. No terminal, execute o comando abaixo para definir o local bucket (O caractere `/` também funciona aqui como alias).
```shell
awsgoes16 local_bucket -v path
#or
awsgoes16 local_bucket --value path
```

<a id="remote-bucket"></a>
### Remote Bucket
O remote bucket é o bucket S3 que possui os arquivos a serem baixados. Por padrão, o remote bucket já está definido para o `noaa-goes16`, logo não é necessário setar esse valor caso queira pegar do repositório oficial do NOAA GOES16.

Esse valor possui alteração permitida para os casos em que o usuário possua um bucket próprio com dados já baixados do NOAA GOES 16 e queira fazer o download deles para o local. Obs.: A estrutura organizacional deste bucket deve ser a mesma do NOAA GOES16 para tudo funcionar corretamente.

#### Via importação
A forma mais básica de se definir o local bucket é passando o path da pasta que salvará os arquivos baixados conforme mostrado abaixo. 
```python
api_goes.remote_bucket = 'noaa-goes16'
```

#### Via CLI
Pela CLI é bem semelhante a forma via importação. No terminal, execute o comando abaixo para definir o local bucket (O caractere `/` também funciona aqui como alias).
```shell
awsgoes16 remote_bucket -v BUCKET_NAME
#or
awsgoes16 remote_bucket --value BUCKET_NAME
```

### Product
O NOAA GOES16 possui uma grande quantidade de produtos diferentes. É possível ver esses produtos executando o comando abaixo:

#### Forma programática
```python
api_goes.list_products()
```
#### Via CLI
```shell
awsgoes16 list_products
```

Caso não seja alterado, o valor default desse parâmetro é: `GLM-L2-LCFA`. Para realizar a alteração desse parâmetro para definir qual produto desejas baixar, basta chamar um método e passar os parâmetros necessários. Neste caso, é necessário apenas um parâmetro conforme mostrado na tabela abaixo:

| Parâmetro    | Descrição       | Default     |
|--------------|-----------------|-------------|
| product_name | Nome do produto | GLM-L2-LCFA |

Para definir este valor, basta executar o comando abaixo baseando-se na forma como está definido sua implementação.

#### Forma programática
```python
api_goes.product = 'product_name'
```
#### Via CLI
```shell
awsgoes16 product -v PRODUCT_NAME
#or
awsgoes16 product --value PRODUCT_NAME
```

### Initial Date | Due Date
É possível definir duas datas para realizar o download de todos os arquivos entre elas. Abaixo está apresentado como essa definição é feita.

#### Forma programática
```python
api_goes.initial_date = '2019-04-18 18'
api_goes.due_date = '2019-05-08 22'
```

#### Via CLI
```shell
awsgoes16 period -id 2019-04-18 -ih 18 -dd 2019-05-08 -dh 22
#or
awsgoes16 period --initial_date 2019-04-18 --initial_hour 18 --due_date 2019-05-08 --due_hour 22
```

| Parâmetro      | Abreviação | Descrição                          | Default |
|----------------|------------|------------------------------------|---------|
| --initial_date | -id        | Data inicial no formato yyyy-mm-dd |         |
| --initial_hour | -ih        | Hora inicial (valor entre 00 e 23) |         |
| --due_date     | -dd        | Data final no formato yyyy-mm-dd   |         |
| --due_hour     | -dh        | Hora final (valor entre 00 e 23)   |         |

### Coordenadas Geográficas (Latitude e Longitude)
As coordenadas geográficas servem para realizar a filtragem da área ao qual o usuário deseja ver os dados. Como o NOAA-GOES16 salva dados de toda a América, essa é uma forma de reduzir o tamanho dos arquivos e baixar apenas o necessário para o estudo. Abaixo está a forma de implementação para definição desses valores:

#### Forma programática
```python
# É necessário passar um dictionary para a estrutura no formato abaixo, sendo os valores referentes a:
# n_lat = north latitude
# s_lat = south latitude
# w_lon = west longitude
# e_lon = east longiture
lat_long = {'n_lat': -22.5, 's_lat': -24.0, 'w_lon': -43.8, 'e_lon': -43.0}
api_goes.lat_long_coords = lat_long
```

#### Via CLI
```shell
awsgoes16 coords --n_lat -22.5 --s_lat -24.0 --w_lon -43.8 --e_lon -43.0
# or
awsgoes16 coords -nl -22.5 -sl -24.0 -wl -43.8 -el -43.0
```

<a id="methods"></a>
## Métodos do AWS GOES16 API Wrapper

A [AWS GOES16 API Wrapper](https://anthonyvii27.github.io/aws-goes16-api-wrapper/) possui diversos métodos implementador para te auxiliar no download dos arquivos do NOAA GOES16. Abaixo estão listados os métodos com suas documentações.

<a id="autenticacao"></a>
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

### Listagem dos buckets
Para visualizar uma listagem dos buckets disponíveis, execute os comandos abaixo baseando-se na forma como está sendo feita a implementação.

#### Forma programática
```python
api_goes.list_buckets()
```

#### Via CLI
```shell
awsgoes16 list_buckets
```

### Listagem dos arquivos dentro de um bucket
Para visualização dos arquivos dentro de um bucket, execute os comandos abaixo baseando-se na forma como está sendo feita a implementação. Além disso, caso o bucket possua pastas aninhadas, basta acrescentar ao path do bucket o caminho das pastas.

#### Forma programática
```python
# LOCAL BUCKET
api_goes.list_bucket_files(bucket_name='local')

# REMOTE BUCKET
api_goes.list_bucket_files()
```

| Parâmetro     | Descrição                                                                    | Default       |
|---------------|------------------------------------------------------------------------------|---------------|
| bucket_name   | Nome do bucket. Caso queira ver o bucket local, defina o valor como 'local'. | Bucket Remoto |

#### Via CLI
```shell
# LOCAL BUCKET
awsgoes16 list_bucket_files --bucket_name local

# REMOTE BUCKET
awsgoes16 list_bucket_files --bucket_name noaa-goes16
```

### Listagem dos produtos disponíveis
Para visualização dos produtos do NOAA GOES16, execute os comandos abaixo baseando-se na forma como está sendo feita a implementação.

#### Forma programática
```python
api_goes.list_products()
```
#### Via CLI
```shell
awsgoes16 list_products
```

### Baixar um arquivo específico
Para baixar um arquivo específico do NOAA GOES16, execute os comandos abaixo baseando-se na forma como está sendo feita a implementação.

#### Forma programática
```python
api_goes.get_file(datetime='2019-04-08 18', filename='FILENAME')
```

| Parâmetro | Descrição                            | Default |
|-----------|--------------------------------------|---------|
| datetime  | Data e hora no formato yyyy-mm-dd HH |         |
| filename  | Nome do arquivo que desejas baixar   |         |

#### Via CLI
```shell
awsgoes16 get_file --filename FILENAME --date DATE --time TIME
# or
awsgoes16 get_file -fn FILENAME -d DATE -t TIME
```

| Parâmetro  | Abreviação | Descrição                          | Default |
|------------|------------|------------------------------------|---------|
| --date     | -d         | Data no formato yyyy-mm-dd         |         |
| --time     | -t         | Hora no formato HH (de 00 a 23)    |         |
| --filename | -fn        | Nome do arquivo que desejas baixar |         |

### Baixar todos os arquivos de um dia
Para baixar todos os arquivos de um produto em um dia, execute os comandos abaixo baseando-se na forma como está sendo feita a implementação.

#### Forma programática
```python
api_goes.get_all_files_one_day('2019-04-08')
```

| Parâmetro | Descrição                                                                                     | Default |
|-----------|-----------------------------------------------------------------------------------------------|---------|
| date      | Data no formato yyyy-mm-dd                                                                    |         |
| logs      | Booleano que define se o usuário deseja ver ou não logs da execução dos downloads no terminal | True    |

#### Via CLI
```shell
awsgoes16 get_all_files_one_day --date DATE --logs False
# or
awsgoes16 get_all_files_one_day -d DATE -l False
```

| Parâmetro | Abreviação | Descrição                                                                                     | Default |
|-----------|------------|-----------------------------------------------------------------------------------------------|---------|
| --date    | -d         | Data no formato yyyy-mm-dd                                                                    |         |
| --logs    | -l         | Booleano que define se o usuário deseja ver ou não logs da execução dos downloads no terminal | True    |

### Download Incremental
Esse método realiza o download incremental dos arquivos restantes a partir do último baixado no seu local bucket, ou seja, a partir do último dia com dados baixados, o programa automáticamente realiza o download de todos os outros arquivos dos dias seguintes até chegar na data mais recente ou ter sua operação finalizada por ação do usuário. Para utilizar desta funcionalidade, execute os comandos abaixo baseando-se na forma como está sendo feita a implementação.

#### Forma programática
```python
api_goes.get_all_files_from_the_last()
```

| Parâmetro | Abreviação | Descrição                                                                                     | Default |
|-----------|------------|-----------------------------------------------------------------------------------------------|---------|
| --logs    | -l         | Booleano que define se o usuário deseja ver ou não logs da execução dos downloads no terminal | True    |

#### Via CLI
```shell
awsgoes16 incremental_download --logs False
# or
awsgoes16 incremental_download -l False
```

| Parâmetro | Abreviação | Descrição                                                                                     | Default |
|-----------|------------|-----------------------------------------------------------------------------------------------|---------|
| --logs    | -s         | Booleano que define se o usuário deseja ver ou não logs da execução dos downloads no terminal | True    |

[Voltar para a configuração dos parâmetros](https://github.com/anthonyvii27/aws-goes16-api-wrapper/blob/master/docs/setting_parameters.md)
