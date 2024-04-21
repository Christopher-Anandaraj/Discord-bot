import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import asyncio
keep_alive()


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), activity = discord.Game(name="with Welt's BLACK hole"))


@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def h(ctx):
    await ctx.send("List of commands available:\n\n hello\n character")

class Character:
    def __init__(self, name, path, damage_type, rarity, hp=None, attack=None, defense=None, speed=None, energy_cost=None, image_url=None):
        self.name = name
        self.path = path
        self.damage_type = damage_type
        self.rarity = rarity
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.energy_cost = energy_cost
        self.image_url = image_url

characters = {
    "acheron": Character("Acheron", "Nihility", "Lightning", "5-Star", 1125, 698, 436, 101, None, "https://s1.zerochan.net/Acheron.600.4141143.jpg"),
    "argenti": Character("Argenti", "Erudition", "Physical", "5-Star", 1047, 737, 363, 103, "90 or 180", "https://static.zerochan.net/Argenti.full.4082846.jpg"),
    "arlan": Character("Arlan", "Destruction", "Lightning", "4-Star", 1199, 599, 330, 102, 110, "https://staticg.sportskeeda.com/editor/2023/05/94d03-16852586050211-1920.jpg"),
    "asta": Character("Asta", "Harmony", "Fire", "4-Star", 1023, 511, 463, 106, 120,"https://ih1.redbubble.net/image.5086393623.8610/flat,750x,075,f-pad,750x1000,f8f8f8.jpg"),
    "aventurine": Character("Aventurine", "Preservation", "Imaginary", "5-Star", 1203, 446, 654, 106, 110,"https://pbs.twimg.com/media/GErnMByaQAA1dXL.jpg"),
    "bailu": Character("Bailu", "Abundance", "Lightning", "5-Star", 1319, 562, 485, 98, 100,"https://www.pockettactics.com/wp-content/sites/pockettactics/2023/01/honkai-star-rail-bailu-1.jpeg"),
    "blackswan": Character("Black Swan", "Nihility", "Wind", "5-Star", 1086, 659, 485, 102, 120,"https://admin.esports.gg/wp-content/uploads/2024/02/Black-Swan-release-date.jpg"),
    "blade": Character("Blade", "Destruction", "Wind", "5-Star", 1358, 543, 485, 97, 130,"https://i.pinimg.com/736x/20/97/f6/2097f67e1c2dc46c893d34676f5b5e85.jpg"),
    "bronya": Character("Bronya", "Harmony", "Wind", "5-Star", 1241, 582, 533, 99, 120,"https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/06/beat-bronya-quest-boss-honkai-star-rail.jpg"),
    "clara": Character("Clara", "Destruction", "Physical", "5-Star", 1319, 737, 485, 90, 110, "https://www.korosenai.es/wp-content/uploads/2023/05/clara-honkai-star-rail.jpg.webp"),
    "danheng": Character("Dan Heng", "Hunt", "Wind", "4-Star", 882, 546, 396, 110, 100, "https://ih1.redbubble.net/image.5086323272.6793/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"),
    "drratio": Character("Dr.Ratio", "Hunt", "Imaginary", "5-Star", 1047, 776, 460, 103, 140,"https://d1lss44hh2trtw.cloudfront.net/assets/article/2024/01/17/dr-ratio_feature.jpg" ),
    "fuxuan": Character("Fu Xuan", "Preservation", "Quantum", "5-Star", 1474, 465, 606, 100, 135, "https://www.escapistmagazine.com/wp-content/uploads/2023/10/Fu-Xuan-Teams.jpeg?fit=1200%2C675"),
    "gallagher": Character("Gallagher", "Abundance", "Fire", "4-Star", 1305, 529, 441, 98, 110, "https://assetsio.gnwcdn.com/Honkai-Star-Rail-Gallagher-materials%2C-kit%2C-and-Eidolons-cover.jpg?width=1200&height=1200&fit=crop&quality=100&format=png&enable=upscale&auto=webp"),
    "gepard": Character("Gepard", "Preservation", "Ice", "5-Star", 1397, 543, 654, 92, 100, "https://honkailab.com/wp-content/uploads/2023/03/Moment-of-Victory_honkailab_genshinlab2.webp"),
    "guinaifen": Character("Guinaifen", "Nihility", "Fire", "4-Star", 882, 582, 441, 106, 120, "https://dotesports.com/wp-content/uploads/2023/06/image_2023-06-26_174512394.png"),
    "hanya": Character("Hanya", "Harmony", "Physical", "4-Star", 917, 564, 352, 110, 140, "https://techraptor.net/sites/default/files/styles/image_header/public/2023-09/honkai-star-rail-hanya-hero.jpg?itok=fAbq-Gs1"),
    "herta": Character("Herta", "Erudition", "Ice", "4-Star", 952, 582, 396, 100, 110, "https://static.wikia.nocookie.net/houkai-star-rail/images/8/8c/Character_Herta_Splash_Art.png/revision/latest?cb=20230216231220" ),
    "himeko": Character("Himeko", "Erudition", "Fire", "5-Star", 1047, 756, 436, 96, 120, "https://www.escapistmagazine.com/wp-content/uploads/2023/10/Himeko-Build.jpeg"),
    "hook": Character("Hook", "Destruction", "Fire", "4-Star", 1340, 617, 352, 94, 120, "https://www.pcgamesn.com/wp-content/sites/pcgamesn/2023/05/honkai-star-rail-best-hook-build.jpg"),
    "huohuo": Character("Huohuo", "Abundance", "Wind", "5-Star", 1358, 601, 509, 98, 140, "https://images-ng.pixai.art/images/orig/10b6f736-cba4-4754-bf51-580e6351ed1a"),
    "imbibitorlunae": Character("Imbibitor Lunae", "Destruction", "Imaginary", "5-Star", 1241, 698, 363, 102, 140, "https://www.pcgamesn.com/wp-content/sites/pcgamesn/2023/07/honkai-star-rail-imbibitor-lunae-dan-heng.jpg"),
    "jingyuan": Character("Jing Yuan", "Erudition", "Lightning", "5-Star", 1164, 698, 485, 99, 130,"https://s.yimg.com/ny/api/res/1.2/uJVkYf8E3jP0FJbKqf2FvA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD02NzU-/https://s.yimg.com/os/creatr-uploaded-images/2023-05/a25ce0e0-f46a-11ed-bbf9-378d9906cf8d" ),
    "jingliu": Character("Jingliu", "Destruction", "Ice", "5-Star", 1435, 679, 485, 96, 140, "https://assetsio.gnwcdn.com/Honkai-Star-Rail-Jingliu-Eidolons-1.jpg?width=1200&height=600&fit=crop&enable=upscale&auto=webp"),
    "kafka": Character("Kafka", "Nihility", "Lightning", "5-Star", 1086, 679, 485, 100, 120, "https://editors.dexerto.com/wp-content/uploads/2023/07/08/Kafka-Honkai-Star-Rail-guide.jpg"),
    "luka": Character("Luka", "Nihility", "Physical", "4-Star", 917, 582, 485, 103, 130, "https://staticg.sportskeeda.com/editor/2023/05/85947-16850103183733-1920.jpg"),
    "luocha": Character("Luocha", "Abundance", "Imaginary", "5-Star", 1280, 756, 363, 101, 100, "https://www.gamespace.com/wp-content/uploads/2023/06/Honkai-Star-Rail-Learn-More-About-Luocha-Yukong.png"),
    "lynx": Character("Lynx", "Abundance", "Quantum", "4-Star", 1058, 493, 551, 100, 100, "https://editors.dexerto.com/wp-content/uploads/2023/06/27/Honkai-Star-Rail-Lynx-abilities.jpg"),
    "march7th": Character("March 7th", "Preservation", "Ice", "4-Star", 1058, 511, 573, 101, 120, "https://assetsio.gnwcdn.com/Honkai-Star-Rail-March-7th-Ult-1.jpg?width=1200&height=630&fit=crop&enable=upscale&auto=webp"),
    "misha": Character("Misha", "Destruction", "Ice", "4-Star", 1270, 599, 396, 96, 100, "https://editors.dexerto.com/wp-content/uploads/2023/12/26/Misha-ascension-materials-Honkai-Star-Rail.jpg"),
    "natasha": Character("Natasha", "Abundance", "Physical", "4-Star", 1164, 476, 507, 98, 90, "https://www.pockettactics.com/wp-content/sites/pockettactics/2023/01/honkai-star-rail-natasha-1.jpeg"),
    "pela": Character("Pela", "Nihility", "Ice", "4-Star", 987, 546, 463, 105, 110, "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/04/honkai-star-rail_-pela.jpg"),
    "qingque": Character("Qingque", "Erudition", "Quantum", "4-Star", 1023, 652, 441, 98, 140, "https://www.pcgamesn.com/wp-content/sites/pcgamesn/2023/06/honkai-star-rail-qingque-build.jpg"),
    "ruanmei": Character("Ruan Mei", "Harmony", "Ice", "5-Star", 1086, 659, 485, 104, 130, "https://www.escapistmagazine.com/wp-content/uploads/2024/01/ruan-mei-honkai-star-rail.jpg?fit=1428%2C857"),
    "sampo": Character("Sampo", "Nihility", "Wind", "4-Star", 1023, 617, 396, 102, 120, "https://i.redd.it/fellas-how-we-feeling-about-sampo-from-hsr-v0-3irq2f8t0seb1.jpg?width=1000&format=pjpg&auto=webp&s=a64f59e562e8c30eedeafc4b74cf1d264661600b"),
    "seele": Character("Seele", "Hunt", "Quantum", "5-Star", 931, 640, 363, 115, 120, "https://static.zerochan.net/Seele.%28Honkai.Star.Rail%29.full.3949005.png"),
    "serval": Character("Serval", "Erudition", "Lightning", "4-Star", 917, 652, 374, 104, 100, "https://oyster.ignimgs.com/mediawiki/apis.ign.com/honkai-star-rail/8/8d/Serval_Screenshot.png?width=1280"),
    "silverwolf": Character("Silver Wolf", "Nihility", "Quantum", "5-Star", 1047, 640, 460, 107, 110, "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/10/honkai-star-rail-leak-teases-silver-wolf-re-run.jpg"),
    "sparkle": Character("Sparkle", "Harmony", "Quantum", "5-Star", 1397, 523, 485, 101, 110, "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/02/honkai-star-rail-sparkle-trailer-screenshot.jpg"),
    "sushang": Character("Sushang", "Hunt", "Physical", "4-Star", 917, 564, 418, 107, 120, "https://i.redd.it/py22tjc5yd8b1.jpg"),
    "tingyun": Character("Tingyun", "Harmony", "Lightning", "4-Star", 846, 529, 396, 112, 130, "https://www.pcgamesn.com/wp-content/sites/pcgamesn/2023/05/honkai-star-rail-tingyun-build.jpg"),
    "topaz": Character("Topaz & Numby", "Hunt", "Fire", "5-Star", 931, 620, 412, 110, 130, "https://www.gamespot.com/a/uploads/original/1624/16240817/4216264-topaz-speech.png"),
    "trailblazerf": Character("Trailblazer (Fire)", "Preservation", "Fire", "5-Star", 1241, 601, 606, 95, 120, "https://static1.srcdn.com/wordpress/wp-content/uploads/2023/04/honkai-star-rail-raise-trailblaze-level-guide.jpg"),
    "trailblazerp": Character("Trailblazer (Physical)", "Destruction", "Physical", "5-Star", 1203, 620, 460, 100, 120, "https://www.pcgamesn.com/wp-content/sites/pcgamesn/2023/05/HonkaiStarRail-Guide-TrailblazerBuild-Header-550x309.jpg"),
    "welt": Character("Welt", "Nihility", "Imaginary", "5-Star", 1125, 620, 509, 102, 120, "https://imgix.bustle.com/uploads/image/2023/5/31/14daf62e-6fad-4be5-ab54-d2e1cd996b8f-welt-aura.jpg"),
    "xueyi": Character("Xueyi", "Destruction", "Quantum", "4-Star", 1058, 599, 396, 103, 120, "https://www.pockettactics.com/wp-content/sites/pockettactics/2023/11/Honkai-Star-Rail-Xueyi.jpg"),
    "yanqing": Character("Yanqing", "Hunt", "Ice", "5-Star", 892, 679, 412, 109, 140, "https://www.siliconera.com/wp-content/uploads/2023/06/yanqing-companion-quest-06302023.png"),
    "yukong": Character("Yukong", "Harmony", "Imaginary", "4-Star", 917, 599, 374, 107, 130, "https://www.pockettactics.com/wp-content/sites/pockettactics/2023/06/honkai-star-rail-yukong-4.jpg"),
}
Bestinslots = {
    "Acheron": ["Along the Passing Shore", "Incessant Rain", "Good Night Sleep Well"],
    "Argenti": ["An Instant Before I Gaze", "Night on the Milky Way", "Geniuses' Repose"],
    "Arlan": ["On the Fall of an Aeon", "The Unreachable Side", "Under the Blue Sky"],
    "Asta": ["Meshing Cogs", "", ""],
    "Aventurine": ["Inherently Unjust Destiny", "Moment of Victory", "Concert for Two"],
    "Bailu": ["Night of Fright", "Time Waits for No One", "Post-Op Conversation"],
    "Black Swan": ["Reforged Remembrance", "Patience Is All You Need", "Eyes of the Prey"],
    "Blade": ["The Unreachable Side", "", "A Secret Vow"],
    "Bronya": ["But the Battle Isn't Over", "Past and Future", "Planetary Rendezvous"],
    "Clara": ["Brighter Than the Sun", "Something Irreplaceable", "Under the Blue Sky"],
    "Dan Heng": ["In the Night", "Cruising in the Stellar Sea", "Only Silence Remains"],
    "Imbibitor Lunae": ["Brighter Than the Sun", "On the Fall of an Aeon", "Under the Blue Sky"],
    "Dr. Ratio": ["Baptism of Pure Thought", "Worrisome, Blissful", "Only Silence Remains"],
    "Fu Xuan": ["She Already Shut Her Eyes", "Moment of Victory", "Landau's Choice"],
    "Gallagher": ["Night of Fright", "Echoes of the Coffin", "Perfect Timing"],
    "Gepard": ["Moment of Victory", "", "Landau's Choice"],
    "Guinaifen": ["Good Night and Sleep Well", "Eyes of the Prey", ""],
    "Hanya": ["Memories of the Past", "", "Meshing Cogs"],
    "Herta": ["Night on the Milky Way", "", "Geniuses' Repose"],
    "Himeko": ["Night on the Milky Way", "", "Geniuses' Repose"],
    "Hook": ["On the Fall of an Aeon", "Under the Blue Sky", "The Moles Welcome You"],
    "Huohuo": ["Night of Fright", "Shared Feeling", "Post-Op Conversation"],
    "Jing Yuan": ["Before Dawn", "Night on the Milky Way", "Geniuses' Repose"],
    "Jingliu": ["I Shall Be My Own Sword", "On the Fall of an Aeon", "Under the Blue Sky"],
    "Kafka": ["Patience Is All You Need", "Good Night Sleep Well", "Eyes of the Prey"],
    "Luka": ["Good Night and Sleep Well", "Patience Is All You Need", "Eyes of the Prey"],
    "Luocha": ["Echoes of the Coffin", "Night of Fright", "Perfect Timing"],
    "Lynx": ["Night of Fright", "Time Waits for No One", "Post-Op Conversation"],
    "March 7th": ["Moment of Victory", "She Already Shut Her Eyes", "Landau's Choice"],
    "Misha": ["On the Fall of an Aeon", "", "The Moles Welcome You"],
    "Natasha": ["Night of Fright", "Time Waits for No One", "Post-Op Conversation"],
    "Pela": ["Resolution Shines As Pearls of Sweat", "", ""],
    "Qingque": ["Night on the Milky Way", "", "Geniuses' Repose"],
    "Ruan Mei": ["Past Self in Mirror", "Memories of the Past", "Meshing Cogs"],
    "Sampo": ["Good Night and Sleep Well", "Eyes of the Prey", "It's Showtime"],
    "Seele": ["In the Night", "Only Silence Remains", "Cruising in the Stellar Sea"],
    "Serval": ["Night on the Milky Way", "", "Geniuses' Repose"],
    "Silver Wolf": ["Resolution Shines As Pearls of Sweat", "Before the Tutorial Starts", "Incessant Rain"],
    "Sparkle": ["Earthly Escapade", "But the Battle Isn't Over", "Past and Future"],
    "Sushang": ["In the Night", "Swordplay", "Cruising in the Stellar Sea"],
    "Tingyun": ["Dance! Dance! Dance!", "", "Meshing Cogs"],
    "Topaz & Numby": ["Worrisome, Blissful", "Only Silence Remains", "Cruising in the Stellar Sea"],
    "Trailblazer (Fire)": ["Moment of Victory", "Landau's Choice", "We Are Wildfire"],
    "Trailblazer (Physical)": ["On the Fall of an Aeon", "Under the Blue Sky", "The Moles Welcome You"],
    "Welt": ["Incessant Rain", "Good Night Sleep Well", "It's Showtime"],
    "Xueyi": ["On the Fall of an Aeon", "The Moles Welcome You", "Under the Blue Sky"],
    "Yanqing": ["In the Night", "Only Silence Remains", "Only Silence Remains"],
    "Yukong": ["Planetary Rendezvous", "Memories of the Past", "But the Battle Isn't Over"]
}

