class Solution:
    def nextGreatestLetter(self, letters, target) :
        if letters[-1]<=target:
            return letters[0]
        else:
            if target in letters and letters.count(target)==1:
                return letters[letters.index(target)+1]
            elif target in letters:
                pos=0
                for i in range(len(letters)):
                    if letters[i]==target:
                        pos=i
                return letters[pos+1]
            else:
                for i in letters:
                    if i>target:
                        return i
