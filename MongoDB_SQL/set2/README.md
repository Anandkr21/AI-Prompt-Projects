# Set 2 : Beginner Level

**Set 2: Beginner Level - Advanced**

We will be using a **`Restaurants`** table / collection for this set of problems. The schema represents a list of restaurants like one might find in a delivery app like Zomato. Each restaurant has an **`id`**, **`name`**, **`cuisine_type`** (e.g., Italian, Chinese), **`location`**, **`average_rating`**, and **`delivery_available`** (a boolean indicating if delivery is available).

**MongoDB Schema:**

```js
{
  "_id": ObjectId(), 
  "name": String,
  "cuisine_type": String,
  "location": String,
  "average_rating": Number,
  "delivery_available": Boolean
}
```

**SQL Schema:**

```sql
CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

```

**Problem 16:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Restaurants`** table / collection with the fields defined above.

```sql
CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

```

```js
db.createCollection("Restaurants", {
    collection: {
        fields: {
            _id: { type: "ObjectId" },
            name: { type: "String" },
            cuisine_type: { type: "String" },
            location: { type: "String" },
            average_rating: { type: "Decimal128" },
            delivery_available: { type: "Boolean" }
        }
    }
});
```

**Problem 17:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.

```sql
INSERT INTO Restaurants (name, cuisine_type, location, average_rating, delivery_available)
VALUES
('The Cheesecake Factory', 'American', '123 Main Street, Anytown, CA 12345', 4.5, TRUE),
('Pizzeria Uno', 'Pizza', '456 Elm Street, Anytown, CA 12345', 4.0, TRUE),
('Panda Express', 'Chinese', '789 Oak Street, Anytown, CA 12345', 3.5, TRUE),
('Subway', 'Sandwiches', '101 First Avenue, Anytown, CA 12345', 3.0, TRUE),
('McDonald''s', 'Fast Food', '202 Second Avenue, Anytown, CA 12345', 2.5, TRUE);

```

```js
db.restaurants.insertMany([
  {
    name: "The Cheesecake Factory",
    cuisine_type: "American",
    location: "123 Main Street, Anytown, CA 12345",
    average_rating: 4.5,
    delivery_available: true
  },
  {
    name: "Pizzeria Uno",
    cuisine_type: "Pizza",
    location: "456 Elm Street, Anytown, CA 12345",
    average_rating: 4.0,
    delivery_available: true
  },
  {
    name: "Panda Express",
    cuisine_type: "Chinese",
    location: "789 Oak Street, Anytown, CA 12345",
    average_rating: 3.5,
    delivery_available: true
  },
  {
    name: "Subway",
    cuisine_type: "Sandwiches",
    location: "101 First Avenue, Anytown, CA 12345",
    average_rating: 3.0,
    delivery_available: true
  },
  {
    name: "McDonald''s",
    cuisine_type: "Fast Food",
    location: "202 Second Avenue, Anytown, CA 12345",
    average_rating: 2.5,
    delivery_available: true
  }
]);

```

**Problem 18:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.
```sql
SELECT *
FROM Restaurants
ORDER BY average_rating DESC;

```

```js
db.restaurants.find().sort({ average_rating: -1 });
```

**Problem 19:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.
```sql
SELECT *
FROM Restaurants
WHERE delivery_available = 1
AND average_rating > 4;
```

```js
db.restaurants.find({
  delivery_available: true,
  average_rating: { $gt: 4 }
});
```
**Problem 20:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.
```sql
SELECT *
FROM Restaurants
WHERE cuisine_type IS NULL
OR cuisine_type = '';
```

```js
db.restaurants.find({
  cuisine_type: { $exists: false }
});

```
**Problem 21:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.
```sql
SELECT COUNT(*)
FROM Restaurants
WHERE delivery_available = 1;
```

```js
db.restaurants.count({
  delivery_available: true
});
```

**Problem 22:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.
```sql
SELECT *
FROM Restaurants
WHERE location LIKE '%New York%';
```

```js
db.restaurants.find({
  location: { $regex: /New York/ }
});
```
**Problem 23:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.
```sql
SELECT AVG(average_rating) AS average_rating
FROM Restaurants;
```

```js
db.restaurants.aggregate([
  {
    $group: {
      "_id": null,
      "average_rating": { $avg: "$average_rating" }
    }
  }
]);
```

**Problem 24:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.
```sql
SELECT *
FROM Restaurants
ORDER BY average_rating DESC
LIMIT 5;
```

```js
db.restaurants.find().sort({ average_rating: -1 }).limit(5);
```

**Problem 25:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the restaurant with **`id`** 3.

```sql
DELETE FROM Restaurants
WHERE id = 3;
```

```js
db.restaurants.deleteOne({ _id: 3 });
```