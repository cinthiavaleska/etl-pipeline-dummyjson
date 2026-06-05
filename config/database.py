from sqlalchemy import create_engine

# =========================================================
# CONFIGURAÇÕES DE CONEXÃO
# =========================================================

usuario = "admin"
senha = "admin"
host = "postgres"
porta = "5432"
banco = "ecommerce"

engine = create_engine(
    f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}"
)