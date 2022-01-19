import json,math

with open("C:/Users/13375/Desktop/拼音输入法/Start_Probability.txt",'r',encoding='UTF-8') as S_Pfile:
    _=S_Pfile.read()
    Start_Probability=json.loads(_)

with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Two.txt",'r',encoding='UTF-8') as H_M_2file:
    _=H_M_2file.read()
    Hidden_Transition_Matrix_Two=json.loads(_)

with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Three.txt",'r',encoding='UTF-8') as H_M_3file:
    _=H_M_3file.read()
    Hidden_Transition_Matrix_Three=json.loads(_)

with open("C:/Users/13375/Desktop/拼音输入法/emission_Matrix.txt",'r',encoding='UTF-8') as e_Mfile:
    _=e_Mfile.read()
    emission_Matrix=json.loads(_)

with open("C:/Users/13375/Desktop/拼音输入法/拼音汉字表.txt",'r',encoding='UTF-8') as P_H_Tfile:
    _=P_H_Tfile.read()
    PinYinHanZiTable=json.loads(_)

def viterbi(pinyinlist,PinYinHanZiTable,Start_Probability,Hidden_Transition_Matrix_Two,Hidden_Transition_Matrix_Three,emission_Matrix):
    V=[{}]
    path={}

    for y in PinYinHanZiTable[pinyinlist[0]]:
        if pinyinlist[0] in emission_Matrix[y]:
            V[0][y]=abs(Start_Probability[pinyinlist[0]][y]*emission_Matrix[y][pinyinlist[0]])
            path[y]=[y]
    
    for t in range(1,len(pinyinlist)):
        V.append({})
        newpath={}
        for y in PinYinHanZiTable[pinyinlist[t]]:
            if pinyinlist[t] in emission_Matrix[y]:
                (prob,state)=max([(abs(V[t-1][y0]*Hidden_Transition_Matrix_Two[y0][y]*emission_Matrix[y][pinyinlist[t]]),y0) for y0 in PinYinHanZiTable[pinyinlist[t-1]] if y0 in V[t-1]])
            if t >= 2:
                if path[state][-2] in Hidden_Transition_Matrix_Three and\
                     state in Hidden_Transition_Matrix_Three[path[state][-2]] and\
                      y in Hidden_Transition_Matrix_Three[path[state][-2]][state]:
                    prob += abs(Hidden_Transition_Matrix_Three[path[state][-2]][state][y])
            V[t][y]=prob
            newpath[y]=path[state]+[y]

        path=newpath
    
    (prob,state)=max([(V[len(pinyinlist)-1][y],y)for y in PinYinHanZiTable[pinyinlist[len(pinyinlist)-1]] ])
    return (prob,path[state])

pinyinlist=['bei','jing','hai','dian','qu','qing','hua','da','xue']
(a,b)=viterbi(pinyinlist,PinYinHanZiTable,Start_Probability,Hidden_Transition_Matrix_Two,Hidden_Transition_Matrix_Three,emission_Matrix)
print(b)
#测试一下!