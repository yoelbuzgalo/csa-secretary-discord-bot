from config import bot, channel_id
class Data:
    def __init__(self, user, name: str, unit_number: int, start_time: str, end_time: str, total_kills: int = None):
        # self.user = user # TODO: Finish here the user, specify what data type in the parameters
        self.name = name
        self.unit_number = unit_number
        self.start_time = start_time
        self.end_time = end_time
        self.total_kills = total_kills
    # Sends to the channel ID specified in config a message when a form is submitted
    async def submit_confirmation(self):
        self.channel = bot.get_channel(channel_id)
        await self.channel.send(f'Test') # TODO: Finish here the statement for server logging