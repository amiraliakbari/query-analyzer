import sys
import operator

def analyze_queries(queries, print_queries=False):
    qtime = 0.0
    qlen = 0
    max_time = 0.0
    jlen = 0
    tables = {}
    sqls = {}
    for query in queries:
        sql = query['sql']
        time = float(query['time'])
        qlen += 1
        qtime += time
        if time > max_time: max_time = time
        if not sql in sqls.keys(): sqls[sql] = 0
        sqls[sql] += 1
        if ' JOIN ' in sql:
            jlen += 1
        ind = sql.find(' FROM `')
        if ind >= 0:
            table = sql[ind+7:sql.find('`', ind+7)]
            if not table in tables.keys(): tables[table] = 0
            tables[table] += 1

    if not qlen: return
    print >> sys.stderr, '\n*************************************************'
    print >> sys.stderr, 'Queries Count:\t%d' % qlen
    print >> sys.stderr, 'Join Queries:\t%d' % jlen
    print >> sys.stderr, 'Total Time: \t%.2f' % qtime
    print >> sys.stderr, 'Maximum Time:\t%.2f' % max_time
    print >> sys.stderr, 'Average Time:\t%.2f' % (qtime / max(1, qlen))
    print >> sys.stderr, 'Table Share:'
    for k, v in sorted(tables.iteritems(), key=operator.itemgetter(1), reverse=True):
        print >> sys.stderr, '\t%d %s' % (v, k)
    print >> sys.stderr, '*************************************************'

    duplicate_queries = filter(lambda item: item[1]>1, sqls.iteritems())
    if duplicate_queries:
        print >> sys.stderr, 'Duplicate Queries:'
        for k, v in duplicate_queries:
            print >> sys.stderr, '\t[x%d] %s' % (v, k)
        print >> sys.stderr, '*************************************************'

    if print_queries:
        for query in queries:
            print >> sys.stderr, query['sql']
        print >> sys.stderr, '*************************************************\n'

    print >> sys.stderr, '\n'

    
queries = [
    {'sql': 'SELECT first_name, last_name FROM table1 WHERE id=1', 'time': 13},
    {'sql': 'SELECT first_name, last_name FROM table1 WHERE id=1', 'time': 8},
    {'sql': 'SELECT first_name, last_name FROM table1 WHERE id=2', 'time': 17},]
analyze_queries(queries, print_queries=True)

