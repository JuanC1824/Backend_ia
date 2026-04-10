import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = f"mysql+pymysql://avnadmin:{os.getenv('PASSWORD_BD')}@reporteloya-davyz2006-bbb8.k.aivencloud.com:11438/defaultdb?ssl_disabled=true"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=True   
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)