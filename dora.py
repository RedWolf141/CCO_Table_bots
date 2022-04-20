


# 최소한 1개의 도라를 만들수 있을때
def makeBag(ts):
    dora = 0
    pan = 0
    old = 0
    if (ts > 15000):
        dora = ts // 15000
        ts = ts % 15000
        #패니팩을 만들수 있는가
        if (ts > 1000):
            pan = ts // 1000
            ts = ts % 1000

            old = ts // 100
            ts = ts % 100
        
        else:
            old = ts // 100
            ts = ts % 100

        string = f'도라의 개수는 {dora}, 보조가방의 개수는 {pan}, 낡은 주머니의 개수는 {old}, 남는 공조의 수는 {ts} 입니다'
        print(string)

    else:
        pan = ts // 1000
        ts = ts % 1000
        
        old = ts // 100
        ts = ts % 100
        string = f'도라의 개수는 {dora}, 보조가방의 개수는 {pan}, 낡은 주머니의 개수는 {old}, 남는 공조의 수는 {ts} 입니다'
        print(string)