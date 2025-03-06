import requests
import json
import subprocess
from pyrogram import Client,filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import tgcrypto
from p_bar import progress_bar
from details import api_id, api_hash, bot_token, sudo_groups
from urllib.parse import parse_qs, urlparse
from subprocess import getstatusoutput
import helper
import logging
import time
import aiohttp
import asyncio
import aiofiles
from aiohttp import ClientSession
from pyrogram.types import User, Message
import sys ,io
import re
import os
from pyrogram.types import InputMediaDocument
import time
import random 
from psutil import disk_usage, cpu_percent, swap_memory, cpu_count, virtual_memory, net_io_counters, boot_time
import asyncio
from pyrogram import Client, filters
from pyrogram.errors.exceptions import MessageIdInvalid
import os
import yt_dlp
from bs4 import BeautifulSoup
from pyrogram.types import InputMediaDocument

botStartTime = time.time()
batch = []
bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)
    
    
# CW Extractor Code (integrated from previous file)
print(render("CW", gradient=["red", "magenta"], align="center"))

text = "📤 CW Extractor | Notes + Videos TXT | Developed in PYTHON 🧲\n"
print(text.center(os.get_terminal_size().columns))

u = [
    "okhttp/5.0.0-alpha.1",
    "okhttp/5.0.0-alpha.2",
    "okhttp/5.0.0-alpha.3",
    "okhttp/5.0.0-alpha.4",
    "okhttp/5.0.0-alpha.5",
    "okhttp/5.0.0-alpha.6",
    "okhttp/5.0.0-alpha.7",
    "okhttp/5.0.0-alpha.8",
    "okhttp/5.0.0-alpha.9",
    "okhttp/5.0.0-alpha.10",
]


headers = {
    'appver': '92',
    'apptype': 'android',
    'Host': 'elearn.crwilladmin.com',
    "accept-encoding": "gzip",
    "user-agent": "Mozilla/5.0",
    "cwkey": "zXRzQ9cKpUBYzsAfbv1KEPQRoj1eytlqUe0w5yRHQvm0gkHYIlNfl7OKm3SAjT3Y",
    "authority": "elearn.crwilladmin.com",
    "accept": "application/json",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://web.careerwill.com",
    "apptype": "web",
    "referer": "https://web.careerwill.com/",
    "user-agent": "okhttp/5.0.0-alpha.2",
}

def get_token(email, password):
    login_data = {
        "deviceType": "android",
        "password": password,
        "deviceModel": "Xiaomi M2007J20CI",
        "deviceVersion": "Q(Android 10.0)",
        "deviceIMEI": "d57adbd8a7b8u9i9",
        "deviceToken": "c8HzsrndRB6dMaOuKW2qMS:APA91bHu4YCP4rqhpN3ZnLjzL3LuLljxXua2P2aUXfIS4nLeT4LnfwWY6MiJJrG9XWdBUIfuA6GIXBPIRTGZsDyripIXoV1CyP3kT8GKuWHgGVn0DFRDEnXgAIAmaCE6acT3oussy2",
        "email": email,
    }


def gettoken():
    data1 = {
        "email": email,
        "password": password,
        "deviceType": "web",
        "deviceVersion": "Chrome 122",
        "deviceModel": "chrome",
    }
    headers1 = headers
    response1 = requests.post(
        "https://elearn.crwilladmin.com/api/v5/login-other",
        headers=headers1,
        data=data1,
    )
    if response1.status_code == 200:
        print("\n✅ Login Successfull!")
        resp1 = response1.text
        token = json.loads(resp1)["data"]["token"]
        return token
    elif response1.status_code == 400:
        print("\n❌ Wrong Credentials!")
        exit()
    else:
        headers["user-agent"] = random.choice(u)
        gettoken()


def printbatches(token):
    headers2["token"] = token
    response2 = requests.get(
        "https://elearn.crwilladmin.com/api/v5/my-batch", headers=headers2
    )
    if response2.status_code == 200:
        resp2 = response2.text
        batch_data = json.loads(resp2)["data"]["batchData"]
        table_data = [(batch["id"], batch["batchName"]) for batch in batch_data]
        print()
        print(
            tabulate(
                table_data, headers=["Batch ID", "Batch Name"], tablefmt="simple_grid"
            )
        )
    else:
        headers2["user-agent"] = random.choice(u)


