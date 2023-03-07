import requests

url = 'https://stock.xueqiu.com/v5/stock/batch/quote.json?symbol=SH000001,SZ399001,SZ399006,SH000688,SH000016,SH000300,BJ899050,HKHSI,HKHSCEI,HKHSTECH,.DJI,.IXIC,.INX'
cookie = 'device_id=83849cfd9eba56e12e1101756276dcc6; xq_a_token=7da3658c0a79fd9ef135510bc5189429ce0e3035; xqat=7da3658c0a79fd9ef135510bc5189429ce0e3035; xq_r_token=c4e290f788b8c24ec35bd4b893dc8fa427e1f229; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY3OTk2MjkxMiwiY3RtIjoxNjc3NzY3OTYwNTYyLCJjaWQiOiJkOWQwbjRBWnVwIn0.Hs5kDWL93JxAD_Us7Y8OgBk_AmpunyWHDHwf0gFDh0De2GWHgryqzKaLyHeUnLexM9YXfWu1-zgdiABIrwBi-IAI6_xuRoVZ2ib1eMQ1NkQSogs6xKzcieisPP0911uYAaY0H79Nba3-Kk_MPiKol_agDYcQ7y6dCXXiiUz4w91KDSCad660PnMA90MNuKpJ2zOK3GOJNuC4CZwVM5GQpHwPV1Q-wAabCV6M5V3zoynx4opmRxzj6jNCjJW1nb-eKVGuX-X-7H8Yb4KTIqec6WHWlRf-Z2rKH2JzU6rgeIU1IOp7FTovFxlVZ1plh7EhQHj9fWnqiXpZ'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    "referer": "https://xueqiu.com/",
    "cookie": cookie,

}
res = requests.get(url, headers=headers)
print(res.text)
