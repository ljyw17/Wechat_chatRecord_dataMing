#coding=utf-8

# from scipy.misc import imread
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import jieba, pandas as pd
from collections import Counter
import jieba.posseg as pseg

def draw_wordcloud(c):

    # d = path.dirname(__file__) #当前文件文件夹所在目录
    # color_mask =  plt.imread(r"F:\download\a.jpeg") #读取背景图片，
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码，文件名不支持中文
        font_path = r"E:\tim\applications\records\code\simhei.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色，默认为黑，可根据需要自定义为颜色
        background_color='white',
        #词云形状，
        # mask=color_mask,
        #允许最大词汇
        max_words=300,
        #最大号字体，如果不指定则为图像高度
        max_font_size=80,
        #画布宽度和高度，如果设置了msak则不会生效
        width=600,
        height = 400,
        margin = 2,
        #词语水平摆放的频率，默认为0.9.即竖直摆放的频率为0.1
        prefer_horizontal = 0.8
        # relative_scaling = 0.6,
        # min_font_size = 10
    ).generate_from_frequencies(c)
    plt.imshow(cloud)
    plt.axis("off")
    plt.show()

    cloud.to_file(r"E:\tim\applications\records\code\word_cloud_H.png")
    # plt.savefig(r"E:\tim\applications\records\code\word_cloud_E.png", format="png")

def get_words(txt):
    seg_list = []
    words = pseg.cut(txt)
    for word, flag in words:
        if flag in ("n", "nr", "ns", "nt", "nw", "nz"):
            # n, "f", "s", "nr", "ns", "nt", "nw", "nz", "PER", "LOC", "ORG", "v"
            # n nr ns nt nw nz
            seg_list.append(word)
    c = Counter() # 计数器
    for x in seg_list:
        if len(x)>1 and x not in ("\r\n"):
            c[x] += 1 #个数加一
    return c.most_common(305)
    print()
    # return " ".join(seg_list)

if __name__=="__main__":

    xls = pd.read_excel(r'E:\tim\applications\records\xlsx\Chat_H.xlsx', header=0)

    # sega = ""
    list = []
    for i in range(len(xls))[::35]:
        list.append(str(xls["content"][i]))
        # sega += str(xls["content"][i])

    c = get_words("".join(list))
    dict = {}
    for i in c:
        dict[i[0]] = i[1]

    # txt = ""
    # for i in lista:
    #     txt += i[0]
    #     txt += " "
    draw_wordcloud(dict)
    # 词云
    print("--")

    # sega = ""
    # segb = ""
    # for i in range(len(xls)):
    #     if xls["status"][i] == 0:
    #         sega += str(xls["content"][i])
    #     if xls["status"][i] == 1:
    #         segb += str(xls["content"][i])
    # lista = get_words(sega)
    # listb = get_words(segb)



    # G = nx.Graph()  # 创建空的网络图
    # edge_list = []
    # node_list = []
    # node_color_list = []
    #
    # G.add_node("我")
    # node_list.append("我")
    # node_color_list.append('#ede85a')
    # i = 0
    # for j in lista[:60]:
    #     # if j[0] in (""):
    #     #     continue
    #     if i < 15:
    #         node_color_list.append('#095dbe')
    #     elif i < 30:
    #         node_color_list.append('#5a9eed')
    #     elif i < 45:
    #         node_color_list.append('#7face1')
    #     else:
    #         node_color_list.append('#e1e8ef')
    #     G.add_node(j[0])
    #     node_list.append(j[0])
    #     G.add_edge("我", j[0])
    #     i += 1
    #
    # G.add_node("老师D")
    # node_list.append("老师D")
    # node_color_list.append('#e9586e')
    # i = -1
    # for j in listb[:60]:
    #     i += 1
    #
    #     if j[0] in node_list:
    #         G.add_edge("老师D", j[0])
    #         continue
    #     # if j[0] in (""):
    #     #     continue
    #     if i < 15:
    #         node_color_list.append('#095dbe')
    #     elif i < 30:
    #         node_color_list.append('#5a9eed')
    #     elif i < 45:
    #         node_color_list.append('#7face1')
    #     else:
    #         node_color_list.append('#e1e8ef')
    #     G.add_node(j[0])
    #     G.add_edge("老师D", j[0])
    #
    # pos = nx.fruchterman_reingold_layout(G)
    #
    # nx.draw_networkx_nodes(G, pos,node_size=280, node_color = node_color_list)
    # nx.draw_networkx_edges(G, pos)
    # nx.draw_networkx_labels(G, pos, font_size=6)
    # # nx.draw(G, with_labels=True, font_weight='bold', node_color = node_color_list)
    # plt.savefig("word_network_D.png",dpi=1800,bbox_inches = 'tight')
    # plt.show()
    #
    # print("--")