@bot.command(name="character")
async def character(ctx, *args):
    if not args:
        await ctx.send("Please provide a character name.")
        return   
    name = " ".join(args).strip()
    if name.lower() in characters:
        character_info = characters[name.lower()]
        if character_info.damage_type == "Fire":
            type_color = discord.Color.red()
        elif character_info.damage_type == "Imaginary":
            type_color = discord.Color.yellow()
        elif character_info.damage_type == "Physical":
            type_color = discord.Color.light_grey()
        elif character_info.damage_type == "Lightning":
            type_color = discord.Color.purple()
        elif character_info.damage_type == "Quantum":
            type_color = discord.Color.blurple()
        elif character_info.damage_type == "Ice":
            type_color = discord.Color.blue()
        elif character_info.damage_type == "Wind":
            type_color = discord.Color.green()
        global cembed
        cembed = discord.Embed(title=character_info.name, description="\n\n", color=type_color)
        cembed.set_image(url=character_info.image_url)
        cembed.add_field(name="Path", value=character_info.path, inline=False)
        cembed.add_field(name="Damage Type", value=character_info.damage_type, inline=False)
        cembed.add_field(name="HP", value=character_info.hp, inline=False)
        cembed.add_field(name="Attack", value=character_info.attack, inline=False)
        cembed.add_field(name="Defense", value=character_info.defense, inline=False)
        cembed.add_field(name="Speed", value=character_info.speed, inline=False)
        cembed.add_field(name="Energy Cost", value=character_info.energy_cost, inline=False)       
        bis_embed = await best_in_slots(ctx, name)
        
        message = await ctx.send(embed=cembed)
        await message.add_reaction("⚔️")  # Add reaction for Best in Slot
    else:
        await ctx.send("Character not found, maybe try !search first?")

