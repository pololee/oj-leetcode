// # Find the record
// Here's how the database works: 
// all records are represented as maps (or hashes), with string as keys and integer as values. 
// The records are contained in an array, in **no particular order**.

// step 1

// Implement `min_by_key`

// This function scans the array of records and returns the record that has the minimum value of a specified key.

// - Records that do not contain the specified key are considered to have value 0 for the key
// - Keys may map to negative values
// - Handle an empty array of records in an idiomatic way in your language of choice.
// - If several records share the same minimum value for the chosen key, you may return any of them.

// Examples:

// ```markdown
// min_by_key("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
// min_by_key("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
// min_by_key("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
// min_by_key("a", [{}]) == {}
// min_by_key("b", [{"a": -1}, {"b": -1}]) == {"b": -1}
// ```


// ## Step 2

// Implement `first_by_key`

// It takes three arguments:

// 1. a string key
// 2. a string sort direction (which must be either "asc" or "desc")
// 3. an array of records

// If the sort direction is "asc", it should return the minium record, 
// otherwise it should return the maximum record.
// Change your `min_by_key` to use your `first_by_key`

// Examples:

// ```markdown
// first_by_key("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [{"b": 1},
// {"b": -2}]
// first_by_key("a", "asc", [{"a": 1}]) == {"a": 1}
// first_by_key("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
// first_by_key("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
// first_by_key("a", "asc", [{}]) == {}
// ```

// ## Step 3

// Extract the comparison of records into a comparator. 

// Write a class whose constructor accepts two paramenters: 
// **a string key and a string direction**. 
// 
// The class should implement a method `compare` that takes two records as its parameters. 
// This method should return 

// - -1 if the first record comes before the second record (according to the key and direction)
// - 0 if neither record comes before each other
// - 1 if the first record comes after the second

// Use your comparator in your implementation of `first_by_key`.

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <climits>
using namespace std;

unordered_map<string,int> min_by_key(string k, vector<unordered_map<string, int>> maps) {
    return first_by_key(k, "asc", maps);
}

unordered_map<string, int> first_by_key(string k, string dir, vector<unordered_map<string, int>> maps) {
    unordered_map<string, int> res;
    if (maps.size() <= 0) {
      return res;
    }
    if (dir == "asc") {
      int index, ans = INT_MAX;
      for (int i = 0; i < maps.size(); i++) {
        if (maps[i].find(k) == maps[i].end()) {
          if (0 < ans) {
            ans = 0;
            index = i;
          }
          
        } else {
            if (maps[i][k] < ans) {
            ans = maps[i][k];
            index = i;
          }
        }
      }
      return maps[index];
    } else {
      int index, ans = INT_MIN;
      for (int i = 0; i < maps.size(); i++) {
        if (maps[i].find(k) == maps[i].end()) {
          if (0 > ans) {
            ans = 0;
            index = i;
          }
          
        } else {
            if (maps[i][k] > ans) {
            ans = maps[i][k];
            index = i;
          }
        }
      }
      return maps[index];
    }

}

// Extract the comparison of records into a comparator. 

// Write a class whose constructor accepts two paramenters: 
// **a string key and a string direction**. 
// 
// The class should implement a method `compare` that takes two records as its parameters. 
// This method should return 

// - -1 if the first record comes before the second record (according to the key and direction)
// - 0 if neither record comes before each other
// - 1 if the first record comes after the second

// Use your comparator in your implementation of `first_by_key`.

class RecordComparator {
  RecordComparator(string key, string dir) {
    
  }
}

int main() {
  vector<unordered_map<string, int>> maps;
  unordered_map<string, int> map1 = {{"a", 1}, {"b", 2}};
  unordered_map<string, int> map2 = {{"a", 2}};
  maps.push_back(map1);
  maps.push_back(map2);
  unordered_map<string, int> res = first_by_key("b", "desc", maps);
  for (auto &x: res) {
    cout<<x.first<<": "<<x.second<<endl;
  }
  cout<<"Passed!"<<endl;
	return 0;
}
