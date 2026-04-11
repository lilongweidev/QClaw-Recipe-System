from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    category = Column(String(50), nullable=False)  # 川菜/粤菜/鲁菜/家常菜等
    ingredients = Column(Text, nullable=False)     # JSON 字符串，存储配料列表
    steps = Column(Text, nullable=False)           # JSON 字符串，存储步骤列表
    cook_time = Column(Integer, nullable=False)    # 分钟
    difficulty = Column(String(20), nullable=False)  # 简单/中等/困难
    created_at = Column(DateTime(timezone=True), server_default=func.now())
