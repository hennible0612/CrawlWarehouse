import pandas as pd
from django.core.management.base import BaseCommand
from sqlalchemy import create_engine

from mallboard.models import Coupang


class Command(BaseCommand):
    help = 'A command to add data from and csv file to database'

    def handle(self, *args, **options):
        print('hello hello hello 안녕 안녕하')

