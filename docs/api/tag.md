# Tag情報関連

## 登録済みタグリスト取得 [GET /api/tag]
* 登録済みタグ情報のリストを返す。

+ Request (application/json)

    + Headers

            Accept: application/json

+ Response 200 (application/json)

    + Attribute (array[Tag])


## 新規タグ登録 [POST /api/page]
* 新規タグを1件登録する。

+ Request (application/json)

    + Headers

            Accept: application/json

    + Attribute (Tagi)

+ Response 201 (application/json)

    + Attribute (Tag)

## Data Structure

### Tag

+ _id: 5ac1971c5294ca0025ad0f35 (string) -タグID 
+ name: コンテナ (string) - タグ名
+ description: OS上に複数の隔離領域を作成することで実現する仮想化技術 (string) - タグの説明
