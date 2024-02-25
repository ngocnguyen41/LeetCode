class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def checkMin(min):
            last = price[0]
            count = 1
            for i in range(1, len(price)):
                if price[i] - last >= min:
                    last = price[i]
                    count += 1
            return count

        left = 0
        right = price[-1] - price[0]
        temp = 0

        while left <= right:
            mid = (right + left) // 2      
            if checkMin(mid) >= k:
                left = mid + 1
                temp = mid
            else:
                right = mid - 1           
        return temp

         