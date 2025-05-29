from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import create_db_and_tables
from src.config import config
from src.routes.auth import router as auth_router
from src.routes.person import router as person_router


async def on_startup():
  create_db_and_tables()


title: str = "Api Police Interceptor"
app = FastAPI(title=title, version="1.0.0", on_startup=[on_startup])

# Routers
app.include_router(auth_router, prefix="/v1/auth", tags=["Auth"])
app.include_router(person_router, prefix="/v1/person", tags=["Person"])

# CORS Middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


# Main Route
@app.get("/health", tags=["Health Check"])
async def health():
  return {"success": True, "message": f"API {title} is running"}


if __name__ == "__main__":
  import uvicorn

  uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=config.APP_PORT,
    reload=config.ENVIROMENT == "development",
  )
