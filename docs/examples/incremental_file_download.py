import os

from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

api_goes = AwsS3ApiGoes16()

lat_long = {'n_lat': -22.5, 's_lat': -24.0, 'w_lon': -43.8, 'e_lon': -43.0}
api_goes.lat_long_coords = lat_long

# THE PART BELOW IS JUST TO CREATE AN INCREMENTAL DOWNLOAD SITUATION.
os.mkdir('tmp')
api_goes.local_bucket = os.getcwd() + '/tmp'
os.makedirs(f'{api_goes.local_bucket}/2019/098')

# THE PROGRAM WILL GET THE LAST FILE YOU HAVE IN YOUR LOCAL BUCKET AND DOWNLOAD ALL FILES AFTER THEM
api_goes.get_all_files_from_the_last()
