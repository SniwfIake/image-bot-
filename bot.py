import discord
from discord import app_commands
import io
from config import TOKEN
from utils.image_api import generate_image

class ImageBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = ImageBot()

@bot.tree.command(name="generate", description="Generate an AI image")
async def generate(interaction: discord.Interaction, prompt: str):

    await interaction.response.defer()

    try:
        image_bytes = generate_image(prompt)

        file = discord.File(io.BytesIO(image_bytes), filename="image.png")

        embed = discord.Embed(
            title="AI Generated Image",
            description=f"`{prompt}`"
        )

        embed.set_image(url="attachment://image.png")

        await interaction.followup.send(embed=embed, file=file)

    except Exception as e:
        await interaction.followup.send(f"Error: {e}")

@bot.event
async def on_ready():
    print(f"Bot ready: {bot.user}")

bot.run(TOKEN)
