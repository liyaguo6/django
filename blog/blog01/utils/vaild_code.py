from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO  # 内存管理工具


def get_vaild_code_img(request):
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    img = Image.new('RGB', (270, 40), color=get_random_color())
    # 方式一
    # f = open('vaildCode.png','wb')
    # img.save(f,'png')
    # f.close()
    # with open('vaildCode.png','rb') as f:
    #     data = f.read()
    # 方式二
    # f = BytesIO()
    # img.save(f,'png')
    # data = f.getvalue()
    # 方式三
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r"static\blog01\font\仿宋_GB2312.ttf", size=38)
    vaild_code_str = ""
    for i in range(5):
        ran_num = str(random.randint(0, 9))
        ran_low_alpha = chr(random.randint(95, 122))
        ran_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([ran_num, ran_low_alpha, ran_upper_alpha])
        draw.text((i * 50 + 30, 5), random_char, get_random_color(), font=font)
        # 保存验证码字符串
        vaild_code_str += random_char
    request.session['vaild_code_str'] = vaild_code_str
    # print(vaild_code_str)

    # for i in range(20):
    #     x1 = random.randint(0,270)
    #     x2 = random.randint(0,270)
    #     y1 = random.randint(0,40)
    #     y2 = random.randint(0,40)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    # draw.point()
    f = BytesIO()
    img.save(f, 'png')
    data = f.getvalue()
    return data