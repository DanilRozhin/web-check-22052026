from fastapi import FastAPI
import httpx

app = FastAPI()

LOGIN = "danilrozhin"


@app.get("/login")
def get_login():
    return LOGIN


@app.get("/id/{N}")
async def get_user_login(N: str):
    url = f"https://nd.kodaktor.ru/users/{N}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json()

    if isinstance(data, list) and data:
        data = data[0]

    login = data.get("login") if isinstance(data, dict) else None
    return login
