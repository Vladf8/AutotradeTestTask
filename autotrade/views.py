from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Dealer, Auto
from django.db.utils import IntegrityError


@csrf_exempt
def create_dealer(request):
    if request.method != 'POST':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be POST'})
    try:
        post_body = dict(request.POST)
        if len(post_body['name'][0]) <= 300 and len(post_body['city'][0]) <= 300 and \
                len(post_body['address'][0]) <= 500:
            dealer = Dealer(name=post_body['name'][0], ogrn=post_body['ogrn'][0], city=post_body['city'][0],
                            address=post_body['address'][0])
            try:
                dealer.clean()
            except ValidationError as e:
                return JsonResponse(status=400, data={'success': False, 'error': str(e)})
        else:
            return JsonResponse(status=400, data={'success': False, 'error': 'The length of the name and city fields '
                                                                             'must be no more than 300 characters and'
                                                                             ' the address must be no more than 500 '
                                                                             'characters'})
    except KeyError as e:
        return JsonResponse(status=400, data={'success': False, 'error': 'request must contain {}'.format(str(e))})
    if len(Dealer.objects.filter(ogrn=post_body['ogrn'][0])) == 0:
        dealer.save()
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'This object already exist'})
    return JsonResponse(status=200, data={'success': True, 'dealer_id': dealer.id})


@csrf_exempt
def delete_dealer(request):
    if request.method != 'DELETE':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be DELETE'})
    if request.GET.get('id') is not None:
        dealer = Dealer.objects.filter(id=request.GET['id'][0])
        if len(dealer) == 1:
            dealer[0].delete()
        elif len(dealer) == 0:
            return JsonResponse(status=400, data={'success': False, 'error': 'id: {} does not exist'.format(request.GET.get('id'))})
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'To delete dealer, need to add param id'})
    return JsonResponse(status=200, data={'success': True})



@csrf_exempt
def update_dealer(request):
    if request.method != 'POST':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be POST'})
    if request.GET.get('id') is not None:
        dealer = Dealer.objects.filter(id=request.GET.get('id'))
        if len(dealer) == 1:
            update_fields = []
            for key in request.POST:
                update_fields.append(key)
                if key == 'ogrn':
                    if request.POST[key].isdigit():
                        dealer[0].ogrn = request.POST[key]
                    else:
                        return JsonResponse(status=400, data={'success': False, 'error': 'ogrn must be integer'})
                elif key == 'name':
                    if len(request.POST[key][0]) <= 300:
                        dealer[0].name = request.POST[key]
                elif key == 'city':
                    if len(request.POST[key][0]) <= 300:
                        dealer[0].city = request.POST[key]
                elif key == 'address':
                    if len(request.POST[key][0]) <= 500:
                        dealer[0].address = request.POST[key]
            try:
                dealer[0].save(update_fields=update_fields)
            except IntegrityError:
                return JsonResponse(status=400, data={'success': False, 'error': 'ogrn must be unique'})
        elif len(dealer) == 0:
            return JsonResponse(status=400,
                                data={'success': False, 'error': 'id: {} does not exist'.format(request.GET.get('id'))})
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'To update dealer, need to add param id'})
    return JsonResponse(status=200, data={'success': True, 'new_dealer': {'id': dealer[0].id,
                                                                          'ogrn': dealer[0].ogrn,
                                                                          'name': dealer[0].name,
                                                                          'city': dealer[0].city,
                                                                          'address': dealer[0].address}})


@csrf_exempt
def get_dealer(request):
    if request.method != 'GET':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be GET'})
    if request.GET.get('id') is not None:
        dealer = Dealer.objects.filter(id=request.GET.get('id'))
        if len(dealer) == 1:
            return JsonResponse(status=200, data={'success': True, 'dealer': {'id': dealer[0].id,
                                                                              'ogrn': dealer[0].ogrn,
                                                                              'name': dealer[0].name,
                                                                              'city': dealer[0].city,
                                                                              'address': dealer[0].address}})
        elif len(dealer) == 0:
            return JsonResponse(status=400,
                                data={'success': False, 'error': 'id: {} does not exist'.format(request.GET.get('id'))})
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'To update dealer, need to add param id'})


