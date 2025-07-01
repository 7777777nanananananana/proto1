from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    image_url = ""
    if request.method == 'POST':
        user_input = request.form.get('userPrompt', '')
        try:
            output = subprocess.check_output(['python', 'medicine.py', user_input], text=True)
            result = output.strip()
            # URL抽出
            product_url = ""
            img_url = ""
            if "URL:" in result:
                parts = result.split("URL:")
                # 商品名: ...
                product_name = parts[0].replace("商品名:", "").strip()
                # URL: ... 画像: ...
                url_and_img = parts[1].strip().split("画像:")
                product_url = url_and_img[0].strip()
                if len(url_and_img) > 1:
                    img_url = url_and_img[1].strip()
                else:
                    img_url = ""
                image_url = img_url if img_url else product_url
        except Exception as e:
            result = f"エラー: {str(e)}"
    return render_template('index.html', result=result, image_url=image_url)

@app.route('/medicine', methods=['POST'])
def diagnosis():
    try:
        user_input = request.form.get('userPrompt', '')
        result = subprocess.run(['python', 'medicine.py', user_input], capture_output=True, text=True)
        output = result.stdout.strip()
        return output  # ← 結果をHTMLに渡す
    except Exception as e:
        return render_template('index.html', result_data=f"エラー: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
