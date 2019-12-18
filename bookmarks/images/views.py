from pdb import set_trace as debug

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ImageCreateForm


@login_required
def image_create(request):
    """Create an image."""
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # Assign current user to the image.
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # Redirect user to new created image detail view.
            return redirect(new_item.get_absolute_url())
    else:
        # Initial data is the url and title of an image from an external website as provided by our JavaScript tool.
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})
