from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result_data=None)

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