@csrf_exempt
def create_auto(request):
    if request.method != 'POST':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be POST'})
    post_body = dict(request.POST)
    try:
        dealer = Dealer.objects.filter(id=post_body['dealer'][0])
        if len(dealer) == 1:
            dealer = Dealer.objects.filter(id=post_body['dealer'][0])[0]
        elif len(dealer) == 0:
            return JsonResponse(status=400, data={'success': False, 'error': 'Dealer with this id is not exist'})
        auto = Auto(car_brand=post_body['car_brand'][0], model_name=post_body['model_name'][0],
                    vin=post_body['vin'][0], top_speed=post_body['top_speed'][0], weight=post_body['weight'][0],
                    mileage=post_body['mileage'][0], horsepower=post_body['horsepower'][0], dealer=dealer)
        try:
            auto.clean()
        except ValidationError as e:
            return JsonResponse(status=400, data={'success': False, 'error': str(e)})
    except KeyError as e:
        return JsonResponse(status=400, data={'success': False, 'error': 'request must contain {}'.format(str(e))})
    if len(Auto.objects.filter(vin=auto.vin)) == 0:
        auto.save()
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'vin must be unique'})
    return JsonResponse(status=200, data={'success': True, 'auto_id': auto.id})


@csrf_exempt
def delete_auto(request):
    if request.method != 'DELETE':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be DELETE'})
    if request.GET.get('id') is not None:
        auto = Auto.objects.filter(id=request.GET.get('id'))
        if len(auto) == 1:
            auto[0].delete()
        else:
            return JsonResponse(status=400,
                                data={'success': False, 'error': 'id: {} does not exist'.format(request.GET.get('id'))})
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'To delete dealer, need to add param id'})
    return JsonResponse(status=200, data={'success': True})


@csrf_exempt
def update_auto(request):
    if request.method != 'POST':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be POST'})
    if request.GET.get('id') is not None:
        auto = Auto.objects.filter(id=request.GET.get('id'))
        if len(auto) == 1:
            update_fields = []
            for key in request.POST:
                update_fields.append(key)
                if key == 'car_brand':
                    auto[0].car_brand = request.POST[key]
                elif key == 'model_name':
                    auto[0].model_name = request.POST[key]
                elif key == 'vin':
                    auto[0].vin = request.POST[key]
                elif key == 'top_speed':
                    auto[0].top_speed = request.POST[key]
                elif key == 'weight':
                    auto[0].weight = request.POST[key]
                elif key == 'mileage':
                    auto[0].mileage = request.POST[key]
                elif key == 'horsepower':
                    auto[0].horsepower = request.POST[key]
                elif key == 'dealer':
                    if request.POST[key].isdigit():
                        dealer = Dealer.objects.filter(id=request.POST[key])
                        if len(dealer) == 1:
                            dealer = dealer[0]
                        else:
                            return JsonResponse(status=400, data={'success': False, 'error': 'Dealer id is not exist'})
                        auto[0].dealer = dealer
                    else:
                        return JsonResponse(status=400, data={'success': False, 'error': 'dealer id must be integer'})
            try:
                try:
                    auto[0].clean()
                except ValidationError as e:
                    return JsonResponse(status=400, data={'success': False, 'error': str(e)})
                auto[0].save(update_fields=update_fields)
            except IntegrityError:
                return JsonResponse(status=400, data={'success': False, 'error': 'vin must be unique'})
        elif len(auto) == 0:
            return JsonResponse(status=400,
                                data={'success': False, 'error': 'id: {} does not exist'.format(request.GET.get('id'))})
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'To update auto, need to add param id'})
    return JsonResponse(status=200, data={'success': True, 'new_auto': {'id': auto[0].id,
                                                                        'car_brand': auto[0].car_brand,
                                                                        'model_name': auto[0].model_name,
                                                                        'vin': auto[0].vin,
                                                                        'top_speed': auto[0].top_speed,
                                                                        'weight': auto[0].weight,
                                                                        'mileage': auto[0].mileage,
                                                                        'horsepower': auto[0].horsepower,
                                                                        'dealer_id': auto[0].dealer.id}})


@csrf_exempt
def get_auto(request):
    if request.method != 'GET':
        return JsonResponse(status=405, data={'success': False, 'error': 'request must be GET'})
    if request.GET.get('id') is not None:
        auto = Auto.objects.filter(id=request.GET.get('id'))
        if len(auto) == 1:
            return JsonResponse(status=200, data={'success': True, 'auto': {'id': auto[0].id,
                                                                            'car_brand': auto[0].car_brand,
                                                                            'model_name': auto[0].model_name,
                                                                            'vin': auto[0].vin,
                                                                            'top_speed': auto[0].top_speed,
                                                                            'weight': auto[0].weight,
                                                                            'mileage': auto[0].mileage,
                                                                            'horsepower': auto[0].horsepower,
                                                                            'dealer_id': auto[0].dealer.id}})
        elif len(auto) == 0:
            return JsonResponse(status=400,
                                data={'success': False, 'error': 'id: {} does not exist'.format(request.GET.get('id'))})
    else:
        return JsonResponse(status=400, data={'success': False, 'error': 'To update auto, need to add param id'})
