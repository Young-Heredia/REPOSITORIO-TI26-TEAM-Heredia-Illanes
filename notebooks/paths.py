"""Rutas y funciones de limpieza compartidas — proyecto TI26."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = REPO_ROOT / "data" / "raw" / "CRM + Sales + Opportunities"
PROCESSED_DIR = REPO_ROOT / "data" / "processed"

CSV_FILES = {
    "accounts": RAW_DATA_DIR / "accounts.csv",
    "products": RAW_DATA_DIR / "products.csv",
    "sales_teams": RAW_DATA_DIR / "sales_teams.csv",
    "sales_pipeline": RAW_DATA_DIR / "sales_pipeline.csv",
    "data_dictionary": RAW_DATA_DIR / "data_dictionary.csv",
}


def clean_accounts(df):
    """Corrige typos en accounts.csv."""
    df = df.copy()
    df["sector"] = df["sector"].replace({"technolgy": "technology"})
    df["office_location"] = df["office_location"].replace({"Philipines": "Philippines"})
    df["subsidiary_of"] = df["subsidiary_of"].fillna("None")
    return df


def clean_pipeline(df):
    """Corrige nombre de producto inconsistente en sales_pipeline.csv."""
    df = df.copy()
    df["product"] = df["product"].replace({"GTXPro": "GTX Pro"})
    return df


def load_crm_tables():
    """Carga y limpia las 4 tablas principales del CRM."""
    import pandas as pd

    accounts = clean_accounts(pd.read_csv(CSV_FILES["accounts"]))
    products = pd.read_csv(CSV_FILES["products"])
    sales_teams = pd.read_csv(CSV_FILES["sales_teams"])
    pipeline = clean_pipeline(pd.read_csv(CSV_FILES["sales_pipeline"]))
    return accounts, products, sales_teams, pipeline


def merge_crm_tables(accounts, products, sales_teams, pipeline):
    """Une pipeline con accounts, products y sales_teams."""
    df = pipeline.merge(accounts, on="account", how="left")
    df = df.merge(products, on="product", how="left")
    df = df.merge(sales_teams, on="sales_agent", how="left")
    return df
