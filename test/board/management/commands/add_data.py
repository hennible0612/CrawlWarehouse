from django.core.management.base import BaseCommand
import pandas as pd
from board.models import MallBoard

class Command(BaseCommand):
    help = "a Command to add data from"
    def handle(self, *args, **options):
        df = pd.read_csv('mall.csv')



