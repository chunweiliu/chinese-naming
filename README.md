# 好筆畫命名參考
輸入當年生肖吉祥字，自動生成姓名學上好筆畫的名字組合

我不懂姓名學，僅試用網路上的命名軟體後，歸納出一些參照康熙字典上的好名字筆畫組合，配上當年生肖的吉祥字，即可生成不同好筆劃的吉祥名字。

經過測試，此算法和諮詢算命老師的結果十分相似，供各位參考品玩。

# 如何執行
1. 新增`good_characters_for_xxx.py` 文件，xxx 為生肖，名稱隨意，重要的是內容須包含一個型別為`dict` 的變數 `good_characters`
2. 修改`good_names.py` 的標頭檔，匯入該文件
```
from good_characters_for_xxx import good_characters
```
3. 修改`familiy_name`
4. 在終端機執行`python good_names.py`