async def best_in_slots(ctx, name):
    if name in Bestinslots:
        slots = Bestinslots[name]
        embed = discord.Embed(title=f"Best in Slots for {name}", color=discord.Color.blurple())
        for i, slot in enumerate(slots, start=1):
            if i == 1:
                field_name = "BIS"
            elif i == 2:
                field_name = "BIS 2"
            elif i == 3:
                field_name = "F2P option"
            else:
                None
            embed.add_field(name=field_name, value=slot if slot else None, inline=True)
        return embed
    else:
        return None


@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:  # Ignore reactions from bots
        return
    if reaction.emoji == "⚔️":
        message = reaction.message
        character_name = message.embeds[0].title  # Get the character name from the embed title
        bis_embed = await best_in_slots(reaction.message.channel, character_name)
        await message.edit(embed=bis_embed)

@bot.event
async def on_reaction_remove(reaction, user):
    if user.bot:  # Ignore reactions from bots
        return
    if reaction.emoji == "⚔️":
        message = reaction.message     
        await message.edit(embed=cembed)



@bot.command()
async def search(ctx):
    response = ""
    await ctx.send("Enter the letter you want to search Characters for:")
    while True:
        try:
            search_letter = await bot.wait_for("message", check=lambda message: message.author == ctx.author and message.channel == ctx.channel, timeout=7)
            if search_letter == "kill":
                break
            search_letter = search_letter.content.lower()
            matched_characters = [char for char in characters if char.lower().startswith(search_letter)]
            if matched_characters:
                for lc in matched_characters:
                    response += f"- {lc}\n"
                embed = discord.Embed(title=f"Matched characters starting with '{search_letter}'", color=discord.Color.dark_gray())  # Fixed color argument
                embed.add_field(name="Result", value=response, inline=False)
                await ctx.send(embed=embed)
                response = ""
            else:
                await ctx.send(f"No characters found with names starting with '{search_letter}'. Please try again.")
        except asyncio.TimeoutError:
            await ctx.send("Search has ended.")
            break


class Lightcone:
    def __init__(self, lcname, lcrarity, lcpath, lchp, lcattack, lcdefense, lcdescription=None):
        self.lcname = lcname
        self.lcrarity = lcrarity
        self.lcpath = lcpath
        self.lchp = lchp
        self.lcattack = lcattack
        self.lcdefense = lcdefense
        self.lcdescription = lcdescription

