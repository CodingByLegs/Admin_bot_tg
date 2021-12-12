from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
#IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
PG_USER = env.str("pg_user")
PG_PASS = env.str("pg_password")
PG_IP = env.str("pg_ip")
