from io import BytesIO
from PIL import Image

from ubot import ldr
from ubot.fixes.fast_telethon import upload_file

@ldr.add("cunny", nsfw=True, help="[cunny](https://t.me/cunnystash) reply to a file to cast homu's majik", extra=-1001296215434, userlocking=True)

async def post_to_cult(event):
    # Allowed users
    ids = [(1153919309), (268188807)]

    if event.sender_id not in ids:
        await event.reply(
            "you don't have the permission to use this command \nCheck [LewdCults](https://t.me/lewdcults) for more information.")
        return

        # What are you going to post if you aren't replying to a file
    if event.is_reply:
        msg = (await event.get_reply_message())

        try:
            await event.delete()
        except:
            pass

        # I don't even know the fuck is this, won't waste time on a "cult" which advertises Russian CP
        try:
            mtype = msg.media.document
        except:
            mtype = "other"

        if mtype != "other":
            msg.text = ""
            msg.raw_text = ""
            sauce = await event.client.send_message(-1001380453551, msg)

            # Resize the image and stuff because Telegram can't handle this, shit devs
            image_io = BytesIO()
            await event.client.download_file(msg, image_io)
            image_png = Image.open(image_io)
            image_png.thumbnail((1920, 1280))
            image_new_io = BytesIO()
            image_png.save(image_new_io, "PNG")
            image_new_io.name = "homu.png"
            image_new_io.seek(0)

            try:
                await msg.delete()
            except:
                pass

            shit = await upload_file(event.client, image_new_io)
            msg = await event.client.send_file(event.extra, shit, force_document=False,
                                               caption=f"{event.args}\n[file](https://t.me/cunnyjuice/{sauce.id})")
            #here goes the actual channel I think?
            await event.client.forward_messages(-1001306233916, msg)
        else:
            await event.reply("ass")
            return
    else:
        await event.reply("ass")
        return
