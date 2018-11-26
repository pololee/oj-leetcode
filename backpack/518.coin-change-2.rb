# @param {Integer} amount
# @param {Integer[]} coins
# @return {Integer}
def change(amount, coins)
  dp = Array.new(amount + 1, 0)
  dp[0] = 1

  (1..amount).to_a.each do |amt|
    coins.each do |coin|
      next if amt < coin

      dp[amt] += dp[amt - coin]
    end
  end

  dp[amount]
end
