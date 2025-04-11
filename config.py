DEBUG = True  # Set to False for production environments

# Thresholds for tiers
TIERS = {
    "Gold": 1000,
    "Silber": 500,
    "Bronze": 0,
}

# Default admins
DEFAULT_ADMINS = [
]


# DB_URL = "sqlite://essencifai"
DB_URL="mssql://nordakademie_admin:Pass@12345@nordakademie-sql-database.database.windows.net:1433/nordakademie_sql_database?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no"
