import sys

OPEN = 0
CLOSE = 1


def parse(html):
    idx = 0
    tags = []
    while True:
        if idx >= len(html):
            break

        # 태그 시작
        if html[idx] == '<':
            flag = OPEN
            idx += 1

            # 닫는 태그인 경우
            if html[idx] == '/':
                flag = CLOSE
                idx += 1

            # 태그 읽기
            tag = ""
            while html[idx] != '>' and idx < len(html):
                # 단일 태그인 경우
                if idx < len(html) - 1 and html[idx] == '/' and html[idx + 1] == '>':
                    tag = ""
                    break

                tag += html[idx]
                idx += 1

            if tag:
                tags.append((flag, tag.split()[0]))
        idx += 1

    ans = "legal"
    stack = []
    for flag, tag in tags:
        if flag == OPEN:
            stack.append(tag)
        else:
            if stack and tag == stack[-1]:
                stack.pop()
            else:
                ans = "illegal"
                break
    if stack:
        ans = "illegal"
    print(ans)


while True:
    s = sys.stdin.readline().rstrip()
    if s == "#":
        break
    parse(s)
