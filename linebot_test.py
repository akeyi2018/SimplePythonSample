from linebot import LineBotApi
from linebot.models import TextSendMessage
import json

def main():
    json_file = 'info.json' 
    with open(json_file, 'r') as f:
        data = json.load(f)
    token = data['token']
    user_id = data['user_id']

    lb = LineBotApi(token)
    message = TextSendMessage(text='おはよう💛')
    lb.push_message(user_id, messages=message)

if __name__ == '__main__':
    main()

