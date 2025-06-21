class Solution:
    def calPoints(self, operations: List[str]) -> int:
        count = []
        for op in operations:
            if op == "C":
                count.pop()
            elif op == "D":
                count.append(2 * count[-1])
            elif op == "+":
                count.append(count[-1] + count[-2])
            else:
                count.append(int(op))
        return sum(count)