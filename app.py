from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    image_url = ""
    tops = ""
    tops_url = ""
    bottoms = ""
    bottoms_url = ""
    if request.method == 'POST':
        user_input = request.form.get('userPrompt', '')
        try:
            output = subprocess.check_output(['python', 'medicine.py', user_input], text=True)
            result = output.strip()
            for line in result.splitlines():
                if line.startswith("トップス:"):
                    parts = line.replace("トップス:", "").strip().split("URL:")
                    tops = parts[0].replace("商品名:", "").strip()
                    tops_url = parts[1].strip() if len(parts) > 1 else ""
                if line.startswith("ボトムス:"):
                    parts = line.replace("ボトムス:", "").strip().split("URL:")
                    bottoms = parts[0].replace("商品名:", "").strip()
                    bottoms_url = parts[1].strip() if len(parts) > 1 else ""
        except Exception as e:
            result = f"エラー: {str(e)}"
    return render_template('index.html', result=result, image_url=image_url,
                           tops=tops, tops_url=tops_url, bottoms=bottoms, bottoms_url=bottoms_url)

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
