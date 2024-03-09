from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from . import views

# we dont use as_view() with viewset class
#details Router
detailsRouter=DefaultRouter(trailing_slash=False)
detailsRouter.register(r'basic',views.BasicDetailsView,basename="basicdetail")#we cannot specify the placeholder position,it will always at end
detailsRouter.register(r'parent',views.ParentDetailsView,basename="parent")
detailsRouter.register(r'address',views.AddressDetailsView,basename="address")
detailsRouter.register(r'additional',views.AdditionalDetailsView,basename="additional")
detailsRouter.register(r'tenschooling',views.TenSchoolingDetailsView,basename="tenschoolingdetail")
detailsRouter.register(r'twlvethschooling',views.TwelfthSchoolingDetailsView,basename="twelfthschoolingdetail")
detailsRouter.register(r'collegedetails',views.CollegeDetailsView,basename="collegedetail")

#academic Router
academicRouter=DefaultRouter(trailing_slash=False)
academicRouter.register(r'tenth',views.TenthView,basename="ten")
academicRouter.register(r'twelfth',views.TwelfthView,basename="twelve")
academicRouter.register(r'college',views.CollegeView,basename="college")

#performance Router
performanceRouter=DefaultRouter(trailing_slash=False)
performanceRouter.register(r'allResponse',views.ResponseApi,basename="Response")

urlpatterns=[
      path(r'/details/', include(detailsRouter.urls)),
      path(r'/academic/', include(academicRouter.urls)),
      path(r'/performance/', include(performanceRouter.urls)),
]