# src/etl/combined_room_section.py

import pandas as pd
from db.connection import get_engine

# -------------------------------
# Extract functions
# -------------------------------
def extract_rooms(engine):
    query = """
        SELECT room_id, room_name
        FROM librarymanagement.tbl_room;
    """
    return pd.read_sql(query, engine)

def extract_sections(engine):
    query = """
        SELECT section_cd, section_name, room_id
        FROM librarymanagement.tbl_section;
    """
    return pd.read_sql(query, engine)

# -------------------------------
# Transform function
# -------------------------------
def transform_room_section(df_rooms, df_sections):
    # Join sections with rooms on room_id
    df_combined = pd.merge(df_sections, df_rooms, on='room_id', how='left')
    
    # Keep only desired columns
    df_combined = df_combined[['section_cd', 'section_name', 'room_id', 'room_name']]
    
    return df_combined

# -------------------------------
# Load function
# -------------------------------
def load_room_section(engine, df, table_name="librarymanagement.tbl_room_section"):
    df.to_sql(table_name.split('.')[-1], engine, schema=table_name.split('.')[0],
              if_exists='replace', index=False)
    print(f"Data loaded into {table_name} successfully!")

# -------------------------------
# Full ETL pipeline
# -------------------------------
def run_room_section_pipeline(engine):
    try:
        # Extract
        df_rooms = extract_rooms(engine)
        df_sections = extract_sections(engine)
        
        # Transform
        df_combined = transform_room_section(df_rooms, df_sections)
        print("Transformation successful. Preview:")
        print(df_combined.head())
        
        # Load
        load_room_section(engine, df_combined)
        
    except Exception as e:
        print("ETL Error:", e)
