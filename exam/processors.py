from exam.fruitipedia_app.models import ProfileModel


def get_profile(request):
    profile = ProfileModel.objects.first()
    return {'profile': profile}