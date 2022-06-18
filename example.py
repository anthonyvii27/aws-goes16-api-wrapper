from awsS3ApiGoes16 import AwsS3ApiGoes16

test = AwsS3ApiGoes16('s3fs')

test.remote_bucket('')
test.local_bucket('/')

test.set_product('GLM-L2-LCFA')

bucket_list = test.s3_client.list_buckets(test.remote_bucket, test.local_bucket)
# bucket_list

file_list = test.s3_client.list_files('noaa-goes16/GLM-L2-LCFA/2019/098/18', test.local_bucket)
# file_list

test.s3_client.get_file('noaa-goes16/GLM-L2-LCFA/2019/098/18/OR_GLM-L2-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc', 'OR_GLM-L2-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc')
