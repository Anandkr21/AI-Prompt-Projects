# Set 4 : Intermediate Level

We'll continue with the **`Rides`** table / collection from the previous set.

**Problem 36:**

- **Prerequisite**: Understand using the MAX and MIN functions in SQL / using sort and limit in MongoDB
- **Problem**: Write a query to find the ride with the highest and lowest **`fare`**.
```sql
-- Ride with the highest fare
SELECT *
FROM Rides
WHERE fare = (SELECT MAX(fare) FROM Rides);

-- Ride with the lowest fare
SELECT *
FROM Rides
WHERE fare = (SELECT MIN(fare) FROM Rides);

```

```js
// Ride with the highest fare
db.Rides.find().sort({ fare: -1 }).limit(1);

// Ride with the lowest fare
db.Rides.find().sort({ fare: 1 }).limit(1);

```
**Problem 37:**

- **Prerequisite**: Understand using the GROUP BY clause in SQL / using aggregate in MongoDB
- **Problem**: Write a query to find the average **`fare`** and **`distance`** for each **`driver_id`**.
```sql
SELECT driver_id, AVG(fare) AS average_fare, AVG(distance) AS average_distance
FROM Rides
GROUP BY driver_id;

```

```js
db.Rides.aggregate([
  {
    $group: {
      _id: "$driver_id",
      average_fare: { $avg: "$fare" },
      average_distance: { $avg: "$distance" }
    }
  }
]);

```
**Problem 38:**

- **Prerequisite**: Understand using HAVING clause in SQL / using match in MongoDB's aggregate pipeline
- **Problem**: Write a query to find **`driver_id`** that have completed more than 5 rides.
```sql
SELECT driver_id, COUNT(*) AS ride_count
FROM Rides
GROUP BY driver_id
HAVING COUNT(*) > 5;

```

```js
db.Rides.aggregate([
  {
    $group: {
      _id: "$driver_id",
      ride_count: { $sum: 1 }
    }
  },
  {
    $match: {
      ride_count: { $gt: 5 }
    }
  }
]);

```
**Problem 39:**

- **Prerequisite**: Understand the use of INNER JOIN in SQL / Lookup in MongoDB
- **Problem**: Assuming there is another collection/table called **`Drivers`** with **`driver_id`** and **`name`** fields, write a query to find the name of the driver with the highest **`fare`**.
```sql
SELECT d.name
FROM Drivers AS d
INNER JOIN Rides AS r ON d.driver_id = r.driver_id
WHERE r.fare = (SELECT MAX(fare) FROM Rides);

```

```js
db.Drivers.aggregate([
  {
    $lookup: {
      from: "Rides",
      localField: "driver_id",
      foreignField: "driver_id",
      as: "rides"
    }
  },
  {
    $unwind: "$rides"
  },
  {
    $match: {
      "rides.fare": { $eq: db.Rides.find().sort({ fare: -1 }).limit(1).next().fare }
    }
  },
  {
    $project: {
      _id: 0,
      name: 1
    }
  }
]);

```
**Problem 40:**

- **Prerequisite**: Understand the concept of subqueries in SQL / using multiple stages in MongoDB's aggregate pipeline
- **Problem**: Write a query to find the top 3 drivers who have earned the most from fares. Return the drivers' ids and total earnings.
```sql
SELECT driver_id, SUM(fare) AS total_earnings
FROM Rides
GROUP BY driver_id
ORDER BY total_earnings DESC
LIMIT 3;

```

```js
db.Rides.aggregate([
  {
    $group: {
      _id: "$driver_id",
      total_earnings: { $sum: "$fare" }
    }
  },
  {
    $sort: {
      total_earnings: -1
    }
  },
  {
    $limit: 3
  },
  {
    $project: {
      _id: 0,
      driver_id: "$_id",
      total_earnings: 1
    }
  }
]);

```
**Problem 41:**

- **Prerequisite**: Understand date and time functions in SQL / MongoDB
- **Problem**: Assuming there's a **`ride_date`** field of date type in the **`Rides`** table / collection, write a query to find all rides that happened in the last 7 days.
```sql
SELECT *
FROM Rides
WHERE ride_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY);

```

```js
const currentDate = new Date();
const sevenDaysAgo = new Date();
sevenDaysAgo.setDate(currentDate.getDate() - 7);

db.Rides.find({
  ride_date: {
    $gte: sevenDaysAgo,
    $lte: currentDate
  }
});

```
**Problem 42:**

- **Prerequisite**: Understand the concept of NULL values and how to handle them in SQL / MongoDB
- **Problem**: Write a query to find all rides where the **`end_location`** is not set.
```sql
SELECT *
FROM Rides
WHERE end_location IS NULL;

```

```js
db.Rides.find({ end_location: { $exists: false } });

```
**Problem 43:**

- **Prerequisite**: Understand the use of complex mathematical operations in SQL / MongoDB
- **Problem**: Write a query to calculate the fare per mile for each ride and return the ride ids and their fare per mile, ordered by fare per mile in descending order.
```sql

```

```js

```
**Problem 44:**

- **Prerequisite**: Understand the use of multiple JOINs in SQL / multiple Lookups in MongoDB
- **Problem**: Assuming there's another collection/table **`Passengers`** with **`passenger_id`** and **`name`** fields, write a query to return a list of all rides including the driver's name and passenger's name.
```sql
SELECT id, fare / distance AS fare_per_mile
FROM Rides
ORDER BY fare_per_mile DESC;

```

```js
db.Rides.aggregate([
  {
    $addFields: {
      fare_per_mile: { $divide: [ "$fare", "$distance" ] }
    }
  },
  {
    $sort: {
      fare_per_mile: -1
    }
  },
  {
    $project: {
      _id: 0,
      id: 1,
      fare_per_mile: 1
    }
  }
]);

```
**Problem 45:**

- **Prerequisite**: Understand how to alter table schemas in SQL / adding and modifying fields in MongoDB documents
- **Problem**: Write a query to add a **`tip`** field to the **`Rides`** table / collection.

```sql
ALTER TABLE Rides
ADD COLUMN tip DECIMAL(6,2);

```

```js
db.Rides.updateMany({}, { $set: { tip: 0 } });

``` 