from sqlalchemy import create_engine

USERNAME = "root"
PASSWORD = "Lakshu@27"
DATABASE = "traffic_violation_db"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DATABASE}"
)

def get_engine():
    return engine