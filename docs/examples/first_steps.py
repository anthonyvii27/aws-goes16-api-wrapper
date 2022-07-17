from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

api_goes = AwsS3ApiGoes16()


# DEFAULT VALUES
print(f'Default Local Bucket: {api_goes.local_bucket}')  # pwd
print(f'Default Product: {api_goes.product}')  # GLM-L2-LCFA


# CHANGING THE LOCAL BUCKET
api_goes.local_bucket = '/Users/username/www/example'
print(f'New local bucket: {api_goes.local_bucket}')


# CHANGING THE LOCAL BUCKET WITH PWD ALIAS
api_goes.local_bucket = '/'
print(f'New local bucket from alias: {api_goes.local_bucket}')


# SETTING INITIAL AND DUE DATE
api_goes.initial_date = '2019-04-18 18'  # yyyy-mm-dd HH
api_goes.due_date = '2019-05-08 18'  # yyyy-mm-dd HH

print(f'Initial date: {api_goes.initial_date}')
print(f'Due date: {api_goes.due_date}')


# SETTING COORDINATES FOR FILTERING
lat_long = {'n_lat': -22.5, 's_lat': -24.0, 'w_lon': -43.8, 'e_lon': -43.0}
api_goes.lat_long_coords = lat_long

print(api_goes.lat_long_coords)
