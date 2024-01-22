# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.context_chunks.client import AsyncContextChunksClient, ContextChunksClient
from .resources.contextual_completions.client import AsyncContextualCompletionsClient, ContextualCompletionsClient
from .resources.embeddings.client import AsyncEmbeddingsClient, EmbeddingsClient
from .resources.health.client import AsyncHealthClient, HealthClient
from .resources.ingestion.client import AsyncIngestionClient, IngestionClient


class PrivateGPTApi:
    def __init__(
        self, *, base_url: str, timeout: typing.Optional[float] = 60, httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url, httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
        )
        self.contextual_completions = ContextualCompletionsClient(client_wrapper=self._client_wrapper)
        self.context_chunks = ContextChunksClient(client_wrapper=self._client_wrapper)
        self.ingestion = IngestionClient(client_wrapper=self._client_wrapper)
        self.embeddings = EmbeddingsClient(client_wrapper=self._client_wrapper)
        self.health = HealthClient(client_wrapper=self._client_wrapper)


class AsyncPrivateGPTApi:
    def __init__(
        self,
        *,
        base_url: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url, httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client
        )
        self.contextual_completions = AsyncContextualCompletionsClient(client_wrapper=self._client_wrapper)
        self.context_chunks = AsyncContextChunksClient(client_wrapper=self._client_wrapper)
        self.ingestion = AsyncIngestionClient(client_wrapper=self._client_wrapper)
        self.embeddings = AsyncEmbeddingsClient(client_wrapper=self._client_wrapper)
        self.health = AsyncHealthClient(client_wrapper=self._client_wrapper)
