import asyncio
import logging

import discord
from discord.ext import commands

import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

intents = discord.Intents.default()
intents.members = True          # Privileged Intent: Beitritt/Austritt-Logs
intents.message_content = True  # Privileged Intent: Inhalt gelöschter/bearbeiteter Nachrichten
# intents.moderation ist in default() enthalten (Audit-Log-Events)


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        for ext in ("cogs.music", "cogs.verses", "cogs.logs"):
            await self.load_extension(ext)

        if config.GUILD_ID:  # sofort verfügbar auf dem eigenen Server
            guild = discord.Object(id=config.GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        else:
            await self.tree.sync()

    async def on_ready(self):
        logging.info("Eingeloggt als %s (%s)", self.user, self.user.id)


if __name__ == "__main__":
    if not config.TOKEN or config.TOKEN == "dein_bot_token_hier":
        raise SystemExit("DISCORD_TOKEN fehlt – kopiere .env.example nach .env und trage ihn ein.")
    asyncio.run(Bot().start(config.TOKEN))
