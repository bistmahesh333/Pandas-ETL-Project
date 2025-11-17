# src/db/connection.py
import configparser
from sqlalchemy import create_engine
import os

def get_engine():
    """
    Create and return a SQLAlchemy engine using config from database.ini
    """
    # Path to database.ini relative to this file
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'config', 'database.ini')
    
    # Load database configuration
    config = configparser.ConfigParser()
    config.read(config_path)
    
    db_config = config['postgres']
    user = db_config['user']
    password = db_config['password']
    host = db_config['host']
    port = db_config['port']
    database = db_config['database']
    
    # Create SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
    return engine
