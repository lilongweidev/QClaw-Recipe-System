"""初始化数据库并插入示例数据"""
import json
from database import engine, Base, SessionLocal
from models import Recipe

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
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80",
        "is_favorite": True,
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
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=800&q=80",
        "is_favorite": True,
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
        "image_url": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=800&q=80",
        "is_favorite": False,
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
        "image_url": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=800&q=80",
        "is_favorite": False,
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
        "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=800&q=80",
        "is_favorite": False,
    },
    {
        "title": "糖醋里脊",
        "category": "鲁菜",
        "ingredients": json.dumps(["猪里脊 300g", "淀粉 适量", "鸡蛋 1个", "番茄酱 3勺", "白醋 2勺", "糖 2勺", "盐 适量", "白芝麻 少许"]),
        "steps": json.dumps([
            "里脊肉切条，加盐、料酒、蛋清腌制15分钟",
            "裹上干淀粉备用",
            "调糖醋汁：番茄酱、白醋、糖、少许盐和清水调匀",
            "油温六成热，下肉条炸至金黄酥脆，捞出复炸一次",
            "锅中留底油，倒入糖醋汁烧开",
            "下炸好的肉条快速翻炒均匀",
            "撒上白芝麻即可出锅"
        ]),
        "cook_time": 40,
        "difficulty": "困难",
        "image_url": "https://images.unsplash.com/photo-1561043433-aaf687c4cf04?w=800&q=80",
        "is_favorite": False,
    },
    {
        "title": "奶油蘑菇汤",
        "category": "西餐",
        "ingredients": json.dumps(["口蘑 200g", "洋葱 半个", "黄油 30g", "奶油 100ml", "面粉 2勺", "鸡汤 300ml", "盐 适量", "黑胡椒 少许"]),
        "steps": json.dumps([
            "口蘑洗净切片，洋葱切丁备用",
            "小火热锅，下黄油融化",
            "下洋葱丁炒至透明",
            "加入面粉翻炒1分钟去生",
            "慢慢倒入鸡汤，边倒边搅拌防止结块",
            "加入蘑菇片，煮10分钟至软烂",
            "倒入奶油搅匀，小火再煮5分钟",
            "加盐和黑胡椒调味，出锅"
        ]),
        "cook_time": 30,
        "difficulty": "中等",
        "image_url": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=800&q=80",
        "is_favorite": False,
    },
    {
        "title": "杨枝甘露",
        "category": "甜品",
        "ingredients": json.dumps(["芒果 2个", "西米 50g", "椰浆 200ml", "淡奶油 100ml", "西柚果肉 适量", "糖 适量"]),
        "steps": json.dumps([
            "西米沸水下锅，煮至中间有小白点，焖5分钟至透明，过凉水备用",
            "芒果去皮切块，一半打泥，一半切丁",
            "椰浆和淡奶油混合，加少许糖调味",
            "西柚剥出果肉备用",
            "碗底铺西米，倒入芒果泥",
            "加入椰奶奶油液",
            "顶部放芒果丁和西柚果肉",
            "冷藏2小时后享用更佳"
        ]),
        "cook_time": 20,
        "difficulty": "简单",
        "image_url": "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=800&q=80",
        "is_favorite": True,
    },
]


def seed():
    db = SessionLocal()
    try:
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
