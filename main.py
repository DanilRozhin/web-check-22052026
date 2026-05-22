from fastapi import FastAPI
import httpx

app = FastAPI()

LOGIN = "danilrozhin"

@app.get("/login")
def get_login():
    return LOGIN

@app.get("/id/{N})
async def get_user_login(N: int):
    url = f"https://nd.kodaktor.ru/users/{N}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers={"Content-Type": None})
    data = response.json()
    login = data.get("login")
    return login
