# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6365, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import QuantumClientConfiguration
from .operations import JobsOperations
from .operations import ProvidersOperations
from .operations import StorageOperations
from .operations import QuotasOperations
from .. import models


class QuantumClient(object):
    """Azure Quantum REST API client.

    :ivar jobs: JobsOperations operations
    :vartype jobs: quantum_client.aio.operations.JobsOperations
    :ivar providers: ProvidersOperations operations
    :vartype providers: quantum_client.aio.operations.ProvidersOperations
    :ivar storage: StorageOperations operations
    :vartype storage: quantum_client.aio.operations.StorageOperations
    :ivar quotas: QuotasOperations operations
    :vartype quotas: quantum_client.aio.operations.QuotasOperations
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param workspace_name: Name of the workspace.
    :type workspace_name: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://quantum.azure.com'
        self._config = QuantumClientConfiguration(subscription_id, resource_group_name, workspace_name, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.jobs = JobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.providers = ProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage = StorageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quotas = QuotasOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "QuantumClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