Lightcones = {
"adversarial": Lightcone("Adversarial", "3★", "Hunt", 740, 370, 264,f"When the wearer defeats an enemy, increases SPD by 10/12/14/16/18% for 2 turn(s)."),
"amber": Lightcone("Amber", "3★", "Preservation", 846, 264, 330,f"Increases the wearer's DEF by 16/20/24/28/32%. If the wearer's current HP is lower than 50%, increases their DEF by a further 16/20/24/28/32%."),
"arrows": Lightcone("Arrows", "3★", "Hunt", 846, 317, 264,f"At the beginning of the battle, increases the wearer's CRIT Rate by 12/15/18/21/24% for 3 turn(s)."),
"chorus": Lightcone("Chorus", "3★", "Harmony", 846, 317, 264,f"After entering battle, increases the ATK of all allies by 8/9/10/11/12%. Effects of the same type cannot stack."),
"collapsingsky": Lightcone("Collapsing Sky", "3★", "Destruction", 846, 370, 198,f"Increases the wearer's Basic ATK and Skill DMG by 20/25/30/35/40%."),
"cornucopia": Lightcone("Cornucopia", "3★", "Abundance", 952, 264, 264,f"When the wearer uses their Skill or Ultimate, their Outgoing Healing increases by 12/15/18/21/24%."),
"dartingarrow": Lightcone("Darting Arrow", "3★", "Hunt", 740, 370, 264,f"When the wearer defeats an enemy, increase ATK by 24/30/36/42/48% for 3 turn(s)."),
"databank": Lightcone("Data Bank", "3★", "Erudition", 740, 370, 264,"Increases the wearer's Ultimate DMG by 28/35/42/49/56%."),
"defense": Lightcone("Defense", "3★", "Preservation", 952, 264, 264,f"When the wearer unleashes their Ultimate, they restore HP by 18/21/24/27/30% of their Max HP."),
"finefruit": Lightcone("Fine Fruit", "3★", "Abundance", 952, 317, 198,"At the beginning of battle, immediately regenerates 6/8/9/11/12 Energy for all allies."),
"hiddenshadow": Lightcone("Hidden Shadow", "3★", "Nihility", 846, 317, 264,f"After using Skill, the wearer's next Basic ATK deals Additional DMG equal to 60/75/90/105/120% of ATK to the target enemy."),
"loop": Lightcone("Loop", "3★", "Nihility", 846, 317, 264,"Increases DMG dealt from its wearer to Slowed enemies by 24/30/36/42/48%."),
"mediation": Lightcone("Mediation", "3★", "Harmony", 846, 317, 264,"Upon battle entry, all allies receive 12/14/16/18/20 increased SPD for 1 turn(s)."),
"meshingcogs": Lightcone("Meshing Cogs", "3★", "Harmony", 846, 317, 264,"After the wearer uses attacks or gets hit, additionally regenerates 4/5/6/7/8 Energy. This effect can only be triggered 1 time per turn."),
"multiplication": Lightcone("Multiplication", "3★", "Abundance", 952, 317, 198,"After the wearer uses their Basic ATK, their next action will be Advanced Forward by 12/14/16/18/20%."),
"mutualdemise": Lightcone("Mutual Demise", "3★", "Destruction", 846, 370, 198,"If the wearer's current HP is lower than 80%, CRIT Rate increases by 12/15/18/21/24%."),
"passkey": Lightcone("Passkey", "3★", "Erudition", 740, 370, 264, "After the wearer uses their Skill, additionally regenerates 8/9/10/11/12 Energy. This effect can only be triggered 1 time per turn."),
"pioneering": Lightcone("Pioneering", "3★", "Preservation", 952, 264, 264, f"When the wearer Breaks an enemy's Weakness, the wearer restores HP by 12/14/16/18/20% of their Max HP."),
"sagacity": Lightcone("Sagacity", "3★", "Erudition", 740, 370, 264,f"When the wearer uses their Ultimate, increases ATK by 24/30/36/42/48% for 2 turn(s)."),
"shatteredhome": Lightcone("Shattered Home", "3★", "Destruction", 846, 370, 198,f"Deals 20/25/30/35/40% increased DMG to any enemies whose HP is above 50%."),
"void": Lightcone("Void", "3★", "Nihility", 846, 317, 264,f"At the start of battle, increases the wearer's Effect Hit Rate by 20/25/30/35/40% for 3 turn(s)."),
"asecretvow": Lightcone("A Secret Vow", "4★", "Destruction", 1058, 476, 264,f"Increases DMG dealt by the wearer by 20/25/30/35/40%. The wearer also deals an extra 20/25/30/35/40% of DMG to enemies with a higher HP percentage than the wearer."),
"beforethetutorialmissionstarts": Lightcone("Before the Tutorial Mission Starts", "4★", "Nihility", 952, 476, 330,"Increases the wearer's Effect Hit Rate by 20/25/30/35/40%. When the wearer attacks enemies that have reduced DEF, regenerates 4/5/6/7/8 Energy."),
"carvethemoon,weavetheclouds": Lightcone("Carve the Moon, Weave the Clouds", "4★", "Harmony", 952, 476, 330, "At the start of the battle and whenever the wearer's turn begins, one of the following effects is applied randomly: All allies' ATK increases by 10/12.5/15/17.5/20%, all allies' CRIT DMG increases by 12/15/18/21/24%, or all allies' Energy Regeneration Rate increases by 6/7.5/9/10.5/12%."),
"concertfortwo": Lightcone("Concert for Two", "4★", "Preservation", 952, 370, 463,"Increases the wearer's DEF by 16/20/24/28/32%. For every on-field character that has a Shield, the DMG dealt by the wearer increases by 4/5/6/7/8%."),
"dance!dance!dance!": Lightcone("Dance! Dance! Dance!", "4★", "Harmony", 952, 423, 396,"When the wearer uses their Ultimate, all allies' actions are Advanced Forward by 16/18/20/22/24%"),
"dayoneofmynewlife": Lightcone("Day One of My New Life", "4★", "Preservation", 952, 370, 463,"Increases the wearer's DEF by 16/18/20/22/24%. After entering battle, increases DMG RES of all allies by 8/9/10/11/12%. Effects of the same type cannot stack."),
"destiny'sthreadsforewoven": Lightcone("Destiny's Threads Forewoven", "4★", "Preservation", 952, 370, 463,"Increases the wearer's Effect RES by 12/14/16/18/20%. For every 100 of DEF the wearer has, increases the DMG dealt by 0.8/0.9/1/1.1/1.2% to a max increase of 32/36/40/44/48%."),
"dreamvilleadventure": Lightcone("Dreamville Adventure", "4★", "Harmony", 953, 423, 397, "After the wearer uses a Basic ATK, Skill, or Ultimate, all allies gain Childishness, which increases the DMG dealt by the corresponding ability they used by 12/14/16/18/20%. Childishness only takes effect with the most recent ability used by the wearer and cannot be stacked."),
"eyesoftheprey": Lightcone("Eyes of the Prey", "4★", "Nihility", 952, 476, 330, f"Increases Effect Hit Rate of its wearer by 20/25/30/35/40% and increases DoT by 24/30/36/42/48%."),
"fermata": Lightcone("Fermata", "4★", "Nihility", 952, 476, 330, "Increases the Break Effect dealt by the wearer by 16/20/24/28/32%, and increases their DMG to enemies afflicted with Shock or Wind Shear by 16/20/24/28/32%. This also applies to DoT."),
"finalvictor": Lightcone("Final Victor", "4★", "Hunt", 953, 476, 331, "Increases the wearer's ATK by 12/14/16/18/20%. When the wearer lands a CRIT hit on enemies, they will gain a stack of Good Fortune. This effect can be stacked 4 time(s). Every stack of Good Fortune the wearer has will increase their CRIT DMG by 8/9/10/11/12%. Good Fortune will be removed at the end of the wearer's turn."),
"flamesafar": Lightcone("Flames Afar", "4★", "Destruction", 1058, 476, 265, f"When the HP lost by the wearer during a single attack exceeds 25% of their Max HP, or if the HP they consume is greater than 25% of their Max HP, then immediately heals them for 15% of their Max HP while also increasing the DMG they deal by 25/31/38/44/50% for 2 turn(s). This effect can only be triggered once every 3 turn(s)."),
"geniuses'repose": Lightcone("Geniuses' Repose", "4★", "Erudition", 846, 476, 396,"Increases the wearer's ATK by 16/20/24/28/32%. When the wearer defeats an enemy, the wearer's CRIT DMG increases by 24/30/36/42/48% for 3 turn(s)."),
"goodnightandsleepwell": Lightcone("Good Night and Sleep Well", "4★", "Nihility", 952, 476, 330,"For every debuff the target enemy has, the DMG dealt by the wearer increases by 12/15/18/21/24%, stacking up to 3 time(s). This effect also applies to DoT."),
"hey,overhere": Lightcone("Hey, Over Here", "4★", "Abundance", 952, 476, 396,
                            "Increases the wearer's Max HP by 8/9/10/11/12%. When the wearer uses Skill, increases Outgoing Healing by 16/19/22/25/28%, lasting for 2 turn(s)."),
"indeliblepromise": Lightcone("Indelible Promise", "4★", "Destruction", 953, 476, 331,
                                "Increases the wearer's Break Effect by 28/35/42/49/56%. When the wearer uses their Ultimate, increases CRIT Rate by 15/18.75/22.5/26.25/30%, lasting for 2 turns."),
"it'sshowtime": Lightcone("It's Showtime", "4★", "Nihility", 1058, 476, 265,
                            f"When the wearer inflicts a debuff on an enemy, they gain a stack of Trick. Every stack of Trick increases the wearer's DMG dealt by 6/7/8/9/10% for a max of 3 stack(s). This effect lasts for 1 turn(s). When the wearer's Effect Hit Rate is greater than or equal to 80%, increases ATK by 20/24/28/32/36%."),
"landau'schoice": Lightcone("Landau's Choice", "4★", "Preservation", 952, 423, 396,
                            "The wearer is more likely to be attacked, but DMG taken is reduced by 16/18/20/22/24%."),
"maketheworldclamor": Lightcone("Make the World Clamor", "4★", "Erudition", 846, 476, 396,
                                "The wearer regenerates 20/23/26/29/32 Energy immediately upon entering battle, and increases Ultimate DMG by 32/40/48/56/64%."),
"memoriesofthepast": Lightcone("Memories of the Past", "4★", "Harmony", 952, 423, 396,
                                "Increases the wearer's Break Effect by 28/35/42/49/56%. When the wearer attacks, additionally regenerates 4/5/6/7/8 Energy. This effect can only be triggered 1 time per turn."),
"nowheretorun": Lightcone("Nowhere to Run", "4★", "Destruction", 952, 529, 264,
                            f"Increases the wearer's ATK by 24/30/36/42/48%. Whenever the wearer defeats an enemy, they restore HP equal to 12/15/18/21/24% of their ATK."),
"onlysilenceremains": Lightcone("Only Silence Remains", "4★", "Hunt", 952, 476, 330,
                                "Increases ATK of its wearer by 16/20/24/28/32%. If there are 2 or fewer enemies on the field, increases wearer's CRIT Rate by 12/15/18/21/24%."),
"pastandfuture": Lightcone("Past and Future", "4★", "Harmony", 952, 423, 396,
                            f"When the wearer uses their Skill, then the next ally taking action (except the wearer) deals 16/20/24/28/32% increased DMG for 1 turn(s)."),
"perfecttiming": Lightcone("Perfect Timing", "4★", "Abundance", 952, 423, 396,
                               f"Increases the wearer's Effect RES by 16/20/24/28/32% and increases Outgoing Healing by an amount that is equal to 33/36/39/42/45% of Effect RES. Outgoing Healing can be increased this way by up to 15/18/21/24/27%."),
"planetaryrendezvous": Lightcone("Planetary Rendezvous", "4★", "Harmony", 1058, 423, 330,
                                    "Upon battle entry, if an ally deals the same DMG Type as the wearer, DMG dealt increases by 12/15/18/21/24%."),
"post-opconversation": Lightcone("Post-Op Conversation", "4★", "Abundance", 1058, 423, 330,
                                    f"Increases Energy Regeneration Rate of its wearer by 8/10/12/14/16% and increases Outgoing Healing when they use their Ultimate by 12/15/18/21/24%."),
"quidproquo": Lightcone("Quid Pro Quo", "4★", "Abundance", 952, 423, 396,
                        "At the start of the wearer's turn, regenerates 8/10/12/14/16 Energy for a randomly chosen ally (excluding the wearer) whose current Energy is lower than 50%."),
"resolution": Lightcone("Resolution Shines As Pearls of Sweat", "4★", "Nihility", 952, 476, 330,
                                                f"When the wearer hits an enemy and if the hit enemy is not already Ensnared, then there is a 60/70/80/90/100% base chance to Ensnare the hit enemy. Ensnared enemies' DEF decreases by 12/13/14/15/16% for 1 turn(s)."),
"returntodarkness": Lightcone("Return to Darkness", "4★", "Hunt", 846, 529, 330,
                                f"Increases the wearer's CRIT Rate by 12/15/18/21/24%. After a CRIT Hit, there is a 16/20/24/28/32% fixed chance to dispel 1 buff on the target enemy. This effect can only trigger once per attack."),
"riverflowsinspring": Lightcone("River Flows in Spring", "4★", "Hunt", 846, 476, 396,
                                f"After entering battle, increases the wearer's SPD by 8/9/10/11/12% and DMG by 12/15/18/21/24%. When the wearer takes DMG, this effect will disappear. This effect will resume after the end of the wearer's next turn."),
"sharedfeeling": Lightcone("Shared Feeling", "4★", "Abundance", 952, 423, 396,
                            "Increases the wearer's Outgoing Healing by 10/12.5/15/17.5/20%. When using Skill, regenerates 2/2/3/3/4 Energy for all allies."),
"subscribefor more!": Lightcone("Subscribe for More!", "4★", "Hunt", 952, 476, 330,
                                f"Increases the DMG of the wearer's Basic ATK and Skill by 24/30/36/42/48%. This effect increases by an extra 24/30/36/42/48% when the wearer's current Energy reaches its max level."),
"swordplay": Lightcone("Swordplay", "4★", "Hunt", 952, 476, 330,
                        "For each time the wearer hits the same target, DMG dealt increases by 8/10/12/14/16%, stacking up to 5 time(s). This effect will be dispelled when the wearer changes targets."),
"thebirthoftheself": Lightcone("The Birth of the Self", "4★", "Erudition", 952, 476, 330,
                                   f"Increases DMG dealt by the wearer's follow-up attacks by 24/30/36/42/48%. If the current HP of the target enemy is below 50% of their Max HP, increases DMG dealt by follow-up attacks by an extra 24/30/36/42/48%."),
"thedaythecosmosfell": Lightcone("The Day The Cosmos Fell", "4★", "Erudition", 953, 476, 331,
                                    f"Increases the wearer's ATK by 16/18/20/22/24%. When the wearer uses an attack and affects no fewer than 2 attacked enemies with a corresponding Weakness, the wearer's CRIT DMG increases by 20/25/30/35/40% for 2 turn(s)."),
"themoleswelcomeyou": Lightcone("The Moles Welcome You", "4★", "Destruction", 846, 476, 396,
                                "When the wearer uses Basic ATK, Skill, or Ultimate to attack enemies, the wearer gains one stack of Mischievous. Each stack increases the wearer's ATK by 12/15/18/21/24%."),
"theseriousnessofbreakfast": Lightcone("The Seriousness of Breakfast", "4★", "Erudition", 846, 476, 396,
                                        f"Increases the wearer's DMG by 12/15/18/21/24%. For every defeated enemy, the wearer's ATK increases by 4/5/6/7/8%, stacking up to 3 time(s)."),
"thisisme!": Lightcone("This Is Me!", "4★", "Preservation", 846, 370, 529,
                        f"Increases the wearer's DEF by 16/20/24/28/32%. Increases the DMG of the wearer when they use their Ultimate by 60/75/90/105/120% of the wearer's DEF. This effect only apply 1 time per enemy target."),
"todayisanotherpeacefulday": Lightcone("Today Is Another Peaceful Day", "4★", "Erudition", 846, 529, 396,
                                        f"After entering battle, increases the wearer's DMG based on their Max Energy. DMG increases by 0.2/0.25/0.3/0.35/0.4% per point of Energy, up to 160 Energy."),
"trendoftheuniversalmarket": Lightcone("Trend of the Universal Market", "4★", "Preservation", 1058, 476, 396,
                                        f"Increases the wearer's DEF by 16/20/24/28/32%. When the wearer is attacked, there is a 100/105/110/115/120% base chance to Burn the enemy. For each turn, the wearer deals DoT that is equal to 40/50/60/70/80% of the wearer's DEF for 2 turn(s)."),
"underthebluesky": Lightcone("Under the Blue Sky", "4★", "Destruction", 952, 476, 330,
                                "Increases the wearer's ATK by 16/20/24/28/32%. When the wearer defeats an enemy, the wearer's CRIT Rate increases by 12/15/18/21/24% for 3 turn(s)."),
"warmthshortenscoldnights": Lightcone("Warmth Shortens Cold Nights", "4★", "Abundance", 1058, 476, 396,
                                        f"Increases the wearer's Max HP by 16/20/24/28/32%. When using Basic ATK or Skill, restores all allies' HP by an amount equal to 2/2.5/3/3.5/4% of their respective Max HP."),
"wearewildfire": Lightcone("We Are Wildfire", "4★", "Preservation", 740, 476, 463,
                            f"At the start of the battle, the DMG dealt to all allies decreases by 8/10/12/14/16% for 5 turn(s). At the same time, immediately restores HP to all allies equal to 30/35/40/45/50% of the respective HP difference between the characters' Max HP and current HP."),
"wewillmeetagain": Lightcone("We Will Meet Again", "4★", "Nihility", 846, 529, 330,
                                 f"After the wearer uses Basic ATK or Skill, the wearer deals 48/60/72/84/96% of ATK as additional DMG to a random enemy that is attacked by abilities."),
"whatisreal?": Lightcone("What Is Real?", "4★", "Abundance", 1058, 423, 331,
                            f"Increases the wearer's Break Effect by 24/30/36/42/48%. Wearer's Basic ATKs restore an amount equal to 2/2.5/3/3.5/4% of Max HP plus 800 for themselves."),
"woof!walktime!": Lightcone("Woof! Walk Time!", "4★", "Destruction", 952, 476, 330,
                            f"Increases the wearer's ATK by 10/12.5/15/17.5/20%, and increases their DMG to enemies afflicted with Burn or Bleed by 16/20/24/28/32%. This also applies to DoT."),
"echoesofthecoffin": Lightcone("Echoes of the Coffin", "5★", "Abundance", 1164, 582, 396,
                                f"Increases the wearer's ATK by 24/28/32/36/40%. After the wearer uses an attack, for each different enemy target the wearer hits, regenerates 3/3.5/4/4.5/5 Energy. Each attack can regenerate Energy up to 3 time(s) this way. After the wearer uses their Ultimate, all allies gain 12/14/16/18/20 SPD for 1 turn."),
"nightoffright": Lightcone("Night of Fright", "5★", "Abundance", 1164, 476, 529,
                            f"Increases the wearer's Energy Regeneration Rate by 12/14/16/18/20%. When any ally uses their Ultimate, the wearer restores HP for the ally currently with the lowest HP percentage by an amount equal to 10/11/12/13/14% of the healed ally's Max HP."),
"timewaitsfornoone": Lightcone("Time Waits for No One", "5★", "Abundance", 1270, 476, 463,
                                f"Increases the wearer's Max HP by 18/21/24/27/30% and Outgoing Healing by 12/14/16/18/20%. When the wearer heals allies, record the amount of Outgoing Healing. When any ally launches an attack, a random attacked enemy takes Additional DMG equal to 36/42/48/54/60% of the recorded Outgoing Healing value."),
"brighterthanthesun": Lightcone("Brighter Than the Sun", "5★", "Destruction", 1164, 582, 396,
                                f"Increases the wearer's CRIT Rate by 18/21/24/27/30%. When the wearer uses their Basic ATK, they will gain 1 stack of Dragon's Call for 2 turns."),
"ishallbemyownsword": Lightcone("I Shall Be My Own Sword", "5★", "Destruction", 1164, 476, 529,
                                f"Each stack of Dragon's Call increases the wearer's ATK by 18/21/24/27/30% and Energy Regeneration Rate by 6/7/8/9/10%. Dragon's Call can be stacked up to 2 times."),
"onthefallofanaeon": Lightcone("On the Fall of an Aeon", "5★", "Destruction", 1270, 476, 463,
                                f"Increases the wearer's Energy Regeneration Rate by 12/14/16/18/20%. When any ally uses their Ultimate, the wearer restores HP for the ally currently with the lowest HP percentage by an amount equal to 10/11/12/13/14% of the healed ally's Max HP."),
"somethingirreplaceable": Lightcone("Something Irreplaceable", "5★", "Destruction", 1058, 635, 396,
                                    f"Increases the wearer's Max HP by 18/21/24/27/30% and Outgoing Healing by 12/14/16/18/20%. When the wearer heals allies, record the amount of Outgoing Healing. When any ally launches an attack, a random attacked enemy takes Additional DMG equal to 36/42/48/54/60% of the recorded Outgoing Healing value."),
"theunreachableside": Lightcone("The Unreachable Side", "5★", "Destruction", 1164, 582, 396,
                                    "Increases the wearer's CRIT DMG by 20/23/26/29/32%. When an ally gets attacked or loses HP, the wearer gains 1 stack of Eclipse, up to a max of 3 stack(s). Each stack of Eclipse increases the DMG of the wearer's next attack by 14/16.5/19/21.5/24%. When 3 stack(s) are reached, additionally enables the attack to ignore 12/14/16/18/20% of the enemy's DEF. This effect will be removed after the wearer uses an attack."),
"aninstantbeforeagaze": Lightcone("An Instant Before A Gaze", "5★", "Erudition", 1058, 529, 396,
                                    f"Whenever the wearer attacks, their ATK is increased by 8/10/12/14/16% in this battle, up to 4 time(s). When the wearer inflicts Weakness Break on enemies, the wearer's DMG increases by 12/15/18/21/24% for 2 turn(s)."),
"beforedawn": Lightcone("Before Dawn", "5★", "Erudition", 1164, 582, 396,
                        f"Increases the wearer's ATK by 24/28/32/36/40%. When the wearer defeats an enemy or is hit, immediately restores HP equal to 8/9/10/11/12% of the wearer's ATK. At the same time, the wearer's DMG is increased by 24/28/32/36/40% until the end of their next turn. This effect cannot stack and can only trigger 1 time per turn."),
"nightonthemilkyway": Lightcone("Night on the Milky Way", "5★", "Erudition", 1270, 582, 330,
                                f"Increases the wearer's CRIT rate by 18/21/24/27/30% and increases their Max HP by 18/21/24/27/30%. When the wearer is attacked or consumes their own HP, their DMG increases by 24/28/32/36/40%. This effect is removed after the wearer uses an attack."),
"butthebattleisn'tover": Lightcone("But the Battle Isn't Over", "5★", "Harmony", 1058, 582, 463,
                                    f"Increases the wearer's CRIT DMG by 36/42/48/54/60%. When the wearer uses their Ultimate, the wearer's Ultimate DMG increases based on their Max Energy; Ultimate DMG increases by 0.36/0.42/0.48/0.54/0.6% per point of Energy, up to 180 Energy."),
"earthlyescapade": Lightcone("Earthly Escapade", "5★", "Harmony", 1058, 582, 463,
                                f"Increases the wearer's CRIT DMG by 36/42/48/54/60%. Increases the wearer's Skill and Ultimate DMG by 18/21/24/27/30%. After the wearer uses their Skill or Ultimate, they gain Somnus Corpus. Upon triggering a follow-up attack, Somnus Corpus will be consumed and the follow-up attack DMG increases by 48/56/64/72/80%."),
"pastselfinmirror": Lightcone("Past Self in Mirror", "5★", "Harmony", 1164, 582, 396,
                                f"For every enemy on the field, increases the wearer's ATK by 9/10.5/12/13.5/15%, up to 5 stacks. When an enemy is inflicted with Weakness Break, the DMG dealt by the wearer increases by 30/35/40/45/50% for 1 turn."),
"baptismofpurethought": Lightcone("Baptism of Pure Thought", "5★", "Hunt", 952, 582, 529,
                                    f"Increases the wearer's CRIT DMG by 20/23/26/29/32%. For every debuff on the enemy target, the wearer's CRIT DMG dealt against this target increases by 8/9/10/11/12%, stacking up to 3 times. When using Ultimate to attack the enemy target, the wearer receives the Disputation effect, which increases DMG dealt by 36/42/48/54/60% and enables their follow-up attacks to ignore 24/28/32/36/40% of the target's DEF. This effect lasts for 2 turns."),
"cruisinginthestellarsea": Lightcone("Cruising in the Stellar Sea", "5★", "Hunt", 952, 582, 463,
                                        f"Increases the wearer's CRIT rate by 8/10/12/14/16%, and increases their CRIT rate against enemies with HP less than or equal to 50% by an extra 8/10/12/14/16%. When the wearer defeats an enemy, their ATK is increased by 20/25/30/35/40% for 2 turn(s)."),
"inthenight": Lightcone("In the Night", "5★", "Hunt", 1058, 582, 463,
                        f"Increases the wearer's CRIT Rate by 18/21/24/27/30%. While the wearer is in battle, for every 10 SPD that exceeds 100, the DMG of the wearer's Basic ATK and Skill is increased by 6/7/8/9/10% and the CRIT DMG of their Ultimate is increased by 12/14/16/18/20%. This effect can stack up to 6 time(s)."),
"sleeplikethedead": Lightcone("Sleep Like the Dead", "5★", "Hunt", 1058, 582, 463,
                                  "Increases the wearer's CRIT DMG by 30/35/40/45/50%. When the wearer's Basic ATK or Skill does not result in a CRIT Hit, increases their CRIT Rate by 36/42/48/54/60% for 1 turn(s). This effect can only trigger once every 3 turn(s)."),
"worrisome,blissful": Lightcone("Worrisome, Blissful", "5★", "Hunt", 1058, 582, 463,
                                f"Increase the wearer's CRIT Rate by 18/21/24/27/30% and their follow-up attacks' DMG by 30/35/40/45/50%. After the wearer uses a follow-up attack, apply the Tame state to the target, stacking up to 2 stacks. When allies hit enemy targets under the Tame state, every Tame stack increases the CRIT DMG dealt by 12/14/16/18/20%."),
"alongthepassingshore": Lightcone("Along the Passing Shore", "5★", "Nihility", 1058, 635, 396,
                                    f"Increases the wearer's CRIT DMG by 36/42/48/54/60%. When the wearer hits an enemy target, inflicts Mirage Fizzle on the enemy, lasting for 1 turn. Each time the wearer attacks, this effect can only trigger 1 time on each target. The wearer deals 24/28/32/36/40% increased DMG to targets afflicted with Mirage Fizzle, and the DMG dealt by the wearer's Ultimate additionally increases by 24/28/32/36/40%."),
"inthenameoftheworld": Lightcone("In the Name of the World", "5★", "Nihility", 1058, 582, 463,
                                    f"Increases the wearer's DMG to debuffed enemies by 24/28/32/36/40%. When the wearer uses their Skill, the Effect Hit Rate for this attack increases by 18/21/24/27/30%, and ATK increases by 24/28/32/36/40%."),
"incessantrain": Lightcone("Incessant Rain", "5★", "Nihility", 1058, 582, 463,
                            f"Increases the wearer's Effect Hit Rate by 24/28/32/36/40%. When the wearer deals DMG to an enemy with 3 or more debuffs, increases CRIT Rate by 12/14/16/18/20%."),
"patienceisallyouneed": Lightcone("Patience Is All You Need", "5★", "Nihility", 1058, 582, 463,
                                    f"Increases DMG dealt by the wearer by 24/28/32/36/40%. After every attack launched by wearer, their SPD increases by 4.8/5.6/6.4/7.2/8%, stacking up to 3 times."),
"reforgedremembrance": Lightcone("Reforged Remembrance", "5★", "Nihility", 1058, 582, 463,
                                    f"Increases wearer's Effect Hit Rate by 40/45/50/55/60%. When the wearer deals DMG to an enemy inflicted with Wind Shear, Burn, Shock, or Bleed, they will individually gain 1 stack of Prophet."),
"solitaryhealing": Lightcone("Solitary Healing", "5★", "Nihility", 1058, 529, 396,
                                f"Increases the wearer's Break Effect by 20/25/30/35/40%. When the wearer unleashes their Ultimate, increases DoT dealt by the wearer by 24/30/36/42/48% for 2 turn(s)."),
"inherentlyunjustdestiny": Lightcone("Inherently Unjust Destiny", "5★", "Preservation", 1058, 423, 661,
                                        f"Increases the wearer's DEF by 40/46/52/58/64%. When the wearer provides a Shield to an ally, the wearer's CRIT DMG increases by 40/46/52/58/64%, lasting for 2 turn(s)."),
"momentofvictory": Lightcone("Moment of Victory", "5★", "Preservation", 1058, 476, 595,
                                f"Increases the wearer's DEF by 24/28/32/36/40% and Effect Hit Rate by 24/28/32/36/40%. Increases the chance for the wearer to be attacked by enemies. When the wearer is attacked, increase their DEF by an additional 24/28/32/36/40% until the end of the wearer's turn."),
"shealreadyshuthereyes": Lightcone("She Already Shut Her Eyes", "5★", "Preservation", 1270, 423, 529,
                                       f"Increases the wearer's Max HP by 24/28/32/36/40% and Energy Regeneration Rate by 12/14/16/18/20%. When the wearer's HP is decreased, increases the DMG of all allies by 9/10.5/12/13.5/15% for 2 turns. At the beginning of each wave, restores HP equal to 80/85/90/95/100% of HP already lost by the character themselves for team."),
"textureofmemories": Lightcone("Texture of Memories", "5★", "Preservation", 1058, 423, 529,
                                f"Increases the wearer's Effect RES by 8/10/12/14/16%. If the wearer is attacked and has no Shield, they gain a Shield equal to 16/20/24/28/32% of their Max HP for 2 turn(s). This effect can only be triggered once every 3 turn(s). If the wearer has a Shield when attacked, the DMG they receive decreases by 12/15/18/21/24%.")
}


