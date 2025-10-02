# analysis_module.py

# 問題点1: 悪い変数名とマジックナンバー
def check_status(data_points):
    # 's'という変数名が何を意味するかわかりにくい
    # '100'という値（マジックナンバー）が何なのか説明がない
    s = 0
    for d in data_points:
        s = s + d
    
    if s > 100:
        return "OK"
    else:
        return "NG"

# 問題点2: 非効率なループと冗長なコード
def find_item(target_item, item_list):
    found = False
    for i in range(len(item_list)):
        if item_list[i] == target_item:
            found = True
    return found

# 問題点3: 致命的なバグ（ゼロ除算エラーの可能性）
def calculate_average(scores):
    # scoresが空のリストの場合、len(scores)が0になり、ZeroDivisionErrorが発生する
    total = sum(scores)
    average = total / len(scores) 
    return average

# 問題点4: コメントアウトされた古いコードが残っている
def get_user_info(user_id):
    # print("Fetching user with ID:", user_id)
    # db.connect()
    # user = db.fetch(user_id)
    # return user
    
    # 新しい仮の実装
    if user_id == 1:
        return { "name": "Taro", "status": "active" }
    else:
        return None
