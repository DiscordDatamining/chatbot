from requests import get, post
from terminut import log
from client import Client, URL
from json import dumps
import random
import requests
import json


class discord:
    def __init__(self: "discord"):
        self.client = Client
        self.typing = URL.typing
        self.messages: str = URL.messages
        self.channel: int = Client.channel
        self.log = log
        self.post = post
        self.get = get

    def get_message(self: "discord") -> None:
        """
        Gets a random message from client/messages.txt and returns it
        """
        try:
            with open(
                "client/messages.txt", "r", encoding="utf-8", errors="replace"
            ) as file:
                messages = file.readlines()
                if messages:
                    message = random.choice(messages)
                    self.log.success(f"Got message! {message.strip()}")
                    return message
                else:
                    self.log.error("No messages found in messages.txt")
        except FileNotFoundError:
            self.log.error("messages.txt not found.")
        except Exception as e:
            self.log.error(f"Error reading message: {e}")
            return None

    def fetch_messages(self: "discord") -> None:
        """
        Fetches messages from a Discord channel and saves them to messages.txt
        """
        try:
            headers = {
                "Authorization": f"{self.client.token}",
            }

            params = {
                "limit": 100,
            }

            response = self.get(
                url=self.messages,
                headers=headers,
                params=params,
            )

            if response.status_code == 200:
                messages = response.json()

                with open("client/messages.txt", "a", encoding="utf-8") as file:
                    for message in messages:
                        file.write(f"{message['content']}\n")

                self.log.success("Messages saved to client/messages.txt")
            else:
                self.log.error(
                    f"Error fetching messages. Status code: {response.status_code}"
                )
                self.log.error(response.text)

        except Exception as e:
            self.log.error(f"Error fetching and saving messages: {e}")

    def send(self: "discord") -> None:
        """
        Sends the message payload
        """
        try:
            type = self.post(
                url=self.typing,
                headers={
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Authorization": f"{self.client.token}",
                    "Content-Length": "0",
                    "Cookie": "__dcfduid=6b31cb807f2f11ee892f65369dc0b9e0; __sdcfduid=6b31cb817f2f11ee892f65369dc0b9e0672781e55c6484ab24b301eb21143c1a32de242ba07289b1bc78ec756c38b072; _cfuvid=PIxkWSqpucz0fImkLwwBQpoeBUC4F9o9XyBDCT507dk-1701650995052-0-604800000; cf_clearance=G9xpEwXAsTfpANMtREjypKfOWENDegk3cNQCZanZaKo-1701651005-0-1-4ff3f30d.65f04045.44c7494f-0.2.1701651005; __cfruid=8a235a3d3e74c59eeaf724527c01ba7c738fc633-1701652007",
                    "Origin": "https://discord.com",
                    "Referer": f"https://discord.com/channels/{self.client.channel}/{self.client.guild}",
                    "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                    "X-Debug-Options": "bugReporterEnabled",
                    "X-Discord-Locale": "en-US",
                    "X-Discord-Timezone": "America/Chicago",
                    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI1MDgzMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
                },
            )
            self.log.debug("Currently trying to type on the channel..")
            if type.status_code == 204:
                try:
                    message = self.get_message()
                    self.log.success("Successfully typed! Moving to message protocol.")
                    payload = self.post(
                        url=self.messages,
                        headers={
                            "Accept": "*/*",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Authorization": f"{self.client.token}",
                            "Content-Length": "103",
                            "Content-Type": "application/json",
                            "Cookie": "__dcfduid=6b31cb807f2f11ee892f65369dc0b9e0; __sdcfduid=6b31cb817f2f11ee892f65369dc0b9e0672781e55c6484ab24b301eb21143c1a32de242ba07289b1bc78ec756c38b072; _cfuvid=PIxkWSqpucz0fImkLwwBQpoeBUC4F9o9XyBDCT507dk-1701650995052-0-604800000; cf_clearance=G9xpEwXAsTfpANMtREjypKfOWENDegk3cNQCZanZaKo-1701651005-0-1-4ff3f30d.65f04045.44c7494f-0.2.1701651005; __cfruid=8a235a3d3e74c59eeaf724527c01ba7c738fc633-1701652007",
                            "Origin": "https://discord.com",
                            "Referer": f"https://discord.com/channels/{self.client.channel}/{self.client.guild}",
                            "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                            "Sec-Ch-Ua-Mobile": "?0",
                            "Sec-Ch-Ua-Platform": '"Windows"',
                            "Sec-Fetch-Dest": "empty",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Site": "same-origin",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                            "X-Debug-Options": "bugReporterEnabled",
                            "X-Discord-Locale": "en-US",
                            "X-Discord-Timezone": "America/Chicago",
                            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI1MDgzMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
                        },
                        json={
                            "mobile_network_type": "unknown",
                            "content": f"{message}",
                            "tts": "false",
                            "flags": 0,
                        },
                    )
                    json_response = payload.json()

                    if payload.status_code == 200:
                        self.log.success(f"Sent message successfully ({message})")
                    else:
                        return self.log.fatal(f"Uncaught error! {json_response}")

                except Exception as e:
                    self.log.error(f"Error! {e}")

        except Exception as e:
            self.log.error(f"Error sending message: {e}")
