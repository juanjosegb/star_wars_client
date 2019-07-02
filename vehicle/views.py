from django.shortcuts import render
from django.views.generic import TemplateView
from consumer.views import vehicles


class VehicleDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        vehicle_information_list = vehicles.get_vehicle(pk)
        vehicle_names = vehicle_information_list.keys()
        vehicle_info = vehicle_information_list.values()
        return render(request, "vehicle.html", {'vehicle_names': vehicle_names, 'vehicle_info': vehicle_info})