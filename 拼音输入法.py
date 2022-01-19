import json,os
from FunctionToUse import *
from os import listdir, makedirs, truncate

HanZiTable_Path="C:/Users/13375/Desktop/拼音输入法作业/拼音汉字表/一二级汉字表.txt"
with open(HanZiTable_Path,'r') as HanZiTable:
    TotalHanzi=HanZiTable.read()
    Hidden_Matrix=tuple(TotalHanzi)

PinYinHanZiTable_Path="C:/Users/13375/Desktop/拼音输入法作业/拼音汉字表/拼音汉字表.txt"
with open(PinYinHanZiTable_Path,'r') as PinYinHanZiTable:
    TotalLines=PinYinHanZiTable.readlines()
    Observation_Matrix=tuple(str.split(' ',1)[0] for str in TotalLines)

NewsDatabase_Path="C:/Users/13375/Desktop/拼音输入法作业/sina_news/"
new_DicList=[]
"""
PinYinHanZiTable_Path="C:/Users/13375/Desktop/拼音输入法作业/拼音汉字表/拼音汉字表.txt"
with open(PinYinHanZiTable_Path,'r') as PinYinHanZiTable:
    TotalLines=PinYinHanZiTable.readlines()
    Observation_Matrix=tuple(str.split(' ',1)[0] for str in TotalLines)

    Start_probability={}
    for i in Observation_Matrix:
        Start_probability[i]={}
    for str in TotalLines:
        HanZiList=list(str.split(' '))
        HanZiList[len(HanZiList)-1]=HanZiList[len(HanZiList)-1][0]
        Start_probability[HanZiList[0]]={j:0 for j in HanZiList[1:]}

PathList=listdir(NewsDatabase_Path)
for subfile in PathList:
    sub_path=NewsDatabase_Path+subfile
    with open(sub_path,'r',encoding='UTF-8') as NewsDatabase:
        TotalDic=NewsDatabase.read()
        DicList=TotalDic.split('}')
        for i in DicList:
            ii=i+'}'
            new_DicList.append(ii)
        new_DicList.pop()
    for i in new_DicList:
        try:
            ii = json.loads(i)
            GetTheHeadWord(ii['html'],Hidden_Matrix,Start_probability)
            GetTheHeadWord(ii['title'],Hidden_Matrix,Start_probability)
        except:
            continue

CalCulateTheRiot(Start_probability)

Start_probability_output =json.dumps(Start_probability)
with open("C:/Users/13375/Desktop/拼音输入法/Start_Probability.txt",'w') as Start_Probability_file:
   Start_Probability_file.write(Start_probability_output)
"""
#Hidden_Transition_Matrix_Two={}
#for i in Hidden_Matrix:
#    Hidden_Transition_Matrix_Two[i]={}
#    Hidden_Transition_Matrix_Two[i]['counter']=0
#    Hidden_Transition_Matrix_Two[i]['single_counter']=0

