from sqlalchemy import create_engine

usuario = "admin"
senha = "admin"
host = "localhost"
porta = "5432"
banco = "pipeline_db"

engine = create_engine(
    f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}"
)

print("Conexão criada com sucesso!")
