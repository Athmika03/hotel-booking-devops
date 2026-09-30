from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("hotel.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "hotel-booking-api"
    })


@app.route("/hotels")
def hotels():
    connection = get_db_connection()

    hotels = connection.execute(
        "SELECT * FROM hotels"
    ).fetchall()

    connection.close()

    return jsonify([dict(hotel) for hotel in hotels])


@app.route("/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO bookings (hotel_id, guest_name, check_in, check_out)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["hotel_id"],
            data["guest_name"],
            data["check_in"],
            data["check_out"]
        )
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Booking created successfully"
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)