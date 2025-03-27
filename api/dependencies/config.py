class conf:
    host = "localhost"
    database = "sandwich_maker_api"
    port = 3306
    user = "root"
    password = "Zohal2003"


#Create an instance of the configuration class
conf = conf()

# Generate the SQLAlchemy database URL dynamically
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{conf.user}:{conf.password}@{conf.host}:{conf.port}/{conf.database}"