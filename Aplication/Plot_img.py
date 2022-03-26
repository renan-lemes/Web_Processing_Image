import matplotlib.pyplot as plt

class PlotImage:
    __init__():
        pass
    
    def show_image(image, title='Image', cmap_type='gray'):
        plt.imshow(image, cmap=cmap_type)
        plt.title(title)
        plt.axis('off')
        plt.show()