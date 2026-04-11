# QClaw 菜谱管理系统

一个简洁美观的菜谱管理后端 API + 网页管理系统。

## 技术栈

- **后端**: Python 3.11 / FastAPI / SQLAlchemy / SQLite
- **前端**: Vue 3 / Vite / Axios
- **部署**: Docker

## 快速开始

### 方式一：本地运行

**后端：**
```bash
cd backend
pip install -r requirements.txt
python init_db.py          # 初始化数据库和示例数据
uvicorn main:app --reload --port 8000
```

**前端（另开一个终端）：**
```bash
cd frontend
npm install
npm run dev
```

打开浏览器访问 http://localhost:5173

### 方式二：Docker 运行

```bash
docker build -t qclaw-recipes .
docker run -d -p 8000:8000 -p 5173:80 qclaw-recipes
```

- 前端：http://localhost:5173
- 后端 API：http://localhost:8000
- API 文档：http://localhost:8000/docs

## 功能特性

- ✅ 菜谱列表浏览（支持分类、搜索、分页）
- ✅ 菜谱详情查看
- ✅ 新增菜谱
- ✅ 编辑菜谱
- ✅ 删除菜谱
- ✅ 初始预置 5 道经典菜谱

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/recipes | 获取菜谱列表 |
| GET | /api/recipes/{id} | 获取菜谱详情 |
| POST | /api/recipes | 新增菜谱 |
| PUT | /api/recipes/{id} | 更新菜谱 |
| DELETE | /api/recipes/{id} | 删除菜谱 |

## 项目结构

```
qclaw-recipe-system/
├── backend/
│   ├── main.py          # FastAPI 入口
│   ├── database.py       # SQLite 配置
│   ├── models.py         # ORM 模型
│   ├── schemas.py        # Pydantic 模型
│   ├── crud.py           # 数据库操作
│   ├── routers/recipes.py
│   ├── init_db.py        # 初始化脚本
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── api/recipes.js
│   │   └── components/
│   └── package.json
└── Dockerfile
```

## License

MIT
"# QClaw-Recipe-System" 
