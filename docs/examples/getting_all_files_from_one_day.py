from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

api_goes = AwsS3ApiGoes16()

# SETTING COORDINATES FOR FILTERING
lat_long = {'n_lat': -22.5, 's_lat': -24.0, 'w_lon': -43.8, 'e_lon': -43.0}
api_goes.lat_long_coords = lat_long

# THE FILES WILL BE SAVED IN YOUR LOCAL BUCKET PATH
api_goes.get_all_files_one_day('2019-04-08')
