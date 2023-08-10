CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    name_user TEXT,
    rut_user TEXT);

CREATE TABLE Vehicles (
    vehicle_id INTEGER PRIMARY KEY);


CREATE TABLE Status (
    status_id INTEGER PRIMARY KEY);


create table Memberships (
    membership_id INTEGER PRIMARY KEY
);

CREATE TABLE Trips (
    trip_id INT PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    vehicle_id INT REFERENCES Vehicles(vehicle_id),
    booking_time TIMESTAMP,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    travel_dist FLOAT,
    membership_id INT REFERENCES Memberships(membership_id),
    status_id INT REFERENCES Status(status_id),
    price_amount FLOAT,
    price_tax FLOAT,
    price_total FLOAT,
    start_location POINT,
    end_location POINT);


