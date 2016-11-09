#!/bin/ruby
class WordSearch
  def search(board, word)
    board.each do |row|
      row.each do |element|
        if word[0] == element
        end
      end
    end
  end

  def printBoard(board)
    board.each do |row|
      row.each do |col|
        print col
      end
      print "\n"
    end
  end
end

test = [[1,2,3], [4,5,6], [7,8,9]]
ws = WordSearch.new
ws.printBoard(test)
