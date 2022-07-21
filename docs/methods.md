# Métodos do AWS GOES16 API Wrapper

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