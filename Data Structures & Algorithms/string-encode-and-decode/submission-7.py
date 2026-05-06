class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += string + "--"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = s.split("--")
        return decoded_list[:-1]