import numpy as ny
import matplotlib.pyplot as plt
import os, cv2
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier

def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
    plt.yticks(())

dir_name= "dataset/faces/"
y=[];X=[];target_names=[]
person_id=0;h=w=300
n_samples=0
class_names=[]
for person_name in os.listdir(dir_name):
    dir_path = dir_name+person_name+"/"
    class_names.append(person_name)
    for image_name in os.listdir(dir_path):
        image_path = dir_path+image_name
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_image= cv2.resize(gray,(h,w))
        v = resized_image.flatten()
        X.append(v)
        n_samples =n_samples+1
        y.append(person_id)
       
        target_names.append(person_name)
    person_id=person_id+1

y=ny.array(y)
X=ny.array(X)
target_names =ny.array(target_names)
n_features = X.shape[1]
print("Number of sampels:",n_samples)
print(X.shape)
n_classes = target_names.shape[0]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=88)

n_components = 150
# print("Extracting the top %d eigenfaces from %d faces"% (n_components, X_train.shape[0]))
pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]

# print("Projecting the input data on the eigenfaces orthonormal basis")
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
# print(X_train_pca.shape,X_test_pca.shape)
lda = LinearDiscriminantAnalysis()
lda.fit(X_train_pca, y_train)
X_train_lda = lda.transform(X_train_pca)
X_test_lda = lda.transform(X_test_pca)
print("Project done...")
clf = MLPClassifier(max_iter=1000, verbose=False).fit(X_train_lda, y_train)
# print("Model Weights:")
model_info = [coef.shape for coef in clf.coefs_]
# print(model_info)
y_pred=[];y_prob=[]

for test_face in X_test_lda:
    prob = clf.predict_proba([test_face])[0]
    class_id = ny.where(prob == ny.max(prob))[0][0]
    y_pred.append(class_id)
    y_prob.append(ny.max(prob))
# Transform the data
y_pred = ny.array(y_pred)
        
prediction_titles=[]
true_positive = 0

for i in range(y_pred.shape[0]):
    true_name = class_names[y_test[i]]
    pred_name = class_names[y_pred[i]]
    result = 'pred: %s, pr: %s \ntrue: %s' % (pred_name, str(y_prob[i])[0:3], true_name)
    prediction_titles.append(result)
    if true_name==pred_name:
        true_positive =true_positive+1
        
print("Accuracy:",true_positive*100/y_pred.shape[0])

plot_gallery(X_test, prediction_titles, h, w)
plt.show()