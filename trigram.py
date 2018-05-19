#!/usr/bin/python

def count(words):
    words = words.replace(" ", "")
    counts = {}
    for i in range(len(words)):
        if i < len(words) - 4:
            word = words[i:i+3]
            for j in range(len(words)):
                if j < len(words) - 4:
                    if words[j:j+3] == word:
                        counts[word] = counts.get(word, 0) + 1
    return counts

words = 'RSZWO RSZCK CSGPS GVRTP CKCSG PRSJP YOGVR NPZND ZWOCH ZCROC GZWOR SZWOR SZCKS XQNHX VNDWJ YNZWO PCPSG VHOSP NGBTZ ZWOCG GOHXC DONDZ WOCHS HZPCP CGZWO QNHXV NDDNH RPCGZ WOYHN KOPPN DVCSX OKZCK SGVCZ PSHLT ROGZB JROZS YWNH'
print count(words)
for i, k in count(words).items():
    if k > 1:
        print(i, k)
