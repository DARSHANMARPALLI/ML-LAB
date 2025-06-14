from sklearn.datasets import load_iris 
iris=load_iris()

x=iris.data 
y=iris.target 
print(x[:5],y[:5])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest =train_test_split(x,y,test_size=0.4,random_state=1) 
print(iris.data.shape)
print(len(xtrain))
print(len(ytest))

from sklearn.neighbors import KNeighborsClassifier 
knn=KNeighborsClassifier(n_neighbors=1) 
knn.fit(xtrain,ytrain)
pred=knn.predict(xtest)

from sklearn import metrics 
print("Accuracy",metrics.accuracy_score(ytest,pred)) 
print(iris.target_names[2]) 
ytestn=[iris.target_names[i] for i in ytest] 
predn=[iris.target_names[i] for i in pred]

print("predicted Actual")
for i in range(len(pred)):
    print(i," ",predn[i]," ",ytestn[i])









*****************OUTPUT*******************
[[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]
 [4.6 3.1 1.5 0.2]
 [5.  3.6 1.4 0.2]] [0 0 0 0 0]
(150, 4)
90
60
Accuracy 0.9666666666666667
virginica
predicted Actual
0   setosa   setosa
1   versicolor   versicolor
2   versicolor   versicolor
3   setosa   setosa
4   virginica   virginica
5   virginica   versicolor
6   virginica   virginica
7   setosa   setosa
8   setosa   setosa
9   virginica   virginica
10   versicolor   versicolor
11   setosa   setosa
12   virginica   virginica
13   versicolor   versicolor
14   versicolor   versicolor
15   setosa   setosa
16   versicolor   versicolor
17   versicolor   versicolor
18   setosa   setosa
19   setosa   setosa
20   versicolor   versicolor
21   versicolor   versicolor
22   versicolor   versicolor
23   setosa   setosa
24   virginica   virginica
25   versicolor   versicolor
26   setosa   setosa
27   setosa   setosa
28   versicolor   versicolor
29   virginica   virginica
30   versicolor   versicolor
31   virginica   virginica
32   versicolor   versicolor
33   virginica   virginica
34   virginica   virginica
35   setosa   setosa
36   versicolor   versicolor
37   setosa   setosa
38   versicolor   versicolor
39   virginica   virginica
40   virginica   virginica
41   setosa   setosa
42   versicolor   virginica
43   virginica   virginica
44   versicolor   versicolor
45   virginica   virginica
46   setosa   setosa
47   setosa   setosa
48   setosa   setosa
49   versicolor   versicolor
50   setosa   setosa
51   setosa   setosa
52   virginica   virginica
53   virginica   virginica
54   virginica   virginica
55   virginica   virginica
56   virginica   virginica
57   versicolor   versicolor
58   virginica   virginica
59   versicolor   versicolor
