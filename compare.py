"""
代码中有从网络上参考或者直接复制过来的内容，对原作者致以谢意！
但因时间有些久了，来源无法一一追溯，故没有列出来源。报以歉意！
"""
# simtext相似度：
# simtext可以计算两文档间四大文本相似性指标，分别为：
#     Sim_Cosine cosine相似性
#     Sim_Jaccard Jaccard相似性
#     Sim_MinEdit 最小编辑距离
#     Sim_Simple 微软Word中的track changes
# import sys
import re
import string
from zhon.hanzi import punctuation as chinese_punctuation  # 中文标点符号
# from docx.shared import RGBColor
# from docx import Document
# from docx.shared import Inches
# import os
from simtext import similarity

findir = 'documents/'  ### The path of the PDFs
foutdir = 'extracted_text/'  ###

english_punctuation = string.punctuation  # 英文标点符号
chi_punc = '|'.join([c for c in chinese_punctuation])
eng_punc = '|'.join([c for c in english_punctuation])
punc = chi_punc + eng_punc
# 注意 punc 中的'||'会导致逐字符分句的情况，所以手动抛去；如果真要把‘|’也当做分隔符，再做研究
punc = punc[:-6] + punc[-4:]


# punc = punc.decode("utf-8")

def not_break(sen):
    return (sen != '\n' and sen != '\u3000' and sen != '' and not sen.isspace())


def filter_data(ini_data):
    # ini_data是由句子组成的string
    new_data = list(filter(not_break, [data.strip() for data in ini_data]))
    return new_data


def split_sentence(para):
    my_stringList = filter_data(re.split(r'' + ("[" + punc + "]"), para))
    """
    flags = [u"，",u"。",u"；",u"：",u"！",u"？",u'“',u"’"]
    for flag in flags:
         para2 = para.replace(flag,"\n")
    print(para2)
    para3=para2.split('\n')
    """
    return my_stringList


