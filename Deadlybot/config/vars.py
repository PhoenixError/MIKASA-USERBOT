# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from Deadlybot.config import Config
else:
    if os.path.exists("config.py"):
        from config import Development as Config

# Deadlybot
