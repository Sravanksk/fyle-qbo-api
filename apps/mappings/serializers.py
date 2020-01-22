from rest_framework import serializers

from .models import GeneralMapping, EmployeeMapping, CategoryMapping, CostCenterMapping, ProjectMapping


class GeneralMappingSerializer(serializers.ModelSerializer):
    """
    General mappings group serializer
    """
    class Meta:
        model = GeneralMapping
        fields = '__all__'


class EmployeeMappingSerializer(serializers.ModelSerializer):
    """
    Employee mappings group serializer
    """
    class Meta:
        model = EmployeeMapping
        fields = '__all__'


class CategoryMappingSerializer(serializers.ModelSerializer):
    """
    Category mappings group serializer
    """
    class Meta:
        model = CategoryMapping
        fields = '__all__'


class CostCenterMappingSerializer(serializers.ModelSerializer):
    """
    CostCenter mappings group serializer
    """
    class Meta:
        model = CostCenterMapping
        fields = '__all__'


class ProjectMappingSerializer(serializers.ModelSerializer):
    """
    Project mappings group serializer
    """
    class Meta:
        model = ProjectMapping
        fields = '__all__'
