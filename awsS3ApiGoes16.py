from awsS3Api import AwsS3Api


class AwsS3ApiGoes16(AwsS3Api):
    initial_date = ""
    due_date = ""
    data_variable = ""
    product = ""

    def __init__(self, s3_client_name="boto3"):
        super().__init__(s3_client_name)
        self.set_remote_bucket("noaa-goes16")

    def set_initial_date(self, date):
        self.initial_date = date

    def set_due_date(self, date):
        self.due_date = date

    def set_data_variable(self, data_variable):
        self.data_variable = data_variable

    def set_product(self, product):
        self.product = product
