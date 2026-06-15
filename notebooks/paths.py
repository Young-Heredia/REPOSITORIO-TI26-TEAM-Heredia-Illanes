"""Rutas compartidas para los notebooks del proyecto TI26."""
from pathlib import Path

# Carpeta raíz del repositorio (un nivel arriba de notebooks/)
REPO_ROOT = Path(__file__).resolve().parent.parent

# CSV originales de Kaggle (subcarpeta con el nombre del zip descargado)
RAW_DATA_DIR = REPO_ROOT / "data" / "raw" / "CRM + Sales + Opportunities"

# Datos procesados y modelos entrenados
PROCESSED_DIR = REPO_ROOT / "data" / "processed"

CSV_FILES = {
    "accounts": RAW_DATA_DIR / "accounts.csv",
    "products": RAW_DATA_DIR / "products.csv",
    "sales_teams": RAW_DATA_DIR / "sales_teams.csv",
    "sales_pipeline": RAW_DATA_DIR / "sales_pipeline.csv",
    "data_dictionary": RAW_DATA_DIR / "data_dictionary.csv",
}
