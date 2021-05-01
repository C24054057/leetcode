class Solution(object):
    def __init__(self):
        self.letters = {'0':'',
                        '1':'',
                        '2':'abc',
                        '3':'def',
                        '4':'ghi',
                        '5':'jkl',
                        '6':'mno',
                        '7':'pqrs',
                        '8':'tuv',
                        '9':'wxyz'}
        self.digits = ''
        self.output = list()

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
# input為空，直接return
        if not digits:
            return self.output
        self.digits = digits
# 進入遞迴
        self.r(letter_combinations='', index_of_current_digit=0)
        return self.output
        
    def r(self, letter_combinations, index_of_current_digit):
        """
        此為遞迴函式，利用迴圈將目前的數字對應到的字母都配對一遍，其中每配對一次就進入遞迴找下個數字對應的字母。遞迴至沒數字時則將串聯好的字母放進list。
        
        :type letter_combinations： str
        # 目前串連好的字母
        :type index_of_current_digit: int
        # input裡欲解讀的第_個數字
        """
        if index_of_current_digit == len(self.digits):
            self.output.append(letter_combinations)
        else:
            for letter in self.letters[self.digits[index_of_current_digit]]:
                tmp_lc = letter_combinations + letter
                self.r(tmp_lc, index_of_current_digit+1)


# s = Solution()
# s.letterCombinations('23')
# s.letterCombinations('')
# s.letterCombinations('2')