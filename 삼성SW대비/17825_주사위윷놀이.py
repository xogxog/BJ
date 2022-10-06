shortcut = {
    10: [10, 13, 16, 19, 25, 300, 35, 40],
    20: [20, 22, 24, 25, 300, 35, 40],
    30: [30, 28, 27, 26, 25, 300, 35, 40]
}


def move(horses, chk, m_cnt, idx, t_sum):  # 말, 지름길체크, 움직일 수, 몇번째말 움직일건지
    # print(f'{idx}번째말을 {m_cnt}만큼 움직일겨')
    # print(f'horses : {horses}, chk : {chk}')
    tmp_horse = horses[:]
    tmp_chk = chk[:]
    tmp_s = t_sum

    tmp_horse[idx] = horses[idx]
    if not tmp_chk[idx]:    # 지름길X
        tmp_horse[idx] += (m_cnt*2)
        if tmp_horse[idx] < 40 and tmp_horse[idx] % 10 == 0:  # 옮기고 도착한 곳이 지름길이면 체크
            tmp_chk[idx] = tmp_horse[idx]
        # 겹치는 말 체크
        if tmp_horse[idx] == 40 and 40 in horses:
            return horses, chk, t_sum, 1
        for i in range(4):
            if (tmp_horse[idx], tmp_chk[idx]) == (horses[i], chk[i]):
                return horses, chk, t_sum, 1

    else:              # 지름길
        for i in range(len(shortcut[tmp_chk[idx]])):
            if shortcut[tmp_chk[idx]][i] == tmp_horse[idx]:
                if i+m_cnt >= len(shortcut[tmp_chk[idx]]):        # 도착
                    tmp_horse[idx] = 41
                    break
                else:
                    tmp_horse[idx] = shortcut[chk[idx]][i+m_cnt]  # 도착X
                    if tmp_horse[idx] == 40 and 40 in horses:
                        return horses, chk, t_sum, 1
                    for j in range(4):
                        if chk[j] and tmp_horse[idx] == horses[j]:  # 겹치는 말
                            return horses, chk, t_sum, 1
                    break

    # print(f'움직이고나서 horses : {tmp_horse}, chk : {tmp_chk}')
    if tmp_horse[idx] == 300:
        tmp_s += 30
    elif tmp_horse[idx] <= 40:
        tmp_s += tmp_horse[idx]

    return tmp_horse, tmp_chk, tmp_s, 0


def play(horses, chk, t_sum, dice_idx):

    global ans
    if dice_idx == 10:
        ans = max(ans, t_sum)
        return

    for j in range(4):
        if horses[j] != 300 and horses[j] > 40:
            pass
        else:
            tmp_h, tmp_c, tmp_sum, flag = move(
                horses, chk, dice[dice_idx], j, t_sum)
            if not flag:
                play(tmp_h, tmp_c, tmp_sum, dice_idx+1)


dice = list(map(int, input().split()))
ans = 0
play([0, 0, 0, 0], [0, 0, 0, 0], 0, 0)
print(ans)
