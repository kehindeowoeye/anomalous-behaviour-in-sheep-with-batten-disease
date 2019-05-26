
# abnormality sampled from one bin
#######################################################################################################
import numpy as np
import matplotlib.pyplot as plt


# width of the bars
barWidth = 0.1

"""

 
# Choose the height of the blue bars
bars1 = [92.0959596,	84.46969697,	88.93939394,	 89.8989899]
bars2 = [16.79292929,	95.15151515,	50.90909091,	89.09090909]
bars3=  [9.090909091,	13.25757576,	40.90909091,	14.01515152]
bars4 = [8.484848485,	11.74242424,	36.36363636,	12.87878788]
 
  


# Choose the height of the error bars (bars1)
c1 = [(86.4386526,97.75326659),(76.41611924,92.5232747),(81.5691547,96.30963318),(83.11395389,96.68402591)]
c2 = [(13.68728696,	19.89857163),(93.02835658,97.27467372),(43.26212702,58.5560548),(85.36326901,92.81854918)]
c3 = [(5.730545306,12.45127288),(8.656016804,17.85913471),(28.72981057,53.08837125),(9.178517484,18.85178555)]
c4 = [(5.250949701,11.71874727),(7.268927062,16.21592142),(24.44743846,48.27983427),(8.028520539,17.72905522)]




yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]


# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center') 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')
#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')
#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy(%)',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
#plt.legend(loc=2, prop={'size': 7})
plt.savefig('1.eps')
plt.show()





#false positives temporal evaluation
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [8.131313131,16.66666667,12.42424242,10.50505051]
bars2 = [86.66666667,27.65151515,0,18.68686869]
bars3= [0,6.060606061,13.88888889,3.03030303]
bars4 = [1.262626263,2.272727273,9.343434343,0]
 
# Choose the height of the error bars (bars1)

c1 = [(2.236055706,14.02657056),(8.546076633,24.7872567),(4.748625325,20.09985952),(3.392909442,17.61719157)]
c2 = [(84.33119224,89.00214109),(20.25073419,35.05229611),(0,0),(12.40025349,24.97348388)]
c3 = [(0,0),(0.557261921,11.5639502),(7.477469011,20.30030877),(-1.216014105,7.276620165)]
c4 = [(-0.542795577,3.068048102),(-1.089522415,5.63497696),(4.409580369,14.27728832),(0,0)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('2.eps')
plt.show()














# number of agents evaluation, accuracy
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [85.37878788,92.69444444,88.02083333,89.296875,87.1875]
bars2 = [67.46212121,66.58333333,64.08854167,58.38541667,57.08333333]
bars3= [22.84090909,25.91666667,16.015625,17.578125,12.1875]
bars4 = [17.95454545,25.08333333,14.921875,16.640625,8.4375]
 
# Choose the height of the error bars (bars1)

c1 = [(75.24166301,95.51591274),(86.40854204,98.98034685),(80.76397229,95.27769438),(82.5586198,96.0351302),(75.81446636,98.56053364)]
c2 = [(55.27722497,79.64701745),(56.40419637,76.76247029),(54.72571085,73.45137248),(49.84822861,66.92260473),(45.90495334,68.26171333)]
c3 = [(13.43352477,32.24829341),(18.34590547,33.48742787),(8.072167457,23.95908254),(9.14535455,26.01089545),(1.246676208,23.12832379)]
c4 = [(9.100890862,26.80820005),(17.50883806,32.6578286),(6.946337277,22.89741272),(8.63854873,24.64270127),(-0.861469257,17.73646926)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]


 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('3.eps')
plt.show()







# number of agents evaluation, false positives
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [18.59848485,8.555555556,12.23958333,10.234375,11.875]
bars2 = [50.87121212,40.91666667,26.25,26.09375,22.96875]
bars3 = [6.818181818,5.833333333,9.635416667,3.125,1.5625]
bars4 = [5.303030303,2.5,4.166666667,3.125,0]
 
# Choose the height of the error bars (bars1)

c1 = [(7.737878377,29.45909132),(2.025782874,15.08532824),(4.915797797,19.56336887),(3.395588352,17.07316165),(0.311721847,23.43827815)]
c2 = [(39.72487181,62.01755243),(32.2771861,49.55614723),(16.61147325,35.88852675),(16.19048873,35.99701127),(9.850070551,36.08742945)]
c3 = [(-0.206285577,13.84264921),(0.467224968,11.1994417),(3.262841629,16.0079917),(0.077842686,6.172157314),(-1.62423976,4.74923976)]
c4 = [(-0.351403275,10.95746388),(-0.338813676,5.338813676),(0.532719524,7.80061381),(0.077842686,6.172157314),(0,0)]

yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]



# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('4.eps')
plt.show()















# abnormality sampled from two different bins
#######################################################################################################
import numpy as np
import matplotlib.pyplot as plt



#(1)
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [68.03030303,66.18686869,72.95454545,75.22727273]
bars2 = [67.42424242,63.91414141,70.42929293,72.1969697]
bars3= [26.89393939,29.16666667,27.77777778,48.48484848]
bars4 = [18.93939394,23.48484848,24.24242424,42.42424242]
 
# Choose the height of the error bars (bars1)
c1 = [(60.17584178,75.88476428),(58.66089619,73.71284118),(65.10505524,80.80403567),(67.81188149,82.64266397)]
c2 = [(59.91977661,74.92870824),(56.53974888,71.28853395),(62.88120366,77.9773822),(65.11095283,79.28298657)]
c3 = [(21.05751566,32.73036313),(23.71394939,34.61938395),(20.65099475,34.90456081),(36.10481301,60.86488396)]
c4 = [(13.4360498,24.44273808),(18.10773721,28.86195976),(17.12113392,31.36371457),(30.18151288,54.66697196)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]
 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm \sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm \sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=2, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('5.eps')
plt.show()







#false positives temporal evaluation
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [9.090909091,8.712121212,8.712121212,8.207070707]
bars2 = [9.797979798,10.80808081,8.409090909,7.651515152]
bars3 = [2.272727273,1.136363636,7.954545455,35.98484848]
bars4 = [2.02020202,1.136363636,6.313131313,28.40909091]


# Choose the height of the error bars (bars1)
c1 = [(2.218771682,15.9630465),(2.289648796,15.13459363),(2.199800603,15.22444182),(2.492533421,13.92160799)]
c2 = [(2.928348224,16.66761137),(3.881643183,17.73451843),(2.133611641,14.68457018),(2.036057164,13.26697314)]
c3 = [(-1.089522415,5.63497696),(-0.544761208,2.81748848),(2.547227741,13.36186317),(26.17555648,45.79414049)]
c4 = [(-1.154691177,5.195095218),(-0.544761208,2.81748848),(1.781083559,10.84517907),(18.97683427,37.84134755)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]
 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm \sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm \sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=2, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('6.eps')
plt.show()














# number of agents evaluation, accuracy
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [79.70238095,72.17592593,72.63888889,67.79761905,57.95454545]
bars2 = [71.2202381,71.48148148,70.55555556,68.69047619,58.93939394]
bars3= [41.2202381,43.75,32.63888889,30.80357143,17.61363636]
bars4 = [36.75595238,37.73148148,24.18981481,24.85119048,14.77272727]
 
# Choose the height of the error bars (bars1)
c1 = [(71.65971875,87.74504316),(62.39386003,81.95799182),(65.55568109,79.72209668),(59.46345105,76.13178705),(47.89784835,68.01124256)]
c2 = [(62.40313648,80.03733971),(61.62174124,81.34122172),(63.62146191,77.4896492),(61.12081904,76.26013334),(50.04588475,67.83290312)]
c3 = [(31.03847284,51.40200335),(30.11270406,57.38729594),(25.11006095,40.16771683),(22.11412732,39.49301554),(10.52689901,24.70037372)]
c4 = [(25.94143781,47.57046696),(24.58416823,50.87879473),(16.93565974,31.44396989),(16.52825617,33.17412478),(8.128515056,21.41693949)]

yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]
 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]


# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm \sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm \sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('7.eps')
plt.show()








# number of agents evaluation, false positives
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [11.10119048,9.305555556,7.152777778,4.821428571,12.5]
bars2 = [11.45833333,11.52777778,7.268518519,6.369047619,10.98484848]
bars3= [1.785714286,13.19444444,10.18518519,15.92261905,21.02272727]
bars4 = [0.892857143,13.88888889,8.796296296,12.35119048,14.20454545]
 
# Choose the height of the error bars (bars1)
c1 = [(3.477862013,18.72451894),(0.753966488,17.85714462),(1.503043087,12.80251247),(-0.485472439,10.12832958),(2.733291285,22.26670872)]
c2 = [(3.167322836,19.74934383),(2.019310594,21.03624496),(1.59365257,12.94338447),(0.78969381,11.94840143),(2.684333356,19.28536361)]
c3 = [(-0.721664416,4.293092988),(5.768832871,20.62005602),(3.861323098,16.50904727),(7.580278961,24.26495913),(9.095511446,32.9499431)]
c4 = [(-0.896468557,2.682182842),(6.567244859,21.21053292),(2.666141694,14.9264509),(4.774329291,19.92805166),(4.180185245,24.22890566)]


yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]
 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm \sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm \sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('8.eps')
plt.show()

































############################################################################################################################
#Real results

#day1

barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [23,16,1,7];
bars2 = [23,20,4,0];
bars3 = [13,20,1,1];
bars4 = [9,13,0,1];
bars5 = [24,22,0,1];
bars6 = [17,19,1,0];
bars7 = [24,23,7,28];
bars8 = [28,30,11,9];
bars9 = [53,49,30,12];
bars10 = [50,56,29,7];
bars11 = [23,24,4,8];
 

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means', r'$\mu \pm 3\sigma$', r'$\mu \pm 3\sigma (log)$'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,320),20))
plt.title('Day 1',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('9.eps')
plt.show()
 









#day2

barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [12,15,0,4];
bars2 = [15,19,0,1];
bars3 = [10,16,1,2];
bars4 = [17,12,4,5];
bars5 = [6,7,0,0];
bars6 = [12,10,0,1];
bars7 = [20,19,8,12];
bars8 = [59,59,32,20];
bars9 = [30,30,10,6];
bars10 = [49,54,26,8];
bars11 = [20,19,4,4];
 

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means', '$\mu \pm 3\sigma$', r'$\mu \pm 3\sigma (log)$'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,320),20))
plt.title('Day 2',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('10.eps')
plt.show()
 









#Day3 
barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [22,26,4,6];
bars2 = [26,25,0,0];
bars3 = [11,14,0,0];
bars4 = [9,10,0,3];
bars5 = [13,17,3,13];
bars6 = [17,18,0,3];
bars7 = [15,19,6,10];
bars8 = [59,53,37,15];
bars9 = [23,28,5,9];
bars10 = [76,75,48,21];
bars11 = [20,24,7,9];
 

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means', r'$\mu \pm 3\sigma$', r'$\mu \pm 3\sigma (log)$'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,320),20))
plt.title('Day 3',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('11.eps')
plt.show()
 


 





#Day 4
barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [6,6,0,2];
bars2 = [10,8,0,3];
bars3 = [10,8,1,3];
bars4 = [12,7,0,1];
bars5 = [11,8,4,0];
bars6 = [4,4,0,2];
bars7 = [6,3,1,3];
bars8 = [71,68,56,16];
bars9 = [14,9,4,2];
bars10 = [22,16,15,1];
bars11 = [7,6,1,4];
 

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means', r'$\mu \pm 3\sigma$', r'$\mu \pm 3\sigma (log)$'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,320),20))
plt.title('Day 4',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('12.eps')
plt.show()
 










#Day 5
barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [13,12,0,3];
bars2 = [9,11,1,0];
bars3 = [15,18,2,0];
bars4 = [20,17,2,0];
bars5 = [30,23,4,2];
bars6 = [11,9,1,6];
bars7 = [34,34,10,4];
bars8 = [39,36,14,6];
bars9 = [30,28,6,5];
bars10 = [37,39,15,3];
bars11 = [33,25,6,1];
 

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means', r'$\mu \pm 3\sigma$', r'$\mu \pm 3\sigma (log)$'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,320),20))
plt.title('Day 5',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('13.eps')
plt.show()
 






#Day 6
barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [31,36,5,0];
bars2 = [27,22,2,4];
bars3 = [32,31,8,4];
bars4 = [29,28,4,1];
bars5 = [17,12,1,7];
bars6 = [17,19,1,0];
bars7 = [12,10,3,1];
bars8 = [27,20,6,4];
bars9 = [30,29,10,7];
bars10 = [59,65,32,6];
bars11 = [23,24,7,4];
 

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means', r'$\mu \pm 3\sigma$', r'$\mu \pm 3\sigma (log)$'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,320),20))
plt.title('Day 6',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('14.eps')
plt.show()
 








#All days total


barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [107,111,10,22];
bars2 = [110,105,7,8];
bars3 = [91,107,13,10];
bars4 = [96,87,10,11];
bars5 = [101,89,12,23];
bars6 = [78,79,3,12];
bars7 = [111,108,35,58];
bars8 = [283,266,156,70];
bars9 = [180,173,65,41];
bars10 = [293,305,165,46];
bars11 = [126,122,29,30];


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means', r'$\mu \pm 3\sigma$', r'$\mu \pm 3\sigma (log)$'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,320),20))
plt.title('Sum over all six days',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('15.eps')
plt.show()
 
"""




