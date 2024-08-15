import requests

from environs import Env

env = Env()
env.read_env()


def  send_message(text):
  BOT_TOKEN = env.str("BOT_TOKEN")
  CHAT_ID = env.str("CHAT_ID")
  PHOTO = "https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg"
  TEXT = text
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
  print(url)
  response = requests.get(url)



