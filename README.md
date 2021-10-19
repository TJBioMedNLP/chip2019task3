# 第五届中国健康信息处理会议-评测任务：临床试验筛选标准短文本分类

**【更新】**: 目前，此数据集已通过中国中文信息学会（CIPS）医疗健康与生物信息处理专业委员会（CHIP），基于合法开放共享理念，用于阿里达摩院开发的[中文医疗信息处理挑战榜CBLUE](https://tianchi.aliyun.com/dataset/dataDetail?spm=5176.22060218.J_2657303350.1.70e82d3dMiiMg3&dataId=95414)。后续如有研究者想基于此数据进行研究，可前往该平台下载数据以及打榜。

- [会议链接](http://cips-chip.org.cn/)
- [评测链接](http://www.cips-chip.org.cn:8088/evaluation)
- [CBLUE链接](https://tianchi.aliyun.com/specials/promotion/2021chinesemedicalnlpleaderboardchallenge)

## 1.任务描述

> 临床试验是指通过人体志愿者也称为受试者进行的科学研究，筛选标准是临床试验负责人拟定的鉴定受试者是否满足某项临床试验的主要指标，分为入组标准和排出标准，一般为无规则的自由文本形式。临床试验的受试者招募一般是通过人工比较病历记录表和临床试验筛选标准完成，这种方式费时费力且效率低下。因此，临床试验面临诸多困境，比如受试者招募难度大，招募时间久，患者流失等等。通过自然语言处理和机器学习的方法对临床试验筛选标准自动解析，并以此构建自动化筛选病人的系统是一个很有前景的研究热点，具有很大的实际应用前景和医学临床价值。
>

本次评测任务的主要目标是针对临床试验筛选标准进行分类，所有文本数据均来自于真实临床试验，经过了初步处理和人工标注。

## 2.任务说明

在本次评测中，我们给定事先定义好的44种筛选标准语义类别和一系列中文临床试验筛选标准的描述句子，参赛者需返回每一条筛选标准的具体类别。

示例如下：

| ID   | 输入(筛选标准)         | 输出(类别)              |
| ---- | ---------------------- | ----------------------- |
| S1   | 年龄>80岁              | Age                     |
| S2   | 近期颅内或椎管内手术史 | Therapy or Surgery      |
| S3   | 血糖<2.7mmol/L         | Laboratory Examinations |

44种预定义的语义类别：

|#|topic groups|semantic categories|
|---|---|----|
|1|`Health Status`|`Disease` `Symptom` `Sign` `Pregnancy-related Activity` `Neoplasm Status` `Non-Neoplasm Disease Stage` `Allergy Intolerance` `Organ or Tissue Status` `Life Expectancy` `Oral related`|
|2|`Treatment or Health Care`|`Pharmaceutical Substance or Drug` `Therapy or Surgery` `Device` `Nursing`|
|3|`Diagnostic or Lab Test`|`Diagnostic` `Laboratory Examinations` `Risk Assessment` `Receptor Status`|
|4|`Demographic Characteristics`|`Age` `Special Patient Characteristic` `Literacy` `Gender` `Education` `Address` `Ethnicity`|
|5|`Ethical Consideration`|`Consent` `Enrollment in other studies` `Researcher Decision` `Capacity` `Ethical Audit` `Compliance with Protocol`|
|6|`Lifestyle Choice`|`Addictive Behavior` `Bedtime` `Exercise` `Diet` `Alcohol Consumer` `Sexual related` `Smoking Status` `Blood Donation`|
|7|`Data or Patient Source`|`Encounter` `Disabilities` `Healthy` `Data Accessible`|
|8|`Other`|`Multiple`|

## 3.评测数据

#### 训练数据

​		训练数据见文件train_data.txt，一共22962条。

#### 验证数据

​		验证数据见文件validation_data.txt，一共7682条。

#### 测试数据

​		测试数据见文件test_data.txt，一共7697条。

#### 评估方法

​		评估脚本见文件chip2019task3_evaluation.py，输入样例见同级目录。

​		使用命令 ：

```
python chip2019task3_evaluation.py ./example_gold.txt ./example_pred.txt
```


#### 句子类别

​		类别定义及标注样例见文件category.xlsx，共44种类别。

## 4.评测结果

共有27支队伍提交结果。

- 总体情况：


| 评价指标   | 最大值   | 最小值   | 平均数   | 中位数   |
| ---------- | -------- | -------- | -------- | -------- |
| Average F1 | 0.810263 | 0.553736 | 0.770502 | 0.788728 |

- 前九名参赛队伍的结果：


| **排名** | **参赛单位**                   | **方法描述**                                                 | **外部数据集**    | **宏平均F1值** |
| -------- | ------------------------------ | ------------------------------------------------------------ | ----------------- | -------------- |
| 1        | 华南理工大学                   | 多种预训练语言模型；额外特征（主题特征提取、句子长度、句子中数字个数、比较符个数、英文字母个数）；集成学习模型。 | 无                | 0.810 263      |
| 2        | 大连理工大学                   | 多种预训练语言模型；神经网络模型（包括卷积神经网络、深层金字塔卷积神经网络、长短期记忆网络、自注意力机制）。 | www.chictr.org.cn | 0.809 936      |
| 3        | 大连理工大学                   | 多种预训练语言模型；神经网络模型（包括卷积神经网络、注意力机制）；额外特征（句法特征、词性特征、关键词特征）。 | 无                | 0.807 456      |
| 4        | 中山大学                       | 多种预训练语言模型。                                         | 无                | 0.800 168      |
| 5        | 中国医学科学院  医学信息研究所 | 单一预训练语言模型。                                         | 无                | 0.800 123      |
| 6        | 北京中科凡语  科技有限公司     | 深度学习模型（词向量加最大池化层、词向量模型、预训练语言模型、文本图卷积神经网络）；统计学模型（支持向量机、随机森林）。 | 无                | 0.797 970      |
| 7        | 中南大学                       | 神经网络模型（文本卷积神经网络、卷积神经网络、注意力加双向长短期记忆网络、卷积神经网络加双向长短期记忆网络、中文分词模型、集成学习模型）；字向量训练（跳字模型、中文词向量、语义向量空间模型）；词向量特征；预训练语言模型向量特征。 | 无                | 0.796 295      |
| 8        | 郑州大学                       | 神经网络模型（卷积神经网络、长短期记忆网络）；统计学模型（支持向量机）；字向量训练（基于预训练语言模型）+词向量训练（语义向量空间模型）；词频-逆文档频率特征。 | 无                | 0.795 773      |
| 9        | 新疆大学                       | 单一预训练语言模型。                                         | 无                | 0.794 909      |

- 会议报告：


| 排名 | 参赛单位     | 队伍名称 | 报告题目                                       | 报告人 |
| ---- | ------------ | -------- | ---------------------------------------------- | ------ |
| 1    | 华南理工大学 | wzm      | 基于BERT与模型融合的短文本分类方法             | 吴梓明 |
| 2    | 大连理工大学 | DUTIR914 | 一种基于预训练模型的医学短文本分类方法         | 李孟颖 |
| 3    | 大连理工大学 | DUTIRTM  | 基于BERT融合多特征的临床试验筛选标准短文本分类 | 丁泽源 |

- 会议海报展示：


| **排名** | **参赛单位**                    | **队伍名称** | **作者**                             | **海报题目**                                   |
| -------- | ------------------------------- | ------------ | ------------------------------------ | ---------------------------------------------- |
| 4        | 中山大学                        | 好果汁队     | 潘智伟，舒丁飞                       | 基于多模型集成学习的临床试验筛选标准短文本分类 |
| 5        | 中国医学科学院   医学信息研究所 | 努力！奋斗！ | 杨飞洪，李姣                         | 基于BERT模型的临床试验筛选短文本分类           |
| 6        | 北京中科凡语科技有限公司        | mini batch   | 王克欣，张萌、王祥宇、付西娜、于志鹏 | 多模型融合的文本分类算法在临床试验筛选中的应用 |
| 7        | 中南大学                        | Morning Tea  | 伍逸凡，余颖 ，李敏                  | 基于不同词向量特征的临床试验筛选标准短文本分类 |
| 8        | 郑州大学                        | zzunlp       | 蔡林坤，刘涛                         | 临床试验筛选标准短文本分类                     |
| 9        | 新疆大学                        | A&D          | 阿依古丽·哈力克，吴迪、李磊          | 基于ERNIE的文本分类                            |

## 5.如何引用

1. Zong, H., Yang, J., Zhang, Z. *et al.* Semantic categorization of Chinese eligibility criteria in clinical trials using machine learning methods. *BMC Med Inform Decis Mak* **21,** 128 (2021). https://doi.org/10.1186/s12911-021-01487-w

2. 宗辉, 张泽宇, 杨金璇, 雷健波, 李作峰, 郝天永, 张晓艳. 基于人工智能的中文临床试验筛选标准文本分类研究. 生物医学工程学杂志, 2021, 38(1): 105-110, 121. doi: [10.7507/1001-5515.202006035](https://kns.cnki.net/kcms/detail/detail.aspx?filename=SWGC202101013&dbcode=CJFD&dbname=CJFD2021&v=s4iZ7yua6hKhoK1gTaBP9OiMEktP5TckXC57PN6ri8awaTa7GvfSp3xie2wgJRmG)

## 6.发表文章

基于此评测数据发表的文章 ：

1. Zong H, Yang J, Zhang Z, Li Z, Zhang X. Semantic categorization of Chinese eligibility criteria in clinical trials using machine learning methods. BMC Med Inform Decis Mak. 2021 Apr 15;21(1):128. doi: 10.1186/s12911-021-01487-w. PMID: 33858409; PMCID: PMC8050926.
2. Zeng K, Xu Y, Lin G, Liang L, Hao T. Automated classification of clinical trial eligibility criteria text based on ensemble learning and metric learning. BMC Med Inform Decis Mak. 2021 Jul 30;21(Suppl 2):129. doi: 10.1186/s12911-021-01492-z. PMID: 34330259; PMCID: PMC8323220.
3. Zeng K, Pan Z, Xu Y, Qu Y. An Ensemble Learning Strategy for Eligibility Criteria Text Classification for Clinical Trial Recruitment: Algorithm Development and Validation. JMIR Med Inform. 2020 Jul 1;8(7):e17832. doi: 10.2196/17832. PMID: 32609092; PMCID: PMC7367522.
4. 宗辉,张泽宇,杨金璇,雷健波,李作峰,郝天永,张晓艳.基于人工智能的中文临床试验筛选标准文本分类研究[J].生物医学工程学杂志,2021,38(01):105-110+121.
5. 杨飞洪,王序文,李姣.基于BERT-TextCNN模型的临床试验筛选短文本分类方法[J].中华医学图书情报杂志,2021,30(01):54-59.
6. 张博,孙逸,李孟颖,郑馥琦,张益嘉,王健,林鸿飞,杨志豪.基于迁移学习和集成学习的医学短文本分类[J].山西大学学报(自然科学版),2020,43(04):947-954.

## 7.评测组织者

- 宗辉，同济大学
- 张晓艳，同济大学
- 李作峰，飞利浦中国研究院
- 郝天永，华南师范大学