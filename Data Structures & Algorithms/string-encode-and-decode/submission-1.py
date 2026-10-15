class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for str in strs:
            encoded_str.append(f"{len(str)}#{str}")
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i=0
        
        while i < len(s):
            j=i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])

            start = j + 1
            end = start + l

            decoded_str.append(s[start:end])
            i = end

        return decoded_str


