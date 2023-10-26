# .txt-->.xml
# ! /usr/bin/python
# -*- coding:UTF-8 -*-
import os
import cv2
import shutil
from xml.dom.minidom import Document

cls_names = ['hat_person', 'no_hat']


def makexml(picPath, txtPath, xmlPath):  # 读取txt路径，xml保存路径，数据集图片所在路径
    if os.path.exists(xmlPath):
        shutil.rmtree(xmlPath)
    os.makedirs(xmlPath)
    files = os.listdir(picPath)
    for i, name in enumerate(files):
        ss=os.path.join(picPath, name)
        print(ss)
        img = cv2.imread(ss)
        Pheight, Pwidth, Pdepth = img.shape

        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        folder = xmlBuilder.createElement("folder")  # folder标签
        folderContent = xmlBuilder.createTextNode("VOC2007")
        folder.appendChild(folderContent)
        annotation.appendChild(folder)

        filename = xmlBuilder.createElement("filename")  # filename标签
        filenameContent = xmlBuilder.createTextNode(name)
        filename.appendChild(filenameContent)
        annotation.appendChild(filename)

        size = xmlBuilder.createElement("size")  # size标签
        width = xmlBuilder.createElement("width")  # size子标签width
        widthContent = xmlBuilder.createTextNode(str(Pwidth))
        width.appendChild(widthContent)
        size.appendChild(width)
        height = xmlBuilder.createElement("height")  # size子标签height
        heightContent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightContent)
        size.appendChild(height)
        depth = xmlBuilder.createElement("depth")  # size子标签depth
        depthContent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthContent)
        size.appendChild(depth)
        annotation.appendChild(size)

        txt = os.path.join(txtPath, name[0:-3] + "txt")
        if not os.path.exists(txt):
            print(txt)
            f = open(os.path.join(xmlPath, name[0:-4] + '.xml'), 'w', encoding="utf-8")
            xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
            f.close()
            continue

        txtFile = open(txt)
        txtList = txtFile.readlines()

        for i in txtList:
            oneline = i.strip().split(" ")
            object = xmlBuilder.createElement("object")
            picname = xmlBuilder.createElement("name")
            nameContent = xmlBuilder.createTextNode(cls_names[int(oneline[0])])
            picname.appendChild(nameContent)
            object.appendChild(picname)
            pose = xmlBuilder.createElement("pose")
            poseContent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(poseContent)
            object.appendChild(pose)
            truncated = xmlBuilder.createElement("truncated")
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)
            difficult = xmlBuilder.createElement("difficult")
            difficultContent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultContent)
            object.appendChild(difficult)
            bndbox = xmlBuilder.createElement("bndbox")
            xmin = xmlBuilder.createElement("xmin")
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)
            ymin = xmlBuilder.createElement("ymin")
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)
            xmax = xmlBuilder.createElement("xmax")
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)
            ymax = xmlBuilder.createElement("ymax")
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)
            object.appendChild(bndbox)
            annotation.appendChild(object)

        f = open(os.path.join(xmlPath, name[0:-4] + '.xml'), 'w', encoding="utf-8")
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()

makexml("E:\helmet\hat/", "E:\helmet\hat_labels/", "E:\helmet\hat_xml/")