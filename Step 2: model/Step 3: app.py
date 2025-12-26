from model.disease_model import predict_disease

print("Disease Prediction System")
print("Enter symptoms (1 = Yes, 0 = No)")

fever = int(input("Fever: "))
cough = int(input("Cough: "))
headache = int(input("Headache: "))
fatigue = int(input("Fatigue: "))

symptoms = [fever, cough, headache, fatigue]
result = predict_disease(symptoms)

print("\nPredicted Disease:", result)
