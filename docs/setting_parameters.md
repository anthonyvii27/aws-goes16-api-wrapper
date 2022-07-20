# Configuração dos parâmetros
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
