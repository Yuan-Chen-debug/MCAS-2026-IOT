from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

images = [
    "images/pic1.jpg",
    "images/pic2.jpg",
    "images/pic3.jpg"
]

current_index = 0  # 全域索引 (0 代表第 1 張, 1 代表第 2 張, 2 代表第 3 張)

@app.route("/")
def index():
    global current_index
    img = images[current_index]
    # 保持傳送 current_index，前端 index.html 會自動做 +1 顯示
    return render_template("index.html", image=img, idx=current_index, total=len(images))

@app.route("/next")
def next_img():
    global current_index
    current_index += 1
    # 索引達到 3 (超過第 3 張) 時，循環回到第 1 張 (索引 0)
    if current_index >= len(images):
        current_index = 0
    return redirect(url_for("index"))

@app.route("/prev")
def prev_img():
    global current_index
    current_index -= 1
    # 索引低於 0 時，循環跳到最後一張 (索引 2)
    if current_index < 0:
        current_index = len(images) - 1
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)