#################################################################################################
#Identifying from the whole population

#Day 1

bars1 = [0,1]		
bars2 = [2,2]	
bars3 = [1,2]		
bars4 = [3,3]		
bars5 = [3,1]		
bars6 = [1,1]
bars7 = [2,2]		
bars8 = [35,37]	
bars9 = [2,2]	
bars10 = [6,5]	
bars11 = [0,0]	


 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,80),10))
plt.title('Day 1',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':14}, bbox_to_anchor=(1,1),fontweight='bold',fontsize = 14)
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('16.eps')
plt.show()







#Day2


bars1 = [1,2]		
bars2 = [0,0]	
bars3 = [3,2]		
bars4 = [2,2]		
bars5 = [1,4]		
bars6 = [1,0]
bars7 = [1,3]		
bars8 = [9,8]	
bars9 = [5,5]	
bars10 = [3,2]	
bars11 = [3,3]	


							

				


 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,80),10))
plt.title('Day 2',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':14}, bbox_to_anchor=(1,1))
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('17.eps')
plt.show()




#Day3


bars1 = [3,4]		
bars2 = [2,3]	
bars3 = [4,8]		
bars4 = [4,5]		
bars5 = [2,1]		
bars6 = [4,4]
bars7 = [0,1]		
bars8 = [3,2]	
bars9 = [8,7]	
bars10 = [21,21]	
bars11 = [4,3]	


		

				


 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,80),10))
