# https://leetcode.com/problems/text-justification/

from typing import List


class Solution:

    def left_justify(self, space: int, words: List[str]) -> str:
        convert = [words[0]]
        for idx in range(1, len(words)):
            space -= 1
            convert.append(" ")
            convert.append(words[idx])
        convert.append(" " * space)
        return "".join(convert)

    def justify(self, space: int, words: List[str]) -> str:
        convert = [words[0]]
        space_count = space // (len(words) - 1)
        space_remain = space % (len(words) - 1)
        for i in range(1, len(words)):
            # If the number of spaces on a line does not divide evenly between words,
            # the empty slots on the left will be assigned more spaces than the slots on the right
            if space_remain:
                space_remain -= 1
                convert.append(" " * (space_count + 1))
            else:
                convert.append(" " * space_count)
            convert.append(words[i])

        return "".join(convert)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        splits = []
        cur_text_width, only_char_size = maxWidth, 0
        row = []
        for word in words:
            if cur_text_width - len(word) >= 0:
                row.append(word)
                only_char_size += len(word)
                cur_text_width -= len(word)
            else:
                # Append (space_count, list of text line words)
                splits.append((maxWidth - only_char_size, row[:]))
                row = [word]
                cur_text_width = maxWidth - len(word)
                only_char_size = len(word)
            # Add space
            cur_text_width -= 1

        if row:
            splits.append((maxWidth - only_char_size, row[:]))

        result = []
        # Justify texts
        for idx in range(len(splits) - 1):
            space, strings = splits[idx][0], splits[idx][1]
            if len(strings) == 1:
                result.append(self.left_justify(space, strings))
            else:
                result.append(self.justify(space, strings))
        # Justify last texts
        result.append(self.left_justify(splits[-1][0], splits[-1][1]))
        return result
