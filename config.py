import json
with open("config.json", "r") as f:
    config = json.load(f)

BOT_TOKEN = config.get("BOT_TOKEN", None)
api_hash= config.get("api_hash", None)
api_id = config.get("api_id", None)
from pyrogram import filters
diyanet = config.get("diyanet", None)
kuran_sure = 'https://kuran.diyanet.gov.tr/Tefsir/'
kuran_api = 'https://api.acikkuran.com/authors'
ezan_vakitleri = config.get("ezan_vakitleri", None)


bot_owner = config.get("bot_owner", None)
log_grup = config.get("log_grup", None)
admin_grup = config.get("admin_grup", None)
admins = config.get("admins", None)
admin_filter = filters.create(lambda _, __, message: message.from_user is not None and message.from_user.id in admins)

ezanlar = ['CQACAgIAAxkBAAEBIUxkLOa9-Uz5P6LL4xu_W9sxkR3N4gACPA0AAjbvQUjejXzzVP3rKB4E', 'CQACAgIAAxkBAAEBIU5kLObVa0o2Qy3c0DkQF9ZLR19W-AAC6goAAu73WEiHdIjXcHtl7B4E',
           'CQACAgIAAxkBAAEBIS9kLOJo42g6i1u5Fdc5qnasQ8PR3QACQAUAAlk0gUjdAAEwcRhRuGYeBA']