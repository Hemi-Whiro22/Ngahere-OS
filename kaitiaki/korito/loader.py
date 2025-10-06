import os
from pathlib import Path
from dotenv import load_dotenv

def load_rito():
    # explicitly load .rito file
    rito_path = Path(__file__).parent / ".env"
    if not rito_path.exists():
        raise FileNotFoundError(f"Missing .rito file at {rito_path}")
    
    load_dotenv(dotenv_path=rito_path)

    return {
        "SUPABASE_URL": os.getenv("SUPABASE_URL"),
        "SUPABASE_KEY": os.getenv("SUPABASE_KEY"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }
