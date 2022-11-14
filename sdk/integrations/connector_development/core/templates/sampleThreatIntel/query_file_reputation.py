from connectors.core.connector import get_logger, ConnectorError
from .utils import invoke_rest_endpoint
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def query_file_reputation(config, params, *args, **kwargs):
    file_hash = params.get('file_hash')
    if not file_hash:
        raise ConnectorError('Missing required input')
    # input sanitization if needed
    # for example, if the target endpoint accepts only certain types as hashes, you could add the validation here

    # next call the rest endpoint on the target server with the required inputs
    # sample code below. to be replaced for the integration
    endpoint = '/get_file_reputation'
    request_body = {'file_hash': file_hash}

    api_response = invoke_rest_endpoint(config, endpoint, 'POST', request_body)
    # data transformation here to add/remove/modify some part of the api response
    # sample code below to add a custom key
    api_response.update({'my_custom_response_key': 'my_custom_value'})
    return api_response
