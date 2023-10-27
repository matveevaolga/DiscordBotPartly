import disnake
from disnake.enums import ButtonStyle
from src.functions.embeds import embed_games_panel
from src.functions.describe import games_panel
import src.modules.panel_games_buttons as pg


class MainPanelButtons(disnake.ui.View):
    def __init__(self, permissions: bool):
        super().__init__(timeout=None)
        self.permissions = permissions

    @disnake.ui.button(label='Игры', style=ButtonStyle.blurple,
                       row=1)
    async def button_user_games(self, button: disnake.ui.Button,
                                 inter: disnake.MessageInteraction):
        '''Команды для Игр через бота'''

        await inter.response.edit_message(
            embed=embed_games_panel(games_panel()),
            view=pg.GamesPanelButtons(self.permissions)
        )
