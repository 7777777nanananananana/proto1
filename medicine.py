# medicine.py
import google.generativeai as genai
import os
import sys

# コマンドライン引数からプロンプトを取得
user_input = sys.argv[1] if len(sys.argv) > 1 else "診断情報が入力されていません"

# Gemini の API キー設定
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "AIzaSyCpLMlPvmI2Y760ZfLxzEndVMmok48gz2E"))

# モデル初期化
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# プロンプトにユーザー入力をそのまま利用
prompt = f"""
${user_input}
また、出力は系統、色、形状などを提示し、出力文章は全体で30文字以内に収めてください。
出力は提案部分のみで大丈夫です。
指示に従いますなどの文言は不要です。

"""

try:
    response = model.generate_content(prompt)
    data = response.text.strip()
    print(data)  # ★ app.py に返すために標準出力へ出力
except Exception as e:
    print(f"エラー: {str(e)}")
