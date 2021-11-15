import pandas as pd
from django.core.management.base import BaseCommand
from esm.models import Esm
from esm.models import Tmon
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = 'A command to add data from and csv file to database'

    def handle(self, *args, **options):
        csv_file = 'esm.csv'
        df = pd.read_csv(csv_file)

        engine = create_engine('sqlite:///db.sqlite3')
        # df = df.drop('del', axis=1)

        df.to_sql(Esm._meta.db_table, con=engine, if_exists='replace',index=True )


    # def handle(self, *args, **options):
    #     csv_file = 'esm.csv'
    #     df = pd.read_csv(csv_file)
    #
    #     engine = create_engine('sqlite:///db.sqlite3')
    #
    #     df.to_sql(Esm._meta.db_table, con=engine, if_exists='replace',index=True )
    #
