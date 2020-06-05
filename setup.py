from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="bot",
    packages=["bot"],
    entry_points={
        "console_scripts": [
            "bot = bot.tele_bot:main",
            ],
        },
    )
