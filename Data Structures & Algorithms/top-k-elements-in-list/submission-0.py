class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            if str(num) in count_dict:
                count_dict[str(num)] += 1
            else:
                count_dict[str(num)] = 1
        sorted_dict = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
        print(sorted_dict)
        top_k_keys = list(sorted_dict.keys())[:k]
        return top_k_keys