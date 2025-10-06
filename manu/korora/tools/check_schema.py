"""
Kororā Database Schema Checker
Updated for Ngahere-OS with Korito integration
"""

import sys
from pathlib import Path

# Add korito to path
sys.path.append(str(Path(__file__).parent.parent / "kaitiaki" / "korito"))
from loader import get_korito_secret

try:
    from supabase import create_client
    import os
except ImportError:
    print("⚠️ Supabase not installed. Install with: pip install supabase")
    sys.exit(1)

def check_database_connection():
    """Kororā checks database connection using Korito's secrets"""
    try:
        # Get secrets from Korito's heart
        supabase_url = get_korito_secret("SUPABASE_URL")
        supabase_key = get_korito_secret("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            print("❌ Kororā: Missing Supabase credentials in Korito's heart")
            return False
        
        # Create Supabase client
        supabase = create_client(supabase_url, supabase_key)
        
        print("🐧 Kororā: Database connection established")
        return supabase
        
    except Exception as e:
        print(f"❌ Kororā: Database connection failed: {e}")
        return False

def check_ngahere_tables():
    """Kororā checks all Ngahere-OS tables"""
    supabase = check_database_connection()
    if not supabase:
        return
    
    # Ngahere-OS essential tables
    ngahere_tables = [
        "audit_logs",           # Kererū's audit logs
        "kaitiaki_actions",     # All kaitiaki actions
        "prompt_history",       # Pīwakawaka's prompt history
        "data_backups",         # Pūkeko's data backups
        "security_events",      # Kahu's security logs
        "health_metrics",       # Tauhou's health data
        "communications",       # Riroriro's messages
        "migrations"            # Kororā's migration history
    ]
    
    print("🐧 Kororā: Checking Ngahere-OS database schema...")
    
    for table in ngahere_tables:
        try:
            response = supabase.table(table).select("*").limit(1).execute()
            print(f"✅ {table} table found")
        except Exception as e:
            print(f"⚠️ Could not access {table}: {e}")

def check_korito_connection():
    """Kororā checks Korito's heart connection"""
    try:
        secrets = get_korito_secret("SUPABASE_URL")
        if secrets:
            print("🌲 Kororā: Korito's heart is connected")
            return True
        else:
            print("❌ Kororā: Korito's heart not found")
            return False
    except Exception as e:
        print(f"❌ Kororā: Cannot connect to Korito's heart: {e}")
        return False

if __name__ == "__main__":
    print("🐧 Kororā: Starting database schema check...")
    
    # Check Korito's heart first
    if check_korito_connection():
        # Check database tables
        check_ngahere_tables()
    else:
        print("❌ Kororā: Cannot proceed without Korito's heart")

