# Set 3: Intermediate Level

**Set 3: Intermediate Level**

We'll continue with a **`Rides`** table / collection for this set of problems. The schema represents a list of rides one might find in a ride-hailing app like Uber. Each ride has an **`id`**, **`driver_id`**, **`passenger_id`**, **`start_location`**, **`end_location`**, **`distance`** (in miles), **`ride_time`** (in minutes), and **`fare`** (in dollars).

**MongoDB Schema:**

```js
{
  "_id": ObjectId(),
  "driver_id": ObjectId(),
  "passenger_id": ObjectId(),
  "start_location": String,
  "end_location": String,
  "distance": Number,
  "ride_time": Number,
  "fare": Number
}

```

**SQL Schema:**

```sql
CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);

```

**Problem 26:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Rides`** table / collection with the fields defined above.

```sql
CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);

```

```js
db.createCollection("Rides", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["driver_id", "passenger_id", "start_location", "end_location", "distance", "ride_time", "fare"],
      properties: {
        driver_id: {
          bsonType: "objectId"
        },
        passenger_id: {
          bsonType: "objectId"
        },
        start_location: {
          bsonType: "string"
        },
        end_location: {
          bsonType: "string"
        },
        distance: {
          bsonType: "number"
        },
        ride_time: {
          bsonType: "number"
        },
        fare: {
          bsonType: "number"
        }
      }
    }
  }
});

```

**Problem 27:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Rides`** table / collection with data of your choice.

```sql
INSERT INTO Rides (id, driver_id, passenger_id, start_location, end_location, distance, ride_time, fare)
VALUES
  (1, 1001, 2001, 'New York', 'Los Angeles', 2800.50, 300.75, 150.25),
  (2, 1002, 2002, 'San Francisco', 'Seattle', 800.20, 90.25, 70.50),
  (3, 1003, 2003, 'London', 'Paris', 400.75, 60.50, 45.75),
  (4, 1001, 2004, 'Tokyo', 'Osaka', 500.30, 75.50, 55.25),
  (5, 1002, 2005, 'Sydney', 'Melbourne', 300.40, 45.75, 35.50);

```

```js
db.Rides.insertMany([
  {
    driver_id: ObjectId("613f5c525ebc2078203a31e1"),
    passenger_id: ObjectId("613f5c525ebc2078203a31e2"),
    start_location: "New York",
    end_location: "Los Angeles",
    distance: 2800.50,
    ride_time: 300.75,
    fare: 150.25
  },
  {
    driver_id: ObjectId("613f5c525ebc2078203a31e3"),
    passenger_id: ObjectId("613f5c525ebc2078203a31e4"),
    start_location: "San Francisco",
    end_location: "Seattle",
    distance: 800.20,
    ride_time: 90.25,
    fare: 70.50
  },
  {
    driver_id: ObjectId("613f5c525ebc2078203a31e5"),
    passenger_id: ObjectId("613f5c525ebc2078203a31e6"),
    start_location: "London",
    end_location: "Paris",
    distance: 400.75,
    ride_time: 60.50,
    fare: 45.75
  },
  {
    driver_id: ObjectId("613f5c525ebc2078203a31e1"),
    passenger_id: ObjectId("613f5c525ebc2078203a31e7"),
    start_location: "Tokyo",
    end_location: "Osaka",
    distance: 500.30,
    ride_time: 75.50,
    fare: 55.25
  },
  {
    driver_id: ObjectId("613f5c525ebc2078203a31e3"),
    passenger_id: ObjectId("613f5c525ebc2078203a31e8"),
    start_location: "Sydney",
    end_location: "Melbourne",
    distance: 300.40,
    ride_time: 45.75,
    fare: 35.50
  }
]);

```
**Problem 28:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all rides, ordered by **`fare`** in descending order.

```sql
SELECT *
FROM Rides
ORDER BY fare DESC;

```

```js
db.Rides.find().sort({ fare: -1 });
```
**Problem 29:**

- **Prerequisite**: Understand using math operations in SQL / MongoDB
- **Problem**: Write a query to calculate the total **`distance`** and total **`fare`** for all rides.

```sql
SELECT SUM(distance) AS total_distance, SUM(fare) AS total_fare
FROM Rides;

```

```js
db.Rides.aggregate([
  {
    $group: {
      _id: null,
      total_distance: { $sum: "$distance" },
      total_fare: { $sum: "$fare" }
    }
  }
]);

```
**Problem 30:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`ride_time`** of all rides.

```sql
SELECT AVG(ride_time) AS average_ride_time
FROM Rides;

```

```js
db.Rides.aggregate([
  {
    $group: {
      _id: null,
      average_ride_time: { $avg: "$ride_time" }
    }
  }
]);

```
**Problem 31:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all rides whose **`start_location`** or **`end_location`** contains 'Downtown'.

```sql
SELECT *
FROM Rides
WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';

```

```js
db.Rides.find({
  $or: [
    { start_location: { $regex: /Downtown/i } },
    { end_location: { $regex: /Downtown/i } }
  ]
});

```
**Problem 32:**

- **Prerequisite**: Understand how to use the COUNT function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to count the number of rides for a given **`driver_id`**.

```sql
SELECT COUNT(*) AS ride_count
FROM Rides
WHERE driver_id = <driver_id>;

```

```js
db.Rides.countDocuments({ driver_id: <driver_id> });

```
**Problem 33:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`fare`** of the ride with **`id`** 4.

```sql
UPDATE Rides
SET fare = <new_fare>
WHERE id = 4;

```

```js
db.Rides.updateOne(
  { _id: ObjectId("4") },
  { $set: { fare: <new_fare> } }
);

```
**Problem 34:**

- **Prerequisite**: Understand using GROUP BY in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the total **`fare`** for each **`driver_id`**.

```sql
SELECT driver_id, SUM(fare) AS total_fare
FROM Rides
GROUP BY driver_id;

```

```js
db.Rides.aggregate([
  {
    $group: {
      _id: "$driver_id",
      total_fare: { $sum: "$fare" }
    }
  }
]);

```
**Problem 35:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the ride with **`id`** 2.

```sql
DELETE FROM Rides
WHERE id = 2;

```

```js
db.Rides.deleteOne({ _id: ObjectId("2") });

```