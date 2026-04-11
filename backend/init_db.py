"""初始化数据库并插入示例数据"""
import json
from database import engine, Base, SessionLocal
from models import Recipe

# 创建表
Base.metadata.create_all(bind=engine)

SEED_RECIPES = [
    {
        "title": "番茄炒蛋",
        "category": "家常菜",
        "ingredients": json.dumps(["番茄 2个", "鸡蛋 3个", "盐 适量", "食用油 2勺", "葱花 少许"]),
        "steps": json.dumps([
            "番茄洗净切块备用",
            "鸡蛋打入碗中加少许盐搅散",
            "热锅冷油，倒入蛋液快速翻炒至凝固，盛出备用",
            "锅中再加少许油，下番茄块翻炒出汁",
            "加入炒好的鸡蛋，调入盐翻炒均匀",
            "撒上葱花即可出锅"
        ]),
        "cook_time": 15,
        "difficulty": "简单",
    },
    {
        "title": "红烧肉",
        "category": "川菜",
        "ingredients": json.dumps(["五花肉 500g", "冰糖 30g", "老抽 2勺", "生抽 1勺", "料酒 2勺", "八角 2个", "桂皮 1小块", "姜片 5片"]),
        "steps": json.dumps([
            "五花肉切成3cm见方的块，冷水下锅焯水去血沫，捞出沥干",
            "锅中放少许油，下冰糖小火炒至焦糖色",
            "下入肉块快速翻炒上色",
            "加入料酒、老抽、生抽翻炒均匀",
            "加入足量开水没过肉块，放入八角、桂皮、姜片",
            "大火烧开后转小火焖煮1小时",
            "大火收汁，汤汁浓稠即可出锅"
        ]),
        "cook_time": 90,
        "difficulty": "中等",
    },
    {
        "title": "蒜蓉西兰花",
        "category": "家常菜",
        "ingredients": json.dumps(["西兰花 1颗", "蒜末 3瓣", "盐 适量", "食用油 1勺", "蚝油 1勺"]),
        "steps": json.dumps([
            "西兰花掰成小朵，用盐水浸泡10分钟后洗净",
            "烧一锅开水，加少许盐和油，下西兰花焯水1分钟捞出",
            "热锅下油，爆香蒜末",
            "下西兰花快速翻炒",
            "加入蚝油和盐调味，翻炒均匀即可出锅"
        ]),
        "cook_time": 10,
        "difficulty": "简单",
    },
    {
        "title": "宫保鸡丁",
        "category": "川菜",
        "ingredients": json.dumps(["鸡胸肉 300g", "花生米 50g", "干辣椒 10个", "花椒 1小把", "葱段 适量", "姜末 适量", "蒜末 适量", "生抽 2勺", "醋 1勺", "糖 1勺", "淀粉 适量"]),
        "steps": json.dumps([
            "鸡胸肉切丁，用盐、料酒、淀粉腌制15分钟",
            "调碗汁：生抽、醋、糖、淀粉、少许水混合均匀",
            "花生米炸至金黄酥脆备用",
            "热锅下油，下花椒和干辣椒段炒出香味",
            "下鸡丁大火翻炒至变色",
            "加入姜末、蒜末、葱段爆香",
            "倒入碗汁快速翻炒均匀",
            "出锅前撒入花生米翻匀即可"
        ]),
        "cook_time": 30,
        "difficulty": "中等",
    },
    {
        "title": "清蒸鲈鱼",
        "category": "粤菜",
        "ingredients": json.dumps(["鲈鱼 1条（约500g）", "葱丝 适量", "姜丝 适量", "蒸鱼豉油 3勺", "料酒 1勺", "热油 2勺"]),
        "steps": json.dumps([
            "鲈鱼处理干净，两面划几刀，抹上料酒和盐腌制10分钟",
            "鱼身铺上葱段和姜片",
            "水开后放入蒸锅，大火蒸8-10分钟",
            "取出倒掉蒸出的水，捡去葱姜",
            "铺上新的葱丝和姜丝",
            "淋上蒸鱼豉油",
            "泼上热油激发香味即可上桌"
        ]),
        "cook_time": 25,
        "difficulty": "简单",
    },
]

def seed():
    db = SessionLocal()
    try:
        # 如果已有数据则跳过
        count = db.query(Recipe).count()
        if count > 0:
            print(f"数据库已有 {count} 条菜谱，跳过初始化。")
            return

        for r in SEED_RECIPES:
            db.add(Recipe(**r))
        db.commit()
        print(f"成功插入 {len(SEED_RECIPES)} 条示例菜谱！")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
