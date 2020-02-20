from .redditor import Redditor


async def setup(bot):
    cog = Redditor()
    bot.add_cog(cog)
    try:
        await cog.start(cog)
    except:
        pass