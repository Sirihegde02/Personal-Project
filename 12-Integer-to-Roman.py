class Solution:
    def intToRoman(self, num: int) -> str:
        #Creating a list of lists in descending order (also added edge cases to this):
        symbol_list = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
        result = \\
        for value, symbol in symbol_list:
            if num // value: #If this isn't possible (value greater than num), then it won't run and will go to the next lower value
                count = num // value #Number of times we will add this symbol to the result
                result += (symbol * count)
                num = num % value #Updating num by getting rid of the first digit now that it was processed
        return result