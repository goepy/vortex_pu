CloudWatchEvents及びLambdaへのアクセス権限追加方法です。

1. AWSにてIAMを開く
1. 左ペインのユーザーを選択
1. 自分のIDを選択
1. アクセス権限の追加を選択
1. 既存のポリシーを直接アタッチにて、「AWSLambdaFullAccess」及び「CloudWatchEventsFullAccess」にチェックし、右下「次のステップ：確認」を選択
1. 確認の上、右下「アクセス権限の追加」を選択
1. アクセス権限タブにて、「AWSLambdaFullAccess」及び「CloudWatchEventsFullAccess」が追加されていることを確認
研修用の環境の為権限がアレなのでできました。怒られたら戻します。