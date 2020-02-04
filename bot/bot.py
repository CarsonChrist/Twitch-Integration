from twitchio.ext import commands
import requests


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token='oauth:csdaxq2uffzl42c7j81uhw3b5x5g4i', client_id='z8tbyizegphc4jsnjlrhwlx271fu5z',
                         nick='HollowGlow', prefix='!',
                         initial_channels=['madcar'])

        self.server_url = "http://127.0.0.1:5000"

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        await self.handle_commands(message)

    @commands.command(name='moron')
    async def left(self, ctx):
        print("left")
        requests.get(self.server_url + "/left")

    @commands.command(name='genius')
    async def right(self, ctx):
        print("right")
        requests.get(self.server_url + "/right")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
