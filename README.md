# PingPongBallGame
使用: python語法 & pygame
遊戲內容: 以擋板控制球，使求不要超出窗外

**第一次用pygame寫遊戲**

## 想法
球撞到擋板會分裂成兩顆
### 程式碼
1. class建立球的屬性
2. 判斷collision是否為擋板
3. 將新增的球存入balls(list)中
4. 更新畫面時以for跑每個球物件

### 小問題
pygame載入音檔有兩種
一種是以音樂(music)，另一種是音效(sound)，兩者的檔案不同
因為我沒轉檔(mp3)所以用msice，所以碰撞音樂撥放時音效沒播完時不能同時發生
