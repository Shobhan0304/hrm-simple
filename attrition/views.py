from django.shortcuts import render
from pickle import load

model = load(open('./savedModels/attr_model.pkl','rb'))

# Create your views here.
def root(request):
    if request.method == 'POST':
        DailyRate = request.POST['DailyRate']
        Department = request.POST['Department']
        DistanceFromHome = request.POST['DistanceFromHome']
        Education = request.POST['Education']
        EducationField = request.POST['EducationField']
        EmployeeNumber = request.POST['EmployeeNumber']
        EnvironmentSatisfaction = request.POST['EnvironmentSatisfaction']
        Gender = request.POST['Gender']
        JobRole = request.POST['JobRole']
        JobSatisfaction = request.POST['JobSatisfaction']
        NumCompaniesWorked = request.POST['NumCompaniesWorked']
        PercentSalaryHike = request.POST['PercentSalaryHike']
        PerformanceRating = request.POST['PerformanceRating']
        RelationshipSatisfaction = request.POST['RelationshipSatisfaction']
        TrainingTimesLastYear = request.POST['TrainingTimesLastYear']
        WorkLifeBalance = request.POST['WorkLifeBalance']
        YearsSinceLastPromotion = request.POST['YearsSinceLastPromotion']
        ypred = model.predict([[DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeNumber, EnvironmentSatisfaction, Gender, JobRole, JobSatisfaction, NumCompaniesWorked, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, TrainingTimesLastYear, WorkLifeBalance, YearsSinceLastPromotion]])
        if (ypred[0] == 0):
            ypred = 'Low Risk of Attrition'
        else:
            ypred = 'High Risk of Attrition'
        return render(request, 'index.html', {'result':ypred})
    return render(request, 'index.html') 