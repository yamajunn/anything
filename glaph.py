display_list = [" " for i in range(8000)]

for i in range(len(display_list)):
    if 4000 < i < 4200:
        display_list[i] = "#"
    if i % 100 == 0:
        display_list[i] = "#"
    
    y = i % 200
    x = i - y*200
    if y == x and y*200+i <= 8000:
        display_list[y*200+x+200*20+100] = "="


for i in range(40):
    display_list[i*200]="\n"

display_str = "".join(display_list)
print(display_str)