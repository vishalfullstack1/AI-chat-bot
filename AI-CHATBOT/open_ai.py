from flask import render_template, session


# @app.route("/")
# def home():
#     session.setdefault("chat_history",[])
#     return render_template("index.html",chat_history=session["chat_history"])









#--------------------------open ai only backemd code----------------

# messages = []

# def completion(message):
#     global messages

#     messages.append({
#         "role": "user",
#         "content": message
#     })

#     chat_completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )

#     reply = chat_completion.choices[0].message.content.strip()

#     messages.append({
#         "role": "assistant",
#         "content": reply
#     })

#     print(f"Shipra: {reply}\n")

# if __name__ == "__main__":
#     print("Shipra: Hi! I’m Shipra, your AI assistant \n")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Shipra: Goodbye! ")
#             break
#         completion(user_input)
