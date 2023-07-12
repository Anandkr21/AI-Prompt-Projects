# Set 1 : Beginner Level

### **MongoDB:**

In MongoDB, we're using a **`Customers`** collection. Each document in the collection represents one customer. Here is the schema of the **`Customers`** collection:

```bash
{
  "_id": ObjectId(), // a unique identifier created by MongoDB itself
  "name": String,
  "email": String,
  "address": String,
  "phone_number": String
}
```

**_id**: This field is a unique identifier for the document. MongoDB automatically generates and assigns an ObjectId to this field when we create a new document.

**name**: This field holds the name of the customer as a string.

**email**: This field holds the email address of the customer as a string.

**address**: This field holds the customer's address as a string.

**phone_number**: This field holds the customer's phone number as a string.

### **SQL:**

In SQL, we're using a **`Customers`** table. Each row in the table represents one customer. Here is the schema of the **`Customers`** table:

```bash
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(50)
);

```

**id**: This field is a unique identifier for the row. We manually assign a unique INT to this field when we create a new row. It's marked as the PRIMARY KEY.

**name**: This field holds the name of the customer as a variable character string (VARCHAR) of length 100.

**email**: This field holds the email address of the customer as a variable character string (VARCHAR) of length 100.

**address**: This field holds the customer's address as a variable character string (VARCHAR) of length 255.

**phone_number**: This field holds the customer's phone number as a variable character string (VARCHAR) of length 50.

**Problem 1:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.

```sql
CREATE TABLE customers (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);
```

```bash
db.createCollection('customers', {
  fields: {
    id: { type: 'int', unique: true },
    name: { type: 'string' },
    email: { type: 'string' },
    address: { type: 'string' },
    phone_number: { type: 'string', nullable: true }
  }
})

```



**Problem 2:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.

```sql
INSERT INTO customers (name, email, address, phone_number)
VALUES
  ('John Doe', 'john.doe@example.com', '123 Main Street, Anytown, CA 12345', '123-456-7890'),
  ('Jane Doe', 'jane.doe@example.com', '456 Elm Street, Anytown, CA 12345', '456-789-0123'),
  ('Mary Smith', 'mary.smith@example.com', '789 Oak Street, Anytown, CA 12345', '789-012-3456'),
  ('Peter Jones', 'peter.jones@example.com', '101 First Avenue, Anytown, CA 12345', '101-202-3030'),
  ('Susan Brown', 'susan.brown@example.com', '202 Second Avenue, Anytown, CA 12345', '202-303-4040');
```

```bash
db.customers.insertMany([
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": "123 Main Street, Anytown, CA 12345",
    "phone_number": "123-456-7890"
  },
  {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "address": "456 Elm Street, Anytown, CA 12345",
    "phone_number": "456-789-0123"
  },
  {
    "name": "Mary Smith",
    "email": "mary.smith@example.com",
    "address": "789 Oak Street, Anytown, CA 12345",
    "phone_number": "789-012-3456"
  },
  {
    "name": "Peter Jones",
    "email": "peter.jones@example.com",
    "address": "101 First Avenue, Anytown, CA 12345",
    "phone_number": "101-202-3030"
  },
  {
    "name": "Susan Brown",
    "email": "susan.brown@example.com",
    "address": "202 Second Avenue, Anytown, CA 12345",
    "phone_number": null
  }
])
```


**Problem 3:**

- **Prerequisite**: Understand basic data fetching in SQL / MongoDB
- **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

```sql
SELECT *
FROM customers;
```

```bash
db.customers.find()
```

**Problem 4:**

- **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
- **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.

```sql
SELECT name, email
FROM customers;
```

```bash
db.customers.find({}, { name: 1, email: 1 })
```

**Problem 5:**

- **Prerequisite**: Understand basic WHERE clause in SQL / MongoDB's find method
- **Problem**: Write a query to fetch the customer with the **`id`** of 3.

```sql
SELECT *
FROM customers
WHERE id = 3;
```

```bash
db.customers.find({ _id: 3 })
```

**Problem 6:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all customers whose **`name`** starts with 'A'.

```sql
SELECT *
FROM customers
WHERE name LIKE 'A%';
```

```bash
db.customers.find({ name: { $regex: /^A/ } })
```

**Problem 7:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.

```bash
SELECT *
FROM customers
ORDER BY name DESC;
```

```bash
db.customers.find().sort({ name: -1 })
```

**Problem 8:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.
  
```sql
    UPDATE customers
    SET address = '12345 Main Street, Anytown, CA 12345'
    WHERE id = 4;
```

```bash
db.customers.updateOne({ _id: 4 }, { $set: { address: "101 Main Street, Anytown, CA 91234" } })
```

**Problem 9:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 3 customers when ordered by **`id`** in ascending order.

```sql
SELECT *
FROM customers
ORDER BY id
LIMIT 3;
```

```bash
db.customers.find().sort({ _id: 1 }).limit(3)
```

**Problem 10:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the customer with **`id`** 2.
  
```sql
DELETE FROM customers
WHERE id = 2;
```

```bash
db.customers.deleteOne({ _id: 2 })
```

**Problem 11:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of customers.
```sql
SELECT COUNT(*) AS total_customers
FROM customers;
```

```bash
db.customers.count()
```

**Problem 12:**

- **Prerequisite**: Understand how to skip rows / documents in SQL / MongoDB
- **Problem**: Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.
- 
```sql
SELECT *
FROM customers
ORDER BY id
OFFSET 2;
```

```bash
db.customers.find().sort({ _id: 1 }).skip(2)
```

**Problem 13:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is greater than 2 and **`name`** starts with 'B'.

```sql
SELECT *
FROM customers
WHERE id > 2
AND name LIKE 'B%';
```

```bash
db.customers.find({
  _id: { $gt: 2 },
  name: { $regex: /^B/ }
})
```



**Problem 14:**

- **Prerequisite**: Understand how to use OR conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is less than 3 or **`name`** ends with 's'.

```sql
SELECT *
FROM customers
WHERE id < 3
OR name LIKE '%s';
```

```bash
db.customers.find({
  $or: [
    { _id: { $lt: 3 } },
    { name: { $regex: /s$/ } }
  ]
})

```

**Problem 15:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all customers where the **`phone_number`** field is not set or is null.

```sql
SELECT *
FROM customers
WHERE phone_number IS NULL
OR phone_number = '';
```

```bash
db.customers.find({
  phone_number: {
    $in: [null, '' ]
  }
})
```