import boto3
from datetime import datetime
from datetime import timedelta
import json

class CloudWatchEventsAccessor:
    """
    CloudWatchへのアクセスを簡易化するクラス
    """
    def __init__(self):
        self.client = boto3.client("events", region_name="ap-northeast-1")
        self.lambda_client = boto3.client("lambda", region_name="ap-northeast-1")
    
    def set_event(self, date_: datetime=datetime.now()+timedelta(minutes=5), id_: int=0):
        """
        CloudWatchEventsにTocaro投稿イベントを追加する。
        
        Parameters
        ----------
        date_ : datetime
            投稿する日付
        id_ : int
            データベースと紐付されるid
        
        Returns
        -------
        rem_name : str
            作成されたイベント名
        """
        rem_name = "fy19pu-reminder-" + date_.strftime("%Y%m%d%H%M")
        self.put_rule(
            Name=rem_name, 
            ScheduleExpression="cron({0:%M %H %d %m ? %Y})".format(date_), 
            State='ENABLED',
            Description='TocaroRemider')
        
        self.put_targets(
            Rule=rem_name,
            Targets=[
                {
                    'Id': 'fy19pu-tocaropost',
                    'Arn': 'arn:aws:lambda:ap-northeast-1:714257649477:function:fy19pu-tocaropost',
                    'Input': json.dumps({"id": id_, "name": rem_name})
                },
            ]
        )
        
        self.lambda_add_permission(
            FunctionName='fy19pu-tocaropost',
            StatementId='fy19pu-lamperm-test' + date_.strftime("%Y%m%d%H%M"),
            Action='lambda:InvokeFunction',
            Principal='events.amazonaws.com',
            SourceArn='arn:aws:events:ap-northeast-1:714257649477:rule/'+rem_name
        )
        
        return rem_name
        
    
    def delete_event(self, name: str):
        """
        CloudWatchEventsからTocaro投稿イベントを削除する。
        
        Parameters
        ----------
        name : str
            削除するイベント名
        """
        self.remove_targets(Rule=name, Ids=["fy19pu-tocaropost",])
        self.delete_rule(Name=name)
        # lambda_permissionの削除処理を未作成。デモでは実装しない。
        return 0
        
    
    def list_rules(self, **kwargs):
        """
        CloudWatchEventsのルールを表示する
        """
        response = self.client.list_rules(**kwargs)
        return response

    def put_rule(self, **kwargs):
        """
        CloudWatchEventsにルールを追加する
        """
        response = self.client.put_rule(**kwargs)
        return response

    def put_targets(self, **kwargs):
        """
        CloudWatchEventsのルールにターゲットを追加する
        """
        response = self.client.put_targets(**kwargs)
        return response
        
    def lambda_add_permission(self, **kwargs):
        """
        Lambdaにパーミッションを追加する
        """
        response = self.lambda_client.add_permission(**kwargs)
        return response
    
    def remove_targets(self, **kwargs):
        """
        CloudWatchEventsからターゲットを削除する
        """
        response = self.client.remove_targets(**kwargs)
        return response
    
    def delete_rule(self, **kwargs):
        """
        CloudWatchEventsからルールを削除する
        """
        response = self.client.delete_rule(**kwargs)
        return response
    

if __name__ == '__main__':
    b = CloudWatchEventsAccessor()
    
#   イベント作成テスト
#    print(b.set_event(id_=3))

#   イベント削除テスト
#    print(b.delete_event("fy19pu-reminder-202001170804"))
    
#    print(b.list_rules(NamePrefix="fy19pu"))
