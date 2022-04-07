# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for GetCertificateAuthority
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-private-ca


# [START privateca_v1beta1_generated_CertificateAuthorityService_GetCertificateAuthority_sync]
from google.cloud.security import privateca_v1beta1


def sample_get_certificate_authority():
    # Create a client
    client = privateca_v1beta1.CertificateAuthorityServiceClient()

    # Initialize request argument(s)
    request = privateca_v1beta1.GetCertificateAuthorityRequest(
        name="name_value",
    )

    # Make the request
    response = client.get_certificate_authority(request=request)

    # Handle the response
    print(response)

# [END privateca_v1beta1_generated_CertificateAuthorityService_GetCertificateAuthority_sync]
