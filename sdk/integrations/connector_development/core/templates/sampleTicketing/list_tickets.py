from connectors.core.connector import get_logger, ConnectorError
from .utils import invoke_rest_endpoint
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def list_tickets(config, params=None, *args, **kwargs):

    # next call the rest endpoint on the target server with the required inputs
    # sample code below. to be replaced for the integration
    endpoint = '/api/tickets/'
    api_response = invoke_rest_endpoint(config, endpoint, 'GET')

    # data transformation here to add/remove/modify some part of the api response
    # sample code below to add a custom key
    api_response.update({'my_custom_response_key': 'my_custom_value'})
    return api_response
