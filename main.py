# main.py
import utils

def main():
  """メインの処理を実行する"""
  a = 10
  b = 5

  # 足し算を実行
  sum_result = utils.add_numbers(a, b)
  print(f"{a} + {b} = {sum_result}")

  # 引き算を実行
  diff_result = utils.subtract_numbers(a, b)
  print(f"{a} - {b} = {diff_result}")

  # マジックナンバーを使っている例
  # 本来は定数として定義すべき
  if a > 9:
    print("aは9より大きいです。")


if __name__ == "__main__":
  main()

```**レビューさせたいポイント:**
*   `if a > 9:` の `9` のような、意味が分かりづらい直接的な値（マジックナンバー）が使われています。

---

### 次のステップ

1.  あなたのPC上で、新しいリポジトリを`git clone`します。
2.  上記の3つのファイル（`README.md`, `utils.py`, `main.py`）をリポジトリのフォルダ内に作成し、内容をコピー＆ペーストします。
3.  以下のコマンドでファイルをコミットし、GitHubにプッシュします。
    ```bash
    git add .
    git commit -m "最初のダミーコードを追加"
    git push
    ```
4.  この状態で、Greptileにリポジトリを登録（Submit）し、その後、以下のような質問（Query）を投げてレビューを依頼してみてください。

**Greptileへの質問（Query）のプロンプト例:**
*   `"このリポジトリのコードをレビューして、改善点を提案してください。"`
*   `"utils.pyの品質について評価してください。"`
*   `"マジックナンバーが使われている箇所はありますか？"`
