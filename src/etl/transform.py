# src/etl/transform.py
import pandas as pd

def join_room_section(engine):
    """
    Fetch all section data and join room_name from tbl_room using room_id.
    Returns a combined DataFrame.
    """
    try:
        # Step 1: Read section table
        section_query = "SELECT * FROM librarymanagement.tbl_section;"
        df_section = pd.read_sql(section_query, engine)
        print("Columns in tbl_section:", df_section.columns.tolist())

        # Step 2: Read only room_id and room_name from room table
        room_query = "SELECT room_id, room_name FROM librarymanagement.tbl_room;"
        df_room = pd.read_sql(room_query, engine)
        print("Columns in tbl_room:", df_room.columns.tolist())

        # Step 3: Join section with room_name on room_id
        if 'room_id' in df_section.columns and 'room_id' in df_room.columns:
            df_combined = pd.merge(df_section, df_room, on='room_id', how='left')
        else:
            print("No room_id to join on. Returning section table only.")
            df_combined = df_section

        return df_combined

    except Exception as e:
        print("ETL Error:", e)
        return pd.DataFrame()
