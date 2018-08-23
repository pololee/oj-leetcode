Question 2:
Implement method:
String[][] categorySuggestions(String[] categories, String[] projects, int k) {
}
Description:
Every project on Thumbtack belongs to a category. Each set of two categories has a relevance score from 0 to 1, which represents how relevant they are to each other. A category has a relevance score of 1.0 to itself.
Every time a project that belongs to a user is completed, the Thumbtack search bar updates to display the k most relevant category suggestions for that user. These top categories are chosen by first sorting all the categories that are relevant to at least one of the already created projects by relevance. Then, in the case that their relevance is equal, they should be sorted by category name. If the same category is relevant to 2 or more projects, it should be included only once with the maximum relevance score. If there are fewer than k total relevant projects, the suggestions list will be shorter than k.
You have a relevance graph of all the Thumbtack categories, represented as an array of strings of comma-separated words. For each string in categories, the first two elements are the categories being compared and the third is their relevance score. You are also given an array of the categories of the projects that a particular user wants to create.
For example:
"House Painting,Interior Painting,0.8" means that House Painting and Interior Painting have a relevance score of 0.8 (i.e. highly relevant)
and "Handyman,Massage Therapy,0.1" means that Handyman and Massage Therapyhave a relevance score of 0.1 (i.e. barely relevant).
Note that if there is no entry for particular pair of categories, it means that their relevance is 0.0 (i.e. they aren't relevant at all and they shouldn't be included in the list of suggestions).
Given the relevance graph categories, the list of the user's projects, and the number of category suggestions the user should see in the Thumbtack search bar k, return an array of arrays that represents the state of the search bar suggestions list after each of the projects in projects is created.
Example
For
categories = ["House Painting,Interior Painting,0.9",
 "Handyman,Massage Therapy,0.1",
 "Handyman,House Painting,0.5",
 "House Painting,House Cleaning,0.6",
 "Furniture Assembly,Handyman,0.8",
 "Furniture Assembly,Massage Therapy,0.1",
 "Plumbing Drain Repair,Junk Removal,0.3"]
projects = ["House Painting", "Handyman"], and k = 3, the output should be
categorySuggestions(categories, projects, k) = [["House Painting", "Interior Painting", "House Cleaning"], ["Handyman", "House Painting", "Interior Painting"]].
After the first project House Painting is completed, the most relevant suggestions are (in order of their relevance):
CategoryRelevance
House Painting 1.0 
Interior Painting 0.9 
House Cleaning 0.6 
Handyman 0.5 
After the second project is completed, the most relevant suggestions are:CategoryRelevance
Handyman 1.0 
House Painting 1.0 
Interior Painting 0.9 
Furniture Assembly 0.8 
House Cleaning 0.6 
Massage Therapy 0.1 
Input/Output
[time limit] 3000ms (java)
[input] array.string categories
Category relevancies given in the format <category1 name>,<category2 name>,<relevance>. relevance is a float number in the range (0,1] and has no more than 6 decimal places after the point.
It is guaranteed that there are no duplicate entries with the same category pairs (i.e. <category1 name> with <category2 name> will be distinct).
Category names can only consists of spaces and English letters.
Guaranteed constraints:
0 ≤ categories.length ≤ 1000,
5 ≤ categories[i].length ≤ 50.
[input] array.string projects
The categories to which the user's projects belong.
Guaranteed constraints:
0 ≤ projects.length ≤ 1000,
1 ≤ projects[i].length ≤ 30.
[input] integer k
The number of category suggestions that should be shown in the user's search bar.
Guaranteed constraints:
0 ≤ k ≤ 50.
[output] array.array.string
Return the state of the search bar suggestions list after each of the projects in projects is created.
[Java] Syntax Tips
// Prints help message to the console
// Returns a string
// 
// Globals declared here will cause a compilation error,
// declare variables inside the function instead!
String helloWorld(String name) {
    System.out.println("This prints to the console when you Run Tests");
    return "Hello, " + name;
}
