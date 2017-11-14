import requests
import datetime


firsturl = 'https://api.telegram.org/bot' # URL на который отправляется запрос
token = '481451821:AAEB30nuW8xoBm2ZTxkxTvfaaS4JVOqb8ak' # токен вашего бота, полученный от @Botfather
secondurl = '/sendMessage?chat_id='
chat_id = '467479566'
lasturl = '&text='
message = '22'
url_base = firsturl + token + '/'
URL = firsturl+token+secondurl+chat_id+lasturl+message

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text', text}
        method = 'sendNessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()
        
        last_update_id = last_update['update_id']


        
def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url_base + 'sendMessage', data=params)
    return response

def  main():
    update_id = last_update(get_updates_json(url_base))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url_base))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url_base))), 'test')
            update_id += 1
    sleep(1)
if __name__ == '__main__':
    main()
    
