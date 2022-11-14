from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('iPGs5vxwAOrwWxjMNjwL8Z841zzs1xCzgXMCf1pmieNwfQCwMB0IT9JT6Bwzygs7Xm+PI521pB/PzulpoOoakO414oG+nhW0pQKKzDCnOITWtAEKSMGnJAZwy+W2jwaR7pvH3lKR+j65TWRx+LJtkgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9a5e01015c3dbcca3b70ff546f606e33')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Are you eating ?"))


if __name__ == "__main__":
    app.run()