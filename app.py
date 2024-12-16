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
        # 使用 ImageCarouselTemplate 展示電影資訊
        image_carousel_template_message = TemplateSendMessage(
            alt_text='電影推薦 - 請使用手機查看完整內容',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/1IrjFiU.jpg',  # 電影1封面
                        action=PostbackAction(
                            label='《音速小子3》',
                            text='《音速小子3》\n簡介：音速小子將展開一場至今最精彩刺激的冒險，索尼克、納克魯斯和塔爾斯再度合作，共同對抗一個全新的敵人，夏特，一個神祕的大壞蛋，擁有他們從未面對過的力量。他們發現他們的每一種能力都比不上這個大壞蛋時，索尼克小隊必須找來一個沒有人會想到的盟友，希望幫助他們阻止夏特，並且保護地球。\n上映日期：2024年12月27日',
                            data='action=001'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/tNg1THs.jpg',  # 電影2封面
                        action=PostbackAction(
                            label='《劇場版「進擊的巨人」完結篇THE LAST ATTACK》',
                            text='《劇場版「進擊的巨人」完結篇THE LAST ATTACK》\n簡介：人類為了躲避巨人威脅而建築高聳城牆，躲在牆中過著苟且偷生的日子。一天，超大型巨人來襲打破了歷經百年的和平，紛亂中失去母親的少年艾連・葉卡自此發誓要驅逐所有巨人，成為與巨人戰鬥的調查軍團的一員。在幾番賭命的險惡戰鬥中，艾倫得到化身為巨人的能力，一邊為人類的勝利做出貢獻，逐步慢慢接近世界的真相。時光流逝，來到牆外世界的艾連選擇與調查軍團的伙伴們分道揚鑣，執行一個驚世駭俗的恐怖計畫。\n上映日期：2025年1月03日',
                            data='action=002'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/uzMQqMT.jpg',  # 電影3封面
                        action=PostbackAction(
                            label='《來福大酒店》',
                            text='《來福大酒店》\n簡介：故事圍繞在一家名為「來福大酒店」的特殊旅館展開,這裡不僅提供住宿,更是一個「病友之家」,為病患和他們的家屬提供了一個可以陪伴看病、幫忙拿藥、協助問診的避風港。在這裡,一群與命運抗爭的陌生人相遇,彼此間發生了一系列溫暖而治癒的故事。\n上映日期：2025年1月10日',
                            data='action=003'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/1IYbSsZ.jpg',  # 電影4封面
                        action=PostbackAction(
                            label='《巴布狄倫：搖滾詩人》',
                            text='《巴布狄倫：搖滾詩人》\n簡介：影片以充滿活力的音樂圈和動盪的文化劇變為背景，一個神祕的19歲男孩帶著吉他和非同小可的才華，從明尼蘇達來到紐約西村，注定要改變美國音樂的軌跡。隨著在成名過程中建立起最親密的關係，民謠音樂的變化也逐漸令他感到躁動不安，並且拒絕被定義，最後做出一個極具爭議的選擇，為全球文化帶來顛覆性的影響。\n上映日期：2025年1月24日',
                            data='action=004'
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
