DEBUG = True  # Set to False for production environments

# Thresholds for tiers
TIERS = {
    "Gold": 1000,
    "Silber": 500,
    "Bronze": 0,
}

# Default admins
DEFAULT_ADMINS = [
    "653799c4-e7ea-4f28-b64d-b545e0700048",
    "78c4c12b-afb8-43eb-8111-364a4eaff302",
]


DB_URL = "sqlite://essencifai"
# DB_URL="mssql://nordakademie_admin:Pass@12345@nordakademie-sql-database.database.windows.net:1433/nordakademie_sql_database?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no"
