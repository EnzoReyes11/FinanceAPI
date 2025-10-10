from contextlib import asynccontextmanager

from fastapi import FastAPI

from .auth import routes as auth_router
from .database import create_db_and_tables
from .users import routes as users_router


def startup_event():
    create_db_and_tables()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup: Initializing resources...")
    startup_event()
    yield

    print("Application shutdown: Cleaning up resources...")
#    if hasattr(app.state, "db_connection"):
#        # Close app.state.db_connection
#        pass

app = FastAPI(lifespan=lifespan)

app.include_router(users_router.router, responses={418: {"description": "I'm a teapot"}},)
app.include_router(auth_router.router, responses={418: {"description": "I'm a teapot"}},)


@app.get("/")
async def root():
    return {"message": "Hello Finance World!"}



def main():
    print('Main function')

if __name__ == "__main__":
    main()
