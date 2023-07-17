import discord
from discord import SelectOption, Interaction
from discord.ui import View, Select
from components.log_form import Log_Form
from data import Data


class Select_District(View):
    @discord.ui.select(
        cls=discord.ui.Select,
        placeholder="Choose the district you patrolled in",
        min_values=1,
        max_values=1,
        options=[SelectOption(label="Financial"), SelectOption(label="Waterfront")],
    )
    async def select_callback(self, interaction: Interaction, select: Select):
        form = Log_Form(district=select.values[0])
        await interaction.response.send_modal(form)
