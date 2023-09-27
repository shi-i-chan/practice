# June 2021

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation

fig = plt.figure()
frames = []

for i in range(0, 800, 10):
    img_path = f"./qtable_charts/{i}.png"
    image = mpimg.imread(img_path)
    image = [plt.imshow(image, animated=True)]
    frames.append(image)

Animation = animation.ArtistAnimation(fig,
                                      frames,
                                      interval=100,
                                      blit=True,
                                      repeat_delay=1000)
#Animation.save('q-table_gif.gif', writer='imagemagick', fps=60)
plt.show()