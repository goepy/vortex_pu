import json
from tocaro_handler import TocaroHandler
from cloudwatchevents_accessor import CloudWatchEventsAccessor


def lambda_handler(event, context):
    
    # tocaro投稿処理
    tocaro = TocaroHandler()
    
    tocaro.set_text("test ID=" + str(event["id"]))
    tocaro.set_color("success")
    tocaro.set_attachments(
        [{
            "title:": "test title",
            "value": "test value"
        }
        ]
    )
    
    r = tocaro.send2tocaro()
    
    
    # CloudWatchEvents削除処理
    b = CloudWatchEventsAccessor()
    b.delete_event(event["name"])
    
    return r


if __name__ == '__main__':
    print(lambda_handler({"id": 1, "name": "test"}, None))
