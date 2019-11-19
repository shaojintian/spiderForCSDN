### KNN Classifier    
from sklearn.neighbors import KNeighborsClassifier
 
clf = KNeighborsClassifier()
clf.fit(train_x, train_y)
__________________________________________________________
 
### Logistic Regression Classifier    
from sklearn.linear_model import LogisticRegression
 
clf = LogisticRegression(penalty='l2')
clf.fit(train_x, train_y)
__________________________________________________________
 
### Random Forest Classifier    
from sklearn.ensemble import RandomForestClassifier
 
clf = RandomForestClassifier(n_estimators=8)
clf.fit(train_x, train_y)
__________________________________________________________
 
### Decision Tree Classifier    
from sklearn import tree
 
clf = tree.DecisionTreeClassifier()
clf.fit(train_x, train_y)
__________________________________________________________
 
### GBDT(Gradient Boosting Decision Tree) Classifier    
from sklearn.ensemble import GradientBoostingClassifier
 
clf = GradientBoostingClassifier(n_estimators=200)
clf.fit(train_x, train_y)
__________________________________________________________
 
###AdaBoost Classifier
from sklearn.ensemble import  AdaBoostClassifier
 
clf = AdaBoostClassifier()
clf.fit(train_x, train_y)
__________________________________________________________
 
### GaussianNB
from sklearn.naive_bayes import GaussianNB
 
clf = GaussianNB()
clf.fit(train_x, train_y)
__________________________________________________________
 
### Linear Discriminant Analysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
 
clf = LinearDiscriminantAnalysis()
clf.fit(train_x, train_y)
__________________________________________________________
 
### Quadratic Discriminant Analysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
 
clf = QuadraticDiscriminantAnalysis()
clf.fit(train_x, train_y)
__________________________________________________________
 
### SVM Classifier    
from sklearn.svm import SVC
 
clf = SVC(kernel='rbf', probability=True)
clf.fit(train_x, train_y)
__________________________________________________________
 
### Multinomial Naive Bayes Classifier    
from sklearn.naive_bayes import MultinomialNB
 
clf = MultinomialNB(alpha=0.01)
clf.fit(train_x, train_y)
