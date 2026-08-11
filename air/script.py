# about, ideal applicants, resources provided, application process, timeline
# wheel: 20-40 --> loop this
s: str = "@keyframes partAnimation {\n"
total = 54 + (40-20+1)*7
pref = 20 + (40-20+1)*7
unit: float = 1/total*100
for i in range(total):
    curr = 0
    if i < 20:
        curr = i
    elif i > pref:
        curr = i - pref + 20
    else:
        curr = (i - 20) % 21 + 20
    f = str(curr+1).zfill(4)
    s += f"{(i+1)*unit}% {{background-image: url(../assets/partA/{f}.webp)}} \n"
s+="\n}"
print(s)