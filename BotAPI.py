from flask import Flask, request, jsonify

from main import bot

app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    print(chatInput)
    return jsonify(chatBotReply=bot(chatInput))

if __name__ == '__main__':
    app.run(host='192.168.1.55', port=5000, debug=True)