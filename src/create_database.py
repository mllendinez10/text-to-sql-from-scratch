"""
Create the SQLite database

The script will:
- Create all tables manually with defined data types.
- Define primary-key and foreign-key constraints.
- Read the product data from Tables.xlsx.
- Insert the Excel data into the corresponding SQLite tables.
- Skip the "Data Dictionary" sheet.

Run this file when the Excel data changes.
"""

from pathlib import Path
import sqlite3
import pandas as pd


# ---------------------------------------------------------------------------
# File paths
# ---------------------------------------------------------------------------

EXCEL_FILE = Path("data/Tables.xlsx")
DATABASE_FILE = Path("database/products.db")


# ---------------------------------------------------------------------------
# Create database tables
# ---------------------------------------------------------------------------

def create_tables(connection):

    # Channel
    connection.execute("""
        CREATE TABLE channel (
            channel_item_number_pk INTEGER PRIMARY KEY,
            designation TEXT NOT NULL,
            length REAL,
            material TEXT,
            coating_material TEXT,
            coating_standard TEXT,
            source_document TEXT,
            source_page INTEGER
        );
    """)

    # Channel technical data
    connection.execute("""
        CREATE TABLE channel_technical_data (
            channel_item_number_fk INTEGER,
            channel_technical_data_id_pk INTEGER PRIMARY KEY,
            t REAL,
            weight REAL,
            fy REAL,
            area REAL,
            ix REAL,
            iy REAL,
            sx REAL,
            sy REAL,
            rx REAL,
            ry REAL,
            ix_eff REAL,
            iy_eff REAL,
            sx_eff REAL,
            sy_eff REAL,
            mal_x REAL,
            phi_ml_x REAL,
            mal_y REAL,
            phi_ml_y REAL,
            mad_x REAL,
            phi_md_x REAL,
            mad_y REAL,
            phi_md_y REAL,
            va_x REAL,
            phi_v_x REAL,
            va_y REAL,
            phi_v_y REAL,
            lu REAL,
            j REAL,
            cw REAL,
            x0 REAL,
            y0 REAL,
            r0 REAL,
            source_document TEXT,
            source_page INTEGER,

            FOREIGN KEY (channel_item_number_fk)
                REFERENCES channel(channel_item_number_pk)
        );
    """)

    # Connector
    connection.execute("""
        CREATE TABLE connector (
            designation TEXT NOT NULL,
            material TEXT,
            connector_item_number_pk INTEGER PRIMARY KEY,
            material_standard TEXT,
            coating_method TEXT,
            source_document TEXT,
            source_page INTEGER
        );
    """)

    # Connector torque
    connection.execute("""
        CREATE TABLE connector_torque (
            connector_item_number_fk INTEGER,
            connector_torque_id_pk INTEGER PRIMARY KEY,
            bolt_designation TEXT,
            torque REAL,
            source_document TEXT,
            source_page INTEGER,

            FOREIGN KEY (connector_item_number_fk)
                REFERENCES connector(connector_item_number_pk)
        );
    """)

    # Connector resistance
    connection.execute("""
        CREATE TABLE connector_resistance (
            connector_item_number_fk INTEGER,
            source_document TEXT,
            source_page INTEGER,
            connector_resistance_id_pk INTEGER PRIMARY KEY,
            angle_connector_quantity INTEGER,
            installation_channel_designation TEXT,
            channel_connector_1_designation TEXT,
            channel_connector_1_quantity INTEGER,
            channel_connector_2_designation TEXT,
            channel_connector_2_quantity INTEGER,
            fx_positive REAL,
            fx_negative REAL,
            fy_positive REAL,
            fy_negative REAL,
            fz_positive REAL,
            fz_negative REAL,
            source_table TEXT,
            configuration_notes TEXT,

            FOREIGN KEY (connector_item_number_fk)
                REFERENCES connector(connector_item_number_pk)
        );
    """)

    print("Created all database tables.")


# ---------------------------------------------------------------------------
# Insert Excel data
# ---------------------------------------------------------------------------

def insert_excel_data(connection):

    sheets = pd.read_excel(
        EXCEL_FILE,
        sheet_name=None,
        engine="openpyxl"
    )

    for sheet_name, dataframe in sheets.items():

        # Skip metadata sheet
        if sheet_name == "Data Dictionary":
            continue

        dataframe.to_sql(
            sheet_name,
            connection,
            if_exists="append",
            index=False
        )

        print(f"Inserted {len(dataframe)} rows into: {sheet_name}")


# ---------------------------------------------------------------------------
# Create database
# ---------------------------------------------------------------------------

def create_database():

    # Delete old database
    if DATABASE_FILE.exists():
        DATABASE_FILE.unlink()

    # Make sure database folder exists
    DATABASE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Create/open SQLite database
    with sqlite3.connect(DATABASE_FILE) as connection:

        # Enable foreign-key checking
        connection.execute(
            "PRAGMA foreign_keys = ON;"
        )

        # Create empty tables
        create_tables(connection)

        # Insert Excel data
        insert_excel_data(connection)

    print(
        f"\nDatabase created: {DATABASE_FILE}"
    )


# ---------------------------------------------------------------------------
# Run script
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    create_database()