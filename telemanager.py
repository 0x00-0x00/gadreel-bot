import sys
import asyncio
import telepot
import re
import os
import time
from shemutils.logger import Logger
from shemutils.database import *
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open

cache_dir = "files"
log = Logger("TeleManager")
db = Database("teleManagerDB")

# Create table system
t1 = Table("CONVERSATIONS", {
    1: ('FROM_USER', TEXT),
    2: ('MESSAGE', TEXT),
    3: ('TIMESTAMP', TEXT)
    })
db.controller.execute(t1.create())

t2 = Table("ARQUIVOS", {
    1: ('FROM_USER', TEXT),
    2: ('FILE_ID', TEXT),
    3: ('FILE_NAME', TEXT),
    })
db.controller.execute(t2.create())


#  Create the data folder
if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)

#  Check if token arg is filled
if len(sys.argv) < 2:
    log.critical("Not enough arguments to run this bot.")
    log.info("Usage: {0} <TOKEN>".format(sys.argv[0]))
    sys.exit(1)
else:
    TOKEN = sys.argv[1]

storage_folders = {
        "photo": "photos" + os.sep,
        "document": "documents" + os.sep,
        "text": "data" + os.sep,
        "video": "videos" + os.sep
        }


def look_for_file(keyword):
    results = set()
    for root, dirc, files in os.walk(cache_dir):
        for file in files:
            if keyword in file:
                path = ''.join(os.path.join(root, file))
                results.add(path)
    return results

def search_file(txt):
    pattern = "(^procurar?|^buscar?|^search?|^pesquisar)\s+(?P<file>[\w\.]+)"
    m = re.match(pattern, txt)
    return look_for_file(m.groupdict())

class BotHandler(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(BotHandler, self).__init__(*args, **kwargs)
        self._count = 0

    @staticmethod
    def _recvd_from(message):
        first_name = message["from"]["first_name"]
        last_name = message["from"]["last_name"]
        username = " ".join([first_name, last_name])
        return first_name, last_name, username

    async def on_chat_message(self, message):
        self._count += 1
        content_type, chat_type, chat_id = telepot.glance(message)
        first_name, last_name, username = self._recvd_from(message)

        #  Code flow based on content_type
        #  Photos (.jpg, .png)
        if content_type == "photo":
            photo_id = message["photo"][0]["file_id"]
            insert_data = t2.insert_data([username, photo_id, photo_id])
            db.controller.execute(insert_data)
            db.save()
            await self.sender.sendMessage("Baixando imagem '{0}' ...".format(photo_id))

            if not os.path.exists(cache_dir + os.sep + photo_id):
                await self.bot.download_file(photo_id, cache_dir + os.sep + photo_id + ".jpg")

            await self.sender.sendMessage("Imagem '{0}' baixada com sucesso!".format(photo_id))


        #  Text data
        elif content_type == "text":
            text = message["text"]
            insert_data = t1.insert_data([username, text, str(time.time())])
            db.controller.execute(insert_data)
            db.save()
            files = search_file(text)
            if len(files) != 0:
                self.sender.sendMessage("Encontrei {0} arquivos com essa palavra.".format(len(files)))
            else:
                self.sender.sendMessage("Nenhum arquivo foi encontrado.")



        # Document (PDF, .DOCX)
        elif content_type == "document":
            document_name = message["document"]["file_name"]
            document_id = message["document"]["file_id"]
            insert_data = t2.insert_data([username, document_id, document_name])
            db.controller.execute(insert_data)
            db.save()

            await self.sender.sendMessage("Baixando arquivo {0} ...".format(document_name))

            if not os.path.exists(cache_dir + os.sep + document_name):
                await self.bot.download_file(document_id, cache_dir + os.sep + document_name)

            await self.sender.sendMessage("Arquivo '{0}' baixado com sucesso!".format(document_name))

        # Videos (.mp4, .mkv)
        elif content_type == "video":
            video_id = message["video"]["file_id"]
            video_name = message["video"]["file_name"]
            insert_data = t2.insert_data([username, video_id, video_name])
            db.controller.execute(insert_data)
            db.save()

            await self.sender.sendMessage("Baixando video {0}".format(video_name))

            if not os.path.exists(cache_dir + os.sep + video_name):
                await self.bot.download_file(video_id, cache_dir + os.sep + video_name)

            await self.sender.sendMessage("Video '{0}' baixado com sucesso!".format(video_name))


        else:
            # Send unknown type message
            await self.sender.sendMessage("Tipo de entrada de dados \
                    desconhecida!")


bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, BotHandler, timeout=60),
    ])

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop())
log.info("TeleManager bot has started.")
loop.run_forever()

