from .table_service import table_service

slack_services = {
    "TABLES_SERVICE": table_service
}


def get_slack_service(service, *args):
    return slack_services.get(service)(*args)
