from electro.models import Informacion
from django.template import RequestContext
from django.shortcuts import render_to_response

def vista_informacion(request):
	todo=Informacion.objects.all()
	
	return render_to_response('informacion.html',{'info':todo}, context_instance=RequestContext(request))