def getbatches(token):
    headers2["token"] = token
    response2 = requests.get(
        "https://elearn.crwilladmin.com/api/v5/my-batch", headers=headers2
    )
    if response2.status_code == 200:
        resp2 = response2.text
        l = len(json.loads(resp2)["data"]["batchData"])
        # print("\n\n*** BATCH ID - COURSE NAME ***\n")
        for i in range(l):
            global batchidl, batchid, batchname
            batchname = json.loads(resp2)["data"]["batchData"][i]["batchName"]
            batchid = json.loads(resp2)["data"]["batchData"][i]["id"]
            # print(f'{batchid} - {batchname}')
            batchidl[batchid] = batchname
        idd = str(
            input("\nEnter Batch ID (comma separated if multiple or 0 for all): ")
        )
        return idd
    else:
        headers2["user-agent"] = random.choice(u)


def get_class_detail(session, classid):
    try:
        response = session.get(f"https://elearn.crwilladmin.com/api/v5/class-detail/{classid}")
        response.raise_for_status()
        lessonurl = response.json()["data"]["class_detail"]["lessonUrl"]
        return lessonurl
    except Exception as e:
        print(f"Error fetching class detail for classid={classid}: {str(e)}")
        return None


def reqq(topicid, topicname, idd, max_retries=3, wait_time=30):
    with requests.Session() as session:
        session.headers.update(headers2)

        for attempt in range(max_retries):
            response4 = session.get(f"https://elearn.crwilladmin.com/api/v5/batch-detail/{idd}?topicId={topicid}")

            if response4.status_code == 200:
                resp4 = response4.text
                try:
                    classes = json.loads(resp4)["data"]["class_list"]["classes"]
                    kk = len(classes)
                except KeyError:
                    print(f"KeyError in JSON response. Retrying in {wait_time} seconds.")
                    time.sleep(wait_time)
                    continue

                with ThreadPoolExecutor(max_workers=5) as executor:
                    futures = [executor.submit(get_class_detail, session, classes[i]["id"]) for i in range(kk)]

                for i, future in enumerate(futures):
                    global vlinks
                    try:
                        lessonurl = future.result()
                        if lessonurl is not None:
                            lessonname = classes[i]["lessonName"]
                            lessonext = classes[i]["lessonExt"]
                            namex = f"{topicname}-{lessonname}"

                            if lessonext == "brightcove":
                                #   vlinks += f"{namex}::https://hydrator.vercel.app/api/hydrate?user={email}&pass={password}&cid={classes[i]['id']}&vid={lessonurl}\n"
                                vlinks += f"{namex}::https://edge.api.brightcove.com/playback/v1/accounts/6206459123001/videos/{lessonurl}/master.m3u8?bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NDA5MTg1NjAsImNvbiI6eyJpcyFkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZW1kaldGQnpURzFJWVVrNWJFeEpLMGR6U25oM1VUMDkiLCJmaXJzdF9uYW1lIjoiZVZaUmJGUkxXRWROV2pGSFFXVTFUMnBXUVhOR1p6MDkiLCJlbWFpbCI6ImFqSnJjbEpGTlRCWU1VOXRlbTFCWjBsc1UxRnRabFU0UWtsSVkwMHJjVUpGZUVwdVZHdGpRaTlWV1QwPSIsInBob25lIjoiWm0xQ04xbEtLMHhLY0doRU1XbHhhMmw1VmpsQlp6MDkiLCJyZWZlcnJhbF9jb2RlIjoiYk14TU4wWm1TRkVQTEZOM1ZUTXdORVMyUkhYNlFUMDkiLCJkZXZpY2VfdHlwZSI6ImFuZHJvaWQiLCJkZXZpY2VfdmVyc2lvbiI6IlEoQW5kcm9pZCAxMC4wKSIsImRldmljZV9tb2RlbCI6IlhpYW9taSBNMjAwN0oyMGM0IiwicmVtb3RlX2FkZHIiOiIxODAuMTQ5LjIyNC4xMTAifX0.Owo-FSrh7aAdgpohia2z8L3ZKyV38OQ1cSsVuA_ExzPg3K5s-sWffQw_vIAPkHpSh08saije6ekMTGJtCiIEfjrVByG-A07gU-lEHOPkcaOpDeIxbLCtzQCtP5zkXtg2B1MKnHOOqfdUt4Yvs82t7ovt-sVPMN4IEHYGEA2E6KrpfByqPos2GcwqHZOBsDH2q-26keSFgdL-gX0tKK4tWywGHyIyyPWDAg7AiP0uFwyEkP3ffXCx0RQevPvODwb1RGnQt3yODRGOz_ub9TW9DLqO8v0rKHEQ-SPC1M1LwsOZZ69TImApuNUdSGHFhwcmyZixufbn-z72X7TYlejzow\n"

                            else:
                                vlinks += f"{namex}::https://www.youtube.com/watch?v={lessonurl}\n"

                    except Exception as e:
                        print(f"Error processing class {i + 1}: {str(e)}")

                return vlinks

            else:
                session.headers["user-agent"] = random.choice(u)
                print(f"Failed attempt {attempt + 1}. Retrying in {wait_time} seconds.")
                time.sleep(wait_time)

        print(f"Maximum retries reached. Unable to fetch data for topicid={topicid}, topicname={topicname}, idd={idd}.")
        return None


