from django import forms
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.decorators import login_required as log_req

class AddObjectXToObjectY(object):
    """
    This is an object view which allows you to set a field on an 
    Object Y to a newly created Object X.
    """
    def __init__(self, classx, classy, form_class=None, attr=None):
        self.classx = classx
        self.classy = classy
        if form_class:
            self.form_class = form_class
        else:
            self.form_class = forms.models.modelform_factory(self.classx)
        if attr:
            self.attr = attr
        else:
            self.attr = '%s_set' % self.classx.__name__.lower()

    def __repr__(self):
        return "Add %s to %s" % (self.classx.__name__, self.classy.__name__)

    def __call__(self, request, *args, **kwargs):
        return self.view(request, *args, **kwargs)

    def view(self, request, *args, **kwargs):
        object_id = kwargs['object_id']
        objecty = self.classy.objects.get(id=object_id)
        if request.method == "POST":
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                objectx = form.save(commit=False)
                objy_attr = getattr(objecty, self.attr)
                objy_attr.add(objectx)
                objectx.save()
                objecty.save()
                return redirect(objectx.get_absolute_url())
        else:
            form = self.form_class()

        context = {
            'form': form,
            'classx_name': self.classx.__name__,
            'classy_name': self.classy.__name__,
            'objecty': objecty,
            'bctxt': 'Add %s' % self.classx.__name__,
        }
        return render_to_response('AddXToY.html', context, 
                                context_instance=RequestContext(request))

