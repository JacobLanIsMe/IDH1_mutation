from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError
import cv2, numpy
import glob, pandas
IDH1 = []
pathes = glob.glob('./*.pdf')
images = convert_from_path("./039_G05_IDH1-W1101_IDH1-exon4F.pdf")
for page in images:
    page.save("2.jpg","JPEG")
img = cv2.imread("./2.jpg")
logo = img[733:1000,14:2325]
bgr = []
for j in range(logo.shape[1]):
    if logo[0,j][0]<150 or logo[0,j][1]<150 or logo[0,j][2]<150:
        bgr.append(j)
px1 = []
px2 = []
for i in range(len(bgr)-1):
    if bgr[i]!=bgr[i+1]-1:
        px1.append(bgr[i])
        px2.append(bgr[i+1])
px = []
px.append(round((px1[0]+bgr[0])/2))
for i in range(len(px1)-1):
    px.append(round((px2[i]+px1[i+1])/2))
px.append(round((px2[-1]+bgr[-1])/2))
color_bgr = []
sequence = []
for i in px:
    color_bgr.append(logo[0,i])
    if logo[0,i][0]>=100 and logo[0,i][1]<90 and logo[0,i][2]<100:
        sequence.append("C")
    if  logo[0,i][1]>=90 and (logo[0,i][0]<100 or logo[0,i][2]<100):
        sequence.append("A")
    if logo[0,i][0]<100 and logo[0,i][1]<90 and logo[0,i][2]>=100:
        sequence.append("T")
    if logo[0,i][0]<100 and logo[0,i][1]<90 and logo[0,i][2]<100:
        sequence.append("G")

for i in range(len(sequence)):
    if (sequence[i]=="A" and sequence[i+1]=="T" and sequence[i+2]=="C" and sequence[i+3]=="A" and sequence[i+4]=="T" and 
        sequence[i+5]=="A" and sequence[i+6]=="G" and sequence[i+7]=="G" and sequence[i+8]=="T" and sequence[i+9]=="C"):
        mutation_px = px[i+10]
        for j in range(50,logo.shape[0]-10):
            print(logo[j,px[i+10]])
        break



"""
for i in range(50,logo.shape[0]-10):
    if logo[i,mutation_px][0]<100 and logo[i,mutation_px][1]<100 and logo[i,mutation_px][2]<100:
        if "G" not in mutation:
            mutation.append("G")
    if logo[i,mutation_px][1]>100 and (logo[i,mutation_px][2]<100 or logo[i,mutation_px][0]<100):
        if "A" not in mutation:
            mutation.append("A")
    if logo[i,mutation_px][0]<100 and logo[i,mutation_px][1]<100 and logo[i,mutation_px][2]>100:
        if "T" not in mutation:
            mutation.append("T")
    if logo[i,mutation_px][0]>100 and logo[i,mutation_px][1]<100 and logo[i,mutation_px][2]<100:
        if "C" not in mutation:
            mutation.append("C")
print(path ,mutation)
IDH1.append([path ,mutation])
"""

"""
cv2.namedWindow("My Image",cv2.WINDOW_NORMAL)
cv2.imshow("My Image", logo)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
f = pandas.read_csv("012_D02_IDH1-W960_IDH1-exon4F.txt", sep="\s+")
f.to_csv("1.csv")
G= [int(i) for i in f.iloc[:,0].to_list()]
A= [int(i) for i in f.iloc[:,1].to_list()]
T= [int(i) for i in f.iloc[:,2].to_list()]
C= [int(i) for i in f.iloc[:,3].to_list()]

print(G)
for i in range(len(G)):
    if T[i]>G[i] and T[i]>A[i] and T[i]>C[i]:
        if T[i+1]>G[i+1] and T[i+1]>A[i+1] and T[i+1]>C[i+1]:
            if C[i+2]>G[i+2] and C[i+2]>A[i+2] and C[i+2]>T[i+2]:
                print(i)

if C[i+2]>G[i+2] and C[i+2]>A[i+2] and C[i+2]>T[i+2]:
"""
"""
import glob, time
pathes = glob.glob('./sequence/*.seq')

with open(time.strftime("%Y%m%d", time.localtime(time.time())) + ".txt", 'w') as f:
    for i in pathes:
        with open(i, 'r') as j:
            seq = j.read()
        f.write(i.split('/')[2]+'\n')
        f.write(seq)

print('Finished')
input()    

print(pathes)
for i in pathes:
    print(i)
"""




