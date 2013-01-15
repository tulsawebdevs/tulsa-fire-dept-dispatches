from django.core.management.base import BaseCommand, CommandError

from dispatches.models import Dispatch



class Command(BaseCommand):
    help = 'Test dispatch notification'
    
    
    def handle(self, *args, **options):
        
        dispatch = Dispatch.objects.get(tf='2013001272') 
        
        dispatch.notify_listeners()


# '2013001118'

# 2013001272