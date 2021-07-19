#!/usr/bin/env python

# Copyright 2021 Google LLC
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

import sys

# [START privateca_create_certificate]
from google.cloud import kms
import google.cloud.security.privateca_v1 as privateca_v1
from google.protobuf import duration_pb2


def create_certificate(
    project_id: str,
    location: str,
    ca_pool_name: str,
    ca_name: str,
    certificate_name: str,
    kms_location: str,
    key_ring_id: str,
    key_id: str,
    key_version_id: str,
    common_name: str,
    domain_name: str,
    certificate_lifetime: int,
) -> None:
    """
    Create a Certificate which is issued by the Certificate Authority present in the CA Pool.
    The key used to sign the certificate is created by the Cloud KMS.

    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
        ca_pool_name: set a unique name for the CA pool.
        ca_name: the name of the certificate authority which issues the certificate.
        certificate_name: set a unique name for the certificate.
        kms_location: Cloud KMS location.
        key_ring_id: ID of the Cloud KMS key ring.
        key_id: ID of the key to use.
        key_version_id: verstion ID of the key to use.
        common_name: a title for your certificate.
        domain_name: fully qualified domain name for your certificate.
        certificate_lifetime: the validity of the certificate in seconds.
    """

    kmsClient = kms.KeyManagementServiceClient()
    caServiceClient = privateca_v1.CertificateAuthorityServiceClient()

    # To sign and issue a certificate, a public key is essential. Here, we are making use
    # of Cloud KMS to retrieve an already created public key. For more info, see: https://cloud.google.com/kms/docs/retrieve-public-key.
    # Generating keys locally is also possible.

    key_version_name = kmsClient.crypto_key_version_path(
        project_id, kms_location, key_ring_id, key_id, key_version_id
    )
    kms_public_key = kmsClient.get_public_key(name=key_version_name)

    # Set the Public Key and its format as obtained from the Cloud KMS.
    public_key = privateca_v1.PublicKey(
        key=str.encode(kms_public_key.pem),
        format_=privateca_v1.PublicKey.KeyFormat.PEM,
    )

    subject_config = privateca_v1.CertificateConfig.SubjectConfig(
        subject=privateca_v1.Subject(common_name=common_name),
        subject_alt_name=privateca_v1.SubjectAltNames(dns_names=[domain_name]),
    )

    # Set the X.509 fields required for the certificate.
    x509_parameters = privateca_v1.X509Parameters(
        key_usage=privateca_v1.KeyUsage(
            base_key_usage=privateca_v1.KeyUsage.KeyUsageOptions(
                digital_signature=True,
                key_encipherment=True,
            ),
            extended_key_usage=privateca_v1.KeyUsage.ExtendedKeyUsageOptions(
                server_auth=True,
                client_auth=True,
            ),
        ),
    )

    # Create certificate.
    certificate = privateca_v1.Certificate(
        config=privateca_v1.CertificateConfig(
            public_key=public_key,
            subject_config=subject_config,
            x509_config=x509_parameters,
        ),
        lifetime=duration_pb2.Duration(seconds=certificate_lifetime),
    )

    # Create the Certificate Request.
    request = privateca_v1.CreateCertificateRequest(
        parent=caServiceClient.ca_pool_path(project_id, location, ca_pool_name),
        certificate_id=certificate_name,
        certificate=certificate,
        issuing_certificate_authority_id=ca_name,
    )
    result = caServiceClient.create_certificate(request=request)

    print("Certificate creation result:", result)


# [END privateca_create_certificate]

