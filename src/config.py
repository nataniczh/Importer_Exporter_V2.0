from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_SERVER: str
    DB_NAME: str
    DB_DRIVER: str
    INITIAL_CATALOG: str
    TRUSTED_CONNECTION: str
    LOCAL_DB_NAME: str
    LOCAL_DB_KEY:str
    

    @property
    def REMOTE_DATABASE_URL(self):
        return (
            f"mssql+pyodbc://{self.DB_SERVER}/{self.INITIAL_CATALOG}?"
            f"driver={self.DB_DRIVER}&"
            f"Trusted_Connection={self.TRUSTED_CONNECTION}"
        )
        
    @property
    def LOCAL_DATABASE_URL(self):
        return(
            f"sqlite+pysqlcipher://:{self.LOCAL_DB_KEY}@/{self.LOCAL_DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()