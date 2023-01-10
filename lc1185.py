class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def isLeap(year):
	        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		        return 1
	        else:
		        return 0
        result = 365 * (year - 1971) + 4
        for i in range(1971, year):
	        result += isLeap(i)
        if isLeap(year):
	        days[1] = 29
        result += sum(days[ : month - 1]) + day
        return d[result % 7]