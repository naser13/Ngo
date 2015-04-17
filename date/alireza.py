from src.Ngo.persons.models import NGO
def say_hello(request):
        return {
            'america': NGO.objects.filter(continent='am'),
            'europe': NGO.objects.filter(continent='er'),
            'africa': NGO.objects.filter(continent='af'),
            'australia': NGO.objects.filter(continent='au'),
            'asia': NGO.objects.filter(continent='as'),
            'say_hello': "Hello",
        }