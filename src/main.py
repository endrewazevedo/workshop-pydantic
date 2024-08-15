from fastapi import FastAPI
from schemas import AllUsersResponse, User, UserResponse
from settings import Settings
import uvicorn


app = FastAPI()

db = []
settings = Settings()

@app.get("/hello", description="Rota para dizer olá ao usuário")
def hello_user():
    username: str = settings.USER
    return {"message": f"Olá, {username}"}

@app.post("/users/", description="Cria um novo usuário", response_model=UserResponse)
def create_user(user: User):
    db.append(user)

    return UserResponse(**user.model_dump())


@app.get("/users/", description="Rota para obter todos os usuários", response_model=AllUsersResponse)
def get_all_users():

    total = len(db)
    return AllUsersResponse(total=total, users=db)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)