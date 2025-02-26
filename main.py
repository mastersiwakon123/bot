import discord
from discord.ext import commands
import datetime
import os 
from myserver import server_on
# Token ของคุณ


intents = discord.Intents.default()
intents.message_content = True

# สร้างคลาส bot
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is online!")

    # สร้าง Rich Presence
    activity = discord.Activity(
        type=discord.ActivityType.streaming,
        name="Meoaw Hub",  # เปลี่ยนได้
        url="https://www.youtube.com/watch?v=g88A3mmF3A0",  # เปลี่ยนได้
        details="Meoaw Hub",  # เปลี่ยนได้
        state="สถานะ: :green_circle: เปิดร้าน !",  # เปลี่ยนได้
        start=datetime.datetime.utcnow(),
    )
    
    await client.change_presence(activity=activity)

    # Rich Presence Assets (รูปภาพใหญ่และเล็ก)
    large_image_url = "https://cdn.discordapp.com/attachments/1090081082373840989/1098958590238281759/Untitled_design.png"
    small_image_url = "https://cdn.discordapp.com/attachments/1090081082373840989/1098959001510748201/1422-black-verify.gif"

    # ใช้ Discord Rich Presence Asset
    r = discord.Activity(
        type=discord.ActivityType.streaming,
        name="Meoaw Hub",
        details="Meoaw Hub",
        state="สถานะ: :green_circle: เปิดร้าน !",  # เปลี่ยนได้
        start=datetime.datetime.utcnow(),
        url="https://www.youtube.com/watch?v=g88A3mmF3A0",
    )
    
    # ตั้งค่าภาพใหญ่และเล็ก
    await client.change_presence(activity=r)

    # เพิ่มปุ่ม (จำกัดได้ 2 ปุ่ม)
    # Discord ไม่รองรับการเพิ่มปุ่มแบบ JS แต่สามารถใส่ลิ้งค์ใน Rich Presence ได้
    # ปุ่ม Discord
    # ปุ่มใน Python API ไม่รองรับ แต่สามารถเพิ่มปุ่มเพิ่มเติมผ่านการแสดงสถานะอื่นๆ
    # กรณีนี้เราจะใช้การแสดงผลใน Rich Presence แทนการเพิ่มปุ่มจริงๆ


server_on()


client.run(os.getenv('TOKEN'))  # ห้ามเปลี่ยน
