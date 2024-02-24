from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from . import views

#details Router
detailsRouter=DefaultRouter(trailing_slash=False)
detailsRouter.register(r'basic',views.BasicDetailsView,basename="basicdetails")
detailsRouter.register(r'schooling',views.SchoolingDetailsView,basename="schoolingdetails")
detailsRouter.register(r'college',views.CollegeDetailsView,basename="collegedetails")

#academic Router
academicRouter=DefaultRouter(trailing_slash=False)
academicRouter.register(r'tenth',views.TenthView,basename="ten")
academicRouter.register(r'twelfth',views.TwelfthView,basename="twelve")
academicRouter.register(r'college',views.CollegeView,basename="college")

#performance Router
performanceRouter=DefaultRouter(trailing_slash=False)
performanceRouter.register(r'resume',views.ResumeView,basename="resume")

urlpatterns=[
      path(r'details/', include(detailsRouter.urls)),
      path(r'academic/', include(academicRouter.urls)),
      path(r'performance/', include(performanceRouter.urls))
]