@bot.command(lcname="lc")
async def lc(ctx, lcname):
    if lcname.lower() in Lightcones:
        lc_info = Lightcones[lcname.lower()]
        if lc_info.lcrarity == "3★":
            type_color = discord.Color.blue()
        elif lc_info.lcrarity == "4★":
            type_color = discord.Color.purple()
        elif lc_info.lcrarity == "5★":
            type_color = discord.Color.yellow()
        embed = discord.Embed(title=lc_info.lcname, description="\n\n", color=type_color)
        embed.add_field(name="Path", value=lc_info.lcpath, inline=False)
        embed.add_field(name="Rarity", value=lc_info.lcrarity, inline=False)
        embed.add_field(name="HP", value=lc_info.lchp, inline=False)
        embed.add_field(name="Attack", value=lc_info.lcattack, inline=False)
        embed.add_field(name="Defense", value=lc_info.lcdefense, inline=False)
        embed.add_field(name="Description", value=lc_info.lcdescription, inline=False)
        await ctx.send(embed=embed)

    else:
        await ctx.send("Lightcone not found, maybe try !searchlc first?")


@bot.command()
async def searchlc(ctx):
    response = ""
    await ctx.send("Enter the letter you want to search Lightcones for:")
    while True:
        try:
            search_letter = await bot.wait_for("message", check=lambda message: message.author == ctx.author and message.channel == ctx.channel, timeout=7)
            search_letter = search_letter.content.lower()
            if search_letter == "kill":
                break
            matched_lcs = [lc for lc in Lightcones if lc.lower().startswith(search_letter)]
            if matched_lcs:
                for lc in matched_lcs:
                    response += f"- {lc}\n"
                embed = discord.Embed(title=f"Matched Lightcones starting with '{search_letter}'", color=discord.Color.dark_gray())  # Fixed color argument
                embed.add_field(name="Result", value=response, inline=False)
                await ctx.send(embed=embed)
                response = ""
            else:
                await ctx.send(f"No Lightcones found with names starting with '{search_letter}'. Please try again.")
        except asyncio.TimeoutError:
            await ctx.send("Search has ended.")
            break

