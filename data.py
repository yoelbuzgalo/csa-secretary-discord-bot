from config import bot, channel_id, sheet
from discord import Embed
import json

class Data:
    def __init__(self, discord_user: str,district: str, name: str, unit_number: int, start_time: str, end_time: str, screenshots: str):
        self.discord_user = discord_user
        self.district = district
        self.name = name
        self.unit_number = unit_number
        self.start_time = start_time
        self.end_time = end_time
        self.screenshots = screenshots
    # Sends to the channel ID specified in config a message when a form is submitted
    async def submit_confirmation(self):
        self.channel = bot.get_channel(channel_id)
        self.embedded_patrol_log = Embed(
            title=f"📋Patrol Log #{self.get_patrol_ID()}",
            description=f"{self.discord_user} has submitted a patrol log!",
        )
        self.embedded_patrol_log.add_field(name="Claimed Unit Number", value=self.unit_number)
        self.embedded_patrol_log.add_field(name="District", value=self.district)
        await self.channel.send(embed=self.embedded_patrol_log)
        self.submit_to_sheet()
        self.update_patrol_ID()

    @staticmethod
    def get_patrol_ID():
        with open("history.json", "r") as file:
            file_dict = json.loads(file.read())
            file.close()
            return file_dict.get("patrol_id")
    @staticmethod
    def update_patrol_ID():
        prev_patrol_ID = int(Data.get_patrol_ID())
        with open("history.json", "w") as file:
            new_dict = {
                "patrol_id": prev_patrol_ID + 1
            }
            file.write(json.dumps(new_dict))
            file.close()

    def submit_to_sheet(self):
        my_sheet = sheet.sheet1
        row = len(my_sheet.get_all_records())
        print(row)
        arr = [self.get_patrol_ID(), self.discord_user, self.district, self.name, self.unit_number, self.start_time, self.end_time, self.screenshots]
        my_sheet.update('A2:H2', [arr])
