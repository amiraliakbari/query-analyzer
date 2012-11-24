'''
Created on Nov 15, 2012

@author: Mehrdad
'''
import sys
import sql

if __name__ == '__main__':
    queries = []
    lines = []
    flag = 0
    if len(sys.argv) == 2:
        if sys.argv[1] == "--print-queries":
            flag = 1
            line = sys.stdin.readline()
            while len(line) > 0:
                lines.append(line)
                line = sys.stdin.readline()
        else:
            f = open(sys.argv[1][2:], 'r')
            lines = f.readlines()
    elif len(sys.argv) == 3:
        flag = 1
        if sys.argv[1] == "--print-queries":
            f = open(sys.argv[2][2:], 'r')
            lines = f.readlines()
        else:
            f = open(sys.argv[1][2:], 'r')
            lines = f.readlines()
    else:
        line = sys.stdin.readline()
        while len(line) > 0:
            lines.append(line)
            line = sys.stdin.readline()
    for i in range(0, len(lines) / 2):
	queryDic = {}
        queryDic['sql'] = lines[i * 2]
        queryDic['time'] = int(lines[i * 2 + 1])
        queries.append(queryDic)
    Dictionary = sql.analyze_queries(queries, flag)
    sql.printDictionary(Dictionary)
