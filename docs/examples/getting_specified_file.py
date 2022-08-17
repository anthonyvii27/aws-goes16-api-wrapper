from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

api_goes = AwsS3ApiGoes16()

# SETTING COORDINATES FOR FILTERING
lat_long = {'n_lat': -22.5, 's_lat': -24.0, 'w_lon': -43.8, 'e_lon': -43.0}
api_goes.lat_long_coords = lat_long

# THE FILE WILL BE SAVED IN YOUR LOCAL BUCKET PATH
api_goes.product = 'ABI-L2-CMIPM'
api_goes.data_variable = 'time_bounds'
api_goes.get_file(datetime='2020-04-07 18', filename='OR_ABI-L2-CMIPM1'
                                                     '-M6C01_G16_s20200981800270_e20200981800327_c20200981800412.nc')

# api_goes.product = 'GLM-L2-LCFA'
# api_goes.data_variable = 'event_energy'
# api_goes.get_file(datetime='2019-04-08 18', filename='OR_GLM-L2'
#                                                      '-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc')
