from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SpeakNextcordBot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "nextcord",
    ],
    description="A python package for adding speak interaction slash command to a Nextcord bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Appez",
    author_email="appez@appez.cafe",
    url="https://github.com/Rs-appez/interaction_discord_bot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.12",
    keywords="discord bot slash_command interaction speak",
    license="GPL-3.0-only",
)
