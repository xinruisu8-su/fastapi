# FastAPI

## 1.安装
打开终端，输入
```shell
$ pip install fastapi 
```

## 2.写app/main.py
```python
from fastapi import FastAPI

app = FastAPI() #创建了一个FastAPI类的对象，对象放入app变量中

@app.get("/")
def home():
    return {"message":"Hello FastAPI"}
```

## 3.运行
首先需要安装uvicorn，这是一个HTTP服务器server。
```shell
$ pip install uvicorn
```
注意为了顺利找到main，我们需要在app下打开终端输入命令
```shell
$ uvicorn main:app --host 0.0.0.0 --port 9000 --reload
```
用uvicorn启动当前写好的项目代码
- --host 0.0.0.0表示同一个网络中的电脑都可以访问这个服务器
- --port 9000这个服务器打开了9000端口（端口任意指定即可）
- --reload表示python代码修改后，这个服务器自动重新运行
## 4. 访问
确保在同一个局域网中，打开浏览器。输入运行这个项目的电脑的IP地址:9000即可 http://192.178.1.123:9000

## 5.
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # 创建了一个FastAPI类的对象，对象放入app变量中

@app.get("/")  # 只要项目运行起来，用户输入地址localhost:9000/，就会执行home函数
# curl -XGET "http://localhost:9000/"
def home():
    return {"message": "Hello FastAPI"}

class LoginForm(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginForm):
    print(data)
    return {"ok": True, "code": 200}
# 在终端敲：
# curl -X POST "http://localhost:9000/login" \
#   -H "Content-Type: application/json" \
#   -d '{"username":"tom","password":"123456"}'
```