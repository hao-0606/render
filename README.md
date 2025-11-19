<div align=center>

# Vercel 設定

</div>

## ▶️ 第一部分：GitHub 倉庫裡要放什麼檔案

### 檔案結構（回歸簡單！）

你的 GitHub 倉庫只需要這樣就好：

```text
/ (根目錄)
  ├── main.py              (你的 FastAPI 程式)
  └── requirements.txt     (套件清單)
```

**就這兩個檔案！** 不用 `vercel.json`，不用 `api/` 資料夾，不用 `mangum`。

---

### 1. main.py

### 2. `requirements.txt` (套件清單)

```txt
fastapi
uvicorn
requests
tiktoken
pydantic
```
---

## ▶️ 第二部分：在 Render 網站上的設定

現在你的 GitHub 倉庫已經準備好了，我們來設定 Render。

### 步驟 1：註冊與連接 GitHub

1. 去 [Render.com](https://render.com)
2. 點右上角「Get Started」或「Sign Up」
3. **選擇「Sign up with GitHub」**（這樣最方便）
4. 授權 Render 存取你的 GitHub

### 步驟 2：建立新服務

1. 登入後，點擊右上角的 **「New +」** 按鈕
2. 選擇 **「Web Service」**
3. 你會看到你的 GitHub 倉庫列表，找到你的 Grok API 專案
4. 點擊該專案右邊的 **「Connect」**

### 步驟 3：填寫設定（重點！）

現在會出現一個設定頁面，請照著下面填：

| 欄位名稱 | 要填什麼 | 說明 |
|---------|---------|------|
| **Name** | `grok-api` (或任何你喜歡的名字) | 這會變成你的網址一部分 |
| **Region** | Singapore (或 Oregon) | 選離你近的，台灣選新加坡 |
| **Branch** | `main` (或 `master`) | 你的 GitHub 分支名稱 |
| **Root Directory** | (留空) | 如果你的檔案在根目錄就留空 |
| **Runtime** | **Python 3** | 一定要選這個！ |
| **Build Command** | `pip install -r requirements.txt` | 自動安裝套件 |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` | 啟動你的 FastAPI |

**特別注意 Start Command：**
- 如果你的檔案叫 `main.py`，就寫 `uvicorn main:app --host 0.0.0.0 --port $PORT`
- 如果你改成 `index.py`，就改成 `uvicorn index:app --host 0.0.0.0 --port $PORT`

### 步驟 4：選擇方案

往下滑會看到 **「Instance Type」**：

- 選擇 **「Free」**（每月 $0，但會休眠）

### 步驟 5：環境變數（選填）

如果你的 `GROK_COOKIE` 不想寫死在程式碼裡，可以在這裡加：

點擊 **「Advanced」** → **「Add Environment Variable」**

- **Key**: `GROK_COOKIE`
- **Value**: (貼上你的 Cookie)

這樣你程式碼裡的 `os.getenv("GROK_COOKIE")` 就能讀到了。

### 步驟 6：部署

點擊最下面的 **「Create Web Service」** 按鈕。

---

## ▶️ 第三部分：等待部署完成

1. Render 會開始自動：
   - 從 GitHub 拉取你的程式碼
   - 執行 `pip install -r requirements.txt`
   - 執行 `uvicorn main:app ...`

2. 你會看到一個即時的「建置日誌」，大概長這樣：
   ```
   ==> Cloning from https://github.com/你的帳號/你的專案...
   ==> Running 'pip install -r requirements.txt'
   ==> Installing fastapi...
   ==> Starting service with 'uvicorn main:app...'
   ==> Your service is live 🎉
   ```

3. **大約 2-3 分鐘後**，上面的狀態會從 `Building` 變成 `Live`（綠色）

4. 你會看到一個網址，類似：
   ```
   https://grok-api-xxxx.onrender.com
   ```

5. **測試：** 打開那個網址，你應該會看到你的 FastAPI 首頁（`/` 路由的回應）

---

## 常見問題

**Q: 部署失敗，顯示找不到 requirements.txt？**
A: 確認 `requirements.txt` 有推送到 GitHub，而且在根目錄。

**Q: 顯示 `tiktoken` 安裝失敗？**
A: 把 `requirements.txt` 裡的 `tiktoken` 那行刪掉，並修改程式碼用我之前給的 try-except 方式處理。

**Q: 服務顯示 Live 了，但打開網址顯示 502？**
A: 檢查 Start Command 是不是 `uvicorn main:app --host 0.0.0.0 --port $PORT`（**注意 `$PORT` 是大寫，且不要改成固定數字**）

**Q: 免費版會休眠是什麼意思？**
A: 如果 15 分鐘沒人用，Render 會把你的服務關掉省資源。下次有人訪問時會自動喚醒（需要等 10-30 秒）。如果要永不休眠，要升級付費版（每月 $7）。

---

準備好了嗎？把檔案整理好推送到 GitHub，然後去 Render 按照上面的設定，5 分鐘後你就有一個能正常運作的 Grok API 了！有問題隨時問我。
