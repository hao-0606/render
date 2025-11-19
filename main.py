from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "Status": "Vercel is working!"}

# 這一行是 Vercel 的關鍵，一定要有
handler = Mangum(app)
