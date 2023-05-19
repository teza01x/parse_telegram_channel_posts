from telethon import TelegramClient, events, sync


api_id = 0 # your api id
api_hash = '' # your api hash
channel_id = 0 # private / non

# Create an instance of TelegramClient
client = TelegramClient('session_name', api_id, api_hash)


async def last_msg_id():
    channel = await client.get_entity(channel_id)
    last_msg = []
    async for message in client.iter_messages(channel, reverse=False):
        if len(last_msg) == 0:
            last_msg.append((message.id, message.text))
            return last_msg[0]


def check_last_msg(client):
    with client:
        last_m = client.loop.run_until_complete(last_msg_id())

    while True:
        with client:
            new_m = client.loop.run_until_complete(last_msg_id())
        if new_m[0] > last_m[0]:
            print(new_m[1])
            break


while True:
    check_last_msg(client)

