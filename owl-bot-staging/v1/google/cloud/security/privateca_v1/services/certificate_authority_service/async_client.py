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
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.security.privateca_v1.services.certificate_authority_service import pagers
from google.cloud.security.privateca_v1.types import resources
from google.cloud.security.privateca_v1.types import service
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import CertificateAuthorityServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import CertificateAuthorityServiceGrpcAsyncIOTransport
from .client import CertificateAuthorityServiceClient


class CertificateAuthorityServiceAsyncClient:
    """[Certificate Authority
    Service][google.cloud.security.privateca.v1.CertificateAuthorityService]
    manages private certificate authorities and issued certificates.
    """

    _client: CertificateAuthorityServiceClient

    DEFAULT_ENDPOINT = CertificateAuthorityServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CertificateAuthorityServiceClient.DEFAULT_MTLS_ENDPOINT

    ca_pool_path = staticmethod(CertificateAuthorityServiceClient.ca_pool_path)
    parse_ca_pool_path = staticmethod(CertificateAuthorityServiceClient.parse_ca_pool_path)
    certificate_path = staticmethod(CertificateAuthorityServiceClient.certificate_path)
    parse_certificate_path = staticmethod(CertificateAuthorityServiceClient.parse_certificate_path)
    certificate_authority_path = staticmethod(CertificateAuthorityServiceClient.certificate_authority_path)
    parse_certificate_authority_path = staticmethod(CertificateAuthorityServiceClient.parse_certificate_authority_path)
    certificate_revocation_list_path = staticmethod(CertificateAuthorityServiceClient.certificate_revocation_list_path)
    parse_certificate_revocation_list_path = staticmethod(CertificateAuthorityServiceClient.parse_certificate_revocation_list_path)
    certificate_template_path = staticmethod(CertificateAuthorityServiceClient.certificate_template_path)
    parse_certificate_template_path = staticmethod(CertificateAuthorityServiceClient.parse_certificate_template_path)
    common_billing_account_path = staticmethod(CertificateAuthorityServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(CertificateAuthorityServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(CertificateAuthorityServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(CertificateAuthorityServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(CertificateAuthorityServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(CertificateAuthorityServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(CertificateAuthorityServiceClient.common_project_path)
    parse_common_project_path = staticmethod(CertificateAuthorityServiceClient.parse_common_project_path)
    common_location_path = staticmethod(CertificateAuthorityServiceClient.common_location_path)
    parse_common_location_path = staticmethod(CertificateAuthorityServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CertificateAuthorityServiceAsyncClient: The constructed client.
        """
        return CertificateAuthorityServiceClient.from_service_account_info.__func__(CertificateAuthorityServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            CertificateAuthorityServiceAsyncClient: The constructed client.
        """
        return CertificateAuthorityServiceClient.from_service_account_file.__func__(CertificateAuthorityServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
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
        return CertificateAuthorityServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CertificateAuthorityServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CertificateAuthorityServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(CertificateAuthorityServiceClient).get_transport_class, type(CertificateAuthorityServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, CertificateAuthorityServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the certificate authority service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.CertificateAuthorityServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
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

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = CertificateAuthorityServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def create_certificate(self,
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


        .. code-block::

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
            parent (:class:`str`):
                Required. The resource name of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]
                associated with the
                [Certificate][google.cloud.security.privateca.v1.Certificate],
                in the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate (:class:`google.cloud.security.privateca_v1.types.Certificate`):
                Required. A
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                with initial field values.

                This corresponds to the ``certificate`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_id (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

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
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_certificate,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_certificate(self,
            request: Union[service.GetCertificateRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.Certificate:
        r"""Returns a
        [Certificate][google.cloud.security.privateca.v1.Certificate].


        .. code-block::

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
            name (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.GetCertificateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_certificate,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_certificates(self,
            request: Union[service.ListCertificatesRequest, dict] = None,
            *,
            parent: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListCertificatesAsyncPager:
        r"""Lists
        [Certificates][google.cloud.security.privateca.v1.Certificate].


        .. code-block::

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
            parent (:class:`str`):
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
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificatesAsyncPager:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.ListCertificatesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_certificates,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCertificatesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def revoke_certificate(self,
            request: Union[service.RevokeCertificateRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.Certificate:
        r"""Revoke a
        [Certificate][google.cloud.security.privateca.v1.Certificate].


        .. code-block::

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
            name (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.RevokeCertificateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.revoke_certificate,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_certificate(self,
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


        .. code-block::

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
            certificate (:class:`google.cloud.security.privateca_v1.types.Certificate`):
                Required.
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                with updated values.

                This corresponds to the ``certificate`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.UpdateCertificateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if certificate is not None:
            request.certificate = certificate
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_certificate,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("certificate.name", request.certificate.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def activate_certificate_authority(self,
            request: Union[service.ActivateCertificateAuthorityRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
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


        .. code-block::

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
            name (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.ActivateCertificateAuthorityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.activate_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_certificate_authority(self,
            request: Union[service.CreateCertificateAuthorityRequest, dict] = None,
            *,
            parent: str = None,
            certificate_authority: resources.CertificateAuthority = None,
            certificate_authority_id: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Create a new
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        in a given Project and Location.


        .. code-block::

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
            parent (:class:`str`):
                Required. The resource name of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]
                associated with the
                [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority],
                in the format ``projects/*/locations/*/caPools/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_authority (:class:`google.cloud.security.privateca_v1.types.CertificateAuthority`):
                Required. A
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                with initial field values.

                This corresponds to the ``certificate_authority`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_authority_id (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
        has_flattened_params = any([parent, certificate_authority, certificate_authority_id])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

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
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def disable_certificate_authority(self,
            request: Union[service.DisableCertificateAuthorityRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Disable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block::

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
            name (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.DisableCertificateAuthorityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.disable_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def enable_certificate_authority(self,
            request: Union[service.EnableCertificateAuthorityRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Enable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block::

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
            name (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.EnableCertificateAuthorityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.enable_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def fetch_certificate_authority_csr(self,
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


        .. code-block::

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
            name (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.FetchCertificateAuthorityCsrRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.fetch_certificate_authority_csr,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_certificate_authority(self,
            request: Union[service.GetCertificateAuthorityRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.CertificateAuthority:
        r"""Returns a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block::

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
            name (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.GetCertificateAuthorityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_certificate_authorities(self,
            request: Union[service.ListCertificateAuthoritiesRequest, dict] = None,
            *,
            parent: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListCertificateAuthoritiesAsyncPager:
        r"""Lists
        [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block::

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
            parent (:class:`str`):
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
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificateAuthoritiesAsyncPager:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.ListCertificateAuthoritiesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_certificate_authorities,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCertificateAuthoritiesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def undelete_certificate_authority(self,
            request: Union[service.UndeleteCertificateAuthorityRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Undelete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that has been deleted.


        .. code-block::

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
            name (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.UndeleteCertificateAuthorityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.undelete_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_certificate_authority(self,
            request: Union[service.DeleteCertificateAuthorityRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Delete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block::

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
            name (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.DeleteCertificateAuthorityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_certificate_authority(self,
            request: Union[service.UpdateCertificateAuthorityRequest, dict] = None,
            *,
            certificate_authority: resources.CertificateAuthority = None,
            update_mask: field_mask_pb2.FieldMask = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Update a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].


        .. code-block::

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
            certificate_authority (:class:`google.cloud.security.privateca_v1.types.CertificateAuthority`):
                Required.
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                with updated values.

                This corresponds to the ``certificate_authority`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.UpdateCertificateAuthorityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if certificate_authority is not None:
            request.certificate_authority = certificate_authority
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_certificate_authority,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("certificate_authority.name", request.certificate_authority.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateAuthority,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_ca_pool(self,
            request: Union[service.CreateCaPoolRequest, dict] = None,
            *,
            parent: str = None,
            ca_pool: resources.CaPool = None,
            ca_pool_id: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Create a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block::

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
            parent (:class:`str`):
                Required. The resource name of the location associated
                with the
                [CaPool][google.cloud.security.privateca.v1.CaPool], in
                the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ca_pool (:class:`google.cloud.security.privateca_v1.types.CaPool`):
                Required. A
                [CaPool][google.cloud.security.privateca.v1.CaPool] with
                initial field values.

                This corresponds to the ``ca_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ca_pool_id (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

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
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_ca_pool,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CaPool,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_ca_pool(self,
            request: Union[service.UpdateCaPoolRequest, dict] = None,
            *,
            ca_pool: resources.CaPool = None,
            update_mask: field_mask_pb2.FieldMask = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Update a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block::

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
            ca_pool (:class:`google.cloud.security.privateca_v1.types.CaPool`):
                Required.
                [CaPool][google.cloud.security.privateca.v1.CaPool] with
                updated values.

                This corresponds to the ``ca_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.UpdateCaPoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if ca_pool is not None:
            request.ca_pool = ca_pool
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_ca_pool,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("ca_pool.name", request.ca_pool.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CaPool,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_ca_pool(self,
            request: Union[service.GetCaPoolRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.CaPool:
        r"""Returns a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block::

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
            name (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.GetCaPoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_ca_pool,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_ca_pools(self,
            request: Union[service.ListCaPoolsRequest, dict] = None,
            *,
            parent: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListCaPoolsAsyncPager:
        r"""Lists [CaPools][google.cloud.security.privateca.v1.CaPool].

        .. code-block::

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
            parent (:class:`str`):
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
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCaPoolsAsyncPager:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.ListCaPoolsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_ca_pools,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCaPoolsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_ca_pool(self,
            request: Union[service.DeleteCaPoolRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Delete a [CaPool][google.cloud.security.privateca.v1.CaPool].

        .. code-block::

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
            name (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.DeleteCaPoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_ca_pool,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def fetch_ca_certs(self,
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


        .. code-block::

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
            ca_pool (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.FetchCaCertsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if ca_pool is not None:
            request.ca_pool = ca_pool

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.fetch_ca_certs,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("ca_pool", request.ca_pool),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_certificate_revocation_list(self,
            request: Union[service.GetCertificateRevocationListRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.CertificateRevocationList:
        r"""Returns a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].


        .. code-block::

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
            name (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.GetCertificateRevocationListRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_certificate_revocation_list,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_certificate_revocation_lists(self,
            request: Union[service.ListCertificateRevocationListsRequest, dict] = None,
            *,
            parent: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListCertificateRevocationListsAsyncPager:
        r"""Lists
        [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList].


        .. code-block::

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
            parent (:class:`str`):
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
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificateRevocationListsAsyncPager:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.ListCertificateRevocationListsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_certificate_revocation_lists,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCertificateRevocationListsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_certificate_revocation_list(self,
            request: Union[service.UpdateCertificateRevocationListRequest, dict] = None,
            *,
            certificate_revocation_list: resources.CertificateRevocationList = None,
            update_mask: field_mask_pb2.FieldMask = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Update a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].


        .. code-block::

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
            certificate_revocation_list (:class:`google.cloud.security.privateca_v1.types.CertificateRevocationList`):
                Required.
                [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
                with updated values.

                This corresponds to the ``certificate_revocation_list`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.UpdateCertificateRevocationListRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if certificate_revocation_list is not None:
            request.certificate_revocation_list = certificate_revocation_list
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_certificate_revocation_list,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("certificate_revocation_list.name", request.certificate_revocation_list.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateRevocationList,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_certificate_template(self,
            request: Union[service.CreateCertificateTemplateRequest, dict] = None,
            *,
            parent: str = None,
            certificate_template: resources.CertificateTemplate = None,
            certificate_template_id: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Create a new
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
        in a given Project and Location.


        .. code-block::

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
            parent (:class:`str`):
                Required. The resource name of the location associated
                with the
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate],
                in the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_template (:class:`google.cloud.security.privateca_v1.types.CertificateTemplate`):
                Required. A
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                with initial field values.

                This corresponds to the ``certificate_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            certificate_template_id (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateTemplate` A [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate] refers to a managed template for certificate
                   issuance.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, certificate_template, certificate_template_id])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

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
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_certificate_template,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateTemplate,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_certificate_template(self,
            request: Union[service.DeleteCertificateTemplateRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""DeleteCertificateTemplate deletes a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block::

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
            name (:class:`str`):
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
            google.api_core.operation_async.AsyncOperation:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.DeleteCertificateTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_certificate_template,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_certificate_template(self,
            request: Union[service.GetCertificateTemplateRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.CertificateTemplate:
        r"""Returns a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block::

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
            name (:class:`str`):
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.GetCertificateTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_certificate_template,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_certificate_templates(self,
            request: Union[service.ListCertificateTemplatesRequest, dict] = None,
            *,
            parent: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListCertificateTemplatesAsyncPager:
        r"""Lists
        [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block::

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
            parent (:class:`str`):
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
            google.cloud.security.privateca_v1.services.certificate_authority_service.pagers.ListCertificateTemplatesAsyncPager:
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
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.ListCertificateTemplatesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_certificate_templates,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCertificateTemplatesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_certificate_template(self,
            request: Union[service.UpdateCertificateTemplateRequest, dict] = None,
            *,
            certificate_template: resources.CertificateTemplate = None,
            update_mask: field_mask_pb2.FieldMask = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Update a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].


        .. code-block::

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
            certificate_template (:class:`google.cloud.security.privateca_v1.types.CertificateTemplate`):
                Required.
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                with updated values.

                This corresponds to the ``certificate_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.security.privateca_v1.types.CertificateTemplate` A [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate] refers to a managed template for certificate
                   issuance.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([certificate_template, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.UpdateCertificateTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if certificate_template is not None:
            request.certificate_template = certificate_template
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_certificate_template,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("certificate_template.name", request.certificate_template.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resources.CertificateTemplate,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-private-ca",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "CertificateAuthorityServiceAsyncClient",
)