#Hidden_Transition_Matrix_Three={}
#for i in Hidden_Matrix:
#    Hidden_Transition_Matrix_Three[i]={}
"""
with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Two.txt",'r',encoding='UTF-8') as Dic2:
    UsedDicTwoList=Dic2.read()
    Hidden_Transition_Matrix_Two=json.loads(UsedDicTwoList)

with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Three.txt",'r',encoding='UTF-8') as Dic3:
    UsedDicThreeList=Dic3.read()
    Hidden_Transition_Matrix_Three=json.loads(UsedDicThreeList)

sub_path=NewsDatabase_Path+'2016-11.txt'
with open(sub_path,'r',encoding='UTF-8') as NewsDatabase:
    TotalDic=NewsDatabase.read()
    DicList=TotalDic.split('}')
    for i in DicList:
        ii=i+'}'
        new_DicList.append(ii)
    new_DicList.pop()
    for i in new_DicList:
        try:
            ii = json.loads(i)
            GetTheHTHO(ii['html'],Hidden_Matrix,Hidden_Transition_Matrix_Two,Hidden_Transition_Matrix_Three)
            GetTheHTHO(ii['title'],Hidden_Matrix,Hidden_Transition_Matrix_Two,Hidden_Transition_Matrix_Three)
        except:
            continue

output1 =json.dumps(Hidden_Transition_Matrix_Two)
output2 =json.dumps(Hidden_Transition_Matrix_Three)
with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Two.txt",'w') as testfile:
    testfile.truncate()
    testfile.write(output1)
with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Three.txt",'w') as testfile1:
    testfile1.truncate()
    testfile1.write(output2)
"""
"""
from pypinyin import NORMAL, pinyin

emission_Matrix={}
for i in Hidden_Matrix:
    emission_Matrix[i]={}
    pinyinlist=pinyin(i,heteronym=True,style=NORMAL)
    for j in pinyinlist[0]:
        emission_Matrix[i][j]=0


with open("C:/Users/13375/Desktop/拼音输入法/emission_Matrix.txt",'r',encoding='UTF-8') as Dic:
    UsedDicList=Dic.read()
    emission_Matrix=json.loads(UsedDicList)

#PathList=listdir(NewsDatabase_Path)
#for subfile in PathList:
sub_path=NewsDatabase_Path+"2016-11.txt"
with open(sub_path,'r',encoding='UTF-8') as NewsDatabase:
    TotalDic=NewsDatabase.read()
    DicList=TotalDic.split('}')
    for i in DicList:
        ii=i+'}'
        new_DicList.append(ii)
    new_DicList.pop()
    for i in new_DicList:
        try:
            ii = json.loads(i)
            GetTheEM(ii['html'],emission_Matrix,Hidden_Matrix)
            GetTheEM(ii['title'],emission_Matrix,Hidden_Matrix)
        except:
            continue

sum = 0
for i in emission_Matrix:
    for j in emission_Matrix[i]:
        sum += emission_Matrix[i][j]
for i in emission_Matrix:
    for j in emission_Matrix[i]:
        if emission_Matrix[i][j]/sum > 0:
            emission_Matrix[i][j]=math.log(emission_Matrix[i][j]/sum)


EM_output=json.dumps(emission_Matrix)
with open("C:/Users/13375/Desktop/拼音输入法/emission_Matrix.txt",'w') as EM_file:
    EM_file.truncate()
    EM_file.write(EM_output)
"""
"""
with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Two.txt",'r',encoding='UTF-8') as Dic2:
    UsedDicTwoList=Dic2.read()
    Hidden_Transition_Matrix_Two=json.loads(UsedDicTwoList)

    for i in Hidden_Transition_Matrix_Two:
        sum = Hidden_Transition_Matrix_Two[i]['single_counter']
        for j in Hidden_Transition_Matrix_Two[i]:
            if sum >0:
                Hidden_Transition_Matrix_Two[i][j]=Hidden_Transition_Matrix_Two[i][j]/sum

    for i in Hidden_Transition_Matrix_Two:
        for j in Hidden_Matrix:
            if j not in Hidden_Transition_Matrix_Two[i]:
                Hidden_Transition_Matrix_Two[i][j]=0

output1 = json.dumps(Hidden_Transition_Matrix_Two)
with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Two.txt",'w') as testfile:
    testfile.truncate()
    testfile.write(output1)
"""
"""
with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Three.txt",'r',encoding='UTF-8') as Dic3:
    UsedDicThreeList=Dic3.read()
    Hidden_Transition_Matrix_Three=json.loads(UsedDicThreeList)

    for i in Hidden_Transition_Matrix_Three:
        for j in Hidden_Transition_Matrix_Three[i]:
            sum = 0
            for k in Hidden_Transition_Matrix_Three[i][j]:
                sum += Hidden_Transition_Matrix_Three[i][j][k]
            for k in Hidden_Transition_Matrix_Three[i][j]:
                if sum > 0:
                    Hidden_Transition_Matrix_Three[i][j][k]=Hidden_Transition_Matrix_Three[i][j][k]/sum

output2 =json.dumps(Hidden_Transition_Matrix_Three)
with open("C:/Users/13375/Desktop/拼音输入法/Hidden_Transition_Matrix_Three.txt",'w') as testfile1:
    testfile1.truncate()
    testfile1.write(output2)
"""
"""
with open("C:/Users/13375/Desktop/拼音输入法/Start_Probability.txt",'r',encoding='UTF-8') as Dic3:
    UsedDicThreeList=Dic3.read()
    Start_Probability=json.loads(UsedDicThreeList)

    for i in Start_Probability:
        sum = 0
        for j in Start_Probability[i]:
            sum += math.exp(Start_Probability[i][j])
        for j in Start_Probability[i]:
            if sum > 0:
                Start_Probability[i][j] = math.exp(Start_Probability[i][j])/sum

output2 =json.dumps(Start_Probability)
with open("C:/Users/13375/Desktop/拼音输入法/Start_Probability.txt",'w') as testfile1:
    testfile1.truncate()
    testfile1.write(output2)
"""