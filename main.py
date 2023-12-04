from discord import discord
from time import sleep

discord().fetch_messages()

while True:
    discord().send()
    sleep(4.5)
