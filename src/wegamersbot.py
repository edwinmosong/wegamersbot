# wegamers.py
# Entry point for the wegamersbot.
# Author: Edwin Mo Song
# Date: 02/05/2017
import datetime
import json
import logging
import os
import os.path

import discord
import asyncio


class WeGamersBot(discord.Client):
    def __init__(self, logger=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logger or self.set_logging()
        self._dbconn = None # TODO

    @classmethod
    def set_logging(cls, logger_name="wegamersbot", filename="discord.log"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename=filename, encoding="utf-8",
                                      mode="w")
        handler.setFormatter(logging.Formatter(
            '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
        return logger

    @classmethod
    def get_discord_token(cls, secrets_file="~/.secrets",
                          secret_key="wegamers"):
        """
        May deprecate this for a better way of passing down the Discord token
        key.
        """
        with open(os.path.expanduser(secrets_file)) as secrets_file:
            return json.load(secrets_file)[secret_key]

    @asyncio.coroutine
    def on_ready(self):
        self._logger.debug({"status": "on_ready",
                            "msg": "logged in as user and id",
                            "user": self.user.name,
                            "id": self.user.id})
        self._startup = datetime.datetime.now()
        message = "Waking up at %s" % str(self._startup)

        channels = yield from self.get_all_channels()
        for channel in channels:
            if channel.name.lower() == "dev":
                self._logger.debug({"action": "send msg to channel",
                                    "channel": channel.name,
                                    "message": message})
                yield from self.send_message(startup_channel, message)
            else:
                self._logger.debug({"action": "channel does not match 'dev'",
                                    "channel": channel.name})

    def run(self, discord_token=None, *args, **kwargs):
        self._logger.info({"status": "starting WeGamersBot."})
        self._discord_token = discord_token or self.get_discord_token()
        super().run(self._discord_token, *args, **kwargs)


if __name__ == "__main__":
    WeGamersBot().run()
