from .index import index
from .slack_service import slack_service

services = {
    "INDEX": index,
    "SLACK_SERVICE": slack_service
}


def get_service(service, *args):
    return services.get(service)(*args)
