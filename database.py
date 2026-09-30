import sqlite3


def create_database():
    connection = sqlite3.connect("hotel.db")

    cursor = connection.cursor()

    # Create hotels table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hotels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL
        )
    """)

    # Add sample hotels
    cursor.execute("""
        INSERT INTO hotels (name, city)
        SELECT 'Grand Palace', 'Bangalore'
        WHERE NOT EXISTS (
            SELECT 1 FROM hotels WHERE name = 'Grand Palace'
        )
    """)

    cursor.execute("""
        INSERT INTO hotels (name, city)
        SELECT 'Ocean View', 'Mangalore'
        WHERE NOT EXISTS (
            SELECT 1 FROM hotels WHERE name = 'Ocean View'
        )
    """)

    # Create bookings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hotel_id INTEGER NOT NULL,
            guest_name TEXT NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL,
            FOREIGN KEY (hotel_id) REFERENCES hotels(id)
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")