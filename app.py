from flask import Flask, jsonify
import string
import random

app = Flask(__name__)

SAVE_FILE = "codesf25.csv"

def generate_code(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(12))

def save_code(code):
    try:
        with open(SAVE_FILE, "a") as f:
            f.write(code + "\n")
        return True
    except:
        return False

@app.route("/api/newcode", methods=["GET"])
def new_code():
    code = generate_code()
    saved = save_code(code)

    return jsonify({
        "code": code,
        "saved": saved
    })

if __name__ == "__main__":
    app.run()
