from flask import Flask
from slackeventsapi import SlackEventAdapter
from .services import get_service
import os


def create_app(configuration_file="settings.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(configuration_file)
    with app.app_context():
        from .blueprints import slack_blueprint
        app.register_blueprint(slack_blueprint)
        slack_event_adapter = SlackEventAdapter(
                            os.environ.get("SIGNING_SECRET"), 
                            os.environ.get("BOT_ENDPOINT"), 
                            app
                        )
        get_service("SLACK_SERVICE", slack_event_adapter)
        return app
