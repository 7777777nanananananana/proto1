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
あなたはユニクロの服の専門家です。ユーザーの要望に合う具体的なユニクロのトップスとボトムスを必ず1つずつ提案してください。
それぞれ「トップス: 商品名: ... URL: ...」「ボトムス: 商品名: ... URL: ...」の形式で返してください。
説明文や余計な文言は不要です。必ずこの形式のみで返してください。

出力例:
トップス: 商品名: エアリズムコットンTシャツ URL: https://www.uniqlo.com/jp/ja/products/E123456-000
ボトムス: 商品名: ウルトラストレッチアクティブジョガーパンツ URL: https://www.uniqlo.com/jp/ja/products/E654321-000
"""

try:
    response = model.generate_content(prompt)
    data = response.text.strip()
    print(data)  # ★ app.py に返すために標準出力へ出力
except Exception as e:
    print(f"エラー: {str(e)}")
