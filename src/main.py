from db.connection import get_engine
from etl.combined_room_section import run_room_section_pipeline
from etl.transform import join_room_section  # Import transform function

def main():
    engine = get_engine()
    
    # Run Room-Section ETL pipeline
    print(run_room_section_pipeline(engine))
    
    # Run join_room_section transform separately (comment if not needed)
    # df_combined = join_room_section(engine)
    # print(df_combined.head())

if __name__ == "__main__":
    main()
