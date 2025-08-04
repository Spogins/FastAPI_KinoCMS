from fastapi import FastAPI
from config.routers import router as app_router

app = FastAPI(title="FastAPI_KinoCMS")

app.include_router(app_router)

if __name__ == "__main__":
    for route in app.routes:
        methods = ",".join(route.methods)
        print(f"{methods:10} {route.path}")