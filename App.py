from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ✅ Hardcoded Gemini API Key (you've shared this one)
genai.configure(api_key="AIzaSyDOt_7AU97sm-i5o6g0cNgCBfziHwQE7Rg")

@app.route("/")
def home():
    return render_template("Index.html")

@app.route("/ai", methods=["POST"])
def ai_response():
    try:
        user_input = request.json.get("prompt")
        if not user_input:
            return jsonify({"message": "❌ Empty input received"}), 400

        # ✅ Using latest Gemini model
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Generate content from user input
        response = model.generate_content(user_input)
        return jsonify({"message": response.text})
    except Exception as e:
        return jsonify({"message": f"❌ Error: {str(e)}"}), 500
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
