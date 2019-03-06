import sys
import json
import argparse

from blocks2go.comm import open_pyscard, open_pyscard_autoreader, CardError
from blocks2go.commands import select_app

def _card_info(args):
	if args.reader is not None:
		reader = open_pyscard(args.reader)
	else:
	    (reader, _) = open_pyscard_autoreader()

	(pin_active, card_id, version) = select_app(reader)

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