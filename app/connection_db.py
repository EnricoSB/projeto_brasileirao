from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import time

# Carregar variáveis do .env
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Espera o banco iniciar
time.sleep(5)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print(f"Conectado ao PostgreSQL: {result.scalar()}")
except Exception as e:
    print(f"Erro ao conectar: {e}")
