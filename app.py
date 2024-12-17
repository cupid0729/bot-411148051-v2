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
    message = event.message.text
    if re.match('查看菜單', message):
        flex_message = FlexSendMessage(
            alt_text='餐廳菜單推薦',
            contents={
                "type": "carousel",
                "contents": [
                    {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://i.imgur.com/8kF9yi5.jpg",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "沙朗牛排",
                                    "weight": "bold",
                                    "size": "xl"
                                },
                                {
                                    "type": "text",
                                    "text": "油花不多，有少許嫩筋，利用水果本身自然酵素嫩化肉質",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm"
                                },
                                {
                                    "type": "text",
                                    "text": "價格: NT 180",
                                    "color": "#333333",
                                    "size": "md"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "postback",
                                        "label": "訂購",
                                        "data": "action=order&item=沙朗牛排"
                                    },
                                    "style": "primary",
                                    "color": "#905c44"
                                }
                            ]
                        }
                    },
                    {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                             "url": "https://i.imgur.com/4xDGvls.jpg",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "豬排",
                                    "weight": "bold",
                                    "size": "xl"
                                },
                                {
                                    "type": "text",
                                    "text": "新鮮溫體豬，利用水果本身自然酵素嫩化肉質",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm"
                                },
                                {
                                    "type": "text",
                                    "text": "價格: NT 170",
                                    "color": "#333333",
                                    "size": "md"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "postback",
                                        "label": "訂購",
                                        "data": "action=order&item=豬排"
                                    },
                                    "style": "primary",
                                    "color": "#905c44"
                                }
                            ]
                        }
                    },
                    {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                             "url": "https://i.imgur.com/qM7t8Lm.jpg",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "香煎雞腿排",
                                    "weight": "bold",
                                    "size": "xl"
                                },
                                {
                                    "type": "text",
                                    "text": "新鮮溫體雞肉，酥脆甜嫩中散發淡淡義式香料味",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm"
                                },
                                {
                                    "type": "text",
                                    "text": "價格: NT 190",
                                    "color": "#333333",
                                    "size": "md"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "postback",
                                        "label": "訂購",
                                        "data": "action=order&item=香煎雞腿排"
                                    },
                                    "style": "primary",
                                    "color": "#905c44"
                                }
                            ]
                        }
                    }
                ]
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入有效的指令"))

@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    if "action=order" in data:
        item = data.split("&item=")[1]
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"已成功將「{item}」加入購物車！")
        )

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
