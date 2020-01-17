import json
from tocaro_handler import TocaroHandler

def lambda_handler(event, context):
    
    
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
    return r

if __name__ == '__main__':
    print(lambda_handler({"id": 1}, None))