# Find the record

In this interview, we'll pretend we are building a new analytical database. 
Don't worry about actually building a database though.



Here's how the database works: all records are represented as maps (or hashes), 
with string as keys and integer as values. 
The records are contained in an array, in **no particular order**.



## Step 1

Implement `min_by_key`

This function scans the array of records and returns the record 
that has the minimum value of a specified key.

- Records that do not contain the specified key are considered to have value 0 for the key
- Keys may map to negative values
- Handle an empty array of records in an idiomatic way in your language of choice.
- If several records share the same minimum value for the chosen key, you may return any of them.

Examples:

```markdown
min_by_key("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
min_by_key("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
min_by_key("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
min_by_key("a", [{}]) == {}
min_by_key("b", [{"a": -1}, {"b": -1}]) == {"b": -1}
```



Java

```java
public static Map<String, Integer> minByKey(String key, List<Map<String, Integer>> records);
```

Python

```python
def min_by_key(key, records):
```

Ruby

```ruby
def min_by_key(key, records)
end
```

## Step 2

Implement `first_by_key`

It takes three arguments:

1. a string key
2. a string sort direction (which must be either "asc" or "desc")
3. an array of records

If the sort direction is "asc", 
it should return the minium record,
otherwise it should return the maximum record.

Change your `min_by_key` to use your `first_by_key`

Examples:

```markdown
first_by_key("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [{"b": 1},
{"b": -2}]
first_by_key("a", "asc", [{"a": 1}]) == {"a": 1}
first_by_key("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
first_by_key("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
first_by_key("a", "asc", [{}]) == {}
```

Java

```java
public static Map<String, Integer> firstByKey(String key, String direction,
List<Map<String, Integer>> records);
```

Python

```python
def firstByKey(key, direction, records):
```

Ruby

```ruby
def firstByKey(key, direction, records)
end
```

## Step 3

Extract the comparison of records into a comparator. 

Write a class whose constructor accepts two paramenters: 
  **a string key and a string direction**. 
The class should implement a method `compare` that takes two records as its parameters. 
This method should return 

- -1 if the first record comes before the second record (according to the key and direction)
- 0 if neither record comes before each other
- 1 if the first record comes after the second

Use your comparator in your implementation of `first_by_key`.
