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
{user_input}
あなたはユニクロの服の専門家です。ユーザーの要望に合う具体的なユニクロ商品名と、その公式商品ページのURLを必ず1つ提案してください。
出力例: 商品名: エアリズムコットンTシャツ　URL: https://www.uniqlo.com/jp/ja/products/E452123-000/00
説明文や余計な文言は不要です。必ず「商品名: ... URL: ...」の形式で返してください。
"""

try:
    response = model.generate_content(prompt)
    data = response.text.strip()
    print(data)  # ★ app.py に返すために標準出力へ出力
except Exception as e:
    print(f"エラー: {str(e)}")
