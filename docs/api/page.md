# Page情報関連
 
 
## 登録済みページリスト取得 [GET /api/page]
* 登録済みページ情報のリストを返す。
 
+ Request (application/json)
 
    + Headers
 
            Accept: application/json
 
+ Response 200 (application/json)

    + Attribute (array[Page])


## 新規ページ登録 [POST /api/page]
* 新規ページを1件登録する。

+ Request (application/json)

    + Headers

            Accept: application/json

    + Attribute (Page)

+ Response 201 (application/json)

    + Attribute (Page)

## 最新登録ページリスト取得 [GET /api/page/new]
* 24時間以内の登録ページのリストを返す

+ Request (application/json)

    + Headers

            Accept: application/json

+ Response 200 (application/json)

    + Attribute (array[Page])


## 新着情報登録 [POST /api/page/new]
* 登録済みサイトの新着情報を取得し登録する。

+ Request (application/json)

    + Headers

            Accept: application/json

    + Attribute (Page)

+ Response 201 (application/json)

    + Attribute (array[Page])




## Data Structure

### Page

+ _id: 5ac1971c5294ca0025ad0f35 (string) - ページID 
+ title: テスト (string) - ページタイトル
+ type: media (string) - ページタイプ
+ page: http://test.com/page - ページURL
+ site: Webニュース - 掲載サイト名
+ keyword (array[stringt])
    + tset1
    + test2
    + test3
+ created_at: 2018-04-02T02:36:12.910000 (string) - 登録日時、datetime
