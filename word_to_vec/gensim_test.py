from gensim.corpora import WikiCorpus  # 使用gensim模块中的WikiCorpus从bz2中获取原始文本数据
import jieba


def myfunction():
    space = ' '
    i = 0
    l = []
    zhwiki_name = ''
    f = open('', 'w')
    wiki = WikiCorpus(zhwiki_name, lemmatize=False, dictionary={})  # xml文件中当初的训练语料
    for text in wiki.get_texts():
        for temp_sentence in text:
            temp_sentence = Converter('zh-hans').convert(temp_sentence)  # 将语料中的繁体字转换为简体
            seg_list = list(jieba.cut(temp_sentence))  # 利用jieba分词
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        i = i + 1

        if (i % 200 == 0):
            print("saved" + str(i) + "articles")
    f.close()


if __name__ == '__main__':
    myfunction()