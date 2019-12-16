# 目的
Pythonコンテストにて「完成」した作品を出品する。

# 期間
2019/11/20-2020/2/21

# メンバー
publicの為個人名は割愛
- リーダー:goepy
- サブリーダー:sirayogi
- メンバー:

# 作るもの
## テーマ
- リマインダー
→ eTeamsからとってこれるか？（ストレッチ）→ 認証を突破できなさそうなので無理ぽ

### 選ばなかったテーマ（忘備）
- 昼飯Bot
→ オリジナリティがない…

- Linuxの問題を投げるBot
→ 問題作成その他諸々が大変

## 技術的な方針
- 片方向(AWS CloudWatch → Tocaro)
- DB有り(django Flamework)
- AWS lambda

## 必要な機能
### django Flamework
- 管理機能
    - リマインド登録機能
    - リマインド削除機能
    - リマインド照会機能
    - USER登録機能
    - USER削除機能
- DB
- CloudWatch管理機能（CloudWatchEventsHandler）（BOTO3）

### Python
- リマインド投稿機能
    - 投稿内容作成機能
    - Tocaro投稿機能（JinKanaiのフレームワーク(<https://github.com/V012TEX/aws-ops-automata/tree/feature/init/billingNotify/functions>)を使いたい）
    - CloudWatch管理機能（CloudWatchEventsHandler）（BOTO3）

# 作成方針
## 開発環境
- AWS Cloud9(基本開発環境), PyCharm等(自宅PC等からアクセスする場合)
- AWS Lambda
- AWS CloudWatchEvents
- Github
- Github Issue(コードレビュー)
- Github Project(進捗管理)
- Tocaro

## 制約事項
- AWSへは(eGate含め)社外からのアクセス禁止
- 残業を利用しての開発は禁止（スクーリングを活用）
- スクーリング及び研修以外でのAWSアクセスは事前申請要
