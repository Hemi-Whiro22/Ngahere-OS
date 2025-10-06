from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv("backend/mauri/.env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def check_tables():
    # Example: check pdf_summaries table exists
    try:
        response = supabase.table("pdf_summaries").select("*").limit(1).execute()
        print("✅ pdf_summaries table found")
    except Exception as e:
        print("⚠️ Could not access pdf_summaries:", e)

if __name__ == "__main__":
    check_tables()

