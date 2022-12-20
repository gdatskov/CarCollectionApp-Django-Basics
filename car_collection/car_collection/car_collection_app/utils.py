from car_collection.car_collection_app.models import Profile


def get_profile():
    try:
        return Profile.objects.last()
    except:
        return None