plt.title('Day 3',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':14}, bbox_to_anchor=(1,1))
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('18.eps')
plt.show()




#sum over the last 3 days

barWidth = 0.05
 
# Choose the height of the blue bars
bars1 = [4,7];
bars2 = [4,5];
bars3 = [8,12];
bars4 = [9,10 ];
bars5 = [6,6];
bars6 = [6,5];
bars7 = [3,6];
bars8 = [47,47];
bars9 = [15,14];
bars10 = [30,28];
bars11 = [7,7];


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]
r6 = [x + 5*barWidth for x in r1]
r7 = [x + 6*barWidth for x in r1]
r8 = [x + 7*barWidth for x in r1]
r9 = [x + 8*barWidth for x in r1]
r10 = [x + 9*barWidth for x in r1]
r11 = [x + 10*barWidth for x in r1]

 

 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r2, bars2, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r4, bars4, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r5, bars5, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Batten sheep',align= 'center')
plt.bar(r6, bars6, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r7, bars7, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r8, bars8, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r9, bars9, width = barWidth, color = 'red', edgecolor = 'black',  capsize=7, label='Normal sheep',align= 'center')
plt.bar(r10, bars10, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
plt.bar(r11, bars11, width = barWidth, color = 'red', edgecolor = 'black', capsize=7, label='Normal sheep',align= 'center')
 
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['GMM', 'K-means'],horizontalalignment = 'left',fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,80),10))
plt.title('Sum over all three days',fontweight='bold',fontsize = 14)
plt.xlabel('Algorithms',fontweight='bold',fontsize = 14)
plt.ylabel('Number of outliers',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':14}, bbox_to_anchor=(1,1))
plt.tight_layout(pad=0)

import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='Batten sheep')
blue_patch = mpatches.Patch(color='blue', label='Normal sheep')