def run_comparing(para1, para2, mymethod="Sim_Cosine", mythreshold=0.5):
    para1 = para1.replace('\n', '')
    para2 = para2.replace('\n', '')
    para12 = para1  ### used for colored text
    para22 = para2  ### used for colored text
    # myoutput = open('检测结果.txt', 'w')

    # fdoc = '检测结果.docx'

    # 创建文档对象
    # 打包时使用：
    # document = Document()
    # 测试时使用(因为会出问题，所以要这样)：
    # document = Document( docx=os.path.join(os.getcwd(),'default.docx') )
    # 添加一级标题
    # document.add_heading(u"使用的方法：%s, 阈值=%10.3f%%" % (mymethod, mythreshold * 100.0), level=1)

    """
    p=document.add_paragraph('')
    xxxx = "使用的方法：%s," % (mymethod)
    yyyy = "阈值=%10.3f%%"  %(mythreshold*100.0)
    run=p.add_run( xxxx+yyyy )
    run.font.color.rgb = RGBColor(250,0,0) 
    """

    # document.add_paragraph('比较的两段为：')
    # document.add_paragraph(para1, style='IntenseQuote')
    # document.add_paragraph(para2, style='IntenseQuote')

    """
    # 添加表格: 1行3列
    table = document.add_table(rows = 1,cols = 2)
    # 获取第一行的单元格列表对象
    hdr_cells = table.rows[0].cells
    # 为每一个单元格赋值
    # 注：值都要为字符串类型
    hdr_cells[0].text = "句子"
    hdr_cells[1].text = "相似度"
    """

    mysentences = split_sentence(para1)
    # print('要查询的文本中句子数目 =', len(mysentences))
    textDB = split_sentence(para2.replace('\n', ''))

    # print("使用的方法：", mymethod, ', 阈值=', mythreshold * 100.0, '%')
    # print("段落1：")
    # print(para1)
    # print("段落2：")
    # print(para2)

    text1color = ""
    text2color = ""
    it2 = 0
    for text2x in textDB:
        it2 += 1
        text2color = text2color + '<font color="red">[' + str(it2) + ']</font>' + text2x

    mean_p_1 = 0.0
    i1 = 0
    pmarker = 0.0
    for sentence in mysentences:
        pmarker = 0.0
        sim = similarity()
        it2 = 0
        imatch = 0
        imatch2 = 0;
        textimatch2 = ''
        i = 0
        for text in textDB:
            it2 += 1
            res = sim.compute(text, sentence)

            i += 1

            if pmarker < res[mymethod]:
                pmarker = res[mymethod]
                imatch = it2
                imatch2 = i
                textimatch2 = text

            if res[mymethod] >= mythreshold:
                mean_p_1 += res[mymethod] * 100.0
                if pmarker < res[mymethod]:
                    pmarker = res[mymethod]

                i1 += 1
                # print("#############################################################")
                # print('相似度    =%10.5f %%' % (res[mymethod] * 100.0))
                # print("句子1：", sentence)
                # print('句子2：  ', text)

                # 往文档中添加段落
                # p = document.add_paragraph('相似度    =')
                # run = p.add_run('%10.5f %%' % (res[mymethod] * 100.0))
                # run.font.color.rgb = RGBColor(250, 0, 0)
                # p.add_run('， 两个句子如下：').bold = True
                # p.add_run('and some ')
                # p.add_run('italic.').italic = True
                # document.add_paragraph(sentence, style='ListBullet')  # 'ListNumber')#style = 'IntenseQuote')
                # document.add_paragraph(text, style='ListBullet')  # 'ListNumber')#style = 'IntenseQuote')

                """
                # 为表格添加一行
                new_cells = table.add_row().cells
                new_cells[0].text = sentence
                new_cells[1].text = ''
                new_cells = table.add_row().cells
                new_cells[0].text = text
                new_cells[1].text = '%10.5f %%'%(res[mymethod]*100.0)
                """

        pc = "(%5.2f%%,%d)" % (pmarker * 100.0, imatch)

        # print(pmarker)
        if pmarker >= mythreshold:
            text1color = text1color + '<font color="red">' + sentence + pc + '</font> <font color="cyan">|</font> '
            xxxx = '<font color="red">' + sentence + '</font>'
            # print(sentence,xxxx)
            para12 = para12.replace(sentence, xxxx)
            yyyy = '<font color="red">' + textimatch2 + '</font>'
            para22 = para22.replace(textimatch2, yyyy)
            # print(para12,sentence,xxxx)
        else:
            text1color = text1color + '<font color="blue">' + sentence + pc + '</font> <font color="cyan">|</font> '
            xxxxx = '<font color="black">' + sentence + '</font>'
            para12 = para12.replace(sentence, xxxxx)
            # yyyyy = '<font color="black">'+ textimatch2+'</font>'
            # para22 = para22.replace(textimatch2,yyyyy)

    text1color = text1color + '\n\n  <font color="black">说明：括号内（第一项为相似度，第二项为与之相似的句子编号)。详情请查看 “检测结果.txt“ 或者 “检测结果.docx“。</font> <font color="red">可能不准确！仅供参考！</font>'

    try:
        mean_only = mean_p_1 / float(i1)
    except:
        mean_only = 0.0

    # print('**************************')
    # print('大于阈值的文本的平均相似度= %10.5f %%' % (mean_only))
    # print('整体平均相似度= %10.5f %%'%(mean_all) , file=myoutput)
    # print("注意整体相似度为所有句子的平均相似度（包含相似度小于阈值的内容）", file=myoutput)
    # print('**************************')

    """
    col_width = [6.5,0.5]
    for col in range(2):
        table.cell(0,col).width = Inches(col_width[col])
    """

    """
    p = document.add_paragraph('')
    run= p.add_run('整体平均相似度= %10.5f %%'%(mean_all) ) 
    run.font.color.rgb = RGBColor(250,0,0)    
    p.add_run("\n注意整体相似度为所有句子的平均相似度（包含相似度小于阈值的内容）").bold = True
    """

    return mean_only, text1color, text2color, para12, para22


def compareTwo(mytext, para, percent):
    # percent = 50
    if not percent:
        percent = 50
    if percent < 0 or percent > 100:
        return {
            'mean_only': 0,
            'text1color': '阈值必须在[0,100]之间',
            'text2color': '阈值必须在[0,100]之间',
            'para1mk': '阈值必须在[0,100]之间',
            'para2mk': '阈值必须在[0,100]之间'
        }
    else:
        threshold = float(percent) / 100.0
        mean_only, text1color, text2color, para1mk, para2mk = run_comparing(mytext, para, mythreshold=threshold)
        outPut = {
            'mean_only': mean_only,
            'text1color': text1color,
            'text2color': text2color,
            'para1mk': para1mk,
            'para2mk': para2mk
        }
        # print(outPut)
        return outPut
    # print(mean_only, "mean_only")
    # print(text1color, "text1color")
    # print(text2color, "text2color")
    # print(para1mk, "para1mk")
    # print(para2mk, "para2mk")

# 执行比较
# mytext = '北极地区冻结主权是不可行的，北极治理构变动，丹麦虽然并不是世界上最靠近北极圈的国家，但它也正试图将北极纳入自己的版图。俄罗斯联邦国家杜马副主席奇林加罗夫率领北极海洋科考团,我吃北极海洋考察'
# para = "北极地区冻结主权不可行的，北极治理的智缘结构变动，丹麦虽然并不是世界北极圈的国家，但它也正试北极纳的版图。俄罗斯联邦国主席奇林领北极海洋科考团"
# compare(mytext, para)
