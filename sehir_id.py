import requests

cookies = {
    'DiB': '!nuS7S3DbVraXq/8AeDsTC74PvKQVZLuXhW7FSlOOBlj7CDv9vvjUnI6nmWkLRvSPWF0X0Avk1PK8KQ==',
    'ai_user': 'm6xCQ|2023-03-17T20:35:58.060Z',
    '_ga_FDS4P8VQEK': 'GS1.1.1679146075.3.1.1679146285.0.0.0',
    '_ga_PWGRBXJKCP': 'GS1.1.1679239848.8.0.1679239848.0.0.0',
    '_ga': 'GA1.3.1488733006.1679037318',
    'arasra342134': 'vn6/5wuPZD3rQYcMA9i3UEWU3vNLxz7OLWJGU+KFrrXatc44RzOP5o+gIpUP3FVvbavgx7ms+pDL3PzMW+QupqjWJOCXcP2weuUFBiYFuUFiT1aVMmfhJvAhrTb6LZ3PZNeU1lKFTWsuC+EmVM7Phdv8bucPIirYeudJ3Jo8OI9zVgxDoEItRqOygl6/orgnMXgz1evv8cdHjs5/1DP8xSk+DmItVNddJSZS0yMJTx0l3SJdyKq6jMcFAV6ShCOUW0pvRTJ/DIBVrXI7HVJADx0GBU4G7H4sr3h7RrBAv+oLfAr9V37J+MthK5qEaSB5FDfxh9BCVyHQwD1c/2ZRAzfNqR5eDVLOOguT8lrlAyg8OVFsiaxxvFl7YsF8kdDia/lC32dBDtEf7IU5VR/1dJs6EgpWvEAUPrQc8DIZiMkQQZOpgXFxYQ8eAw1D/EFuuicdbf9FrkNowhbRNDyekbumicYvoSfb3DVZ2Zx16JGJHgZ+iDOQ9Nx7JHSLFyv/UKVTR7PjpI1B1kiHDEaQgf5C4h19VlqUfF3pdsM8Lr3SveRgRwT+03LlOnqCFVRBon+qSVE1VCX1EvOI2YHsdc0e8dJ1dPBbX+TLVZfYidbh8rhHwdEgr3zLgMCgDnf0INMU6Jl+BQc+gqfzSaWtj2G7V/5kHNKiiAGXsvTKaORpEEDCQOx3v0iRGP6oy/KKJpvfeO0BGhk91sbXhCcWkWPF/giDPEpOAM7lG1OGRh+V2JBEjvyyugEp5zaMbAhkKCbBHALVIXMQb4WZ0xOtVTKvQ/fH6XdKJVuDBJvhZd00TLCHod639+xCps4xbRk5v/xc0v1sOR1d6QNtmWA0ICNmXlPv6QbA36gtBXiwNan3caaRCZQJaaZGdUJF1r7tMjRp8Gkto2vl8NEUzYmF7z2WaZGZoKk3yxCWxnqi1z6T9pks/w0J5GBzb9dChRf/MwGoJ4mffsUdiNm+b3oQWHw5sEQKopYyE/cRxs4ZP0zNWMOplhHDJt5DT31INPnGXV/7fna/VfekgHVR0ISELNvW0pU5oZWBQBKNchJaU6aLOSS7W/cPpPfOwSHgA1hdZ6GPO0sm+iEbdIO7sZ3OBg46EklNmCTqE9jw4Xtl/jaVUU566F9BttXi/CvQvcyTkmEDhL4n1YvH7Z8lVmzEgyr0sfrC0KpglE/3JLNIMITtDgd9519ej+riI7CfJJoAZ1iOFGb4Yi5bbVF/6VkZcKDBNMwaWre1de8m3FHl4t101/eCLP6vlLOMzDUC5gapNn3knuwArA5KuLLhYY43Ek0u22/hrzPnVpT+po7jUfA2/6Y5LOx3UVvTTDb4uRHjtMKdsw5WJwaS2NuZ+O5assGRpat2ht5X+Nw0fBTzLvHjrqv8eTUHnvmxhh6hZMsgYF/zTtHFhDgxxKRGaSPRtHiOQYg+7c0dYZW52gsKbiuAIpZVfSD8nLbF63OKr/UKI8rKST6baTLkykIK2bAyVMq1zYgaE25RrxAcxGLzbsm1n/x7rQ54fcmFQvXfl5oCv3nwJQhBOdV0UwNV5lY7yDmunwinIWWjv12e3FDy1lzdcXnr8yK2DJHLSgsBPR0gNhr+cXtEb+izalQXQ1ZUHgtjVccf9g89e+8MIu7stKiQuDlq4UkVQXAZoO6pDcHFdzs9Z/+7UE8VSMQVYEg4c6WlUYxA4nxO/Ir+8TG5fPFmNZdxBBxOBS4V1OmaU0sfzwqt/gWWdJFpgvbIUYuGoQ==',
    '_gid': 'GA1.3.698586631.1680452813',
    'dib_ilce_id': '9146',
    '_gat_gtag_UA_3381057_30': '1',
    'TS012e65ba': '011aa44a385a0fff52a8eb6f6d52acf83244a82e9efaa71df8e28973f1dd2e61172a6dcacdf1d7ade45e7494486b43a42f69a269e4a6d34c9e59e89855687147b27f6e220c1a6f4029a32e4c455b4b5af3d52cfe4001eb7bc490d872d9242310d9d5f195f7e727673720c11108c55ef4ab0c58bb577fb98c9f3cacf7d031d1f8c9c61c584e7759ca21104326200bcdc92f0a808af7',
    'TSe78d6aab077': '083d721e09ab2800ebf89b49a6d98e57984f50e7398b9910936c566d05d2136ae1512858c624aef28ab4a2d8396ccfaf08576aaa7b172000fb65241651bbddcc69aea2cb2d73557a814fcff64639875c240d31108dfaa96b',
    'ai_session': 'XdHmL|1680468352740|1680468369961.6',
    'TS00000000076': '083d721e09ab2800f974068dd4cb75f3af74477775092acc55e4c79d4d22db8eff796a0dc4dd32563aa6a13565adffa808252edcad09d000b79ea8ae8dddd7b6f0549f853cd5cf30ce8d8903bee9f76bf5a084016fef1a62ba59ab14a854786d5b716c3164a578a7a1066833e785a1b27b8f7cb1276d19a9f3805289d3f81ae04f85195744177a04abc03339308d96db2520b91dcc22cb2d50133ff3d8be8ab70887f14bdc4aeb01e29cb0c482faeff03b14daf876c44e6a04514bf8985af6e5c376aa5d76f2183822d9db08314684dd4f071a4788d64d2e321312819f351617673244f6224f52e4dd1f081123f1f01067514d1d4916b55ad6dbc47d2250f34f1b05f5e86e7418bd',
    'TSPD_101_DID': '083d721e09ab2800f974068dd4cb75f3af74477775092acc55e4c79d4d22db8eff796a0dc4dd32563aa6a13565adffa808252edcad063800e3745e769a9c4b036013123ae04f93e443d084eaeeab3b92be20edbf7c38d6b92e4620218d6fb9f4abcc345a2847d39a74d75fb8b5acd152',
    'TSe78d6aab029': '083d721e09ab28004e865b3790719a418fa709abf8f4cf1341ee3d2ed64881c51424c4e61009e722699f17e0ebdbf312',
    'TSPD_101': '083d721e09ab280024ec1c80b8175d6c422700bb1b98ca8809d8c1bc777cadef74b82994adc0207f3d8006f1c3902d30082542a3060518000c7728f18a3ed97db1e815dcdfaf25391dc7b943108c99db',
    'TS003fd7e5027': '083d721e09ab2000e798b478dfce00e2e59cc211dc25859f1179c2a9e35a31eafd5ffd8a26a69c880869a871e2113000c5de30e13285d376e10f6e66c784568acfd3365833e41d05e28e2813a6231a9c51e8d323d4547dde44ea9c615be1cc91',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'DiB=!nuS7S3DbVraXq/8AeDsTC74PvKQVZLuXhW7FSlOOBlj7CDv9vvjUnI6nmWkLRvSPWF0X0Avk1PK8KQ==; ai_user=m6xCQ|2023-03-17T20:35:58.060Z; _ga_FDS4P8VQEK=GS1.1.1679146075.3.1.1679146285.0.0.0; _ga_PWGRBXJKCP=GS1.1.1679239848.8.0.1679239848.0.0.0; _ga=GA1.3.1488733006.1679037318; arasra342134=vn6/5wuPZD3rQYcMA9i3UEWU3vNLxz7OLWJGU+KFrrXatc44RzOP5o+gIpUP3FVvbavgx7ms+pDL3PzMW+QupqjWJOCXcP2weuUFBiYFuUFiT1aVMmfhJvAhrTb6LZ3PZNeU1lKFTWsuC+EmVM7Phdv8bucPIirYeudJ3Jo8OI9zVgxDoEItRqOygl6/orgnMXgz1evv8cdHjs5/1DP8xSk+DmItVNddJSZS0yMJTx0l3SJdyKq6jMcFAV6ShCOUW0pvRTJ/DIBVrXI7HVJADx0GBU4G7H4sr3h7RrBAv+oLfAr9V37J+MthK5qEaSB5FDfxh9BCVyHQwD1c/2ZRAzfNqR5eDVLOOguT8lrlAyg8OVFsiaxxvFl7YsF8kdDia/lC32dBDtEf7IU5VR/1dJs6EgpWvEAUPrQc8DIZiMkQQZOpgXFxYQ8eAw1D/EFuuicdbf9FrkNowhbRNDyekbumicYvoSfb3DVZ2Zx16JGJHgZ+iDOQ9Nx7JHSLFyv/UKVTR7PjpI1B1kiHDEaQgf5C4h19VlqUfF3pdsM8Lr3SveRgRwT+03LlOnqCFVRBon+qSVE1VCX1EvOI2YHsdc0e8dJ1dPBbX+TLVZfYidbh8rhHwdEgr3zLgMCgDnf0INMU6Jl+BQc+gqfzSaWtj2G7V/5kHNKiiAGXsvTKaORpEEDCQOx3v0iRGP6oy/KKJpvfeO0BGhk91sbXhCcWkWPF/giDPEpOAM7lG1OGRh+V2JBEjvyyugEp5zaMbAhkKCbBHALVIXMQb4WZ0xOtVTKvQ/fH6XdKJVuDBJvhZd00TLCHod639+xCps4xbRk5v/xc0v1sOR1d6QNtmWA0ICNmXlPv6QbA36gtBXiwNan3caaRCZQJaaZGdUJF1r7tMjRp8Gkto2vl8NEUzYmF7z2WaZGZoKk3yxCWxnqi1z6T9pks/w0J5GBzb9dChRf/MwGoJ4mffsUdiNm+b3oQWHw5sEQKopYyE/cRxs4ZP0zNWMOplhHDJt5DT31INPnGXV/7fna/VfekgHVR0ISELNvW0pU5oZWBQBKNchJaU6aLOSS7W/cPpPfOwSHgA1hdZ6GPO0sm+iEbdIO7sZ3OBg46EklNmCTqE9jw4Xtl/jaVUU566F9BttXi/CvQvcyTkmEDhL4n1YvH7Z8lVmzEgyr0sfrC0KpglE/3JLNIMITtDgd9519ej+riI7CfJJoAZ1iOFGb4Yi5bbVF/6VkZcKDBNMwaWre1de8m3FHl4t101/eCLP6vlLOMzDUC5gapNn3knuwArA5KuLLhYY43Ek0u22/hrzPnVpT+po7jUfA2/6Y5LOx3UVvTTDb4uRHjtMKdsw5WJwaS2NuZ+O5assGRpat2ht5X+Nw0fBTzLvHjrqv8eTUHnvmxhh6hZMsgYF/zTtHFhDgxxKRGaSPRtHiOQYg+7c0dYZW52gsKbiuAIpZVfSD8nLbF63OKr/UKI8rKST6baTLkykIK2bAyVMq1zYgaE25RrxAcxGLzbsm1n/x7rQ54fcmFQvXfl5oCv3nwJQhBOdV0UwNV5lY7yDmunwinIWWjv12e3FDy1lzdcXnr8yK2DJHLSgsBPR0gNhr+cXtEb+izalQXQ1ZUHgtjVccf9g89e+8MIu7stKiQuDlq4UkVQXAZoO6pDcHFdzs9Z/+7UE8VSMQVYEg4c6WlUYxA4nxO/Ir+8TG5fPFmNZdxBBxOBS4V1OmaU0sfzwqt/gWWdJFpgvbIUYuGoQ==; _gid=GA1.3.698586631.1680452813; dib_ilce_id=9146; _gat_gtag_UA_3381057_30=1; TS012e65ba=011aa44a385a0fff52a8eb6f6d52acf83244a82e9efaa71df8e28973f1dd2e61172a6dcacdf1d7ade45e7494486b43a42f69a269e4a6d34c9e59e89855687147b27f6e220c1a6f4029a32e4c455b4b5af3d52cfe4001eb7bc490d872d9242310d9d5f195f7e727673720c11108c55ef4ab0c58bb577fb98c9f3cacf7d031d1f8c9c61c584e7759ca21104326200bcdc92f0a808af7; TSe78d6aab077=083d721e09ab2800ebf89b49a6d98e57984f50e7398b9910936c566d05d2136ae1512858c624aef28ab4a2d8396ccfaf08576aaa7b172000fb65241651bbddcc69aea2cb2d73557a814fcff64639875c240d31108dfaa96b; ai_session=XdHmL|1680468352740|1680468369961.6; TS00000000076=083d721e09ab2800f974068dd4cb75f3af74477775092acc55e4c79d4d22db8eff796a0dc4dd32563aa6a13565adffa808252edcad09d000b79ea8ae8dddd7b6f0549f853cd5cf30ce8d8903bee9f76bf5a084016fef1a62ba59ab14a854786d5b716c3164a578a7a1066833e785a1b27b8f7cb1276d19a9f3805289d3f81ae04f85195744177a04abc03339308d96db2520b91dcc22cb2d50133ff3d8be8ab70887f14bdc4aeb01e29cb0c482faeff03b14daf876c44e6a04514bf8985af6e5c376aa5d76f2183822d9db08314684dd4f071a4788d64d2e321312819f351617673244f6224f52e4dd1f081123f1f01067514d1d4916b55ad6dbc47d2250f34f1b05f5e86e7418bd; TSPD_101_DID=083d721e09ab2800f974068dd4cb75f3af74477775092acc55e4c79d4d22db8eff796a0dc4dd32563aa6a13565adffa808252edcad063800e3745e769a9c4b036013123ae04f93e443d084eaeeab3b92be20edbf7c38d6b92e4620218d6fb9f4abcc345a2847d39a74d75fb8b5acd152; TSe78d6aab029=083d721e09ab28004e865b3790719a418fa709abf8f4cf1341ee3d2ed64881c51424c4e61009e722699f17e0ebdbf312; TSPD_101=083d721e09ab280024ec1c80b8175d6c422700bb1b98ca8809d8c1bc777cadef74b82994adc0207f3d8006f1c3902d30082542a3060518000c7728f18a3ed97db1e815dcdfaf25391dc7b943108c99db; TS003fd7e5027=083d721e09ab2000e798b478dfce00e2e59cc211dc25859f1179c2a9e35a31eafd5ffd8a26a69c880869a871e2113000c5de30e13285d376e10f6e66c784568acfd3365833e41d05e28e2813a6231a9c51e8d323d4547dde44ea9c615be1cc91',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'dnt': '1',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


from utils import sehirler_kod
import json
d = {}
for i in sehirler_kod:
    print(i)
    response = requests.get(f'https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_kod[i]}/{i}-icin-namaz-vakti', cookies=cookies, headers=headers)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    soup = soup.find_all('select')
    kk = {}
    for j in (soup[2].contents):
        if j != '\n':
            liste_data = (str(j['data-url']).replace('/tr-TR/', '').replace('-icin-namaz-vakti', '').split('/'))
            for x in liste_data:
                kk.update({liste_data[1]:int(liste_data[0])})
        else:
            continue
    dd = {i:kk}
    d.update(dd)
with open('sehirler_ilceler_kod.json', 'w') as f:
    json.dump(d, f, indent=4)

#print((soup[2].contents))