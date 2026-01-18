# -*- coding: utf-8 -*-
# 餐飲服務與餐廳類型 英翻中專項測驗程式（繁體版）
import random

# 中英對照字典
catering_dict = {
    "Buffet Service": "自助餐服務",
    "Cabin Catering Service": "機艙餐飲服務",
    "Cafeteria Service": "自助式餐廳服務",
    "Catering Service": "宴會餐飲承辦服務",
    "Counter Service": "櫃檯式服務",
    "Delivery Service": "外送服務",
    "Drive-in Service": "汽車餐廳服務",
    "Drive-through Service": "得來速服務",
    "In-flight Service": "機上餐飲服務",
    "Room Service": "客房送餐服務",
    "Table Service": "桌餐服務",
    "Take-out Service": "外帶服務",
    "Club Member Restaurants": "會員制俱樂部餐廳",
    "Combination Restaurants": "複合式餐廳",
    "Community Restaurants": "社區餐廳",
    "Independent Restaurants": "獨立餐廳",
    "À La Carte Restaurants": "單點式餐廳",
    "Filling Station": "加油站附設餐廳",
    "Restaurant Chains": "連鎖餐廳",
    "Specialty Restaurants": "特色餐廳",
    "Theme Restaurants": "主題餐廳",
    "Luxury Restaurants": "豪華餐廳"
}

def start_english_to_chinese_quiz():
    print("====== 餐飲英翻中專項測驗 ======\n")
    # 輸入題目數量
    total_questions = int(input("請輸入要測驗的題目數量："))
    # 隨機選取題目
    quiz_items = random.sample(list(catering_dict.items()), total_questions)
    
    score = 0
    for i, (eng, chi) in enumerate(quiz_items, 1):
        user_ans = input(f"第{i}題：{eng} → 請翻譯為中文：")
        # 判斷答案（忽略大小寫和前後空格）
        if user_ans.strip() == chi:
            print("✅ 答對了！\n")
            score += 1
        else:
            print(f"❌ 答錯了，正確答案是：{chi}\n")
    
    # 顯示成績
    print("====== 測驗結束 ======")
    print(f"總題數：{total_questions} | 答對：{score} | 得分率：{score/total_questions*100:.1f}%")

if __name__ == "__main__":
    start_english_to_chinese_quiz()