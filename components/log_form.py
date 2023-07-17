import time
from discord.ui import Modal, TextInput
from discord import Interaction, TextStyle
# from data import Data


# Log Form Class is inherited by Modal class imported w/ discord package, it reads all created class variables and appends the inherited modal class children.
class Log_Form(Modal):
    def __init__(self, district):
        super().__init__(title="Patrol Log")
        self.district = district

    name = TextInput(
        label="Name",
        required=True,
        placeholder="Enter Your Name",
        min_length=1,
        max_length=20,
        style=TextStyle.short,
    )
    unit_number = TextInput(
        label="Unit Number",
        required=True,
        placeholder="Enter Your Unit Number",
        min_length=4,
        max_length=4,
        style=TextStyle.short,
    )
    start_time = TextInput(
        label="Start Time (hh:mm)",
        required=True,
        placeholder="Example: 02:20",
        min_length=5,
        max_length=5,
        style=TextStyle.short,
    )
    end_time = TextInput(
        label="End Time (hh:mm)",
        required=True,
        placeholder="Example: 04:30",
        min_length=5,
        max_length=5,
        style=TextStyle.short,
    )
    total_kills = TextInput(
        label="Total Kills/Arrests",
        required=False,
        placeholder="(Optional)",
        min_length=0,
        max_length=3,
        style=TextStyle.short,
    )

    async def on_submit(self, interaction: Interaction):
        # Checks if the unit number is integers only
        try:
            int(self.unit_number.value)
        except ValueError:
            await interaction.response.send_message(
                "Invalid unit number input, please try again"
            )
            return
        # Checks if the time input is valid format
        try:
            time.strptime(self.start_time.value, "%H:%M")
            time.strptime(self.end_time.value, "%H:%M")
        except ValueError:
            await interaction.response.send_message(
                "One of your time inputs are entered incorrectly, please try again"
            )
            return
        # Check total kills if it is an integer only,
        if self.total_kills.value:
            try:
                num = int(self.total_kills.value)
                if num > 0:
                    await interaction.response.send_message(
                        "Please attach your screenshots of every round so that we can verify and record your kills"
                    )
                    return
            except ValueError as error:
                await interaction.response.send_message(f"Invalid input for kills")
                return
        # data = Data(name=self.name.value, unit_number=self.unit_number.value, start_time=self.start_time.value, end_time=self.end_time.value, total_kills=self.total_kills.value)
        # await data.submit_confirmation()
        await interaction.response.send_message(
            f"Recorded, thank you for submitting your patrol log {self.name}"
        )
