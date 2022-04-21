"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current = 0
        last = len(words)
        out_lines = []
        
        while current < last:
            spaces_needed = maxWidth - len(words[current])
            nxt = current + 1
            
            while nxt < last and spaces_needed - (1 + len(words[nxt])) >= 0:
                spaces_needed -= 1 + len(words[nxt])
                nxt += 1
                
            gaps_needed = nxt - current - 1
            space_per_gap = 0
            leftovers = 0
            end_spaces = spaces_needed
            
            if gaps_needed != 0 and nxt != last:
                space_per_gap = spaces_needed // gaps_needed
                leftovers = spaces_needed % gaps_needed
                end_spaces = 0
            
            line = words[current]
            for j in range(current + 1, nxt):
                line += " " * (1 + space_per_gap + (1 if leftovers > 0 else 0)) + words[j]
                leftovers -= 1
            
            line += " " * end_spaces
            out_lines.append(line)
            current = nxt
            
        return out_lines
                