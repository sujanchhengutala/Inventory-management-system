from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView 
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
#========================================================================================================================== 
                    # Item-type view() using MOdelViewSet 
#==========================================================================================================================
class ItemTypeView(ModelViewSet):
    queryset = ItemsType.objects.all()
    serializer_class = ItemTypeSerializer
    
#========================================================================================================================== 
                    # Department view() using ModelViewSet
#==========================================================================================================================

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

#========================================================================================================================== 
                    # Item view() using GenericAPIView
#==========================================================================================================================

class ItemView(GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
# ******************************************************************************************************************************************************** 

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many = True) #here queryset is directly pass because it is convertion object to JSON
        return Response({"status":200, "data":serializer.data})
    
# ******************************************************************************************************************************************************** 

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data) #here data is passed in data because it is convertion json to object
        if(serializer.is_valid()):
            serializer.save()
            return Response({"message":"Item is created", "data":serializer.data, "status":"200"})
        else:
            # return Response({"message":"Unable to created item", "data":serializer.errors, "status":"401"})
            return Response(serializer.errors)
            
 #========================================================================================================================== 
                    # Vendor view() using GenericAPIView
#==========================================================================================================================       
class VendorView(GenericAPIView): 
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
# ******************************************************************************************************************************************************** 

    def get(self, request):
        querySet = self.get_queryset()
        serializer = self.serializer_class(querySet, many = True)
        return Response({"status":200, "message":serializer.data})

        
# ******************************************************************************************************************************************************** 

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data = data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status":200, "message":serializer.data,})
        else:
            return Response({"status":401, "message":serializer.errors,})
            
    
    
    
    