import discord
from discord.ext import commands
from discord import app_commands

token = '[token you get from discord dev portal]' #token you get from the bot tab in the discord dev portal
intents = discord.Intents.default() #declaring that you're using default discord intents (permissions to access certain events)
intents.message_content = True #declaring privileged intent (special perms)

class Client(commands.Bot): #declaring Bot class
    async def on_ready(self): #when the bot is online (if everything went smoothly) run the next line of code
        print("[any message you want]") #prints in the TERMINAL any msg you want, for example something like "bot is running". its a string, it can be anything

        try:  #if the bot is running, try to run the next line of code
            synced = await self.tree.sync() #sync the slash commands
            print(f"[{len(synced)} number oif commands are ready]") #prints in the TERMINAL a message that indicates how many slash commands have been synced (if they're available or not)

        except Exception as e: #if the bot cant run, print the next line of code
            print(f"[bot didnt work because: ]", e) #print a message saying bot didnt work, also prints the error msg in the TERMINAL

    async def on_message(self, message): #when the bot sees a message in chat:
            if message.author == self.user: #if the author of the msg was bot-kun itself, then...
                return #... ignore it
            
            if message.content.startswith("[trigger message]"): #if the msg contains a certain word...
                await message.channel.send(f"[the msg you want the bot to say]") #... the bot sends a message saying something

        
client = Client(command_prefix='!', intents=intents) #make it so commands need to have the '!' symbol at the start (can be anything else if you want).
                                                     #I wont be using '!' commands tho cuz they're lame and slash commands are a lot cooler (since they can be used in dms)

#the following are all slash commands:

#command to make the bot say something
@client.tree.command(name="[title]", description="[description]") #command's name and description, for example /gif or smth
@app_commands.allowed_installs(guilds=True, users=True) #who can use this command? only guild members or people in general?
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) #where can this command be used?
async def ears(interaction: discord.Interaction): #when the command is triggered...
    await interaction.response.send_message("[msg you want the bot to say]") #...the bot says something


#command that sends gifs or images (its the same thing as before, you dumbahh weezo)
@client.tree.command(name="[title]", description="[description]") #command's name and description
@app_commands.allowed_installs(guilds=True, users=True) #who can use this command? only guild members or people in general?
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) #where can this command be used?
async def no (interaction: discord.Interaction): #when the command is triggered...
    await interaction.response.send_message("[link to the gif or img]") ##...the bot says something. you only need to put the link here cuz discord embed's them automatically


#command to make the bot say what you want it to say (/echo text: peepeepoopoo or something idfk)
@client.tree.command(name="[title]", description="[description]") #command's name and description
@app_commands.allowed_installs(guilds=True, users=True) #who can use this command? only guild members or people in general?
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) #where can this command be used?
async def echo(interaction: discord.Interaction, echo: str): #when the command is triggered and the user has filled in the 'text' field...
    await interaction.response.send_message(echo) #...the bot says whatever was in the text field


#command to make the bot send an embedded message
@client.tree.command(name="[title]", description="[description]") #command's name and description
@app_commands.allowed_installs(guilds=True, users=True) #who can use this command? only guild members or people in general?
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) #where can this command be used?
async def carrd(interaction: discord.Interaction): #when the command is triggered...
    embed = discord.Embed(title = "[embed's title]", url="[the link embedded in the title]", description= "[embed's description]", color= discord.Colour.light_theme()) #set the embed's properties. for the colour, look it up online
    embed.set_thumbnail(url="[link to the image thats going to be the embed's thumbnail]") #set the embed's thumbnail
    await interaction.response.send_message(embed = embed) #... the bot sends the embedded msg


client.run(token) #runs the bot using the token defined at the start