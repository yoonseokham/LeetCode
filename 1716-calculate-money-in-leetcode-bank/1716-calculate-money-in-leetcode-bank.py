class Solution:
    def totalMoney(self, n: int) -> int:
        previous_monday_save = 0
        saved_money = 0
        for i in range(n):
            if not i%7:
                previous_monday_save += 1
            saved_money += i % 7 + previous_monday_save
        return saved_money