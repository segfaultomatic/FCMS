# TFRM Systems API helper code.
from urllib.parse import urljoin
import requests


def query_sapi(endpoint, filter, query, includes):
    """
    Queries the SAPI.
    :param includes: Which related data entries to request
    :param endpoint: What endpoint (Within JSONAPI scope) to hit
    :param filter: What filter to apply
    :param query: The query string
    :return: SAPI's JSON response.
    """
    url = 'https://systems.api.fuelrats.com/api/'
    if endpoint not in ['systems', 'populated_systems']:
        return None
    r = requests.get(urljoin(url, f"{endpoint}?filter[{filter}]={query}&include={includes}"))
    r.raise_for_status()
    return r.json()


def get_system_by_name(system):
    return query_sapi('systems','name:eq', system, '')


def get_coords(system):
    sys = get_system_by_name(system)
    if sys['data']:
        return sys['data'][0]['attributes']['coords']