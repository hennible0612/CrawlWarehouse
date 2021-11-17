from django.core.management.base import BaseCommand
import pandas as pd
from board.models import MallBoard
import csv
import os



class Command(BaseCommand):
    def handle(self, *args, **options):
        from board.models import MallBoard
        with open('mall.csv', encoding='UTF8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = MallBoard(name=row.name, age=row['age'], mySelf=row['mySelf'], job=row['job'])
                p.save()
