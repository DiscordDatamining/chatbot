"""
Configuration
"""


class Client:
    guild: int = 898237461904375968
    channel: int = 1180612641954213888
    token: str = ""


class URL:
    Client: Client

    typing: str = f"https://discord.com/api/v9/channels/{Client.channel}/typing"
    messages: str = f"https://discord.com/api/v9/channels/{Client.channel}/messages"
