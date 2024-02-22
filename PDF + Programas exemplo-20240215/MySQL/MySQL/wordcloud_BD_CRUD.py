import matplotlib.pyplot as plt
from wordcloud import WordCloud

import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = "pymysql MySQL Workbench AUTO_NUMBER INT SMAILINT DATETIME CURRENT_TIMESTAMP INTERVAL CRUD BLOB CREATE DATABASE DROP ALTER INSERT SELECT UPDATE DELETE FROM WHERE ORDER BY GROUP BY HAVING"
wc = WordCloud(width=800,height=450, background_color='white', min_font_size=14).generate(text)
print(type(wc))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.savefig("crud_MySQL.png", format="png")
plt.show()

