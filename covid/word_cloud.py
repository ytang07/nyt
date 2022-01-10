from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# wordcloud function
def word_cloud(text, filename):
    stopwords = set(STOPWORDS)
    stopwords.add("covid")
    frame_mask=np.array(Image.open("cloud_shape.png"))
    wordcloud = WordCloud(max_words=50, mask=frame_mask, stopwords=stopwords, background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(f'{filename}.png')
