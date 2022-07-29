from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data

# Create your views here.




def ml_app_index(request):

    if(request.method == "POST"):
        form = DataForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('ml_app-predictions')

    else:
        form = DataForm()
        context = {
        'form': form,
        }
        return render(request, "index_ml_app.html", context)

def mal_app_predictions(request):
    resultats_CCardiaque_predis = Data.objects.all()
    context = {
        'resultats_CCardiaque_predis': resultats_CCardiaque_predis
    }


    return render(request, "predictions.html", context)