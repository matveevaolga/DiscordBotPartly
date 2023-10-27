import disnake
from disnake.ext import commands
from src.modules.panel_main_buttons import MainPanelButtons
from src.functions.embeds import embed_user_panel
from src.functions.describe import user_panel


class Actions(commands.Cog):
    '''Действия'''

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(name='панель_действий')
    async def main_panel(self, inter: disnake.ApplicationCommandInteraction):
        '''Описание всех твоих возможностей'''
        
        embed = embed_user_panel(user_panel())
        # perm = check_permissions(inter.author)
        
        # if perm:
        #     await inter.send(embed=embed,
        #                      view=MainPlusPanelButtons(perm), ephemeral=True)
        # else:
        await inter.send(embed=embed,
                         view=MainPanelButtons(False), ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Actions(bot))
