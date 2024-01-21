from mongoengine import connect
import configparser
import urllib.parse

config = configparser.ConfigParser()
config.read("config.ini")

mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

escaped_username = urllib.parse.quote_plus(mongo_user)
escaped_password = urllib.parse.quote_plus(mongodb_pass)

# As you may see, I changed the amount of pools because I had issues with connection
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@{domain}/?retryWrites=true&w=majority&maxPoolSize=100"

connect(db=db_name, host=uri)
