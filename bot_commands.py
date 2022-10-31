import discord
import os
from discord.ext import commands
import json

with open('data\\commands.json', 'r') as f:
    cmds = json.load(f)

with open('data\\config.json', 'r') as f:
    prefix = json.load(f)['discord']['Command-Prefix']


class Commands:
    def __init__(self, command):
        self.command = command.strip().lower()
        self.commands = cmds
        self.isCmd = False
        self.isAli = False
        self.cList = []
        self.aliases = []
        self.args = []
        self.descriptions = []
        self.usages = []

    def main(self) -> object:
        command = Commands(self, self.command)
        command.getCommands()
        command.getCommandPrefix()
        command.isAlias()
        command.isCommand()
        command.returnCommand()
        return command

    if __name__ == '__main__':
        main(None)

    def getCommands(self) -> None:
        for x in cmds:
            self.cList.append(x)
            self.args.append(cmds[x]['args'])
            self.aliases.append(cmds[x]['aliases'])
            self.descriptions.append(cmds[x]['description'])
            self.usages.append(cmds[x]['usage'])
        return

    def getCommandPrefix(self) -> None:
        with open('config.json', 'r') as f:
            prefix = json.load(f)['discord']['Command-Prefix']
            self.prefix = prefix
            return prefix

    def isCommand(self) -> bool:
        result = bool(
            [x for x in self.aliases if self.command in self.cList or self.command in x])
        self.isCmd = result
        return result

    def isAlias(self) -> bool:
        isAlias = bool(
            [alias for alias in self.aliases if self.command in alias])
        self.isAli = isAlias
        return isAlias

    def returnCommand(self) -> function:
        method_list = [method for method in dir(Commands) if callable(
            getattr(Commands, method)) and method.startswith('_') is False]
        print(method_list)
        if self.command in method_list:
            return
        return

    def writeToFile():
        with open('\\messages\\user_messages', 'w') as file:
            file.write()

    @bot.command
    async def help(self, ctx, *args) -> None:
        if args is not None and Commands(args).isCommand() is True or Commands(args).isAlias() is True:
            obj = Commands(args)
            await ctx.send(obj)
        await ctx.send(args)
        await ctx.send(cmd)
        return

    @bot.command
    async def jail(ctx) -> None:
        pass

    @bot.command
    async def record(ctx, args) -> None:
        pass

    @bot.command
    async def roar(ctx) -> None:
        pass


def printMenu():
    for x in cmds:
        embed = discord.Embed(
            title='Sentinel-bot Commands',
            description=cmds,
            color=discord.Colour(12)
        )
        embed.add_field(
            name=cmds[x],
            value='{0} \n{1}'.format(
                cmds[x]['usage'], cmds[x]['description'])
        )

        # def saveHistory(user, duration, start=0, end=0):


bot = commands.Bot(Commands.self.prefix,
                   intents=discord.Intents.default())
