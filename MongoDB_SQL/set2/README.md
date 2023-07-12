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

**Problem 17:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.

**Problem 18:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.

**Problem 19:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.

**Problem 20:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.

**Problem 21:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.

**Problem 22:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.

**Problem 23:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.

**Problem 24:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.

**Problem 25:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the restaurant with **`id`** 3.