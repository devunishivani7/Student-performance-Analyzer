import numpy as np
def calculate_mean(students):
    marks=students[:,0]
    return np.mean(marks)
def calculate_standarddeviation(students):
    marks=students[:,0]
    return np.std(marks)
def topper(names,students):
    marks=students[:,0]
    topper_index=np.argmax(marks)
    topper_name=names[topper_index]
    topper_marks=marks[topper_index]
    return topper_name,topper_marks
def calculate_pass_percentage(students):
    marks=students[:,0]
    passed=np.sum(marks>=50)
    total=len(marks)
    percentage=(passed/total)*100
    return percentage
def calculate_correlation(students):
    hours=students[:,2]
    marks=students[:,0]
    corr=np.corrcoef(hours,marks)[0,1]
    return corr
def predict_performance(names,students):
    marks=students[:,0]
    hours=students[:,2]
    for i in range(len(names)):
        if marks[i]>85 and hours[i]>3:
            print(names[i],"->Excellent")
        elif marks[i]>60:
            print(names[i],"->Average")
        else:
            print(names[i],"->Needs Improvement")
def calculate_outliers(names,students):
    marks=students[:,0]
    out=np.mean(marks)
    out1=np.std(marks)
    for i in range(len(names)):
        z_score=(marks[i]-out)/out1
        if abs(z_score)>2:
            print(names[i],"->is an outlier")
