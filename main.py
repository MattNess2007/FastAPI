from fastapi import FastAPI, Body
import random
import psutil
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/api/status")
def read_root():
    html_content = "<h2>Все гуд,все работает!</h2>"
    return HTMLResponse(content=html_content)

@app.get("/api/pc")
def read_root():
    cpu= psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return (f"Загрузка CPU: {cpu}%"),(f"RAM: {ram.percent}% (Всего: {ram.total / (1024**3):.2f} GB)"),(f"Диск: {disk.percent}% (Свободно: {disk.free / (1024**3):.2f} GB)")

@app.get("/api/random-number")
def read_root():
    num = random.randint(1, 1000)
    return num

@app.get("/api/sayhello")
def hello(name:str = Body(embed=True)):
    return {"message": f"Привет, {name}"}