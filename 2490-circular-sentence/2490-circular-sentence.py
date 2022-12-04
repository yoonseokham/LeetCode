class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_list = list(sentence.split())
        sentence_list.append(sentence_list[0])
        for index,value in enumerate(sentence_list[:-1]):
            if value[-1] != sentence_list[index+1][0]:
                return False
        return True