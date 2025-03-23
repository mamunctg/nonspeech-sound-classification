
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix
import numpy as np



# multiclass = np.array([[2, 1, 0, 0],
#                        [1, 2, 0, 0],
#                        [0, 0, 1, 0],
#                        [0, 0, 0, 1]])



#M18- acc-76.69 org test and train
# multiclass = np.array([[82,	1,	2,	6	,0	,1,	6,	0,	1	,1],
#                        [ 3	,136,	1,	4,	0,	2	,8,	2,	2,	2],
#                         [0,	3,	54	,3,	2,	1	,3,	4	,0,	0],
#                         [2	,2	,3,	115,	1	,0	,4,	4,	9	,0],
#                         [0	,10,	4,	4	,10,	0,	1,	0	,1,	0],
#                         [1	,6	,0	,0	,0	,19,	0,	0	,0	,4],
#                         [1	,0	,1,	2,	0	,0,	65	,0	,0,	1],
#                         [0	,2,	2,	0	,0,	0	,2,	21,	1,	2],
#                         [4,	10,	4,	12	,0	,3	,2,	1	,38,	1],
#                         [0,	0,	1,	0,	0,	3,	0,	0	,0	,16]])

### M11-tran set augment only acc-77.24
#
# multiclass=np.array([[85	,0,	2,	2,	0	,1	,8,	0,	0,	2],
# [5,	126,	2	,2	,0,	6,	4	,3,	1,	11],
# [0,	0	,59,	2,	2	,1	,0,	6,	0,	0],
# [2,	0	,5,	115,	5,	0,	1,	7,	5,	0],
# [0,	2	,4,	2,	22,	0,	0,	0,	0,	0],
# [1,	1	,1,	0,	0	,20	,2,	0,	0,	5],
# [3,	0,	1,	0,	0	,0,	59,	6,	0,	1],
# [0,	1	,4,	0,	0,	0	,0	,23	,0	,2,],
# [0,	7,	8,	11,	8	,0,	1,	4,	33,	3],
# [0,0	,0,	0,	0,	2,	0,	0,	0	,18]])
#
# ###M18-acc-70.63 test and train augmented
#
# multiclass=np.array([[445,	2	,28	,7	,1,	0,	71,	5	,12	,9],
# [14,	489,	5,	11	,2	,47	,19	,19,	1,	33],
# [1	,12	,449,	29,	31,	25,	13,	30,	2,	8],
# [7,	0	,16	,449,	28,5	,7	,15,	32,	1],
# [1,	78	,60,	35,	319,	5,	7	,12,	4,	5],
# [4	,22,	4,	0	,5,	349,	0	,1	,0	,125],
# [20	,1	,8	,10,	0	,12	,415,	14,	1,	21],
# [3,	28,	97,	8,	13,	9	,11,	351,	7,	33],
# [5	,50,	64	,70,	94,	21	,16	,46,	194	,32],
# [1	,0	,0	,0,	3,	39,	3,	3,	0	,531]])

#  M18- acc-75.45 train only augment

multiclass=np.array([[ 85,   1  , 3  , 2 ,  0  , 0  , 6   ,0  , 0 ,  3],
 [  6, 120  , 6 ,  2,   0 ,  9 ,  4 ,  2  , 2 ,  9],
 [  0 ,  0 , 60 ,  4  , 2  , 1  , 0 ,  2 ,  0 ,  1],
 [  2  , 0  , 5 ,111 ,  9 ,  0  , 2  , 4,   7 ,  0],
 [  0 ,  4  , 5  , 3 , 17 ,  0,   0 ,  0 ,  1 ,  0],
 [  1 ,  2 ,  0,   0 ,  0 , 20  , 0  , 0 ,  0 ,  7],
 [  3 ,  0  , 2 ,  1 ,  0 ,  3 , 58   ,1  , 0  , 2],
 [  0  , 1 ,  2  , 0  , 0,   0 ,  0,  26 ,  0 ,  1],
 [  3,   4  , 9 ,  5,  14 ,  0 ,  1   ,2 , 31 ,  6],
 [  0 ,  0 ,  0  , 0 ,  0,   1,   0 ,  0 ,  0,  19]])

#class_names = ['class a', 'class b', 'class c', 'class d']
class_names =['baby cry','breath','cough','laugh','man cry','man yawn','screaming','sneeze','woman cry','woman yawn']

fig, ax = plot_confusion_matrix(conf_mat=multiclass,
                                colorbar=True,
                                show_absolute=False,
                                show_normed=True,
                                class_names=class_names)

plt.savefig('M18-acc-75.45  train only   aug.jpg', bbox_inches='tight', dpi=500, format='jpg')
plt.show()