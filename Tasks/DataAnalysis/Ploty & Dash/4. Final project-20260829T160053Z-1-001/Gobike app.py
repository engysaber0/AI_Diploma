"""
Ford GoBike Database Viewer — PyQt5 + PostgreSQL
--------------------------------------------------
A small desktop app to browse the star-schema database built in Part 1.

Requirements:
    pip install PyQt5 psycopg2-binary

Run:
    python gobike_app.py
"""

import sys
import psycopg2
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QLabel,
    QMessageBox, QHeaderView
)
from PyQt5.QtCore import Qt

DB_CONFIG = {
    "host": "127.0.0.1",
    "dbname": "gobike",
    "user": "postgres",
    "password": "alxgood000",
    "port": 5433,
}
print(repr(DB_CONFIG))

QUERIES = {
    "All trips (joined)": """
        SELECT f.trip_id, s1.station_name AS start_station, s2.station_name AS end_station,
               u.user_type, u.gender, u.age, f.duration_sec
        FROM fact_trips f
        JOIN dim_station s1 ON f.start_station_id = s1.station_id
        JOIN dim_station s2 ON f.end_station_id  = s2.station_id
        JOIN dim_user u     ON f.user_id = u.user_id
        ORDER BY f.trip_id;
    """,
    "Trip count by user type": """
        SELECT user_type, COUNT(*) AS trip_count, ROUND(AVG(duration_sec)) AS avg_duration_sec
        FROM fact_trips f JOIN dim_user u ON f.user_id = u.user_id
        GROUP BY user_type
        ORDER BY trip_count DESC;
    """,
    "Trip count by gender": """
        SELECT gender, COUNT(*) AS trip_count
        FROM fact_trips f JOIN dim_user u ON f.user_id = u.user_id
        GROUP BY gender
        ORDER BY trip_count DESC;
    """,
    "Top stations (by trips started)": """
        SELECT s.station_name, COUNT(*) AS trips_started
        FROM fact_trips f JOIN dim_station s ON f.start_station_id = s.station_id
        GROUP BY s.station_name
        ORDER BY trips_started DESC
        LIMIT 10;
    """,
    "All stations": "SELECT * FROM dim_station ORDER BY station_id;",
}


class GoBikeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ford GoBike — Database Viewer")
        self.resize(950, 600)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Query:"))

        self.query_picker = QComboBox()
        self.query_picker.addItems(QUERIES.keys())
        top_bar.addWidget(self.query_picker, stretch=1)

        run_btn = QPushButton("Run")
        run_btn.clicked.connect(self.run_query)
        top_bar.addWidget(run_btn)

        layout.addLayout(top_bar)

        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        self.status = QLabel("Ready.")
        layout.addWidget(self.status)

        self.conn = None
        self.connect_db()

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.status.setText("Connected to 'gobike' database.")
        except Exception as e:
            QMessageBox.critical(self, "Connection Error", str(e))
            self.status.setText("Connection failed.")

    def run_query(self):
        if self.conn is None:
            self.connect_db()
            if self.conn is None:
                return

        sql = QUERIES[self.query_picker.currentText()]
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]

            self.table.setRowCount(len(rows))
            self.table.setColumnCount(len(colnames))
            self.table.setHorizontalHeaderLabels(colnames)

            for r, row in enumerate(rows):
                for c, val in enumerate(row):
                    self.table.setItem(r, c, QTableWidgetItem(str(val)))

            self.status.setText(f"{len(rows)} rows returned.")
        except Exception as e:
            QMessageBox.critical(self, "Query Error", str(e))
            self.status.setText("Query failed.")


def main():
    print("Step 1: Creating QApplication...")
    app = QApplication(sys.argv)
    print("Step 2: QApplication created OK")

    print("Step 3: Creating GoBikeApp window (this connects to the DB)...")
    window = GoBikeApp()
    print("Step 4: GoBikeApp window created OK")

    print("Step 5: Calling show()...")
    window.show()
    print("Step 6: show() called, entering event loop...")

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()