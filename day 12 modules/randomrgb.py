from random import randint
def rgb_color_gen():
    a,b,c=randint(0,255),randint(0,255),randint(0,255)
    return (f'rgb ({a},{b},{c}))')
print(rgb_color_gen())
