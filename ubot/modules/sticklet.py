# SPDX-License-Identifier: GPL-2.0-or-later

import io
import textwrap

from PIL import Image, ImageDraw, ImageFont

from ubot.micro_bot import micro_bot

ldr = micro_bot.loader


@ldr.add(pattern="slet")
async def sticklet(event):
    sticktext = event.args

    if not sticktext:
        await event.edit("`I need text to sticklet!`")
        return

    await event.delete()

    sticktext = textwrap.wrap(sticktext, width=20)
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    font = ImageFont.truetype("ubot/resources/RobotoMono-Regular.ttf", size=fontsize)

    while True:
        current_size = draw.multiline_textsize(sticktext, font=font, stroke_width=8, spacing=-10)

        if current_size[0] > 512 or current_size[1] > 512:
            fontsize -= 3
            font = ImageFont.truetype("ubot/resources/RobotoMono-Regular.ttf", size=fontsize)
        else:
            break

    width, height = draw.multiline_textsize(sticktext, font=font, stroke_width=8, spacing=-10)
    image = Image.new("RGBA", (512, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.multiline_text(((512-width)/2, -10), sticktext, font=font, fill="white", stroke_width=8, stroke_fill="black", spacing=-10)

    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    await event.client.send_file(event.chat_id, image_stream)
