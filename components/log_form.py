import time
from discord.ui import Modal, TextInput
from discord import Interaction, TextStyle
from data import Data


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
        label="Start Time (GMT/UTC)",
        required=True,
        placeholder="hh:mm",
        min_length=5,
        max_length=5,
        style=TextStyle.short,
    )
    end_time = TextInput(
        label="End Time (GMT/UTC)",
        required=True,
        placeholder="hh:mm",
        min_length=5,
        max_length=5,
        style=TextStyle.short,
    )
    screenshots = TextInput(
        label="Screenshot Links",
        required=True,
        placeholder="Attach screenshot links so that we can update the registry of your patrol logs, kills and arrests",
        style=TextStyle.paragraph,
    )
    async def on_submit(self, interaction: Interaction):
        # Checks if the unit number is integers only
        try:
            int(self.unit_number.value)
        except ValueError:
            await interaction.response.send_message(
                "```diff\n-Error: Invalid unit number input```Please try again"
            )
            return
        # Checks if the time input is valid format
        try:
            t1 = time.strptime(self.start_time.value, "%H:%M")
            t2 = time.strptime(self.end_time.value, "%H:%M")
            if (t2.tm_hour*60+t2.tm_min) - (t1.tm_hour*60+t1.tm_min) <= 0:
                raise Exception("```diff\n-Error: Invalid time input, end time must be greater than start time```Please try again")
        except ValueError:
            await interaction.response.send_message(
                "```diff\n-Error: One of your time inputs are entered incorrectly```Please try again"
            )
            return
        except Exception as e:
            await interaction.response.send_message(e)
            return
        data = Data(discord_user=str(interaction.user), district=self.district,name=self.name.value, unit_number=self.unit_number.value, start_time=self.start_time.value, end_time=self.end_time.value, screenshots=self.screenshots.value)
        await data.submit_confirmation()
        await interaction.response.send_message(
            f"```diff\n+Success: Thank you for submitting your patrol log {interaction.user}```"
        )
