import re

with open('input') as f:
    lines = f.read().splitlines()

output = ''

# TODO: just strip .jpg name title

test = """'        a(href="img/galerie/entstehung/IMG_3272.JPG" data-sub-html="<h4>IMG_3272.JPG - 18. Dezember 2017</h4>")'"""

image_counter = 1

for l in lines:
    stripped_l = l.strip()
    if stripped_l.startswith('a(href=') or stripped_l.startswith('img(alt='):
        new_l = re.sub(r"(?<=\"<h4>).*(?=\d\d\.)", "", l)
        new_l = re.sub(r"(?<=img\(alt=\").*(?=\d\d\. )", "", new_l)
        output += new_l
    else:
        # h2 tags or other things not important to modify
        output += l
    if stripped_l.startswith('a(href='):
        image_counter += 1
    output += '\n'

print(output)
