from django.shortcuts import render
from django.core.exceptions import PermissionDenied

""" Error handling """


def handler404(request, exception):
    """Function to render the 404 page."""
    return render(request, '404.html', status=404)


def handler500(request):
    """ Function to render the 500 page."""
    return render(request, '500.html', status=500)


def handler403(request, exception):
    """Function to render the 403 page."""
    if isinstance(exception, PermissionDenied):
        return render(request, '403.html', status=403)
    else:
        # Handle unexpected errors with a generic 500 error page
        return render(request, '500.html', status=500)