artifact_stats = {
    "Head": {
        "Flat HP": {"Stat Rate": "100.00%", "Drop Rate": "25.00%", "Run Drop Rate": "12.50%", "Avg Stamina": 152},
    },
    "Hands": {
        "Flat Attack": {"Stat Rate": "100.00%", "Drop Rate": "25.00%", "Run Drop Rate": "12.50%", "Avg Stamina": 152}
    },
    "Body": {
        "HP %": {"Stat Rate": "20.00%", "Drop Rate": "5.00%", "Run Drop Rate": "2.50%", "Avg Stamina": 760},
        "Atk %": {"Stat Rate": "20.00%", "Drop Rate": "5.00%", "Run Drop Rate": "2.50%", "Avg Stamina": 760},
        "Def %": {"Stat Rate": "20.00%", "Drop Rate": "5.00%", "Run Drop Rate": "2.50%", "Avg Stamina": 760},
        "Crit Rate": {"Stat Rate": "10.00%", "Drop Rate": "2.50%", "Run Drop Rate": "1.25%", "Avg Stamina": 1520},
        "Crit Dmg": {"Stat Rate": "10.00%", "Drop Rate": "2.50%", "Run Drop Rate": "1.25%", "Avg Stamina": 1520},
        "Healing %": {"Stat Rate": "10.00%", "Drop Rate": "2.50%", "Run Drop Rate": "1.25%", "Avg Stamina": 1520},
        "Effect Hit Rate": {"Stat Rate": "10.00%", "Drop Rate": "2.50%", "Run Drop Rate": "1.25%", "Avg Stamina": 1520}
    },
    "Boots": {
        "HP %": {"Stat Rate": "30.00%", "Drop Rate": "7.50%", "Run Drop Rate": "3.75%", "Avg Stamina": 507},
        "Atk %": {"Stat Rate": "30.00%", "Drop Rate": "7.50%", "Run Drop Rate": "3.75%", "Avg Stamina": 507},
        "Def %": {"Stat Rate": "30.00%", "Drop Rate": "7.50%", "Run Drop Rate": "3.75%", "Avg Stamina": 507},
        "Speed": {"Stat Rate": "10.00%", "Drop Rate": "2.50%", "Run Drop Rate": "1.25%", "Avg Stamina": 1520}
    },
    "Sphere": {
        "HP %": {"Stat Rate": "12.00%", "Drop Rate": "6.00%", "Per Set Rate": "3.00%", "Avg Stamina": 633},
        "Atk %": {"Stat Rate": "12.00%", "Drop Rate": "6.00%", "Per Set Rate": "3.00%", "Avg Stamina": 633},
        "Def %": {"Stat Rate": "12.00%", "Drop Rate": "6.00%", "Per Set Rate": "3.00%", "Avg Stamina": 633},
        "Element": {"Stat Rate": "9.14%", "Drop Rate": "4.57%", "Per Set Rate": "2.29%", "Avg Stamina": 831}
    },
    "Rope": {
        "HP %": {"Stat Rate": "26.00%", "Drop Rate": "13.00%", "Per Set Rate": "6.50%", "Avg Stamina": 292},
        "Atk %": {"Stat Rate": "26.00%", "Drop Rate": "13.00%", "Per Set Rate": "6.50%", "Avg Stamina": 292},
        "Def %": {"Stat Rate": "26.00%", "Drop Rate": "13.00%", "Per Set Rate": "6.50%", "Avg Stamina": 292},
        "Break Effect": {"Stat Rate": "16.00%", "Drop Rate": "8.00%", "Per Set Rate": "4.00%", "Avg Stamina": 475},
        "Energy RR": {"Stat Rate": "6.00%", "Drop Rate": "3.00%", "Per Set Rate": "1.50%", "Avg Stamina": 1267}
    }
}


