from fastapi import APIRouter
from pydantic import BaseModel
from kaitiaki.korora.korora import Korora

router = APIRouter()
korora = Korora()

class DatabaseConnectionInput(BaseModel):
    connection_string: str
    database_name: str

class MigrationInput(BaseModel):
    migration_name: str
    migration_sql: str

class SchemaValidationInput(BaseModel):
    schema_name: str
    schema_definition: dict

@router.get("/")
async def korora_status():
    """Kororā status - the database keeper is managing"""
    return korora.get_status()

@router.get("/database")
async def get_database_status():
    """Kororā's database management status"""
    return korora.get_database_status()

@router.get("/migrations")
async def get_migration_history():
    """Kororā's migration history"""
    return korora.get_migration_history()

@router.post("/connect")
async def manage_connection(data: DatabaseConnectionInput):
    """Kororā manages database connection"""
    result = korora.manage_database_connection(data.connection_string, data.database_name)
    return {
        "kaitiaki": korora.name,
        "action": "connection_managed",
        "result": result
    }

@router.post("/migrate")
async def run_migration(data: MigrationInput):
    """Kororā runs database migration"""
    result = korora.run_migration(data.migration_name, data.migration_sql)
    return {
        "kaitiaki": korora.name,
        "action": "migration_run",
        "result": result
    }

@router.post("/validate")
async def validate_schema(data: SchemaValidationInput):
    """Kororā validates database schema"""
    result = korora.validate_schema(data.schema_name, data.schema_definition)
    return {
        "kaitiaki": korora.name,
        "action": "schema_validated",
        "result": result
    }
