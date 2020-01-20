import json
from tocaro_handler import TocaroHandler
from cloudwatchevents_accessor import CloudWatchEventsAccessor
import urllib.request

def lambda_handler(event, context):
    url = '' + event["id"] + '/'
    
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
    except urllib.error.HTTPError as err:
        print(err.code)
    except urllib.error.URLError as err:
        print(err.reason)
    
    # tocaro投稿処理
    tocaro = TocaroHandler()
    
    tocaro.set_text("※※※リマインドです※※※")
    tocaro.set_color("success")
    tocaro.set_attachments(
        [{
            "title": "日時",
            "value": body["date"]
        },
        {
            "title": "内容",
            "value": body["text"]
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
