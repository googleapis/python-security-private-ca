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
from collections import OrderedDict
import os
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.security.privateca_v1.services.certificate_authority_service import (
    pagers,
)
from google.cloud.security.privateca_v1.types import resources
from google.cloud.security.privateca_v1.types import service
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import CertificateAuthorityServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import CertificateAuthorityServiceGrpcTransport
from .transports.grpc_asyncio import CertificateAuthorityServiceGrpcAsyncIOTransport


class CertificateAuthorityServiceClientMeta(type):
    """Metaclass for the CertificateAuthorityService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[CertificateAuthorityServiceTransport]]
    _transport_registry["grpc"] = CertificateAuthorityServiceGrpcTransport
    _transport_registry[
        "grpc_asyncio"
    ] = CertificateAuthorityServiceGrpcAsyncIOTransport

    def get_transport_class(
        cls, label: str = None,
    ) -> Type[CertificateAuthorityServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class CertificateAuthorityServiceClient(
    metaclass=CertificateAuthorityServiceClientMeta
):
    """[Certificate Authority
    Service][google.cloud.security.privateca.v1.CertificateAuthorityService]
    manages private certificate authorities and issued certificates.
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "privateca.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CertificateAuthorityServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CertificateAuthorityServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> CertificateAuthorityServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CertificateAuthorityServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def ca_pool_path(project: str, location: str, ca_pool: str,) -> str:
        """Returns a fully-qualified ca_pool string."""
        return "projects/{project}/locations/{location}/caPools/{ca_pool}".format(
            project=project, location=location, ca_pool=ca_pool,
        )

    @staticmethod
    def parse_ca_pool_path(path: str) -> Dict[str, str]:
        """Parses a ca_pool path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/caPools/(?P<ca_pool>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def certificate_path(
        project: str, location: str, ca_pool: str, certificate: str,
    ) -> str:
        """Returns a fully-qualified certificate string."""
        return "projects/{project}/locations/{location}/caPools/{ca_pool}/certificates/{certificate}".format(
            project=project,
            location=location,
            ca_pool=ca_pool,
            certificate=certificate,
        )

    @staticmethod
    def parse_certificate_path(path: str) -> Dict[str, str]:
        """Parses a certificate path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/caPools/(?P<ca_pool>.+?)/certificates/(?P<certificate>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def certificate_authority_path(
        project: str, location: str, ca_pool: str, certificate_authority: str,
    ) -> str:
        """Returns a fully-qualified certificate_authority string."""
        return "projects/{project}/locations/{location}/caPools/{ca_pool}/certificateAuthorities/{certificate_authority}".format(
            project=project,
            location=location,
            ca_pool=ca_pool,
            certificate_authority=certificate_authority,
        )

    @staticmethod
    def parse_certificate_authority_path(path: str) -> Dict[str, str]:
        """Parses a certificate_authority path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/caPools/(?P<ca_pool>.+?)/certificateAuthorities/(?P<certificate_authority>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def certificate_revocation_list_path(
        project: str,
        location: str,
        ca_pool: str,
        certificate_authority: str,
        certificate_revocation_list: str,
    ) -> str:
        """Returns a fully-qualified certificate_revocation_list string."""
        return "projects/{project}/locations/{location}/caPools/{ca_pool}/certificateAuthorities/{certificate_authority}/certificateRevocationLists/{certificate_revocation_list}".format(
            project=project,
            location=location,
            ca_pool=ca_pool,
            certificate_authority=certificate_authority,
            certificate_revocation_list=certificate_revocation_list,
        )

    @staticmethod
    def parse_certificate_revocation_list_path(path: str) -> Dict[str, str]:
        """Parses a certificate_revocation_list path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/caPools/(?P<ca_pool>.+?)/certificateAuthorities/(?P<certificate_authority>.+?)/certificateRevocationLists/(?P<certificate_revocation_list>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def certificate_template_path(
        project: str, location: str, certificate_template: str,
    ) -> str:
        """Returns a fully-qualified certificate_template string."""
        return "projects/{project}/locations/{location}/certificateTemplates/{certificate_template}".format(
            project=project,
            location=location,
            certificate_template=certificate_template,
        )

    @staticmethod
    def parse_certificate_template_path(path: str) -> Dict[str, str]:
        """Parses a certificate_template path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/certificateTemplates/(?P<certificate_template>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, CertificateAuthorityServiceTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the certificate authority service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, CertificateAuthorityServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, CertificateAuthorityServiceTransport):
            # transport is a CertificateAuthorityServiceTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
            )

    def create_certificate(
        self,
        request: Union[service.CreateCertificateRequest, dict] = None,
        *,
        parent: str = None,
        certificate: resources.Certificate = None,
        certificate_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.Certificate:
        r"""Create a new
        [Certificate][google.cloud.security.privateca.v1.Certificate] in
        a given Project, Location from a particular
        [CaPool][google.cloud.security.privateca.v1.CaPool].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_create_certificate():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                certificate = privateca_v1.Certificate()
                certificate.pem_csr = "pem_csr_value"

                request = privateca_v1.CreateCertificateRequest(
                    parent="parent_value",
                    certificate=certificate,
                )

                # Make the request
                response = client.create_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.CreateCertificateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.CreateCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificate].
            parent (str):
                Required. The resource name of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]
                associated with the
                [Certificate][google.cloud.security.privateca.v1.Certificate],
                in the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate (google.cloud.security.privateca_v1.types.Certificate):
                Required. A
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                with initial field values.

                This corresponds to the ``certificate`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_id (str):
                Optional. It must be unique within a location and match
                the regular expression ``[a-zA-Z0-9_-]{1,63}``. This
                field is required when using a
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                in the Enterprise [CertificateAuthority.Tier][], but is
                optional and its value is ignored otherwise.

                This corresponds to the ``certificate_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.Certificate:
                A [Certificate][google.cloud.security.privateca.v1.Certificate] corresponds to a signed X.509 certificate issued by a
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, certificate, certificate_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateCertificateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateCertificateRequest):
            request = service.CreateCertificateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if certificate is not None:
                request.certificate = certificate
            if certificate_id is not None:
                request.certificate_id = certificate_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_certificate]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_certificate(
        self,
        request: Union[service.GetCertificateRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.Certificate:
        r"""Returns a
        [Certificate][google.cloud.security.privateca.v1.Certificate].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_get_certificate():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.GetCertificateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.GetCertificateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.GetCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificate].
            name (str):
                Required. The
                [name][google.cloud.security.privateca.v1.Certificate.name]
                of the
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.Certificate:
                A [Certificate][google.cloud.security.privateca.v1.Certificate] corresponds to a signed X.509 certificate issued by a
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetCertificateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetCertificateRequest):
            request = service.GetCertificateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_certificate]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_certificates(
        self,
        request: Union[service.ListCertificatesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCertificatesPager:
        r"""Lists
        [Certificates][google.cloud.security.privateca.v1.Certificate].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_list_certificates():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.ListCertificatesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_certificates(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.ListCertificatesRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.ListCertificates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificates].
            parent (str):
                Required. The resource name of the location associated
                with the
                [Certificates][google.cloud.security.privateca.v1.Certificate],
                in the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificatesPager:
                Response message for
                [CertificateAuthorityService.ListCertificates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificates].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListCertificatesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListCertificatesRequest):
            request = service.ListCertificatesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_certificates]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCertificatesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def revoke_certificate(
        self,
        request: Union[service.RevokeCertificateRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.Certificate:
        r"""Revoke a
        [Certificate][google.cloud.security.privateca.v1.Certificate].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_revoke_certificate():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.RevokeCertificateRequest(
                    name="name_value",
                    reason="ATTRIBUTE_AUTHORITY_COMPROMISE",
                )

                # Make the request
                response = client.revoke_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.RevokeCertificateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.RevokeCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.RevokeCertificate].
            name (str):
                Required. The resource name for this
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                in the format
                ``projects/*/locations/*/caPools/*/certificates/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.Certificate:
                A [Certificate][google.cloud.security.privateca.v1.Certificate] corresponds to a signed X.509 certificate issued by a
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.RevokeCertificateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.RevokeCertificateRequest):
            request = service.RevokeCertificateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.revoke_certificate]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_certificate(
        self,
        request: Union[service.UpdateCertificateRequest, dict] = None,
        *,
        certificate: resources.Certificate = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.Certificate:
        r"""Update a
        [Certificate][google.cloud.security.privateca.v1.Certificate].
        Currently, the only field you can update is the
        [labels][google.cloud.security.privateca.v1.Certificate.labels]
        field.


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_update_certificate():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                certificate = privateca_v1.Certificate()
                certificate.pem_csr = "pem_csr_value"

                request = privateca_v1.UpdateCertificateRequest(
                    certificate=certificate,
                )

                # Make the request
                response = client.update_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.UpdateCertificateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.UpdateCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificate].
            certificate (google.cloud.security.privateca_v1.types.Certificate):
                Required.
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                with updated values.

                This corresponds to the ``certificate`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. A list of fields to be
                updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.Certificate:
                A [Certificate][google.cloud.security.privateca.v1.Certificate] corresponds to a signed X.509 certificate issued by a
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([certificate, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateCertificateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateCertificateRequest):
            request = service.UpdateCertificateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if certificate is not None:
                request.certificate = certificate
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_certificate]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("certificate.name", request.certificate.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def activate_certificate_authority(
        self,
        request: Union[service.ActivateCertificateAuthorityRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Activate a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that is in state
        [AWAITING_USER_ACTIVATION][google.cloud.security.privateca.v1.CertificateAuthority.State.AWAITING_USER_ACTIVATION]
        and is of type
        [SUBORDINATE][google.cloud.security.privateca.v1.CertificateAuthority.Type.SUBORDINATE].
        After the parent Certificate Authority signs a certificate
        signing request from
        [FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr],
        this method can complete the activation process.


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_activate_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                subordinate_config = privateca_v1.SubordinateConfig()
                subordinate_config.certificate_authority = "certificate_authority_value"

                request = privateca_v1.ActivateCertificateAuthorityRequest(
                    name="name_value",
                    pem_ca_certificate="pem_ca_certificate_value",
                    subordinate_config=subordinate_config,
                )

                # Make the request
                operation = client.activate_certificate_authority(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.ActivateCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.ActivateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority].
            name (str):
                Required. The resource name for this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                in the format
                ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateAuthority` A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.ActivateCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ActivateCertificateAuthorityRequest):
            request = service.ActivateCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.activate_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_certificate_authority(
        self,
        request: Union[service.CreateCertificateAuthorityRequest, dict] = None,
        *,
        parent: str = None,
        certificate_authority: resources.CertificateAuthority = None,
        certificate_authority_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Create a new
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        in a given Project and Location.


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_create_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                certificate_authority = privateca_v1.CertificateAuthority()
                certificate_authority.type_ = "SUBORDINATE"
                certificate_authority.key_spec.cloud_kms_key_version = "cloud_kms_key_version_value"

                request = privateca_v1.CreateCertificateAuthorityRequest(
                    parent="parent_value",
                    certificate_authority_id="certificate_authority_id_value",
                    certificate_authority=certificate_authority,
                )

                # Make the request
                operation = client.create_certificate_authority(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.CreateCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.CreateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateAuthority].
            parent (str):
                Required. The resource name of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]
                associated with the
                [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority],
                in the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_authority (google.cloud.security.privateca_v1.types.CertificateAuthority):
                Required. A
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                with initial field values.

                This corresponds to the ``certificate_authority`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_authority_id (str):
                Required. It must be unique within a location and match
                the regular expression ``[a-zA-Z0-9_-]{1,63}``

                This corresponds to the ``certificate_authority_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateAuthority` A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [parent, certificate_authority, certificate_authority_id]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateCertificateAuthorityRequest):
            request = service.CreateCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if certificate_authority is not None:
                request.certificate_authority = certificate_authority
            if certificate_authority_id is not None:
                request.certificate_authority_id = certificate_authority_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def disable_certificate_authority(
        self,
        request: Union[service.DisableCertificateAuthorityRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Disable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_disable_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.DisableCertificateAuthorityRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.disable_certificate_authority(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.DisableCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.DisableCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.DisableCertificateAuthority].
            name (str):
                Required. The resource name for this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                in the format
                ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateAuthority` A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.DisableCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DisableCertificateAuthorityRequest):
            request = service.DisableCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.disable_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def enable_certificate_authority(
        self,
        request: Union[service.EnableCertificateAuthorityRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Enable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_enable_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.EnableCertificateAuthorityRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.enable_certificate_authority(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.EnableCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.EnableCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.EnableCertificateAuthority].
            name (str):
                Required. The resource name for this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                in the format
                ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateAuthority` A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.EnableCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.EnableCertificateAuthorityRequest):
            request = service.EnableCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.enable_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def fetch_certificate_authority_csr(
        self,
        request: Union[service.FetchCertificateAuthorityCsrRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.FetchCertificateAuthorityCsrResponse:
        r"""Fetch a certificate signing request (CSR) from a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that is in state
        [AWAITING_USER_ACTIVATION][google.cloud.security.privateca.v1.CertificateAuthority.State.AWAITING_USER_ACTIVATION]
        and is of type
        [SUBORDINATE][google.cloud.security.privateca.v1.CertificateAuthority.Type.SUBORDINATE].
        The CSR must then be signed by the desired parent Certificate
        Authority, which could be another
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        resource, or could be an on-prem certificate authority. See also
        [ActivateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_fetch_certificate_authority_csr():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.FetchCertificateAuthorityCsrRequest(
                    name="name_value",
                )

                # Make the request
                response = client.fetch_certificate_authority_csr(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.FetchCertificateAuthorityCsrRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr].
            name (str):
                Required. The resource name for this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                in the format
                ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.FetchCertificateAuthorityCsrResponse:
                Response message for
                   [CertificateAuthorityService.FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.FetchCertificateAuthorityCsrRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.FetchCertificateAuthorityCsrRequest):
            request = service.FetchCertificateAuthorityCsrRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.fetch_certificate_authority_csr
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_certificate_authority(
        self,
        request: Union[service.GetCertificateAuthorityRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CertificateAuthority:
        r"""Returns a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_get_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.GetCertificateAuthorityRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_certificate_authority(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.GetCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.GetCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateAuthority].
            name (str):
                Required. The
                [name][google.cloud.security.privateca.v1.CertificateAuthority.name]
                of the
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.CertificateAuthority:
                A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetCertificateAuthorityRequest):
            request = service.GetCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_certificate_authorities(
        self,
        request: Union[service.ListCertificateAuthoritiesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCertificateAuthoritiesPager:
        r"""Lists
        [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_list_certificate_authorities():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.ListCertificateAuthoritiesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_certificate_authorities(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.ListCertificateAuthoritiesRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.ListCertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateAuthorities].
            parent (str):
                Required. The resource name of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]
                associated with the
                [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority],
                in the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificateAuthoritiesPager:
                Response message for
                   [CertificateAuthorityService.ListCertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateAuthorities].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListCertificateAuthoritiesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListCertificateAuthoritiesRequest):
            request = service.ListCertificateAuthoritiesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_certificate_authorities
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCertificateAuthoritiesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def undelete_certificate_authority(
        self,
        request: Union[service.UndeleteCertificateAuthorityRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Undelete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that has been deleted.


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_undelete_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.UndeleteCertificateAuthorityRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.undelete_certificate_authority(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.UndeleteCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.UndeleteCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.UndeleteCertificateAuthority].
            name (str):
                Required. The resource name for this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                in the format
                ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateAuthority` A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.UndeleteCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UndeleteCertificateAuthorityRequest):
            request = service.UndeleteCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.undelete_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_certificate_authority(
        self,
        request: Union[service.DeleteCertificateAuthorityRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Delete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_delete_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.DeleteCertificateAuthorityRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_certificate_authority(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.DeleteCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.DeleteCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateAuthority].
            name (str):
                Required. The resource name for this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                in the format
                ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateAuthority` A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.DeleteCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DeleteCertificateAuthorityRequest):
            request = service.DeleteCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_certificate_authority(
        self,
        request: Union[service.UpdateCertificateAuthorityRequest, dict] = None,
        *,
        certificate_authority: resources.CertificateAuthority = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Update a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_update_certificate_authority():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                certificate_authority = privateca_v1.CertificateAuthority()
                certificate_authority.type_ = "SUBORDINATE"
                certificate_authority.key_spec.cloud_kms_key_version = "cloud_kms_key_version_value"

                request = privateca_v1.UpdateCertificateAuthorityRequest(
                    certificate_authority=certificate_authority,
                )

                # Make the request
                operation = client.update_certificate_authority(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.UpdateCertificateAuthorityRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.UpdateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateAuthority].
            certificate_authority (google.cloud.security.privateca_v1.types.CertificateAuthority):
                Required.
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                with updated values.

                This corresponds to the ``certificate_authority`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. A list of fields to be
                updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateAuthority` A [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority] represents an individual Certificate Authority.
                   A
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   can be used to create
                   [Certificates][google.cloud.security.privateca.v1.Certificate].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([certificate_authority, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateCertificateAuthorityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateCertificateAuthorityRequest):
            request = service.UpdateCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if certificate_authority is not None:
                request.certificate_authority = certificate_authority
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_certificate_authority
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("certificate_authority.name", request.certificate_authority.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_ca_pool(
        self,
        request: Union[service.CreateCaPoolRequest, dict] = None,
        *,
        parent: str = None,
        ca_pool: resources.CaPool = None,
        ca_pool_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Create a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_create_ca_pool():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                ca_pool = privateca_v1.CaPool()
                ca_pool.tier = "DEVOPS"

                request = privateca_v1.CreateCaPoolRequest(
                    parent="parent_value",
                    ca_pool_id="ca_pool_id_value",
                    ca_pool=ca_pool,
                )

                # Make the request
                operation = client.create_ca_pool(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.CreateCaPoolRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.CreateCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCaPool].
            parent (str):
                Required. The resource name of the location associated
                with the
                [CaPool][google.cloud.security.privateca.v1.CaPool], in
                the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ca_pool (google.cloud.security.privateca_v1.types.CaPool):
                Required. A
                [CaPool][google.cloud.security.privateca.v1.CaPool] with
                initial field values.

                This corresponds to the ``ca_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ca_pool_id (str):
                Required. It must be unique within a location and match
                the regular expression ``[a-zA-Z0-9_-]{1,63}``

                This corresponds to the ``ca_pool_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CaPool` A [CaPool][google.cloud.security.privateca.v1.CaPool] represents a group of
                   [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority]
                   that form a trust anchor. A
                   [CaPool][google.cloud.security.privateca.v1.CaPool]
                   can be used to manage issuance policies for one or
                   more
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   resources and to rotate CA certificates in and out of
                   the trust anchor.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, ca_pool, ca_pool_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateCaPoolRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateCaPoolRequest):
            request = service.CreateCaPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if ca_pool is not None:
                request.ca_pool = ca_pool
            if ca_pool_id is not None:
                request.ca_pool_id = ca_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_ca_pool]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CaPool,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_ca_pool(
        self,
        request: Union[service.UpdateCaPoolRequest, dict] = None,
        *,
        ca_pool: resources.CaPool = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Update a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_update_ca_pool():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                ca_pool = privateca_v1.CaPool()
                ca_pool.tier = "DEVOPS"

                request = privateca_v1.UpdateCaPoolRequest(
                    ca_pool=ca_pool,
                )

                # Make the request
                operation = client.update_ca_pool(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.UpdateCaPoolRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.UpdateCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCaPool].
            ca_pool (google.cloud.security.privateca_v1.types.CaPool):
                Required.
                [CaPool][google.cloud.security.privateca.v1.CaPool] with
                updated values.

                This corresponds to the ``ca_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. A list of fields to be
                updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CaPool` A [CaPool][google.cloud.security.privateca.v1.CaPool] represents a group of
                   [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority]
                   that form a trust anchor. A
                   [CaPool][google.cloud.security.privateca.v1.CaPool]
                   can be used to manage issuance policies for one or
                   more
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   resources and to rotate CA certificates in and out of
                   the trust anchor.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([ca_pool, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateCaPoolRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateCaPoolRequest):
            request = service.UpdateCaPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if ca_pool is not None:
                request.ca_pool = ca_pool
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_ca_pool]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("ca_pool.name", request.ca_pool.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CaPool,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_ca_pool(
        self,
        request: Union[service.GetCaPoolRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CaPool:
        r"""Returns a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_get_ca_pool():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.GetCaPoolRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_ca_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.GetCaPoolRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.GetCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCaPool].
            name (str):
                Required. The
                [name][google.cloud.security.privateca.v1.CaPool.name]
                of the
                [CaPool][google.cloud.security.privateca.v1.CaPool] to
                get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.CaPool:
                A [CaPool][google.cloud.security.privateca.v1.CaPool] represents a group of
                   [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority]
                   that form a trust anchor. A
                   [CaPool][google.cloud.security.privateca.v1.CaPool]
                   can be used to manage issuance policies for one or
                   more
                   [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                   resources and to rotate CA certificates in and out of
                   the trust anchor.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetCaPoolRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetCaPoolRequest):
            request = service.GetCaPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_ca_pool]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_ca_pools(
        self,
        request: Union[service.ListCaPoolsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCaPoolsPager:
        r"""Lists [CaPools][google.cloud.security.privateca.v1.CaPool].

        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_list_ca_pools():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.ListCaPoolsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_ca_pools(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.ListCaPoolsRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.ListCaPools][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCaPools].
            parent (str):
                Required. The resource name of the location associated
                with the
                [CaPools][google.cloud.security.privateca.v1.CaPool], in
                the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCaPoolsPager:
                Response message for
                   [CertificateAuthorityService.ListCaPools][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCaPools].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListCaPoolsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListCaPoolsRequest):
            request = service.ListCaPoolsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_ca_pools]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCaPoolsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_ca_pool(
        self,
        request: Union[service.DeleteCaPoolRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Delete a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_delete_ca_pool():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.DeleteCaPoolRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_ca_pool(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.DeleteCaPoolRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.DeleteCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCaPool].
            name (str):
                Required. The resource name for this
                [CaPool][google.cloud.security.privateca.v1.CaPool] in
                the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.DeleteCaPoolRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DeleteCaPoolRequest):
            request = service.DeleteCaPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_ca_pool]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def fetch_ca_certs(
        self,
        request: Union[service.FetchCaCertsRequest, dict] = None,
        *,
        ca_pool: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.FetchCaCertsResponse:
        r"""FetchCaCerts returns the current trust anchor for the
        [CaPool][google.cloud.security.privateca.v1.CaPool]. This will
        include CA certificate chains for all ACTIVE
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        resources in the
        [CaPool][google.cloud.security.privateca.v1.CaPool].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_fetch_ca_certs():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.FetchCaCertsRequest(
                    ca_pool="ca_pool_value",
                )

                # Make the request
                response = client.fetch_ca_certs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.FetchCaCertsRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.FetchCaCerts][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCaCerts].
            ca_pool (str):
                Required. The resource name for the
                [CaPool][google.cloud.security.privateca.v1.CaPool] in
                the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``ca_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.FetchCaCertsResponse:
                Response message for
                   [CertificateAuthorityService.FetchCaCerts][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCaCerts].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([ca_pool])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.FetchCaCertsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.FetchCaCertsRequest):
            request = service.FetchCaCertsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if ca_pool is not None:
                request.ca_pool = ca_pool

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.fetch_ca_certs]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("ca_pool", request.ca_pool),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_certificate_revocation_list(
        self,
        request: Union[service.GetCertificateRevocationListRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CertificateRevocationList:
        r"""Returns a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_get_certificate_revocation_list():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.GetCertificateRevocationListRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_certificate_revocation_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.GetCertificateRevocationListRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.GetCertificateRevocationList][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateRevocationList].
            name (str):
                Required. The
                [name][google.cloud.security.privateca.v1.CertificateRevocationList.name]
                of the
                [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.CertificateRevocationList:
                A [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList] corresponds to a signed X.509 certificate
                   Revocation List (CRL). A CRL contains the serial
                   numbers of certificates that should no longer be
                   trusted.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetCertificateRevocationListRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetCertificateRevocationListRequest):
            request = service.GetCertificateRevocationListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_certificate_revocation_list
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_certificate_revocation_lists(
        self,
        request: Union[service.ListCertificateRevocationListsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCertificateRevocationListsPager:
        r"""Lists
        [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_list_certificate_revocation_lists():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.ListCertificateRevocationListsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_certificate_revocation_lists(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.ListCertificateRevocationListsRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.ListCertificateRevocationLists][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateRevocationLists].
            parent (str):
                Required. The resource name of the location associated
                with the
                [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList],
                in the format
                ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificateRevocationListsPager:
                Response message for
                   [CertificateAuthorityService.ListCertificateRevocationLists][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateRevocationLists].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListCertificateRevocationListsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListCertificateRevocationListsRequest):
            request = service.ListCertificateRevocationListsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_certificate_revocation_lists
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCertificateRevocationListsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_certificate_revocation_list(
        self,
        request: Union[service.UpdateCertificateRevocationListRequest, dict] = None,
        *,
        certificate_revocation_list: resources.CertificateRevocationList = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Update a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_update_certificate_revocation_list():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.UpdateCertificateRevocationListRequest(
                )

                # Make the request
                operation = client.update_certificate_revocation_list(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.UpdateCertificateRevocationListRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.UpdateCertificateRevocationList][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateRevocationList].
            certificate_revocation_list (google.cloud.security.privateca_v1.types.CertificateRevocationList):
                Required.
                [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
                with updated values.

                This corresponds to the ``certificate_revocation_list`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. A list of fields to be
                updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateRevocationList` A [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList] corresponds to a signed X.509 certificate
                   Revocation List (CRL). A CRL contains the serial
                   numbers of certificates that should no longer be
                   trusted.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([certificate_revocation_list, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateCertificateRevocationListRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateCertificateRevocationListRequest):
            request = service.UpdateCertificateRevocationListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if certificate_revocation_list is not None:
                request.certificate_revocation_list = certificate_revocation_list
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_certificate_revocation_list
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "certificate_revocation_list.name",
                        request.certificate_revocation_list.name,
                    ),
                )
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateRevocationList,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_certificate_template(
        self,
        request: Union[service.CreateCertificateTemplateRequest, dict] = None,
        *,
        parent: str = None,
        certificate_template: resources.CertificateTemplate = None,
        certificate_template_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Create a new
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
        in a given Project and Location.


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_create_certificate_template():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.CreateCertificateTemplateRequest(
                    parent="parent_value",
                    certificate_template_id="certificate_template_id_value",
                )

                # Make the request
                operation = client.create_certificate_template(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.CreateCertificateTemplateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.CreateCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateTemplate].
            parent (str):
                Required. The resource name of the location associated
                with the
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate],
                in the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_template (google.cloud.security.privateca_v1.types.CertificateTemplate):
                Required. A
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                with initial field values.

                This corresponds to the ``certificate_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_template_id (str):
                Required. It must be unique within a location and match
                the regular expression ``[a-zA-Z0-9_-]{1,63}``

                This corresponds to the ``certificate_template_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateTemplate` A [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate] refers to a managed template for certificate
                   issuance.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [parent, certificate_template, certificate_template_id]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateCertificateTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateCertificateTemplateRequest):
            request = service.CreateCertificateTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if certificate_template is not None:
                request.certificate_template = certificate_template
            if certificate_template_id is not None:
                request.certificate_template_id = certificate_template_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_certificate_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateTemplate,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_certificate_template(
        self,
        request: Union[service.DeleteCertificateTemplateRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""DeleteCertificateTemplate deletes a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_delete_certificate_template():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.DeleteCertificateTemplateRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_certificate_template(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.DeleteCertificateTemplateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.DeleteCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateTemplate].
            name (str):
                Required. The resource name for this
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                in the format
                ``projects/*/locations/*/certificateTemplates/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.DeleteCertificateTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DeleteCertificateTemplateRequest):
            request = service.DeleteCertificateTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_certificate_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_certificate_template(
        self,
        request: Union[service.GetCertificateTemplateRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CertificateTemplate:
        r"""Returns a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_get_certificate_template():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.GetCertificateTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_certificate_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.GetCertificateTemplateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.GetCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateTemplate].
            name (str):
                Required. The
                [name][google.cloud.security.privateca.v1.CertificateTemplate.name]
                of the
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.types.CertificateTemplate:
                A [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate] refers to a managed template for certificate
                   issuance.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetCertificateTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetCertificateTemplateRequest):
            request = service.GetCertificateTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_certificate_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_certificate_templates(
        self,
        request: Union[service.ListCertificateTemplatesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCertificateTemplatesPager:
        r"""Lists
        [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_list_certificate_templates():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.ListCertificateTemplatesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_certificate_templates(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.ListCertificateTemplatesRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.ListCertificateTemplates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateTemplates].
            parent (str):
                Required. The resource name of the location associated
                with the
                [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate],
                in the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificateTemplatesPager:
                Response message for
                   [CertificateAuthorityService.ListCertificateTemplates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateTemplates].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListCertificateTemplatesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListCertificateTemplatesRequest):
            request = service.ListCertificateTemplatesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_certificate_templates
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCertificateTemplatesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_certificate_template(
        self,
        request: Union[service.UpdateCertificateTemplateRequest, dict] = None,
        *,
        certificate_template: resources.CertificateTemplate = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Update a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block:: python

            from google.cloud.security import privateca_v1

            def sample_update_certificate_template():
                # Create a client
                client = privateca_v1.CertificateAuthorityServiceClient()

                # Initialize request argument(s)
                request = privateca_v1.UpdateCertificateTemplateRequest(
                )

                # Make the request
                operation = client.update_certificate_template(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.security.privateca_v1.types.UpdateCertificateTemplateRequest, dict]):
                The request object. Request message for
                [CertificateAuthorityService.UpdateCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateTemplate].
            certificate_template (google.cloud.security.privateca_v1.types.CertificateTemplate):
                Required.
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                with updated values.

                This corresponds to the ``certificate_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. A list of fields to be
                updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateTemplate` A [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate] refers to a managed template for certificate
                   issuance.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([certificate_template, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateCertificateTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateCertificateTemplateRequest):
            request = service.UpdateCertificateTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if certificate_template is not None:
                request.certificate_template = certificate_template
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_certificate_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("certificate_template.name", request.certificate_template.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.CertificateTemplate,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-private-ca",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("CertificateAuthorityServiceClient",)
