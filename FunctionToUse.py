import math,json
from pypinyin import NORMAL, pinyin,lazy_pinyin
def GetTheHeadWord(str,Hidden_Matrix,Start_probability):
    index=0
    for s in str:
        if s =='，' or s=='。' or index == 0 or s==' ' or s=='：'or s =='！'or s== '？'or s=='；':
            if index<=len(str)-4 and str[index+1] in Hidden_Matrix:
                pinyinlist=pinyin(str[index+1:index+5],heteronym=True,style=NORMAL)
                Start_probability[pinyinlist[0][0]][str[index+1]]+=1
        index += 1

def CalCulateTheRiot(Start_probability):
    sum = 0
    for k in Start_probability:
        for j in Start_probability[k]:
            sum += Start_probability[k][j]
    for k in Start_probability:
        for j in Start_probability[k]:
            if Start_probability[k][j] >0:
                Start_probability[k][j]=math.log(Start_probability[k][j]/sum)

def GetTheHTHO(str,Hidden_Matrix,Hidden_Transition_Matrix_Two,Hidden_Transition_Matrix_Three):
    index = 0
    for s in str:
        if s in Hidden_Matrix and index+1 <= len(str)-1 and str[index+1] in Hidden_Matrix:
            if str[index+1] in Hidden_Transition_Matrix_Two[s]:
                Hidden_Transition_Matrix_Two[s][str[index+1]] += 1
            else :
                Hidden_Transition_Matrix_Two[s][str[index+1]] = 1
            Hidden_Transition_Matrix_Two[s]['single_counter'] += 1
            Hidden_Transition_Matrix_Two[s]['counter'] += 1
        elif (s in Hidden_Matrix and index+1 <= len(str)-1 and (str[index+1] == '。' or str[index+1] == '，' or str[index+1] == ' ' or str[index+1] == '；'or str[index+1] == '？'or str[index+1] == '！')) or\
             (s in Hidden_Matrix and index+1 == len(str)):
            Hidden_Transition_Matrix_Two[s]['counter'] += 1

        if s in Hidden_Matrix and index+2 <= len(str)-1 and str[index+1] in Hidden_Matrix:
            if str[index+1] in Hidden_Transition_Matrix_Three[s]:
                if str[index+2] in Hidden_Transition_Matrix_Three[s][str[index+1]]:
                    Hidden_Transition_Matrix_Three[s][str[index+1]][str[index+2]] += 1
                else:
                    Hidden_Transition_Matrix_Three[s][str[index+1]][str[index+2]] = 1
            else:
                Hidden_Transition_Matrix_Three[s][str[index+1]]={}
                Hidden_Transition_Matrix_Three[s][str[index+1]][str[index+2]] = 1

        index += 1

def GetTheEM(str,emission_Matirx,Hidden_Matrix):
    pinyinlist=lazy_pinyin(str,errors='ignore')
    index=0
    for i in str:
        if '\u4e00' <= i <= '\u9fff':
            if i in Hidden_Matrix:
                emission_Matirx[i][pinyinlist[index]] += 1
                index += 1
            else:
                index += 1

