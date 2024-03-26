from config import DotFile, Env, EnvConfig

config = EnvConfig(DotFile(".env-dev", Env.LOCAL))

DB_NAME = config("DB_NAME", str, default="game-api")
DB_HOST = config("DB_HOST", str)

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRES = 10  # minutes
REFRESH_TOKEN_EXPIRES = 5  # days