plt.legend(handles=[red_patch, blue_patch])
              
# Show graphic
plt.savefig('19.eps')
plt.show()
 




"""
###################################


#plots for info_theory paper


x3 = np.array([1.96168672787661,1.78315064305665,1.89222664274969,1.88734229857179,1.95939829859849,1.63128307158802])
x2 =np.array([1.38952722818897,1.16201605400818,1.33041569944706,1.20195701041029,1.38064513566515,1.00050517019464]);

t = list(range(1,7))

ax = axs[0,0]
ax.errorbar(x, y, yerr=yerr, fmt='o')


my_xticks = ['1st','2nd','3rd','4th','5th','6th'];

bar2 = np.array([0.0469835517837369, 0.0620871408182204, 0.0461825176383515, 0.0673727062579248, 0.0520722843063135,0.0461345946539694]);
bar1 = np.array([0.0355559331182429, 0.0418583793104196,0.0461302237262728,0.0297315006077399,0.0357991334647614,0.0538540292194969])



plt.xlim([0,7])
plt.ylim([0.9,2.5])
plt.plot(t, x2, linestyle="--", color="r")
plt.xlabel('Days')
plt.ylabel('Entropy(bits)')
plt.title('Mean variation in entropy over six days with synthetic data')
plt.xticks(t,my_xticks)

p1, = plt.errorbar(t, x3,xerr=bar1,yerr=bar1, linestyle="-", color="b")
p2, = plt.errorbar(t, x2, xerr = bar2, yerr = bar2, linestyle="--", color="r")
plt.legend([p1,p2],["Normal Sheep","Abnormal Sheep"],loc='upper right')
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles,labels)

plt.savefig('syth.eps',format='eps',dpi=1000)
plt.show()

"""
###################################################################################
#Bigger plots













