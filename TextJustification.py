class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cur, res, numoflet = [], [], 0
        for w in words:
            if len(w) + len(cur) + numoflet > maxWidth:
                for i in xrange(maxWidth - numoflet):
                    cur[i % (len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, numoflet = [], 0
            cur += [w]
            numoflet += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]