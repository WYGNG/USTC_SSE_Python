# -*- coding:utf-8 -*-
import numpy as np

def compute_errlist(m, s, t):
    errlist = []
    len1 = len(s)
    len2 = len(t)
    while len1 != 0 or len2 != 0:
        if m[len1][len2][3] == m[len1][len2][0] and m[len1][len2][0] == m[len1-1][len2-1][3]:
            len1 -= 1
            len2 -= 1
            #print 'copy: ' + s[len1] + ' to ' + t[len2]
        elif m[len1][len2][3] == m[len1][len2][0] and m[len1][len2][0] == m[len1-1][len2-1][3] + 1:
            len1 -= 1
            len2 -= 1
            errlist.insert(0, [u'错', len1, s[len1], len2, t[len2]])
            #print u'错字: [' + str(len1) + '] ' + s[len1] + ' to [' +  str(len2) + '] ' + t[len2]
        elif m[len1][len2][3] == m[len1][len2][1] and m[len1][len2][1] != 0:
            len1 -= 1
            errlist.insert(0, [u'多', len1, s[len1], len2, ''])
            #print u'多字: [' + str(len1) + '] ' + s[len1] + ' to [' +  str(len2) + '] *'
        elif m[len1][len2][3] == m[len1][len2][2] and m[len1][len2][2] != 0:
            len2 -= 1
            errlist.insert(0, [u'缺', len1, '', len2, t[len2]])
            #print u'缺字: [' + str(len1) + '] * to [' +  str(len2) + '] '+ t[len2]
    return errlist
def get_errlist(s, t):
    len1 = len(s)
    len2 = len(t)
    m = np.zeros((len1 + 1, len2 + 1, 4), int)
    for i in range(len1 + 1):
        m[i][0][1] = i
        m[i][0][3] = i
    for j in range(len2 + 1):
        m[0][j][2] = j
        m[0][j][3] = j
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s[i-1] == t[j-1]:
                m[i][j][0] = m[i-1][j-1][3] #copy(cost 0)
            else:
                m[i][j][0] = m[i-1][j-1][3] + 1 #replace(cost 1)
            m[i][j][1] = m[i-1][j][3] + 1 #delete(cost 1)
            m[i][j][2] = m[i][j-1][3] + 1 #insert(cost 1)
            # the least cost until this step
            m[i][j][3] = min(m[i][j][0], m[i][j][1], m[i][j][2])
    return compute_errlist(m, s, t)

def match(s, t):
    errlist = get_errlist(s, t)
    idx = -2
    elog = ''
    pos1_s = ''
    str1 = ''
    pos2_s = ''
    str2 = ''
    pos1_e = ''
    pos2_e = ''
    errtype = ''

    spos = set()
    tpos = set()
    logs = []
    for err in errlist:
        if err[1] > idx + 1 or (err[1] > idx and errtype == u'缺' == err[0]):
            if idx >= 0:
                pos1 = '[' + pos1_s + '-' + pos1_e + ']' if pos1_s != pos1_e else '[' + pos1_s + ']'
                pos2 = '[' + pos2_s + '-' + pos2_e + ']' if pos2_s != pos2_e else '[' + pos2_s + ']'
                log = pos1 + str1 + u'&nbsp;→&nbsp;' + pos2 + str2
                prefix = ''
                if pos1_s == '0' and pos1_e != str(len(s) - 1) and len(s) > 0:
                    prefix = u'句首'
                if pos1_s != '0' and pos1_e == str(len(s) - 1) and len(s) > 0:
                    prefix = u'句尾'
                log = prefix + errtype + u'字:' + log
                logs.append(log)
                #print log
            pos1_s = str(err[1])
            str1 = ''
            pos2_s = str(err[3])
            str2 = ''
            errtype = ''
        pos1_e = str(err[1])
        str1 += err[2]
        pos2_e = str(err[3])
        str2 += err[4]
        idx = err[1]
        if errtype.find(err[0]) < 0: errtype += err[0]
        if err[2] != '': spos.add(err[1])
        if err[4] != '': tpos.add(err[3])
    if idx >= 0:
        pos1 = '[' + pos1_s + '-' + pos1_e + ']' if pos1_s != pos1_e else '[' + pos1_s + ']'
        pos2 = '[' + pos2_s + '-' + pos2_e + ']' if pos2_s != pos2_e else '[' + pos2_s + ']'
        #log = pos1 + str1 + '&nbsp;-&gt;&nbsp;' + pos2 + str2
        log = pos1 + str1 + u'&nbsp;→&nbsp;' + pos2 + str2
        prefix = ''
        if pos1_s == '0' and pos1_e != str(len(s) - 1) and len(s) > 0:
            prefix = u'句首'
        if pos1_s != '0' and pos1_e == str(len(s) - 1) and len(s) > 0:
            prefix = u'句尾'
        log = prefix + errtype + u'字:' + log
        logs.append(log)
        #print log

    return spos, tpos, logs

def demo(item):
    its = item.split(',')
    imgname = its[0]
    s = its[1]
    t = its[2]
    spos, tpos, logs = match(s, t)
    print('------------result--------------')
    for log in logs:
        print(log)
    print(spos)
    print(tpos)

if __name__ == '__main__':
    s = 'img_941_1,为无限责任么同,华为有限责任公司'
    demo(s)
    