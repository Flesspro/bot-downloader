import telebot
import urllib.request
import datetime
import config

def dt(u): return datetime.datetime.utcfromtimestamp(u)

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text', 'contact', 'document'])
def download(message):
    print(message)
    if message.content_type == 'document':
        date_time = dt(message.date)
        date_string = '{0}{1:02d}{2:02d}'.format(date_time.year, date_time.month, date_time.day)
        document_title = message.document.file_name

        download_to = config.downloadPC + '{0}_{1}'.format(date_string, document_title)
        print(download_to)

        download_file_id = message.document.file_id
        download_file = bot.get_file(download_file_id)
        print (download_file_id)

        download_file_path = download_file.file_path
        print (download_file_path)

        download_from = "https://api.telegram.org/file/bot{0}/{1}".format(config.token, download_file_path)
        print (download_from)

        urllib.request.urlretrieve(download_from, download_to)


if __name__ == '__main__':
    print("bot has started..")
    while True:
        try:
            bot.polling(none_stop=False)
        except:
           pass
