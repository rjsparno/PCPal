from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.template import loader

from .models import CPU
from .models import GPU
from .models import RAM
from .models import MOBO
from .models import HDD
from .models import PSU
from .models import TWR
# Create your views here.

def cpu_index(request):
    latest_cpu_list = CPU.objects.order_by('cpu_price')[:100]
    latest_gpu_list = GPU.objects.order_by('gpu_price')[:100]
    latest_ram_list = RAM.objects.order_by('ram_price')[:100]
    latest_mobo_list = MOBO.objects.order_by('mobo_price')[:100]
    latest_hdd_list = HDD.objects.order_by('-hdd_price')[:100]
    latest_psu_list = PSU.objects.order_by('psu_price')[:100]
    latest_case_list = TWR.objects.order_by('twr_price')[:100]
    context = {
        'latest_cpu_list': latest_cpu_list,
        'latest_gpu_list': latest_gpu_list, 
        'latest_ram_list': latest_ram_list, 
        'latest_mobo_list': latest_mobo_list, 
        'latest_hdd_list': latest_hdd_list, 
        'latest_psu_list': latest_psu_list,
        'latest_case_list': latest_case_list,
    }
    return render(request, 'PCPal/index.html', context)
 
