from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AccountOne, AccountThree, AccountTwo


def get_app_one_childs(email, out=[]):
    childs = AccountOne.objects.filter(parent__email=email)
    if not childs.exists():
        return
    for child in childs:
        out.append(child.email)
        get_app_one_childs(child.email, out)


@api_view(['GET',])
def app_one_view(request):
    data = request.GET
    email = data.get('email', None)
    count_of_child = 0
    out = []
    if email:
        acc = AccountOne.objects.filter(email=email).last()
        if acc and acc.left_child:
            out.append(acc.left_child.email)
            get_app_one_childs(acc.left_child.email, out)
            count_of_child = len(out)
    else:
        accounts = AccountOne.objects.all()
        count_of_child = accounts.count()

    return Response({'count': count_of_child})


def get_app_two_childs(email, out=[]):
    account = AccountTwo.objects.get(email=email)
    child = account.left_child
    if child:
        out.append(child.email)
        get_app_two_childs(child.email, out)
    child = account.right_child
    if child:
        out.append(child.email)
        get_app_two_childs(child.email, out)


@api_view(['GET',])
def app_two_view(request):
    data = request.GET
    email = data.get('email', None)
    count_of_child = 0
    out = []
    if email:
        acc = AccountTwo.objects.filter(email=email).last()
        if acc:
            get_app_two_childs(email, out)
            count_of_child = len(out)
    else:
        accounts = AccountTwo.objects.all()
        count_of_child = accounts.count()

    return Response({'count': count_of_child})


def get_app_three_childs(email, out=[]):
    childs = AccountOne.objects.filter(parent__email=email)
    if not childs.exists():
        return
    for child in childs:
        out.append(child.email)
        get_app_one_childs(child.email, out)


@api_view(['GET',])
def app_three_view(request):
    data = request.GET
    email = data.get('email', None)
    count_of_child = 0
    out = []
    if email:
        acc = AccountThree.objects.filter(email=email).last()
        if acc:
            get_app_three_childs(email, out)
            count_of_child = len(out)
    else:
        accounts = AccountThree.objects.all()
        count_of_child = accounts.count()

    return Response({'count': count_of_child})
