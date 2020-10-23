# from django.db import connection
# from django.core.signals import request_finished
# from django.dispatch import receiver
# from .models import Cloth

# @receiver (pre_save, sender=Cloth)
# def cloth_pre_save(sender, **kwargs) :
#     image = kwargs['instance'].clothImage
#     sleeveType = kwargs['instance'].sleeveType
#     pantsType = kwargs['instance'].pantsType
#     print(sender.clothImage)

#     if (sleeveType and not pantsType) :
#         for field in sender.meta.fields :
#             if field.name == 'clothImage' :
#                 field.upload_to = 'cloth/sleeve'
#         super(Cloth, sender)
#         print(image.upload_to)
#     elif (pantsType and not sleeveType) :
#         for field in sender.meta.fields :
#             if field.name == 'clothImage' :
#                 field.upload_to = 'cloth/pants'
#         super(Cloth, sender)

#     else :
#         raise InterruptedError



from django.core.signals import request_finished
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .models import ViewOfUser
from mypage.models import CustomUser
from .views import selectCloth

@receiver(request_finished, sender=selectCloth)
def callback_to_selectCloth(sender, **kwargs) :
    if sender.request.method == 'POST' and sender.request.user :
        view = ViewOfUser.objects.filter(product = sender.cloth)
        if not view :
            user = CustomUser.objects.get(id=sender.request.user.id)
            view = ViewOfUser(
                users = user,
                product = sender.cloth 
            )
            view.save()
        else :
            view.look += 1
            view.save()
    else :
        pass