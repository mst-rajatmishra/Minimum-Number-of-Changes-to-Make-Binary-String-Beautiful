class Solution:
    def minChanges(self, s: str) -> int:
        # Initialize the number of changes needed
        changes = 0
        
        # Traverse the string in steps of 2 (pair by pair)
        for i in range(0, len(s), 2):
            # If the two characters in the pair are different, we need to change one of them
            if s[i] != s[i + 1]:
                changes += 1
        
        return changes

