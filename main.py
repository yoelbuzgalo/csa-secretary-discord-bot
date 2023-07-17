from config import bot, token
from components.select_district import Select_District
from discord import ButtonStyle, Interaction
from discord.ui import Button, View


@bot.event
async def on_ready():
    print("CSA Sheriffs Department Secretary Bot is up and running!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Error syncing, error: {e}")


# Handles user request, when user types in "/log"
@bot.tree.command(name="log")
async def handle_log_request(interaction: Interaction):
    user = interaction.user
    button = Button(label="Submit a patrol log", style=ButtonStyle.green, emoji="📋")
    button.callback = send_log_form_for_completion
    view = View()
    view.add_item(button)
    if interaction.guild:
        await interaction.response.send_message("Thank you for requesting a patrol log form! I have sent it to you in the DMs", ephemeral=True)
    else:
        await interaction.response.send_message("Thank you for requesting a patrol log form!")
    await user.send(
        f"Hello {user}!\nPlease be advised that this is a CSA sheriff discord bot. Any fraudulent or misuse of this tool is forbidden and can be reviewed by CSA sheriff officers.\nAcknowledging that, what would you like to do?",
        view=view,
    )

# Send back to user the form when created with class
async def send_log_form_for_completion(interaction: Interaction):
    await interaction.response.send_message(view=Select_District())

def run_app():
    bot.run(token)

if __name__ == "__main__":
    run_app()
