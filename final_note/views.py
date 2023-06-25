from django.shortcuts import render, HttpResponse
from .models import Validacion

def index(request):
    return render(request, 'index.html')


def asignar_clasificacion(nota_c3):
    if nota_c3< 2.0:
        return ('Excelente','Coronao!!','&#128526;')
    elif 2.0 <= nota_c3 and nota_c3< 3.0:
        return ('Bueno','Esta relajado eso','&#128517')
    elif 3.0 <= nota_c3 and nota_c3< 3.8:
        return ('Aceptable','Ponte las pilas','&#128528;')
    elif 3.8 <= nota_c3 and nota_c3< 4.5:
        return ('Difícil','Ponte a rezar','&#128591;')
    elif 4.5 <= nota_c3 and nota_c3<= 5.0:
        return ('Milagro','No vayas a llorar ahora',"&#128534;")
    else:
        return ('Perdido','LLoralo','&#128557;')

def calcular_nota(request):
    if request.method == 'POST':
        n1 = float(request.POST['nota_c1'])
        n2 = float(request.POST['nota_c2'])
        
        # Validación de rango de notas
        if n1 < 0 or n1 > 5 or n2 < 0 or n2 > 5:
            return render(request, 'index.html', {
                "mensaje_error": 'ingresa las notas en el rango que es Njd'
            })
        
        # Cálculo de la nota necesaria para ganar
        else:
            n3 = round((-n1 * 0.3 - n2 * 0.35 + 3.0) / 0.35, 2)
            clasificacion = asignar_clasificacion(n3)
            
            # Creación de una nueva instancia del modelo Validacion
            nueva_validacion = Validacion.objects.create(
                nota_c1=n1,
                nota_c2=n2,
                nota_c3=n3,
                clasificacion=clasificacion[0],
            )
            nueva_validacion.save()
            
            return render(request, 'index.html', {
                "nota_final": n3,
                "mensaje": clasificacion[1],
                "emogi": clasificacion[2]
            })
