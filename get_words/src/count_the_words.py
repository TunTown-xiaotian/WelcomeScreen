
GET_WORDS='result.txt'

def load_words():
    count_dict = {}
    words_list=[]
    try:
        with open(GET_WORDS, 'r', encoding='utf-8') as s:
            for line in s:
                words=line.strip().split()
                if not line:
                    print("this line is empty!")
                    continue
                for word in words:
                    count_dict[word] = count_dict.get(word,0) + 1
        for word,count in count_dict.items():
            words_list.append((word,count))
        sorted_list = sorted(words_list, reverse=True,key=lambda x:x[1])
        print(sorted_list)

    except FileNotFoundError:
        print("FileNotFoundError")
        pass
        return None
    return words


def words_cleaning(word):
    words= word.upper()
    return words

if __name__ == "__main__":
    load_words()