def batchtopicp(idd, a):
    pdf = ""
    headers2["token"] = a
    response3 = requests.get(
        f"https://elearn.crwilladmin.com/api/v5/batch-topic/{idd}?type=notes",
        headers=headers2,
    )
    if response3.status_code == 200:
        resp3 = response3.text
        ll = len(json.loads(resp3)["data"]["batch_topic"])
        for ii in range(0, ll):
            topicid = json.loads(resp3)["data"]["batch_topic"][ii]["id"]
            topicname = json.loads(resp3)["data"]["batch_topic"][ii]["topicName"]
            # print(f'{topicid}-{topicname}')
            reqqp(topicid, topicname, idd)

    elif response3.status_code == 401:
        print("Someone logged in..token changed")
        exit()
    else:
        headers2["user-agent"] = random.choice(u)
        batchtopicp(idd, a)


def batchtopic(idd):
    namex = ""
    response3 = requests.get(
        f"https://elearn.crwilladmin.com/api/v5/batch-topic/{idd}?type=class",
        headers=headers2,
    )
    if response3.status_code == 200:
        resp3 = response3.text
        ll = len(json.loads(resp3)["data"]["batch_topic"])
        for i in range(ll):
            topicid = json.loads(resp3)["data"]["batch_topic"][i]["id"]
            topicname = json.loads(resp3)["data"]["batch_topic"][i]["topicName"]
            reqq(topicid, topicname, idd)
    else:
        headers2["user-agent"] = random.choice(u)
        time.sleep(0.8)
        batchtopic(idd)


def reqqp(topicid, topicname, idd):
    response4 = requests.get(
        f"https://elearn.crwilladmin.com/api/v5/batch-notes/{idd}?topicId={topicid}",
        headers=headers2,
    )
    if response4.status_code == 200:
        resp4 = response4.text
        kk = len(json.loads(resp4)["data"]["notesDetails"])
        for i in range(kk):
            pdfname = json.loads(resp4)["data"]["notesDetails"][i]["docTitle"]
            docurl = json.loads(resp4)["data"]["notesDetails"][i]["docUrl"]
            # print(f'{topicname}-{pdfname}::{docurl}')
            global pdf
            pdf += f"{topicname}-{pdfname}::{docurl}\n"
            # print(f'{topicname}-{pdfname}::{docurl}')
    else:
        headers2["user-agent"] = random.choice(u)
        reqqp(topicid, topicname, idd)


headers2 = headers
global namex
namex = ""
global pdf
pdf = ""
passed = 0
batchidl = {}
      
@bot.on_message(filters.command(["start"]) & filters.chat(sudo_groups))
async def start_handler(bot: Client, m: Message):
    menu_text = (
        "Welcome to **TXT** Downloader Bot! \n\n"
        "[Generic Services]\n"
        "1. For All PDF /pdf\n"
        "2. For TXT /txt \n"
    )
    
    await m.reply_text(menu_text)


@bot.on_message(filters.command(["restart"]))
async def restart_handler(bot: Client, m: Message):
 rcredit = "Bot Restarted by " + f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
 if (f'{m.from_user.id}' in batch or batch == []) or m.from_user.id == sudo_groups:
    await m.reply_text("Restarted ✅", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
 else:
 	await m.reply_text("You are not started this batch 😶.")

def meFormatter(milliseconds) -> str:
    milliseconds = int(milliseconds) * 1000
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)}d, " if days else "")
        + (f"{str(hours)}h, " if hours else "")
        + (f"{str(minutes)}m, " if minutes else "")
        + (f"{str(seconds)}s, " if seconds else "")
        + (f"{str(milliseconds)}ms, " if milliseconds else "")
    )
    return tmp[:-2]
  
def humanbytes(size):
    size = int(size)
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return f"{str(round(size, 2))} {Dic_powerN[n]}B"

