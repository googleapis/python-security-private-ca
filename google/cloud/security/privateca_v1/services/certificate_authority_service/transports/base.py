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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

from google.cloud.security.privateca_v1.types import resources, service

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-private-ca",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class CertificateAuthorityServiceTransport(abc.ABC):
    """Abstract transport class for CertificateAuthorityService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "privateca.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_certificate: gapic_v1.method.wrap_method(
                self.create_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate: gapic_v1.method.wrap_method(
                self.get_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificates: gapic_v1.method.wrap_method(
                self.list_certificates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.revoke_certificate: gapic_v1.method.wrap_method(
                self.revoke_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate: gapic_v1.method.wrap_method(
                self.update_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.activate_certificate_authority: gapic_v1.method.wrap_method(
                self.activate_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_certificate_authority: gapic_v1.method.wrap_method(
                self.create_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.disable_certificate_authority: gapic_v1.method.wrap_method(
                self.disable_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_certificate_authority: gapic_v1.method.wrap_method(
                self.enable_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_certificate_authority_csr: gapic_v1.method.wrap_method(
                self.fetch_certificate_authority_csr,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate_authority: gapic_v1.method.wrap_method(
                self.get_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificate_authorities: gapic_v1.method.wrap_method(
                self.list_certificate_authorities,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undelete_certificate_authority: gapic_v1.method.wrap_method(
                self.undelete_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_certificate_authority: gapic_v1.method.wrap_method(
                self.delete_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate_authority: gapic_v1.method.wrap_method(
                self.update_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_ca_pool: gapic_v1.method.wrap_method(
                self.create_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_ca_pool: gapic_v1.method.wrap_method(
                self.update_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_ca_pool: gapic_v1.method.wrap_method(
                self.get_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_ca_pools: gapic_v1.method.wrap_method(
                self.list_ca_pools,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_ca_pool: gapic_v1.method.wrap_method(
                self.delete_ca_pool,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_ca_certs: gapic_v1.method.wrap_method(
                self.fetch_ca_certs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate_revocation_list: gapic_v1.method.wrap_method(
                self.get_certificate_revocation_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificate_revocation_lists: gapic_v1.method.wrap_method(
                self.list_certificate_revocation_lists,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate_revocation_list: gapic_v1.method.wrap_method(
                self.update_certificate_revocation_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_certificate_template: gapic_v1.method.wrap_method(
                self.create_certificate_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_certificate_template: gapic_v1.method.wrap_method(
                self.delete_certificate_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_certificate_template: gapic_v1.method.wrap_method(
                self.get_certificate_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_certificate_templates: gapic_v1.method.wrap_method(
                self.list_certificate_templates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_certificate_template: gapic_v1.method.wrap_method(
                self.update_certificate_template,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def create_certificate(
        self,
    ) -> Callable[
        [service.CreateCertificateRequest],
        Union[resources.Certificate, Awaitable[resources.Certificate]],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate(
        self,
    ) -> Callable[
        [service.GetCertificateRequest],
        Union[resources.Certificate, Awaitable[resources.Certificate]],
    ]:
        raise NotImplementedError()

    @property
    def list_certificates(
        self,
    ) -> Callable[
        [service.ListCertificatesRequest],
        Union[
            service.ListCertificatesResponse,
            Awaitable[service.ListCertificatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def revoke_certificate(
        self,
    ) -> Callable[
        [service.RevokeCertificateRequest],
        Union[resources.Certificate, Awaitable[resources.Certificate]],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate(
        self,
    ) -> Callable[
        [service.UpdateCertificateRequest],
        Union[resources.Certificate, Awaitable[resources.Certificate]],
    ]:
        raise NotImplementedError()

    @property
    def activate_certificate_authority(
        self,
    ) -> Callable[
        [service.ActivateCertificateAuthorityRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_certificate_authority(
        self,
    ) -> Callable[
        [service.CreateCertificateAuthorityRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def disable_certificate_authority(
        self,
    ) -> Callable[
        [service.DisableCertificateAuthorityRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def enable_certificate_authority(
        self,
    ) -> Callable[
        [service.EnableCertificateAuthorityRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_certificate_authority_csr(
        self,
    ) -> Callable[
        [service.FetchCertificateAuthorityCsrRequest],
        Union[
            service.FetchCertificateAuthorityCsrResponse,
            Awaitable[service.FetchCertificateAuthorityCsrResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate_authority(
        self,
    ) -> Callable[
        [service.GetCertificateAuthorityRequest],
        Union[
            resources.CertificateAuthority, Awaitable[resources.CertificateAuthority]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_certificate_authorities(
        self,
    ) -> Callable[
        [service.ListCertificateAuthoritiesRequest],
        Union[
            service.ListCertificateAuthoritiesResponse,
            Awaitable[service.ListCertificateAuthoritiesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def undelete_certificate_authority(
        self,
    ) -> Callable[
        [service.UndeleteCertificateAuthorityRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_certificate_authority(
        self,
    ) -> Callable[
        [service.DeleteCertificateAuthorityRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate_authority(
        self,
    ) -> Callable[
        [service.UpdateCertificateAuthorityRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_ca_pool(
        self,
    ) -> Callable[
        [service.CreateCaPoolRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_ca_pool(
        self,
    ) -> Callable[
        [service.UpdateCaPoolRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_ca_pool(
        self,
    ) -> Callable[
        [service.GetCaPoolRequest], Union[resources.CaPool, Awaitable[resources.CaPool]]
    ]:
        raise NotImplementedError()

    @property
    def list_ca_pools(
        self,
    ) -> Callable[
        [service.ListCaPoolsRequest],
        Union[service.ListCaPoolsResponse, Awaitable[service.ListCaPoolsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_ca_pool(
        self,
    ) -> Callable[
        [service.DeleteCaPoolRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_ca_certs(
        self,
    ) -> Callable[
        [service.FetchCaCertsRequest],
        Union[service.FetchCaCertsResponse, Awaitable[service.FetchCaCertsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate_revocation_list(
        self,
    ) -> Callable[
        [service.GetCertificateRevocationListRequest],
        Union[
            resources.CertificateRevocationList,
            Awaitable[resources.CertificateRevocationList],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_certificate_revocation_lists(
        self,
    ) -> Callable[
        [service.ListCertificateRevocationListsRequest],
        Union[
            service.ListCertificateRevocationListsResponse,
            Awaitable[service.ListCertificateRevocationListsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate_revocation_list(
        self,
    ) -> Callable[
        [service.UpdateCertificateRevocationListRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_certificate_template(
        self,
    ) -> Callable[
        [service.CreateCertificateTemplateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_certificate_template(
        self,
    ) -> Callable[
        [service.DeleteCertificateTemplateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate_template(
        self,
    ) -> Callable[
        [service.GetCertificateTemplateRequest],
        Union[resources.CertificateTemplate, Awaitable[resources.CertificateTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def list_certificate_templates(
        self,
    ) -> Callable[
        [service.ListCertificateTemplatesRequest],
        Union[
            service.ListCertificateTemplatesResponse,
            Awaitable[service.ListCertificateTemplatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate_template(
        self,
    ) -> Callable[
        [service.UpdateCertificateTemplateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("CertificateAuthorityServiceTransport",)
