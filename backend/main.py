import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles
from database import engine, Base
from routers import recipes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="QClaw 菜谱管理系统", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}


# 静态文件服务（生产模式）
DIST_PATH = os.path.join(os.path.dirname(__file__), "frontend_dist")
if os.path.isdir(DIST_PATH):
    app.mount("/assets", StaticFiles(directory=os.path.join(DIST_PATH, "assets")), name="assets")
    app.mount("/", StaticFiles(directory=DIST_PATH, html=True), name="spa")


@app.get("/")
async def root():
    if os.path.isdir(DIST_PATH):
        return FileResponse(os.path.join(DIST_PATH, "index.html"))
    return {"message": "QClaw 菜谱管理系统 API v2.0", "docs": "/docs"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