@bot.on_message(filters.command(["pdf"]) & filters.chat(sudo_groups))
async def c_pdf(bot: Client, m: Message):
    editable = await m.reply_text("**Hello I am All in one pdf DL Bot\n\nSend TXT file To Download.**")
    input99: Message = await bot.listen(editable.chat.id)
    x = await input99.download()
    await input99.delete(True)
    try:
        with open(x, "r", encoding="utf-8") as f:
            content = f.read().split("\n")
        links = [i.split(":", 1) for i in content if i]
        os.remove(x)
    except Exception as e:
        logging.error(e)
        await m.reply_text("Invalid file input ❌.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found in given txt {len(links)}\n\nSend From range, you want to download,\n\nInitial is 1")
    input1: Message = await bot.listen(editable.chat.id)
    count = int(input1.text)

    await m.reply_text("**Enter Batch Name**")
    inputy: Message = await bot.listen(editable.chat.id)
    raw_texty = inputy.text

    try:
        for i in range(count - 1, len(links)):
            name = links[i][0].strip()
            url = links[i][1].strip()
            cc = f'{str(count).zfill(3)}. {name}.pdf\n\n**Batch:-** {raw_texty}\n\n'
            
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{name}.pdf", 'wb') as pdf_file:
                    pdf_file.write(response.content)
                await m.reply_document(f'{name}.pdf', caption=cc)
                os.remove(f'{name}.pdf')
            else:
                await m.reply_text(f"Failed to download {name}.pdf")

            count += 1
            time.sleep(2)
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Completed ✅")

@bot.on_message(filters.command(["stats"]))
async def stats(_,event: Message):
    logging.info('31')
    currentTime = meFormatter((time.time() - botStartTime))
    osUptime = meFormatter((time.time() - boot_time()))
    total, used, free, disk= disk_usage('/')
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(net_io_counters().bytes_sent)
    recv = humanbytes(net_io_counters().bytes_recv)
    cpuUsage = cpu_percent(interval=0.5)
    p_core = cpu_count(logical=False)
    t_core = cpu_count(logical=True)
    swap = swap_memory()
    swap_p = swap.percent
    swap_t = humanbytes(swap.total)
    memory = virtual_memory()
    mem_p = memory.percent
    mem_t = humanbytes(memory.total)
    mem_a = humanbytes(memory.available)
    mem_u = humanbytes(memory.used)
    stats = f'Bot Uptime: {currentTime}\n'\
            f'OS Uptime: {osUptime}\n'\
            f'Total Disk Space: {total}\n'\
            f'Used: {used} | Free: {free}\n'\
            f'Upload: {sent}\n'\
            f'Download: {recv}\n'\
            f'CPU: {cpuUsage}%\n'\
            f'RAM: {mem_p}%\n'\
            f'DISK: {disk}%\n'\
            f'Physical Cores: {p_core}\n'\
            f'Total Cores: {t_core}\n'\
            f'SWAP: {swap_t} | Used: {swap_p}%\n'\
            f'Memory Total: {mem_t}\n'\
            f'Memory Free: {mem_a}\n'\
            f'Memory Used: {mem_u}\n'
    
    await event.reply_text(f"{stats}")    


