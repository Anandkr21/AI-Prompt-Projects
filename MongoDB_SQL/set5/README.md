# Set 5: Advanced Level (Optional)

We'll continue with the **`Rides`** table / collection from the previous set.

**Problem 46:**

- **Prerequisite**: Understand using the UNION operator in SQL / using $facet and $unionWith in MongoDB
- **Problem**: Assuming there's another collection/table **`FutureRides`** with the same schema as **`Rides`**, write a query to create a union of **`Rides`** and **`FutureRides`**.

**Problem 47:**

- **Prerequisite**: Understand window functions in SQL / the use of $bucket and $rank in MongoDB's aggregate pipeline
- **Problem**: Write a query to rank drivers based on the total fare they've collected.

**Problem 48:**

- **Prerequisite**: Understand nested queries and the IN keyword in SQL / using the $in operator in MongoDB
- **Problem**: Write a query to find all rides where the **`driver_id`** is among the top 5 drivers with the most rides.

**Problem 49:**

- **Prerequisite**: Understand the use of CASE or IF statements in SQL / using $cond in MongoDB
- **Problem**: Write a query to classify rides based on **`distance`**: 'Short' if the distance is less than 5 miles, 'Medium' if the distance is between 5 and 15 miles, and 'Long' for distances over 15 miles.

**Problem 50:**

- **Prerequisite**: Understand the use of advanced statistical functions in SQL / MongoDB's aggregate pipeline
- **Problem**: Write a query to calculate the variance and standard deviation of **`fare`** for each driver.

**Problem 51:**

- **Prerequisite**: Understand using complex date and time functions in SQL / MongoDB
- **Problem**: Assuming there's a **`ride_date`** field of date type in the **`Rides`** table / collection, write a query to find the busiest day of the week (when most rides happened).

**Problem 52:**

- **Prerequisite**: Understand recursive queries in SQL / recursive $lookup in MongoDB
- **Problem**: Assuming there's a **`Rides`** table / collection where each ride can have a follow-up ride (**`next_ride_id`**), write a query to find all subsequent rides for a given ride id.

**Problem 53:**

- **Prerequisite**: Understand advanced uses of the GROUP BY clause in SQL / using $group with multiple fields in MongoDB
- **Problem**: Write a query to find the total **`distance`** and **`fare`** for each **`driver_id`** and **`passenger_id`** pair.

**Problem 54:**

- **Prerequisite**: Understand using arrays and array functions in SQL / MongoDB
- **Problem**: Assuming there's a **`tags`** field in the **`Rides`** collection (an array of strings), write a query to find all rides that have the tag 'business'.

**Problem 55:**

- **Prerequisite**: Understand full-text search in SQL / MongoDB
- **Problem**: Assuming there's a **`notes`** field in the **`Rides`** collection/table, write a query to find all rides where the **`notes`** contain the word 'airport'.