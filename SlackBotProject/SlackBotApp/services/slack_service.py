from .slack_services import get_slack_service
import slack
import os


def slack_service(*args):
    slack_event_adapter, = args
    client = slack.WebClient(token=os.environ.get("TOKEN"))
    bot_id = client.api_call("auth.test")["user_id"]
    
    @slack_event_adapter.on("message")
    def message(payload):
        event = payload.get("event")

        text = event.get("text")
        current_channel = event.get("channel")
        current_user_id = event.get("user")
        
        if bot_id != current_user_id and text is not None:
            get_slack_service("TABLES_SERVICE", text, client, current_channel)
