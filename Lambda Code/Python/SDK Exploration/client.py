# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except
# in compliance with the License. A copy of the License is located at
#
# https://aws.amazon.com/apache-2-0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import boto3

client = boto3.client('s3')

response = client.list_objects_v2(Bucket='<BUCKET_NAME>')

for content in response['Contents']:
    obj_dict = client.get_object(Bucket='<BUCKET_NAME>', Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])
