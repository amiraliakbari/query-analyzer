import sys
import operator

def printDictionary(analyzed):
    s = '***************************\n'
    for k in analyzed.keys():
        v = analyzed[k]
        print (s)
        print k, '\n'
        for str in v:
            print str, '\n'
        print '\n'

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

    if not qlen:
        return
    ret = {}
    ret['General Informations'] = []
    ret['General Informations'].append('Queries Count:\t%d' % qlen)
    ret['General Informations'].append('Join Queries:\t%d' % jlen)
    ret['General Informations'].append('Total Time: \t%.2f' % qtime)
    ret['General Informations'].append('Maximum Time:\t%.2f' % max_time)
    ret['General Informations'].append('Average Time:\t%.2f' % (qtime / max(1, qlen)))
    ret['Table Share'] = []
    for k, v in sorted(tables.iteritems(), key=operator.itemgetter(1), reverse=True):
        ret['Talbe Share'].append('\t%d %s' % (v, k));
    

    duplicate_queries = filter(lambda item: item[1]>1, sqls.iteritems())
    if duplicate_queries:
        ret['Duplicate Queries'] = []
        for k, v in duplicate_queries:
            ret['Duplicate Queries'].append('\t[x%d] %s' % (v, k))

    if print_queries:
        ret['All queries'] = []
        for query in queries:
            ret['All queries'].append(query['sql'])

    return ret

