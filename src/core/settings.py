from config import DotFile, Env, EnvConfig

config = EnvConfig(DotFile(".env-dev", Env.LOCAL))

DB_NAME = config("DB_NAME", str, default="game-api")
DB_HOST = config("DB_HOST", str)
