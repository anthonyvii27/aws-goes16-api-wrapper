from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

apiGoes = AwsS3ApiGoes16()
apiGoes.product = 'GLM-L2-LCFA'

print(f'Remote bucket: {apiGoes.remote_bucket}')
print(f'Local bucket: {apiGoes.local_bucket}')
print(f'Product: {apiGoes.product}')

apiGoes.initial_date = '2019-04-18 18'
apiGoes.due_date = '2019-05-08 18'

print(f'Initial date: {apiGoes.initial_date}')
print(f'Due date: {apiGoes.due_date}')

print('\n')

apiGoes.local_bucket = '/Users/testing'
print(f'New local bucket: {apiGoes.local_bucket}')

apiGoes.local_bucket = '/'
print(f'New local bucket from alias: {apiGoes.local_bucket}')

apiGoes.local_bucket = '/Users/anthonysilva/Development/github/aws-goes16-api-wrapper/tmp'

print('\n')

# apiGoes.list_buckets()

print('\n')

# apiGoes.list_bucket_files(bucket_name="local")

print('\n')

# apiGoes.list_products()

print('\n')

lat_long = {'n_lat': -22.5, 's_lat': -24.0, 'w_lon': -43.8, 'e_lon': -43.0}
apiGoes.lat_long_coords = lat_long
print(apiGoes.lat_long_coords)

# apiGoes.get_file(datetime='2019-04-08 18', filename='OR_GLM-L2'
#                                                     '-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc')

# apiGoes.get_all_files_one_day('2019-04-08')

apiGoes.get_all_files_from_the_last()