
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

class LoginForm(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginForm):
    print(data)
    return {"ok": True, "code": 200}

# curl -X POST "http://localhost:9000/login" \
#   -H "Content-Type: application/json" \
#   -d '{"username":"tom","password":"123456"}'