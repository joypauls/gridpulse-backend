from dotenv import load_dotenv
import os

load_dotenv()

EIA_API_KEY = os.getenv("EIA_API_KEY")
EIA_BASE_URL = "https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/"

if not EIA_API_KEY:
    raise RuntimeError("EIA_API_KEY not found in environment")
