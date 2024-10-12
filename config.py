import os
from dotenv import load_dotenv

ENV_FILES = ['.env', '.flaskenv']

def load_env():
    for env_file in ENV_FILES:
        env = os.path.join(os.getcwd(), env_file)

        if os.path.exists(env):
            load_dotenv(env)
