from abc import ABC, abstractmethod
from typing import Tuple, final


class HttpProvider(ABC):
    @abstractmethod
    def add_endpoint(self, url, method, endpoint):
        raise NotImplementedError

    @abstractmethod
    def format_response(self, response: Tuple[int, dict]):
        """
        This method is to format a generic response to
        work correctly within the networks interface.

        The input to this function is generated by
        `_internal_handle`
        """
        raise NotImplementedError

    @final
    def _internal_handle(self, endpoint, request):
        """
        this is the internal handle method, its implementation
        does not change between different providers
        """
        response = endpoint.handle(endpoint.get_inputs(request))
        endpoint.send_callbacks(response)
        return response