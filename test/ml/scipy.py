from scipy.misc import imread


def test1():
    # 读取图片
    img = imread("timg.jpg")
    # 获取图片的数据类型
    img_type = img.dtype
    print(img_type)  # uint8
    # 获取图片的大小
    img_shape = img.shape
    print(img_shape)  # (310, 493, 3)
    # 获取图片的高
    img_height = img_shape[0]
    print(img_height)  # 310
    # 获取图片的宽
    img_width = img_shape[1]
    print(img_width)  # 493
    # 获取图片的通道数
    img_channel = img_shape[2]
    # 通道数为1表示黑白图片，通道数为3表示彩色图片
    print(img_channel)  # 3


if __name__ == "__main__":
    test1()
