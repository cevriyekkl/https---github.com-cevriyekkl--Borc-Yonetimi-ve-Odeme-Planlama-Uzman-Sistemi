#Geri ödeme planları oluşturma.

from sklearn.tree import DecisionTreeClassifier

def create_repayment_plan(features, plans, new_data):
    clf = DecisionTreeClassifier()
    clf = clf.fit(features, plans)
    plan = clf.predict([new_data])
    return plan