@bot.on_message(filters.command(["txt"]) & filters.chat(sudo_groups))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("**Hello DeAr**, I am Txt Downloader Bot.\nI can download videos from **TXT file** one by one.\n\n**Developer: Smile Bhai** \n**Language:** Python\n**Framework:** 🔥Pyrogram\n\nNow Send Your TXT File:-\n") 
    input_msg = await bot.listen(editable.chat.id)
    x = await input_msg.download()
    
    await input_msg.delete(True)

    path = f"./downloads/{m.chat.id}"
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"Downloaded by [{m.from_user.first_name}](tg://user?id={m.from_user.id})" if m.from_user else "Downloaded anonymously"
    
    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = [i.split("://", 1) for i in content]
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
    
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend from where you want to download (initial is **1**)")
    input0 = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or send `df` for grabbing it from txt.**")
    input1 = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    b_name = file_name if raw_text0 == 'df' else raw_text0
    
    await editable.edit("**Enter resolution**")
    input2 = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    res = {
        "144": "256x144",
        "240": "426x240",
        "360": "640x360",
        "480": "854x480",
        "720": "1280x720",
        "1080": "1920x1080"
    }.get(raw_text2, "UN")

    await editable.edit("**Enter Caption or send `df` for default or just /skip**")
    input3 = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    creditx = {
        'df': credit,
        '/skip': ''
    }.get(raw_text3, raw_text3)
    await input3.delete(True)
   
    await editable.edit("Now send the **Thumb url**\nEg » ```https://telegra.ph/file/0633f8b6a6f110d34f044.jpg```\n\nor Send `no`")
    input6 = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    count = int(raw_text) if len(links) > 1 else 1
    
    try:
        message = await bot.send_message(sudo_groups, f"❇️ {b_name}")
        await message.pin()
        
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'your-access-token'}).json()['url']

            elif '/master.mpd' in url:
                id =  url.split("/")[-2]
                url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                cc = f'** {str(count).zfill(3)}.** {name1} {res}.mkv\n\n**Batch:-** {b_name}\n\n{creditx}'
                cc1 = f'** {str(count).zfill(3)}.** {name1}.pdf \n\n**Batch:-** {b_name}\n\n{creditx}'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                        count += 1
                        os.remove(ka)
                        time.sleep(5)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'aria2c -o "{name}.pdf" "{url}"'
                        os.system(cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                        time.sleep(5)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ Downloading »**\n\n**Name:-** `{name}\n\nQuality:- {raw_text2}`\n\n**With ❤️ From Admins.**"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(20)

            except Exception as e:
                await m.reply_text(
                    f"**Downloading Interrupted **\n\n{str(e)}\n**Name:-**  {name}\n\n**Link:-** \n\n `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done ✅")
    
    
    
    
@bot.on_message(filters.command(["cw"]) & filters.chat(sudo_groups))
async def cw_handler(bot: Client, m: Message):
    email = input("Enter E-Mail/Phone: ")
    password = input("Enter Password: ")  #Consider using getpass for better security
    try:
        a = gettoken(email, password)  #Call gettoken with email and password
        printbatches(a)
        idd = getbatches(a)
        start = time.time()

        if idd == "0":
            # Process all batches
            for idd, name in batchidl.items():
                vlinks = ""
                pdf = ""  #Initialize pdf variable here for each batch
                print(f"\nGetting PDF Links for batch {idd} ({name})...")
                batchtopicp(idd, a)
                # Reverse the order of lines for notes file
                with open(f"{idd}_{name}_notes.txt", "w", encoding="utf-8") as file:
                    reversed_pdf = "\n".join(reversed(pdf.strip().split("\n")))
                    file.write(reversed_pdf)

                print("PDF Extraction Done ✅\n")
                print(f"Getting Videos Links for batch {idd} ({name})...")
                vlinks = batchtopic(idd)  #vlinks should be returned by batchtopic

                # Reverse the order of lines for videos file
                with open(f"{idd}_{name}_videos.txt", "w", encoding="utf-8") as file:
                    reversed_vlinks = "\n".join(reversed(vlinks.strip().split("\n")))
                    file.write(reversed_vlinks)

                print("Videos Extraction Done ✅\n")
                end = time.time()
                print(f"Done in {end - start}")
                await m.reply_text(f"Batch {idd} ({name}) extraction complete!") # Notify user per batch


        else:
            # Process selected batches
            selected_ids = [int(batch_id.strip()) for batch_id in idd.strip().split(",")]
            for batch_id in selected_ids:
                if batch_id in batchidl:
                    vlinks = ""
                    pdf = "" #Initialize pdf variable here for each batch
                    print(f"\nGetting PDF Links for batch {batch_id} ({batchidl[batch_id]})...")
                    batchtopicp(batch_id, a)

                    # Reverse the order of lines for notes file
                    with open(
                        f"{batch_id}_{batchidl[batch_id]}_notes.txt", "w", encoding="utf-8"
                    ) as file:
                        reversed_pdf = "\n".join(reversed(pdf.strip().split("\n")))
                        file.write(reversed_pdf)

                    print("PDF Extraction Done ✅\n")
                    print(f"Getting Videos Links for batch {batch_id} ({batchidl[batch_id]})...")
                    vlinks = batchtopic(batch_id)

                    # Reverse the order of lines for videos file
                    with open(
                        f"{batch_id}_{batchidl[batch_id]}_videos.txt", "w", encoding="utf-8"
                    ) as file:
                        reversed_vlinks = "\n".join(reversed(vlinks.strip().split("\n")))
                        file.write(reversed_vlinks)

                    print("Videos Extraction Done ✅\n")
                    end = time.time()
                    print(f"Done in {end - start}")
                    await m.reply_text(f"Batch {batch_id} ({batchidl[batch_id]}) extraction complete!") # Notify user per batch
                else:
                    await m.reply_text(f"Invalid Batch ID: {batch_id}")

        await m.reply_text("CareerWill Extraction Complete!")

    except Exception as e:
        await m.reply_text(f"Error during CareerWill extraction: {str(e)}")
        
        
        
        
        
        
bot.run()

