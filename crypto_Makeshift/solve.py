c = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"[::-1]
print(c)

new_flag = ''
for i in range(0, len(c), 3):
    new_flag += c[i+1]
    new_flag += c[i+2]
    new_flag += c[i]

print(new_flag)
