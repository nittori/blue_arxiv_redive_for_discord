#https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f
# インストールした discord.py を読み込む
import discord
import os 
import get_paper

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ.get("ACCESS_TOKEN")

# 接続に必要なオブジェクトを生成
client = discord.Client()

CHANNEL_ID = int(os.environ.get("channel_id")) # 任意のチャンネルID:int

# 任意のチャンネルで挨拶する非同期関数を定義
async def post_message(message):
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(message)

# bot起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    papers = get_paper.get_paper()
    
    if len(papers) == 0:
        print("Today has no paper ...")
    else:
        for paper in papers:
            message = f"author : {paper['author']}\n"+\
                      f"publish_date : {paper['published']}\n"+\
                      f"title : {paper['title']}\n"+\
                      f"url : {paper['url']}\n"
            print(message)
            await post_message(message) # 非同期関数を実行
    await client.logout()
client.run(TOKEN)