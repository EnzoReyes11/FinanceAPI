from fastapi import FastAPI

from .auth import routes as auth_router
from .users import routes as users_router

app = FastAPI()

app.include_router(users_router.router, responses={418: {"description": "I'm a teapot"}},)
app.include_router(auth_router.router, responses={418: {"description": "I'm a teapot"}},)


@app.get("/")
async def root():
    return {"message": "Hello Finance World!"}


def main():
    print('Main function')

if __name__ == "__main__":
    main()
