from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
# Creating Query Set
# stu = Student.objects.all()
# Converting Query Set stu to List of Python Dict / Serializing Query Set
# serializer = StudentSerializer(stu, many = True)

# print(serializer.data)

# JSONRenderer Converts serialized data to JSON

# import JSONRenderer
from rest_framework.renderers import JSONRenderer
# Render data into Json
json_data = JSONRenderer().render(serializer.data)