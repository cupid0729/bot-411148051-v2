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
        if re.match('電影推薦', message):
        try:
            image_carousel_template_message = TemplateSendMessage(
                alt_text='電影推薦 - 請使用手機查看完整內容',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/1IrjFiU.jpg',
                            action=MessageAction(
                                label='《音速小子3》',
                                text='《音速小子3》\n簡介：全新冒險故事...\n上映日期：2024年12月27日'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/tNg1THs.jpg',
                            action=MessageAction(
                                label='《進擊的巨人 完結篇》',
                                text='《進擊的巨人》最終戰役，震撼登場！\n上映日期：2025年1月03日'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/uzMQqMT.jpg',
                            action=MessageAction(
                                label='《來福大酒店》',
                                text='《來福大酒店》感人故事，歡笑與淚水交織...\n上映日期：2025年1月10日'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/1IYbSsZ.jpg',
                            action=MessageAction(
                                label='《巴布狄倫：搖滾詩人》',
                                text='搖滾巨星的傳奇旅程！\n上映日期：2025年1月24日'
                            )
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)