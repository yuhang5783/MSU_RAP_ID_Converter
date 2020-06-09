#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Description: 将水稻参考基因组RAP基因ID与MSU基因ID相互转换
@Description: 自动识别输入ID类型并输出对应类型
@Version: 0.01
@Author: Hang Yu
@Date: 2019-09-11 22:47:11
@LastEditTime: 2020-06-09 11:52:12
'''
# 将对应关系储存到字典
# 互相转换均存在“一对多”的情况
relation_rap2msu = {}
relation_msu2rap = {}
for line in open("RAP-MSU_2020-06-03.txt"):
    line = line.strip()
    rap = str(line.split("\t")[0])
    msu = str(line.split("\t")[1])
    msu_gene_list=[]
    if "," in msu:
        for transcript in msu.split(","):
            gene_id = transcript.split(".")[0]
            if gene_id not in msu_gene_list:
                msu_gene_list.append(gene_id)
    if ("," not in msu) and (msu != "None"):
        msu_gene_list.append(msu.split(".")[0])
    if msu == "None":
        msu_gene_list.append(msu)

    # rap2msu字典
    relation_rap2msu[rap] = msu_gene_list
    
    # msu2rap字典
    for msu_gene in msu_gene_list:
        if msu_gene not in relation_msu2rap.keys():
            relation_msu2rap[msu_gene] = []
            relation_msu2rap[msu_gene].append(rap)
        if msu_gene in relation_msu2rap.keys():
            if rap not in relation_msu2rap[msu_gene]:
                relation_msu2rap[msu_gene].append(rap)

# 根据ID类型创建输出文件
first_line = open("your-id-list-one-gene-per-line.txt").readline()
if first_line.startswith("Os"):
    res_msu = open("res.rap2msu.xls", "w")
if first_line.startswith("LOC_"):
    res_rap = open("res.msu2rap.xls", "w")

# 根据ID进行输出结果
for gene_id in open("your-id-list-one-gene-per-line.txt"):
    gene_id = gene_id.strip()
    
    # 检测到输入ID为RAP
    if gene_id.startswith("Os"):
        gene_id_rap = gene_id
        if gene_id_rap in relation_rap2msu.keys():
            gene_id_msu_list = relation_rap2msu[gene_id_rap]
            for gene_id_msu in gene_id_msu_list:
                res_msu.write(gene_id_rap + "\t" + gene_id_msu + "\n")
        else:
            res_msu.write(gene_id_rap + "\t" + "None" + "\n")
    
    # 检测到输入ID为MSU
    if gene_id.startswith("LOC_"):
        gene_id_msu = gene_id
        if gene_id_msu in relation_msu2rap.keys():
            gene_id_rap_list = relation_msu2rap[gene_id_msu]
            for gene_id_rap in gene_id_rap_list:
                res_rap.write(gene_id_msu + "\t" + gene_id_rap + "\n")
        else:
            res_rap.write(gene_id_msu + "\t" + "None" + "\n")

# 根据ID类型关闭文件
if first_line.startswith("Os"):
    res_msu.close()
if first_line.startswith("LOC_"):
    res_rap.close()
