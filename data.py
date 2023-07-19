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
        try:
            if self.submit_to_sheet():
                self.channel = bot.get_channel(channel_id)
                self.embedded_patrol_log = Embed(
                title=f"📋Patrol Log #{self.get_patrol_ID()}",
                description=f"{self.discord_user} has submitted a patrol log!",
                )
                self.embedded_patrol_log.add_field(name="Claimed Unit Number", value=self.unit_number)
                self.embedded_patrol_log.add_field(name="District", value=self.district)
                await self.channel.send(embed=self.embedded_patrol_log)
                self.update_patrol_ID()
        except Exception as e:
            print(f'There was an error trying to submit a confirmation message to the channel, error: {e}')

    # Opens and reads the history file to get the patrol ID
    @staticmethod
    def get_patrol_ID():
        with open("history.json", "r") as file:
            file_dict = json.loads(file.read())
            file.close()
            return file_dict.get("patrol_id")
        
    # Updates the history file upon successfully submitting the patrol log
    @staticmethod
    def update_patrol_ID():
        prev_patrol_ID = int(Data.get_patrol_ID())
        with open("history.json", "w") as file:
            new_dict = {
                "patrol_id": prev_patrol_ID + 1
            }
            file.write(json.dumps(new_dict))
            file.close()

    # Submits all of the data attributes to google sheet, returns True if successful otherwise False
    def submit_to_sheet(self)->bool:
        my_sheet = sheet.sheet1
        row = len(my_sheet.get_all_records())
        arr = [self.get_patrol_ID(), self.discord_user, self.district, self.name, self.unit_number, self.start_time, self.end_time, self.screenshots]
        try:
            my_sheet.update(f'A{row+2}:H{row+2}', [arr])
            return True
        except Exception as e:
            print(f'There was an error trying to submit to the google sheet:{e}')
            return False
