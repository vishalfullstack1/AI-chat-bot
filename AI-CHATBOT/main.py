# pip install openai

from urllib import response
from flask import Flask, redirect,render_template, request, session, url_for
from openai import OpenAI
import config 

client = OpenAI(api_key=config.open_ai) 
app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def home():
    session.setdefault("chat_history", [])
    return render_template("index.html",chat_history=session["chat_history"])


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["text"]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Shipra, a helpful and friendly AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response.choices[0].message.content
    print(f"User: {user_input}")
    print(f"Bot: {reply}")
    session["chat_history"].append({"user": user_input, "bot": reply})
    session.modified = True 
    print(session["chat_history"])  
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)


