import sys

input = sys.stdin.readline

def main(s):
    while True:
        st = []
        tmp = ''
        # true : 열림 , false : 닫힘
        rcnt_st = False
        # 태그가 될 수 있는 값들 리스트에 저장
        for i in s:
            if i == '<' and rcnt_st == False:
                rcnt_st = True
                tmp += i
            elif rcnt_st:
                tmp += i
                if i == '>':
                    st.append(tmp)
                    tmp = ''
                    rcnt_st = False
                elif i == '<':
                    return 'illegal'
        ans = []
        # 태그가 유효한지 검사
        while st:
            s_tmp = st.pop(0)
            # 단독 태그가 아닌 경우에 조건 검사
            if s_tmp[-2] != '/':
                # 닫는 태그인 경우 조합 확인
                if s_tmp[1] == '/':
                    # 여는 태그가 스택에 없는 경우 검사
                    if len(ans) == 0:
                        return 'illegal'
                    # 닫는 태그가 속성 값을 지니고 있는 경우 검사
                    for i in s_tmp:
                        if i == ' ':
                            return 'illegal'
                    # 각 태그 값 비교
                    if ans[-1][1:len(s_tmp)-2] == s_tmp[2:-1]:
                        ans.pop() # 같을 경우 여는 태그 제거로 쌍 완성
                    else:
                        return 'illegal' # 안 맞으면 리턴
                else:
                    ans.append(s_tmp)
        if len(ans) == 0:
            return 'legal' # 모든 태그가 쌍을 이루는 경우
        else:
            return 'illegal' # 여는 태그가 남은 경우

if __name__ == "__main__":
    while True:
        s = input().rstrip()
        if s == '#':
            break
        print(main(s))