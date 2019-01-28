import sys
import json
import argparse

from blockchain2go.comm import open_pyscard, CardError
from blockchain2go.commands import select

def _card_info(args):
  reader = open_pyscard(args.reader)
  (pin_active, card_id, version) = select(reader)

  if args.machine_readable:
    json.dump({
      'status': 'success',
      'pin_active': pin_active,
      'card_id': card_id.hex(),
      'version': version}, fp=sys.stdout)
  else:
    print('PIN is: ' + ('ENABLED' if pin_active else 'disabled'))
    print('Card ID (hex): ' + card_id.hex())
    print('Version: ' + version)

def add_subcommand(subparsers):
  parser = subparsers.add_parser('card_info', description='Retrieve card information')
  parser.set_defaults(func=_card_info)