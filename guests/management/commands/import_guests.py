from django.core.management import BaseCommand
from guests import csv_import


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        csv_import.import_guests(filename)
