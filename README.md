# ORDERLY Python / Django Interview

Hi,

感謝您

這是根據您的回覆所訂製的問題，大約會花費 3- 5 小時的挑戰時間

若您決定要開始這項挑戰，請 fork 此專案，並將每個問題的答案放至對應的資料夾

完成後，請發個PR到此專案

### 挑戰一: OO觀念運用 (folder: x_1)

> 現在您的手上有 2 支手機，手機來自不同品牌，其規格屬性大同小異，但各自擁有一項特殊功能，請使用OO繼承及如下的規格，設計出這 3 支手機的class。

```
手機共通屬性: price, camera_count, screen_size
特殊功能: special_freature() 

手機一 google phone:
price=10, camera_count=3, screen_size=5
special_freature 輸入一個int list, 回傳偶數且大於10的元素，並由大至小進行排序
例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]

手機二 taiwan phone:
price=20, camera_count=1, screen_size=3
special_freature
輸入一個數字自動計算Fibonacci斐波那契數列的運算結果，並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
例如: ---

```


### 挑戰二: Django 客戶排序 (RFM) (folder: x_2)
> 請於 Django 中設計一個 view，並完成 4 個 RFM 函式，再透過 URL GET，以 return json 的型式完成函式回傳。 

```
RFM 指標說明:
用三個向度分析消費者的重要程度：
1. Recency 新進度: 最後一次消費距離現在的時距
2. Frequency 消費頻率: 此消費者消費次數的密集度
3. Monetary Value 消費額: 此消費者的總消費金額
三種向度各分成五級，而 RFM 總值即為三項度值加總。
```

> 現在您的手上有所有消費者的 RFM 值 ( /x_2/rfm.csv )，需要設計四個函式將消費者列表分別以三種向度以及 RFM 總值排序。已知的條件有: 
- 消費者列表: 所有消費者的 ID 及 RFM 值 ( `list<clients>` )
  - R ( `int` recency )
  - F ( `int` frequency )
  - M ( `int` monetary )
  - ID ( `int` ID)

> 需要設計的函式（亦可以寫在同一個函式，指標用 flag 判斷）: 
- 將 ID 以倒 R 值排序回傳 (大到小) ( `function` sort_by_recency( ) )
- 將 ID 以倒 F 值排序回傳 (大到小) ( `function` sort_by_frequency( ) )
- 將 ID 以 M 值排序回傳 (小到大) ( `function` sort_by_monetary( ) )
- 將 ID 以倒 RFM 總值排序回傳 (大到小) ( `function` sort_by_RFM( ) )


### 挑戰三: Project 開發分配 (folder: x_3)
> 現在有一個商用軟體產品，該產品剛上線滿一年，已有一定的客戶量體，但系統穩定度不足，且功能仍然簡陋，因此產品開始有許多的需求要被分配開發資源，假設現在是星期三早上10點鐘，請您針對以下狀況進行思考，並說明每一項的應對方式:
```
(A) 重量級客戶10天前提出的改進需求，需耗時6小時完成，此需求你評估認為非常實用。
(B) 昨天晚上系統發出的 alert, 警示訊息為客戶操作出錯
(C) 早上九點系統發出的 alert, 警示訊息為DB異常
(D) 剛剛你無意中注意到的前台破圖，大約20分鐘可搞定
(E) 近三天專注開發的一項功能，如果現在不接著工作，很可能會忘記重要事項
(F) 昨天寫程式時，無意中發現的程式bug，但不在自已掌管範圍內
.....
````


## 當您挑戰結束時，請在您的最後一次 commit 中輸入您對此份工作，在程式上的期待，謝謝您。

