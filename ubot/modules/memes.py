from asyncio import sleep
from random import choice

from ubot import ldr

emoji = list("😂😝🤪🤩😤🥵🤯🥶😱🤔😩🙄💀👻🤡😹👀👁👌💦🔥🌚🌝🌞🔫💯")
b_emoji = "🅱️"
a_emoji = "🅰️"
i_emoji = "ℹ️"

filler = "Give me some text to fuck it up!"

owo_faces = "owo uwu owu uwo u-u o-o OwO UwU @-@ ;-; ;_; ._. (._.) (o-o) ('._.) (｡◕‿‿◕｡)" \
    " (｡◕‿◕｡) (─‿‿─) ◔⌣◔ ◉_◉".split(sep=" ")

vibe_checks = "Shitting pants…|Unshitting pants…|Checking for good vibes…|Checking for bad vibes…|" \
    "Analyzing wiggly air…|Sniffing for poopy pants…|Eating a Snickers…|Ripping paper with an eraser…|" \
    "Vibing…|Connecting to dial-up…|Writing stupid quotes…|Consuming carbohydrates…|Hydrating…|" \
    "Feeding the wolf…|OwO what's this?|Eating 3 week old pancakes…|Doing quick maths…|Squatting…|" \
    "Thinking real hard…|Making slime in science class…|Orang man bad…|Browsing 4chan…|Breathing…|" \
    "Uh oh, stinky…|Splitting strings…|Breaking pencils…|Yeeting…|Releasing Half-Life 3…|Failing…|" \
    "He do look kinda chill doe…|Cats are liquid…|Stay hydrated…|Using random.choice()…|Licking 9-volt batteries…|" \
    "Building vibecheck.exe…|Building vibecheck.so…|Flashing custom ROMs…|Suffocating my demons…|" \
    "Reticulating splines…|Drinking maple syrup…|Failing at life…|Calibrating battery…|Foraging…|" \
    "Show me how to lie, you're getting better all the time…|Becoming Pneuma…|Contracting AIDS…|" \
    "Checkra1n…|Checkm8 motherfucker…|Exploiting your denial…|Checking the door lights…|Flashing Bonnie…|" \
    "Opening loot-boxes…|Vibing…|Updating to Python 3.8.0…|Having information leading to the arrest of Hil-…|" \
    "Epstein didn't kill himself…|Cracking open the boys with a cold hatchet…|I'm gonna be sick…|" \
    "I can feel it in my blood and in my bones…|Writing commit messages…|Creating redsn0w…".split(sep="|")

zal_chars = " ̷̡̛̮͇̝͉̫̭͈͗͂̎͌̒̉̋́͜ ̵̠͕͍̩̟͚͍̞̳̌́̀̑̐̇̎̚͝ ̸̻̠̮̬̻͇͈̮̯̋̄͛̊͋̐̇͝͠ ̵̧̟͎͈̪̜̫̪͖̎͛̀͋͗́̍̊͠ ̵͍͉̟͕͇͎̖̹̔͌̊̏̌̽́̈́͊ͅ ̷̥͚̼̬̦͓͇̗͕͊̏͂͆̈̀̚͘̚ ̵̢̨̗̝̳͉̱̦͖̔̾͒͊͒̎̂̎͝ ̵̞̜̭̦̖̺͉̞̃͂͋̒̋͂̈́͘̕͜ ̶̢̢͇̲̥̗̟̏͛̇̏̊̑̌̔̚ͅͅ ̷̮͖͚̦̦̞̱̠̰̍̆̐͆͆͆̈̌́ ̶̲͚̪̪̪͍̹̜̬͊̆͋̄͒̾͆͝͝ ̴̨̛͍͖͎̞͍̞͕̟͑͊̉͗͑͆͘̕ ̶͕̪̞̲̘̬͖̙̞̽͌͗̽̒͋̾̍̀ ̵̨̧̡̧̖͔̞̠̝̌̂̐̉̊̈́́̑̓ ̶̛̱̼̗̱̙͖̳̬͇̽̈̀̀̎̋͌͝ ̷̧̺͈̫̖̖͈̱͎͋͌̆̈̃̐́̀̈".replace(" ", "")


@ldr.add("cp")
async def copypasta(event):
    text_arg = await ldr.get_text(event, default=filler)

    text_arg = await shitpostify(text_arg)
    text_arg = await mockify(text_arg)
    text_arg = await emojify(text_arg)
    cp_text = await vaporize(text_arg)

    await event.edit(cp_text)


@ldr.add("mock")
async def mock(event):
    text_arg = await ldr.get_text(event, default=filler)

    mock_text = await mockify(text_arg)

    await event.edit(mock_text)


