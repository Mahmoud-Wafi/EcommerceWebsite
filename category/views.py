from django.shortcuts import render
from .models import Category
# from django.shortcuts import render, get_object_or_404
# from .models import Category
# from product.models import Product
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.http import Http404
# from django.views.decorators.cache import cache_page
# from django.conf import settings
# from django.utils.decorators import method_decorator
# from django.views import View
# from django.views.generic import ListView, DetailView
# from django.utils.text import slugify
# from django.urls import reverse
# from django.http import HttpResponseRedirect
# from django.contrib import messages
# from django.utils import timezone
# from django.core.cache import cache
# from django.views.decorators.vary import vary_on_cookie
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.http import require_GET
# from django.utils.translation import gettext as _
# from django.utils.translation import get_language   


def category_list(request):
    
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'category.html', {'category': category})
            