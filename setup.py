from setuptools import setup, find_packages

setup(
    name="interaction_discord_bot",
    version="0.1.13",
    packages=find_packages(),
    install_requires=[
        "nextcord",
    ],
    description="cog for discord bot interaction with user",
    author="Appez",
)
