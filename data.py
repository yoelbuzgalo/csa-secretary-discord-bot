from config import bot, channel_id, sheet
from discord import Embed
import json

print(sheet.sheet1.get('A1'))

class Data:
    def __init__(self, discord_user: str,district: str, name: str, unit_number: int, start_time: str, end_time: str, total_kills: int = None):
        self.discord_user = discord_user
        self.district = district
        self.name = name
        self.unit_number = unit_number
        self.start_time = start_time
        self.end_time = end_time
        self.total_kills = total_kills
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