from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from home import models


def get_backgrounds():
    result = {}
    for place in models.BACKGROUND_PLACES:
        try:
            p = models.Background.objects.filter(place=place[0]).latest()
        except:
            pass
        else:
            result.update({
                place[0]: p.resized_image.url
            })
    return result

def send_contact_email(request):
    send_mail(
        '[Contato do EstudioLapa.com] - Mensagem de %(name)s' % request.POST,
        u'''
        Olá,

        Alguém enviou uma mensagem através do site:

        Remetente: %(name)s

        Email: %(email)s

        Mensagem: %(message)s

        Att,
        Adminstrador
        ''' % request.POST, settings.EMAIL_HOST_USER,
        ['contato@estudiolapa.com'], fail_silently=False
    )
    messages.success(request, 'E-mail de contanto enviado com sucesso.')


def home(request):
    context = {
        'categories': models.Category.objects.all(),
        'works': models.Work.objects.order_by('-updated_at'),
        'backgrounds': get_backgrounds()
    }

    if request.method == 'POST':
        send_contact_email(request)

    return render(request, 'home.html', context)
