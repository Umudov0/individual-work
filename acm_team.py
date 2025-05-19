def acm_team(t):
    m, c = 0, 0
    for i in range(len(t)):
        for j in range(i+1, len(t)):
             if s > m: m, c = s, 1
             elif s==m: c+= 1
    return [m, c]


