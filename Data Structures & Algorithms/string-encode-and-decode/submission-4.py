class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the '#' marking end of the length
            j = s.find('#', i)
            length = int(s[i:j])
            # The next `length` chars are the actual string
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result

