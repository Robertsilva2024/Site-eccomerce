from django.shortcuts import render
from django.views import View

class Payment(View):
    def get(self, request):
        return render(request, 'payment.html')
