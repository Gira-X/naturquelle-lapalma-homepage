import os
from PIL import Image

template = '''
        a(href="XX")
            img(src="XY")
'''

# needs to start and end with /
dirs_to_process = ['/img/galerie/']

cwd = os.getcwd()
for d in dirs_to_process:
    full_dir = cwd + d
    thumbs = os.path.join(full_dir, 'thumbs/')
    if not os.path.exists(thumbs):
        os.mkdir(os.path.join(full_dir, 'thumbs/'))
    files = [f for f in os.scandir(full_dir)
             if os.path.isfile(os.path.join(full_dir, f)) and
             f.name.endswith('.jpg')]
    for f in files:
        im = Image.open(f.path)
        im.thumbnail((350, 350))
        im.save(f"{full_dir}thumbs/{f.name}")
        absolute_img = f.path[f.path.find('img/'):]
        thumb_img = absolute_img[absolute_img.find('img/'):] + 'thumbs/'
        print(template
              .replace('XX', f'{d[1:]}{f.name}')
              .replace('XY', f'{d[1:]}thumbs/{f.name}'))
