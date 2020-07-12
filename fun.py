import json

from PIL import Image
from jieba.analyse import extract_tags
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as plt
import numpy as np
import platform


def find_team_name(id):
    with open('teamId.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data[str(id)]


def find_player_name(id):
    with open('playerId.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data[str(id)]


def calculate_news(name):
    with open('news.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    related_news = []
    related_news_body = []
    i = 0
    for temp in data:
        i += 1
        '''if i % 100 == 0:
            print(i)'''
        for t2 in temp['labels']:
            if t2['name'] == name:
                related_news.append(temp)
                related_news_body.append(temp['newsBody'])
                break
    return related_news_body


def calculate_keywords(news_list):
    text = ""
    for s in news_list:
        text += s
    keywords = extract_tags(text, topK=100, withWeight=True, allowPOS=())
    # for word, weight in keywords:
    #     print(word, weight)
    print(keywords)
    return keywords


def draw_word_cloud(keywords, nid, type):
    if not keywords:
        return False

    # 设置背景图片
    background = np.array(Image.open("温格.jpg"))
    '''if type == 0:
        background = np.array(Image.open("温格.jpg"))
    elif type == 1:
        background = np.array(Image.open("斯托克城.png"))'''

    sys_str = platform.system()
    if sys_str == "Linux":
        font_path = r'SIMSUN.TTC'
    elif sys_str == "Windows":
        font_path = r'C:\Windows\Fonts\SimSun.TTC'
    # print(font_path)
    wc = WordCloud(background_color='White', max_words=1000, mask=background,
                   max_font_size=500, random_state=444, font_path=font_path)

    # 生成词云, keywords是上一步中jieba提取的关键词
    wc.generate_from_frequencies(dict(keywords))

    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(background)

    # 以下代码显示图片
    plt.figure(figsize=(7, 8))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")

    # 绘制词云
    # recolor wordcloud and show
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    # 0球员 1图片
    if type == 0:
        # plt.savefig('image/player' + str(nid) + '.png')
        wc.to_file('image/player' + str(nid) + '.png')
    elif type == 1:
        # plt.savefig('image/team' + str(nid) + '.png')
        wc.to_file('image/team' + str(nid) + '.png')
    plt.axis("off")

    return True
