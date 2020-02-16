#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution {
private:
  bool searchWord(vector<vector<char> > &board, int m, int n,
    string word, int &count, vector<vector<bool> > &visited){

    int num_row = board.size();
    int num_col = board[0].size();

    if (m < 0 || m >= num_row || n < 0 || n >= num_col)
      return false;

    if(true == visited[m][n])
      return false;

    if(word[count] == board[m][n]){
      visited[m][n] = true;
      count++;
      if(count == word.size())
        return true;
      bool matched = searchWord(board, m-1, n, word, count, visited)
              || searchWord(board, m, n+1, word, count, visited)
              || searchWord(board, m+1, n, word, count, visited)
              || searchWord(board, m, n-1, word, count, visited);
      if(true == matched)
        return true;
      else{
        visited[m][n] = false;
        count--;
        return false;
      }
    }
    else
      return false;
 }

public:
  bool exist(vector<vector<char> > &board, string word){
    if (word.size() == 0 || board.size() == 0)
      return false;

    int num_row = board.size();
    int num_col = board[0].size();
    vector<vector<bool> > visited(num_row, vector<bool> (num_col, false));
    for (int i = 0; i < num_row; ++i)
    {
      for (int j = 0; j < num_col; ++j)
      {
        if (board[i][j] == word[0]) {
          int count = 0;
          if (searchWord(board, i, j, word, count, visited)){
            return true;
          }
        }
      }
    }
    return false;
  }

  void printMatrix(vector<vector<char> > &board){
    for (int i = 0; i < board.size(); ++i)
    {
      for (int j = 0; j < board[0].size(); ++j)
      {
        printf("%c ", board[i][j]);
      }
      printf("\n");
    }
  }
};

int main(int argc, char const *argv[])
{
  vector<vector<char> > board;

  char tm_1[] = "CAA";
  vector<char> test_1(tm_1, tm_1 + sizeof(tm_1) / sizeof(char) - 1);
  board.push_back(test_1);

  char tm_2[] = "AAA";
  vector<char> test_2(tm_2, tm_2 + sizeof(tm_2) / sizeof(char) - 1);
  board.push_back(test_2);

  char tm_3[] = "BCD";
  vector<char> test_3(tm_3, tm_3 + sizeof(tm_3) / sizeof(char) - 1);
  board.push_back(test_3);

  Solution sol;
  sol.printMatrix(board);

  string word("AAB");
  if (sol.exist(board, word))
  {
    printf("true\n");
  }
  else {
    printf("false\n");
  }
  return 0;
}