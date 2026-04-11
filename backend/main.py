import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from database import engine, Base
from routers import recipes

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="QClaw 菜谱管理系统", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册 API 路由（API 路由优先）
app.include_router(recipes.router)

# 生产模式配置
DIST_PATH = os.path.join(os.path.dirname(__file__), "frontend_dist")
PRODUCTION_MODE = os.path.isdir(DIST_PATH)


@app.get("/api/health")
def health():
    return {"status": "ok"}


if PRODUCTION_MODE:
    # 一次性挂载 dist 目录（Starlette 会处理 / 和 /assets/ 等）
    from starlette.staticfiles import StaticFiles
    app.mount("/", StaticFiles(directory=DIST_PATH, html=True), name="dist")

    @app.get("/")
    async def root():
        return FileResponse(os.path.join(DIST_PATH, "index.html"))
else:
    @app.get("/")
    def root():
        return {"message": "QClaw 菜谱管理系统 API", "docs": "/docs"}
