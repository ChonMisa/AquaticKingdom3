def fish_upload(instance, filename):
    return f'fish_images/{instance.fish.id}/{filename}'


def accessories(instance, filename):
    return f'accessory_images/{instance.id}/{filename}'


def upload_avatar_for_user(instance, filename):
    return f'upload_avatar_for_user/{instance.id}/{filename}'


def fish_food_images(instance, filename):
    return f'ffood_images/{instance.id}/{filename}'
