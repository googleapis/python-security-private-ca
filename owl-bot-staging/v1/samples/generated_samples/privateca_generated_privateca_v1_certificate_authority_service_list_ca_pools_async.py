# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Snippet for ListCaPools
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-private-ca


# [START privateca_generated_privateca_v1_CertificateAuthorityService_ListCaPools_async]
from google.cloud.security import privateca_v1


async def sample_list_ca_pools():
    # Create a client
    client = privateca_v1.CertificateAuthorityServiceAsyncClient()

    # Initialize request argument(s)
    request = privateca_v1.ListCaPoolsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_ca_pools(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

# [END privateca_generated_privateca_v1_CertificateAuthorityService_ListCaPools_async]
