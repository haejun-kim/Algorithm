import sys
sys.stdin = open("1181_단어정렬_input.txt")

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
words = list(set(words))
# word_dict = {}

words.sort()
words.sort(key=lambda x: len(x))
print(words)
# for word in words:
#     word_dict[word] = len(word)
#
# sorted_dict = sorted(word_dict.items(), key=lambda item: item[1])
#
# for word in sorted_dict:
#     print(word[0])