"""

# abnormality sampled from two bins bigger flock
#######################################################################################################

# width of the bars



# Choose the height of the blue bars
bars1 = [53.7803030303030,	56.9671717171717,	57.8661616161616,	58.7828282828283]
bars2 = [27.1540404040404,	31.5227272727273,	34.5681818181818,	48.3813131313131]

 

# Choose the height of the error bars (bars1)
c1 = [(46.0883801426710,	61.4722259179350),(48.8471725603742,	65.0871708739692),(50.1129324167020,	65.6193908156212),(51.0832963228471,	66.4823602428095)]
c2 = [(23.2573081672560,	31.0507726408248),(27.5584509318589,	35.4870036135956),(30.8831247949928,	38.2532388413709),(41.2314677230731,	55.5311585395532)]





yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
#r3 = [x + 2*barWidth for x in r1]
#r4 = [x + 3*barWidth for x in r1]


# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center') 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy(%)',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
#plt.legend(loc=2, prop={'size': 7})
plt.savefig('1.eps')
plt.show()





# Choose the height of the blue bars
bars1 = [10.7986529586346,	15.2716707142287,	8.61580186161526,	7.34723994025996]
bars2 = [41.1363636363636,	14.3181818181818,	19.8787878787879,	0]

 

# Choose the height of the error bars (bars1)
c1 = [(3.38129556799401,	18.2160103492751),(6.84203544150291,	23.7013059869544),(1.96265657743206,	15.2689471457985),(1.05838110625392,	13.6360987742660)]
c2 = [(31.3674662464215,	50.9052610263057),(6.05838636994586,	22.5779772664178),(10.6228446621453,	29.1347310954304),(0,	0)]





yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]



# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center') 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('2.eps')
plt.show()























# number of agents evaluation, accuracy
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [63.1011904761905,	55.9807017543860,	57.1009199134199,	55.6094696969697,	51.9640151515152]
bars2 = [49.0773809523810,	35.0017543859649,	32.2981601731602,	30.4511363636364,	27.4521780303030]

# Choose the height of the error bars (bars1)

c1 = [(53.8962071779750,	72.3061737744059),(48.6185842460962,	63.3428192626757),(47.8498721595572,	66.3519676672826),(46.4972405944222,	64.7216987995172),(42.0644400651716,	61.8635902378587)]
c2 = [(39.9060019226077,	58.2487599821543),(30.4160317411647,	39.5874770307651),(27.3829172178319,	37.2134031284885),(25.6296645552491,	35.2726081720236),(22.1119543233855,	32.7924017372205)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]



 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')



 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('3.eps')
plt.show()














# number of agents evaluation, false positives
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars


bars1 = [14.7301596652787,	11.4569633176905,	7.28961143023643,	5.67148375199362,	11.6865890186203]
bars2 = [19.3214285714286,	17.9657894736842,	19.0146103896104,	16.2159090909091,	21.9346590909091]

 
# Choose the height of the error bars (bars1)



c1 = [(5.49762291567961,	23.9626964148778),(4.20552856326797,	18.7083980721131),(-0.258526911027219,	14.8377497715001),(-1.07343702297932,	12.4164045269666),(1.98548277173785,	21.3876952655027)]
c2 = [(9.90330329327024,	28.7395538495869),(9.64582922573034,	26.2857497216381),(8.34611334738696,	29.6831074318338),(5.87857124625343,	26.5532469355648),(10.0743854663909,	33.7949327154273)]


yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]




# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')


# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('4.eps')
plt.show()






# abnormality sampled from one bin bigger flock
#######################################################################################################

# width of the bars


# Choose the height of the blue bars
bars1 = [70.2474747474747,	72.8838383838384,	72.0075757575758,	67.8308080808081]
bars2 = [70.7272727272727,	30.4343434343434,	33.7979797979798,	81.8787878787879]

 

# Choose the height of the error bars (bars1)
c1 = [(60.7342141511145,	79.7607353438350),(63.7633608330148,	82.0043159346620),(62.8309515650416,	81.1841999501100),(58.3564929828750,	77.3051231787412)]
c2 = [(68.0107836875176,	73.4437617670279),(25.7044983410963,	35.1641885275906),(28.3317044259907,	39.2642551699689),(79.8533234753795,	83.9042522821963)]





yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
#r3 = [x + 2*barWidth for x in r1]
#r4 = [x + 3*barWidth for x in r1]


# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center') 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy(%)',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
#plt.legend(loc=2, prop={'size': 7})
plt.savefig('5.eps')
plt.show()




# Choose the height of the blue bars
bars1 = [20.1907338442311,	15.4892107761785,	19.4900296215221,	14.2689926966607]
bars2 = [47.4012445887446,	19.1666666666667,	22.1969696969697,	33.4242424242424]

 

# Choose the height of the error bars (bars1)
c1 = [(10.6927914446649,	29.6886762437973),(6.93970526078453,	24.0387162915724),(10.0531538951474,	28.9269053478969),(6.00422984890220,	22.5337555444192)]
c2 = [(42.3219089347425,	52.4805802427467),(12.0810661900743,	26.2522671432590),(16.9058591290983,	27.4880802648411),(27.2902894147832,	39.5581954337016)]





yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]



# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center') 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('6.eps')
plt.show()






# number of agents evaluation, accuracy
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [79.6972222222222,	75.9270833333333,	70.2013888888889,	63.9732142857143,	63.4134615384616]
bars2 = [56.8500000000000,	52.8541666666667,	53.9826388888889,	53.7797619047619,	53.0865384615385]

# Choose the height of the error bars (bars1)

c1 = [(70.8877674291488,	88.5066770152957),(65.5816284173450,	86.2725382493216),(59.1672751246727,	81.2355026531051),(53.1982551883380,	74.7481733830906),(52.5470609321818,	74.2798621447413)]
c2 = [(47.5784046562282,	66.1215953437717),(42.8075075395822,	62.9008257937511),(44.1873419436634,	63.7779358341144),(44.7187331456326,	62.8407906638912),(43.9572706368901,	62.2158062861868)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]



 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')



 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('7.eps')
plt.show()



# number of agents evaluation, false positives
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars


bars1 = [14.9627357020415,	18.6258050348860,	16.8922265176708,	23.6175637913836,	12.6492036343154]
bars2 = [36.3419642857143,	34.7154017857143,	31.7805059523810,	26.7251275510204,	22.9914148351648]

 
# Choose the height of the error bars (bars1)



c1 = [(6.10920129656959,	23.8162701075133),(7.62915050715714,	29.6224595626149),(6.33632265938614,	27.4481303759554),(12.6206856300686,	34.6144419526986),(3.83321694092507,	21.4651903277058)]
c2 = [(25.6952512604183,	46.9886773110103),(23.3414534268506,	46.0893501445780),(21.3002685326178,	42.2607433721441),(17.4110061076288,	36.0392489944121),(13.3526983714826,	32.6301312988471)]


yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]


# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]




# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')


# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('8.eps')
plt.show()



#################################################################
#Smaller flock one abnormal bin


# Choose the height of the blue bars
bars1 = [84.9242424242424,	89.1919191919192,	84.6464646464647,	87.8787878787879]
bars2 = [96.9696969696970,	78.4343434343434,	8.40909090909091,	46.7676767676768]
bars3=  [9.39393939393939,	25.7575757575758,	13.6363636363636,	31.8181818181818]
bars4 = [8.48484848484848,	22.7272727272727,	11.7424242424242,	25.7575757575758]
 
  


# Choose the height of the error bars (bars1)
c1 = [(76.3798274153615,	93.4686574331234),(82.1358211260872,	96.2480172577512),(76.6049675095856,	92.6879617833437),(80.8688469969908,	94.8887287605850)]
c2 = [(95.1933350662462,	98.7460588731478),(72.5705524532501,	84.2981344154367),(5.71477790427008,	11.1034039139117),(39.0128277877341,	54.5225257476194)]
c3 = [(5.71269223121059,	13.0751865566682),(16.8046790364874,	34.7104724786641),(8.79336261867982,	18.4793646540475),(20.2803728079073,	43.3559908284563)]
c4 = [(4.71960769007500,	12.2500892796220),(14.3263632643153,	31.1281821902302),(7.14086528901324,	16.3439831958352),(14.9250447191981,	36.5901067959534)]




yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]


# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center') 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')
#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')
#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy(%)',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
#plt.legend(loc=2, prop={'size': 7})
plt.savefig('9.eps')
plt.show()



#false positives temporal evaluation
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [17.3484848484848,	14.5202020202020,	15.2525252525253,	10.1262626262626]
bars2 = [31.8181818181818,	16.6666666666667,	87.3737373737374,	0]
bars3= [1.76767676767677,	7.57575757575758,	5.05050505050505,	12.1212121212121]
bars4 = [1.76767676767677,	2.27272727272727,	4.79797979797980,	9.09090909090909]
 
# Choose the height of the error bars (bars1)
c1 = [(8.33355366448362,	26.3634160324861),(6.81081618931878,	22.2295878510853),(7.18546366076126,	23.3195868442892),(3.34448871859526,	16.9080365339300)]
c2 = [(24.3847576128751,	39.2516060234885),(10.8279806059424,	22.5053527273909),(83.3683168449092,	91.3791579025656),(0,	0)]
c3 = [(-0.735271404907033,	4.27062494026057),(1.02098902915475,	14.1305261223604),(0.284879748497535,	9.81613035251257),(5.28246597205530,	18.9599582703689)]
c4 = [(-0.735271404907032,	4.27062494026057),(-0.307205253111068,	4.85265979856561),(0.153359805460322,	9.44259979049927),(3.42362654914571,	14.7581916326725)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('10.eps')
plt.show()






# number of agents evaluation, accuracy
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [85.4947916666666,	87.5000000000000,	89.3382352941177,	87.9166666666666,	83.8281250000000]
bars2 = [70.7552083333333,	59.2261904761905,	53.4313725490197,	49.4583333333333,	53.4375000000000]
bars3= [34.6875000000000,	33.2142857142857,	11.3970588235294,	12.6250000000000,	13.9062500000000]
bars4 = [27.4218750000000,	34.2857142857143,	11.3970588235294,	8.25000000000000,	11.1718750000000]
 
# Choose the height of the error bars (bars1)

c1 = [(77.3232304653854,	93.6663528679479),(75.2663845893876,	99.7336154106124),(81.9220713951970,	96.7543991930383),(78.8245275729596,	97.0088057603737),(75.7684323049571,	91.8878176950429)]
c2 = [(60.9893825414168,	80.5210341252498),(44.6606475626441,	73.7917333897368),(44.4579220456079,	62.4048230524314),(36.7048454698899,	62.2118211967767),(43.1586434702651,	63.7163565297349)]
c3 = [(24.0456911609981,	45.3293088390019),(16.9057115258246,	49.5228599027468),(5.33009061452746,	17.4640270325314),(5.39177669720705,	19.8582233027930),(7.74940851022766,	20.0630914897723)]
c4 = [(17.4823680991118,	37.3613819008882),(17.9643402127138,	50.6070883587148),(5.21585808122419,	17.5782595658346),(3.00801154070987,	13.4919884592901),(5.76317076692334,	16.5805792330767)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]


 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1) ,fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('11.eps')
plt.show()


# number of agents evaluation, false positives
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [16.8229166666667,	19.6428571428571,	12.2794117647059,	9.37500000000000,	14.7135416666667]
bars2 = [33.4635416666667,	34.2261904761905,	31.4950980392157,	35.2083333333333,	36.1979166666667]
bars3 = [8.59375000000000,	19.6428571428571,	3.67647058823529,	2.50000000000000,	4.68750000000000]
bars4 = [5.20833333333333,	16.0714285714286,	2.20588235294118,	1.25000000000000,	3.12500000000000]
 
# Choose the height of the error bars (bars1)

c1 = [(8.34109449319287,	25.3047388401405),(5.98395318790508,	33.3017610978092),(4.74762342419465,	19.8112001052171),(0.198371469609420,	18.5516285303906),(6.56494873246415,	22.8621346008692)]
c2 = [(23.7600678714105,	43.1670154619229),(17.8829815756464,	50.5693993767346),(22.2954221709148,	40.6947739075166),(22.1590704896957,	48.2575961769710),(26.6392227512285,	45.7566105821048)]
c3 = [(2.08501912327862,	15.1024808767214),(8.51106835086432,	30.7746459348500),(-0.667682241164052,	8.02062341763464),(-2.55672730009190,	7.55672730009191),(-0.634131468000559,	10.0091314680006)]
c4 = [(0.294939799657000,	10.1217268670097),(6.68434542639442,	25.4585117164627),(-0.297939067807781,	4.70970377369013),(-1.27836365004595,	3.77836365004595),(-1.25556464139436,	7.50556464139436)]

yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]



# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('12.eps')
plt.show()



#########################################################################
#smaller flock from two different distributions



# Choose the height of the blue bars
bars1 = [76.9696969696970,	74.6464646464647,	71.5656565656566,	74.1919191919192]
bars2 = [71.3636363636364,	70.6060606060606,	71.1868686868687,	71.5404040404040]
bars3=  [33.3333333333333,	21.8181818181818,	29.1666666666667,	40.9090909090909]
bars4 = [29.7979797979798,	18.1818181818182,	23.1060606060606,	34.0909090909091]
 
  


# Choose the height of the error bars (bars1)
c1 = [(69.5692887729595,	84.3701051664344),(68.1545121514505,	81.1384171414788),(64.3985658137452,	78.7327473175680),(67.0695189981720,	81.3143193856663)]
c2 = [(63.9155713446300,	78.8117013826427),(64.1108781758064,	77.1012430363148),(64.5414821180404,	77.8322552556971),(64.5081117592431,	78.5726963215649)]
c3 = [(26.9051515445276,	39.7615151221391),(17.1957384258021,	26.4406252105615),(23.3031526297601,	35.0301807035732),(31.7847567535637,	50.0334250646181)]
c4 = [(22.8852498865030,	36.7107097094566),(13.3240053966554,	23.0396309669810),(17.0737992080432,	29.1383220040780),(24.6535200087633,	43.5282981730549)]




yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]


# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center') 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')
#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')
#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy(%)',fontweight='bold',fontsize = 14)
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1) ,fontweight = 'bold', fontsize = 14)
plt.tight_layout(pad=7)
#plt.legend(loc=2, prop={'size': 7})
plt.savefig('13.eps')
plt.show()



#false positives temporal evaluation
# width of the bars
barWidth = 0.1
 
 

 
# Choose the height of the blue bars
bars1 = [ 5.55555555555556,	1.51515151515152,	3.03030303030303,	6.13636363636364]
bars2 = [7.07070707070707,	2.65151515151515,	1.21212121212121,	6.18686868686869]
bars3= [8.71212121212122,	0,	0,	14.6464646464646]
bars4 = [6.94444444444445,	0,	0.757575757575758,	11.1111111111111]
 
# Choose the height of the error bars (bars1)

c1 = [(0.0664503635113274,	11.0446607475998),(-1.51081501271515,	4.54111804301819),(-1.21601410476914,	7.27662016537520),(0.678481880140027,	11.5942453925872)]
c2 = [(1.17433463795680,	12.9670795034573),(-1.10290710736055,	6.40593741039085),(
-1.20865201017213,	3.63289443441455),(0.733433825994582,	11.6403035477428)]
c3 = [(4.07625024205100,	13.3479921821914),(0,	0),(0,	0),(8.69756739604539,	20.5953618968839)]
c4 = [(2.79118272612718,	11.0977061627617),(0,	0),(-0.755407506357578,	2.27055902150909),(5.52869999788457,	16.6935222243377)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['150', '300', '450', '600'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Duration of abnormal movement(secs)',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
 
# Show graphic
plt.savefig('14.eps')
plt.show()




# number of agents evaluation, accuracy
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [81.5151515151515,	76.3690476190476,	66.1111111111111,	70.9649122807018,	76.7307692307692]
bars2 = [79.8106060606061,	70.2976190476190,	67.0370370370371,	68.6184210526316,	71.4102564102564]
bars3= [32.2727272727273,	44.9404761904762,	26.2962962962963,	28.3771929824561,	23.5576923076923]
bars4 = [23.1439393939394,	40.0595238095238,	22.3611111111111,	26.3377192982456,	16.7948717948718]
 
# Choose the height of the error bars (bars1)

c1 = [(73.4329579933345,	89.5973450369685),(68.6574604255943,	84.0806348125009),(55.6086290671700,	76.6135931550522),(64.2968847597067,	77.6329398016968),(69.4017445651026,	84.0597938964358)]
c2 = [(72.0369141656820,	87.5842979555301),(62.6691464386424,	77.9260916565957),(57.0661138735281,	77.0079602005460),(62.0671020835789,	75.1697400216842),(63.9581802838337,	78.8623325366791)]
c3 = [(25.2497282915439,	39.2957262539106),(36.4564730161849,	53.4244793647675),(16.5511823481756,	36.0414102444170),(22.1806943245141,	34.5736916403982),(16.9081286692120,	30.2072559461726)]
c4 = [(15.4964756684864,	30.7914031193924),(31.1873519031476,	48.9316957159000),(12.7301664235484,	31.9920557986738),(19.6674424872930,	33.0079961091983),(
10.5799035978233,	23.0098399919203)]



yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]
r5 = [x + 4*barWidth for x in r1]


 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('Accuracy%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1),fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=7)
# Show graphic
plt.savefig('15.eps')
plt.show()





# number of agents evaluation, false positives
# width of the bars
barWidth = 0.1
 
# Choose the height of the blue bars
bars1 = [5.22727272727273,	3.57142857142857,	7.40740740740741,	3.94736842105263,	1.44230769230769]
bars2 = [6.55303030303030,	3.57142857142857,	4.62962962962963,	5.26315789473684,	1.44230769230769]
bars3 = [5.68181818181818,	0,	8.79629629629629,	9.53947368421052,	4.80769230769231]
bars4 = [3.40909090909091,	0.892857142857143,	7.40740740740741,	7.56578947368421,	3.84615384615385]
 
# Choose the height of the error bars (bars1)

c1 = [(-0.940634055368832,	11.3951795099143),(-1.44332883235253,	8.58618597520968),(-1.16547840774061,	15.9802932225554),(-0.531717964434303,	8.42645480653957),(-1.45324582257092,	4.33786120718630)]
c2 = [(0.158113483093451,	12.9479471229672),(-1.44332883235253,	8.58618597520968),(-2.05786140368137,	11.3171206629406),(0.387468151597861,	10.1388476378758),(-1.45324582257092,	4.33786120718630)]
c3 = [(-0.197350707423895,	11.5609870710603),(0,	0),(2.54778569778008,	15.0448068948125),(5.06870382707373,	14.0102435413473),(0.663983963573417,	8.95140065181120)]
c4 = [(-1.66740389618320,	8.48558571436502),(-0.896468556508165,	2.68218284222245),(1.61804960288253,	13.1967652119323),(3.45005589402257,	11.6815230533458),(
0.100687811181929,	7.59161988112576)]

yer1 = [bars1[i] - c1[i][1] for i in range(len(c1))]
yer2 = [bars2[i] - c2[i][1] for i in range(len(c2))]
yer3 = [bars3[i] - c3[i][1] for i in range(len(c3))]
yer4 = [bars4[i] - c4[i][1] for i in range(len(c4))]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + 2*barWidth for x in r1]
r4 = [x + 3*barWidth for x in r1]



# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'magenta', edgecolor = 'black', yerr=yer1, capsize=7, label='GMM',error_kw = dict(ecolor='gray'),align= 'center')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='K-means',error_kw = dict(ecolor='gray'),align= 'center')

#create red bars
plt.bar(r3, bars3, width = barWidth, color = 'red', edgecolor = 'black', yerr=yer3, capsize=7, label=r'$\mu \pm 3\sigma$',error_kw = dict(ecolor='gray'),align= 'center')

#create green bars
plt.bar(r4, bars4, width = barWidth, color = 'green', edgecolor = 'black', yerr=yer4, capsize=7, label=r'$\mu \pm 3\sigma (log)$',error_kw = dict(ecolor='gray'),align= 'center')
 

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['1', '2', '3', '4', '5'],fontweight='bold',fontsize = 14)
plt.yticks(range(0,max(0,100),10))
plt.xlabel('Number of agents',fontweight='bold',fontsize = 14)
plt.ylabel('False Positives(%)',fontweight='bold',fontsize = 14)
#plt.legend(loc=1, prop={'size': 7})
plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1), fontweight = 'bold',fontsize = 14)
plt.tight_layout(pad=0)
# Show graphic
plt.savefig('16.eps')
plt.show()
"""







