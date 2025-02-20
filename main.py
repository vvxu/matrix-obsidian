import simplematrixbotlib as botlib
from utils.handle_couchdb import CouchDBManager
from datetime import datetime
from config import *

# 建立数据库连接
server_url = f'https://{db_user}:{db_password}@{db_url}'
manager = CouchDBManager(server_url, db_name)

# 建立matrix连接
creds = botlib.Creds(matrix_url, matrix_user, matrix_pwd)
bot = botlib.Bot(creds)

# 用于记录工作信息
@bot.listener.on_message_event
async def worker(room, message):
    match = botlib.MessageMatch(room, message, bot)

    if message.sender == sender_id and match.is_not_from_this_bot() and match.command(Prefix):
    	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    	write_data = f"{pre_data} {current_time} {' '.join(arg for arg in match.args())}\n"
    	result = manager.add_document(write_data, parent_doc_id)
    	message = "主人，我已经记录好啦！" if result else "主人，记录出错啦！赶紧找找原因！"
    	await bot.api.send_text_message(room.room_id, message)

bot.run()