class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        temp = []
        

        for i in range(len(boxes)):
            if boxes[i] == "1":
                temp.append(i)
        print(temp)
        for i in range(len(boxes)):
            count = 0
            for j in temp:
                count += abs(i - j)
            result.append(count)

        return result
