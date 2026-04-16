# for each day, calculate the number of days since jan 1, 1971
# to do this, we first calculate the difference in days between the years
# 3, 7, 11, 15, 19, etc. years after will be a leap year
# so the number of leap days will be (diff years + 1) // 4
# so do 365 + leap days 
# then, add the days for the month
# if year % 4 == 0 and year != 2100, it's a leap year
# so, we add the sum of all months <= that month, which is an arr with a running sum
#then, we add the days
# dayof[total days % 7] is our answer

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        diff_years = year - 1971
        years_days = diff_years * 365 + (diff_years+2)//4
        days_before = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                     #        J   F   M   A   M   J  J   A    S   O   N   D
        if year % 4 == 0 and year != 2100:
            days_before[3] += 1
        months_days = []
        cur_sum = 0
        for n in days_before:
            cur_sum += n
            months_days.append(cur_sum)
        all_days = years_days + months_days[month] + day-1

        return days[all_days % 7]