@ldr.add("vap")
async def vapor(event):
    text_arg = await ldr.get_text(event, default=filler)

    vapor_text = await vaporize(text_arg)

    await event.edit(vapor_text)


@ldr.add("pop")
async def popifycmd(event):
    text_arg = await ldr.get_text(event, default=filler)

    pop_text = await popify(text_arg)

    await event.edit(pop_text)


@ldr.add("cheem")
async def cheemifycmd(event):
    text_arg = await ldr.get_text(event, default=filler)

    cheems_text = await cheemify(text_arg)

    await event.edit(cheems_text)


@ldr.add("zal")
async def zalgo(event):
    text_arg = await ldr.get_text(event, default=filler)

    zalgo_text = await zalgofy(text_arg)

    await event.edit(zalgo_text)


@ldr.add("owo")
async def owo(event):
    text_arg = await ldr.get_text(event, default=filler)

    owo_text = await owoify(text_arg)

    await event.edit(owo_text)


@ldr.add("yoda")
async def yodafy(event):
    text_arg = await ldr.get_text(event, default=filler)

    async with ldr.aioclient.get("http://yoda-api.appspot.com/api/v1/yodish", params={"text": text_arg}) as response:
        if response.status == 200:
            yoda_text = (await response.json())["yodish"]
        else:
            await event.edit(f"An error occurred: **{response.status}**")
            return

    await event.edit(yoda_text)


@ldr.add("vibecheck")
async def vibecheck(event):
    if event.is_reply:
        await event.edit("`Performing vibe check…`")
    else:
        await event.edit("`Performing self vibe check…`")

    for _ in range(7):
        await sleep(4)
        try:
            await event.edit(f"`{choice(vibe_checks)}`")
        except:
            pass

    await sleep(4)
    if choice([True, False]):
        await event.edit("`Vibe check passed!`")
    else:
        await event.edit("`Vibe check failed!`")


async def shitpostify(text):
    text = text.replace("dick", "peepee")
    text = text.replace("ck", "cc")
    text = text.replace("lol", "honk honk")
    text = text.replace("though", "tho")
    text = text.replace("cat", "pussy")
    text = text.replace("dark", "dank")

    return text


async def popify(text):
    text = text.replace(" ", "!_")

    return text


async def cheemify(text):
    text = text.replace("ese", "ms")
    text = text.replace("se", "mse")
    text = text.replace("ck", "mk")
    text = text.replace("ake", "amke")
    text = text.replace("as", "ams")
    text = text.replace("n", "m")
    text = text.replace("ab", "amb")
    text = text.replace("lp", "lmp")
    text = text.replace("ke", "mke")
    text = text.replace("ec", "emc")
    text = text.replace("ig", "img")
    text = text.replace("ob", "omb")
    text = text.replace("pep", "pemp")
    text = text.replace("pop", "pomp")
    text = text.replace("rib", "rimb")

    return text


async def mockify(text):
    mock_text = ""

    for letter in text:
        if choice([True, False]):
            mock_text += letter.lower()
        else:
            mock_text += letter.upper()

    return mock_text


async def emojify(text):
    text = text.replace("ab", "🆎")
    text = text.replace("cl", "🆑")
    text = text.replace("b", "🅱️")
    text = text.replace("a", "🅰️")
    text = text.replace("i", "ℹ️")
    text = text.replace("AB", "🆎")
    text = text.replace("CL", "🆑")
    text = text.replace("B", "🅱️")
    text = text.replace("A", "🅰️")
    text = text.replace("I", "ℹ️")

    emoji_text = ""

    for letter in text:
        if letter == " ":
            emoji_text += choice(emoji)
        else:
            emoji_text += letter

    return emoji_text


async def vaporize(text):
    vapor_text = ""
    char_distance = 65248

    for letter in text:
        ord_letter = ord(letter)
        if ord('!') <= ord_letter <= ord('~'):
            letter = chr(ord_letter + char_distance)
        vapor_text += letter

    return vapor_text


async def owoify(text):
    text = text.replace("r", "w")
    text = text.replace("R", "W")
    text = text.replace("n", "ny")
    text = text.replace("N", "NY")
    text = text.replace("ll", "w")
    text = text.replace("LL", "W")
    text = text.replace("l", "w")
    text = text.replace("L", "W")

    text += f" {choice(owo_faces)}"

    return text


async def zalgofy(text):
    zalgo_text = ""

    for letter in text:
        if letter == " ":
            zalgo_text += letter
            continue

        letter += choice(zal_chars)
        letter += choice(zal_chars)
        letter += choice(zal_chars)
        zalgo_text += letter

    return zalgo_text
