# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('BRKn+F0OIE+685bVs5cQxIxBnxnol3mfbJ3BqkIbjRYkFf2iVdsA3UVMMOVbbg0bTpKWkJvOg5Qt3jhjAoZNPtznG0etwmOTy7lUEA3AdcQCL/QeUPY8i2ZClB7LdL6m0cn7XTQt8+f5qho/+DaaMQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('3a4f2a107a7feb30a41f21c125816be6')

line_bot_api.push_message('U4492871599fb3e554d18bdb13adcdbbb', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('我想吃飯',message):
        flex_message = TextSendMessage(text='請點選您想要的餐點',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="牛肉麵", text="牛肉麵")),
                                   QuickReplyButton(action=MessageAction(label="牛肉飯", text="牛肉飯")),
                                   QuickReplyButton(action=MessageAction(label="貢丸湯", text="貢丸湯")),
                                   QuickReplyButton(action=MessageAction(label="虱目魚湯", text="虱目魚湯")),
                                   QuickReplyButton(action=MessageAction(label="紅茶", text="紅茶")),
                                   QuickReplyButton(action=MessageAction(label="綠茶", text="綠茶"))
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif message in ["牛肉麵", "牛肉飯", "貢丸湯","虱目魚湯", "紅茶", "綠茶"]:
        # 回應用戶選擇的選項
        reply_text = f"您已成功將【{message}】加入購物車。"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
