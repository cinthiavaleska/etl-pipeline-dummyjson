from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "cinthia",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="dummyjson_etl_pipeline",
    description="""
    Pipeline ETL completo utilizando a API DummyJSON.
    Extração, transformação, modelagem Gold e carga
    em PostgreSQL utilizando Airflow.
    """,
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dummyjson", "etl", "postgres", "airflow"],
) as dag:
    dag.doc_md = """
    # DummyJSON ETL Pipeline

    Pipeline de Engenharia de Dados desenvolvido para estudo.

    ## Fluxo

    DummyJSON API → Raw → Silver → Gold → PostgreSQL → Power BI

    ## Tecnologias

    - Python
    - Pandas
    - PostgreSQL
    - Docker
    - Apache Airflow
    - Power BI
    """
    # =========================================================
    # EXTRACT
    # =========================================================

    extract_products = BashOperator(
        task_id="extract_products",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/extract/extract_products.py
        """
    )

    extract_users = BashOperator(
        task_id="extract_users",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/extract/extract_users.py
        """
    )

    extract_carts = BashOperator(
        task_id="extract_carts",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/extract/extract_carts.py
        """
    )

    # =========================================================
    # TRANSFORM
    # =========================================================

    transform_products = BashOperator(
        task_id="transform_products",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/transform/transform_products.py
        """
    )

    transform_users = BashOperator(
        task_id="transform_users",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/transform/transform_users.py
        """
    )

    transform_carts = BashOperator(
        task_id="transform_carts",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/transform/transform_carts.py
        """
    )

    # =========================================================
    # GOLD
    # =========================================================

    dim_products = BashOperator(
        task_id="dim_products",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/gold/dim_products.py
        """
    )

    dim_users = BashOperator(
        task_id="dim_users",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/gold/dim_users.py
        """
    )

    dim_address = BashOperator(
        task_id="dim_address",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/gold/dim_address.py
        """
    )

    fact_cart_items = BashOperator(
        task_id="fact_cart_items",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/gold/fact_cart_items.py
        """
    )

    # =========================================================
    # LOAD
    # =========================================================

    load_dim_products = BashOperator(
        task_id="load_dim_products",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/load/load_dim_products.py
        """
    )

    load_dim_users = BashOperator(
        task_id="load_dim_users",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/load/load_dim_users.py
        """
    )

    load_dim_address = BashOperator(
        task_id="load_dim_address",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/load/load_dim_address.py
        """
    )

    load_fact_cart_items = BashOperator(
        task_id="load_fact_cart_items",
        bash_command="""
        cd /opt/airflow &&
        PYTHONPATH=/opt/airflow python scripts/load/load_fact_cart_items.py
        """
    )

    # =========================================================
    # DEPENDÊNCIAS
    # =========================================================

    extract_products >> transform_products >> dim_products >> load_dim_products

    extract_users >> transform_users

    transform_users >> dim_users >> load_dim_users

    transform_users >> dim_address >> load_dim_address

    extract_carts >> transform_carts >> fact_cart_items >> load_fact_cart_items