@bot.command(name="droprate")
async def droprate(ctx, key_name: str):
    key_name = key_name.capitalize()  # Ensure key_name is capitalized
    if key_name in artifact_stats:
        embed = discord.Embed(title=f"Droprate for {key_name}", color=discord.Color.blurple())
        for stat_name, stat_info in artifact_stats[key_name].items():
            value_str = "\n".join([f"{k}: {v}" for k, v in stat_info.items()])
            embed.add_field(name=stat_name, value=value_str, inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid artficat type. Please choose from\n-Head\n-Hands\n-Body\n-Boots\n-Sphere\n-Rope")
'''
@bot.command()
async def recommend(ctx):
    characters = ["Qingque E4","Bronya","Tingyun","Pela","Herta","Jing Yuan","Silver Wolf","Luocha","Kafka","Dan Heng IL","Fu Xuan","Jingliu","Topaz","Huo Huo","Argenti","Ruan Mei","Dr Ratio","Black Swan","Sparkle","Acheron","Aventurine","Jiaoqiu","Boothill","Robin","Sam","Jade"]
    global yes
    yes = ["Tingyun","Pela","Herta"]
    no = ["Jiaoqiu","Boothill","Robin","Sam","Jade"]

    teams = [
        ["Dan Heng IL","Tingyun","Sparkle"],
        ["Jingliu","Bronya","Ruan Mei"],
        ["Acheron","Pela","Silver Wolf"],
        ["Kafka","Black Swan","Ruan Mei",],
        ["Dr Ratio","Topaz","Ruan Mei"],
        ["Jing Yuan","Sparkle","Tingyun"],
        ["Argenti","Sparkle","Tingyun"],
        ["Herta","Sparkle","Tingyun"],
        ["Qingque E4","Sparkle","Tingyun"]
    ]

    MoC = ["Acheron","Kafka","Dan Heng IL","Jingliu","Qingque E4","Dr Ratio","Jing Yuan"]
    MoC_Wanted = []
    Pf = ["Argenti","Herta","Acheron","Kafka","Jing Yuan"]
    Pf_Wanted = []
    Sustain = ["Fu Xuan","Aventurine","Huo Huo","Luocha"]
    Sustain_Wanted = []

    score = {character: 0 for character in characters}

    async def update_scores(reference_list, delta):
        for team in teams:
            for character in team:
                if character in reference_list:
                    for character in team:
                        score[character] += delta

    async def find_character_to_recruit(reference_list, target_score):
        for character in reference_list:
            if score[character] >= target_score:
                return character
        return None

    async def ext_MoC_Wanted():
        target_scores = [3, 2, 1, 0]
        for target_score in target_scores:
            character_found = find_character_to_recruit(MoC, target_score)
            if character_found:
                for team in teams:
                    if character_found in team:
                        MoC_Wanted.extend(team)
                break  # Stop searching once a character is found

    async def ext_PF_Wanted():
        target_scores = [3, 2, 1, 0]
        for target_score in target_scores:
            character_found = find_character_to_recruit(Pf, target_score)
            if character_found:
                for team in teams:
                    if character_found in team:
                        Pf_Wanted.extend(team)
                break

    async def calculate_safety():
        safety = 0
        for character in yes:
            if character in Sustain:
                safety += 1
        return safety

    async def populate_Sustain_Wanted(safety):
        Sustain_Wanted.clear()  # Clear the existing list
        if safety == 0:
            Sustain_Wanted.extend(Sustain[:2])
        elif safety == 1:
            for character in Sustain:
                if character not in yes:
                    Sustain_Wanted.append(character)
                    break

    async def combine(list1, list2, list3=None):
        if list3 is None:
            list3 = []  # Set an empty list as default if list3 is not provided
        combined_list = list1 + list2 + list3  # Combine the three lists
        unique_list = list(set(combined_list))  # Remove duplicates using set and convert back to list
        return unique_list

    
    async def reset_scores():
        for character in characters:
            score[character] = 0

    async def remove_characters_in_yes(final_list):
        return [character for character in final_list if character not in yes]


    for character in characters:
        await ctx.send(f"Do you have {character}? (yes/no)")

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['y', 'n']

        try:
            response = await bot.wait_for('message', check=check, timeout=60)  # Wait for user's response
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond. Exiting command.")
            return

        if response.content.lower() == 'yes':
            yes.append(character)
        elif response.content.lower() == 'no':
            no.append(character)

    await update_scores(yes, 1)
    await ext_MoC_Wanted()
    await update_scores(MoC_Wanted, -3)
    await ext_MoC_Wanted()
    await reset_scores()
    temp1 = await combine(yes, MoC_Wanted)
    await update_scores(temp1, 1)
    await ext_PF_Wanted()
    await update_scores(Pf_Wanted, -3)
    await ext_PF_Wanted()

    
    safety = await calculate_safety()
    await populate_Sustain_Wanted(safety)
    
    final = await combine(MoC_Wanted,Pf_Wanted,Sustain_Wanted)
    final = await remove_characters_in_yes(final)
    final.sort()

    final = await combine(MoC_Wanted, Pf_Wanted, Sustain_Wanted)
    final = await remove_characters_in_yes(final)
    final.sort()
    response = "\nMatrix of Prescience Recommendation:\n\n"
    if len(final) == 0:
        response += "Save for future characters!\n"
    else:
        for character in final:
            response += f"{character}\n"

    await ctx.send(response)

'''


bot.run(token=os.environ.get('token'))



