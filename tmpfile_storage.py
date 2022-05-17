
'''
Write a tool that can be called in CLI with 
  --key <name of key>, where "key" is key in JSON or dict
  --val <value>, where "val" is the value to store.
  
If the tool is called with --key only, the output is the value stored in this key.
If --val is given add a <value> to key(not overriding its previous content)
  

Вашей задачей будет написать реализацию утилитыstorage.py.

Утилита может вызваться со следующими параметрами:

--key <имя ключа> , где <имя ключа> - ключ по которому сохраняются/получаются значения

--val <значение>, где <значение> - сохраняемое значение.

Если при запуске утилиты переданы оба ключа, происходит добавление переданного значения по ключу и сохранение данных в файле.
 Если передано только имя ключа, происходит чтение файла хранилища и вывод на печать значений, которые были сохранены по данному ключу. 
  Обратите внимание, что значения по одному ключу не перезаписываются, а добавляются к уже сохраненным. Другими словами - 
по одному ключу могут храниться несколько значений. При выводе на печать, значения выводятся в порядке их добавления в хранилище.
'''

import os
import tempfile
import argparse
import json


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--key", help="The dictionary key to fetch or insert a value")
	parser.add_argument("--val", help="The value to store")
	args = parser.parse_args()

	if args.key and args.val:
		#print("Store value into a file")
		#print(f'Calling function store_value({args.key},{args.val},{f})')
		store_value(args.key, args.val, f)
	elif args.key:
		#print('Fetch value(s) from file')
		fetch_value(args.key, f)
	else:
		print("Arguments are required\n   Example:\n   ./storage.py --key key_value --val value(optional)")
		exit()


def temp_file():
	if not os.path.exists(tempfile.gettempdir()+'/storage.data'):
		f = open(tempfile.gettempdir()+'/storage.data','w')
		json.dump(dict(),f)
		f.flush()
		f.close()
	f = open(tempfile.gettempdir()+'/storage.data', 'r+')	
	return f


def store_value(key, value, f):
	#print(f'{key} - {value} will be written to {f}')
	# add values

	mystorage = json.load(f)
	#print(f'Key is {key}, value is {value} and file is {f}. And type of storage is {type(mystorage)}\n\n\n\n\n')
	if key in mystorage:
		mystorage[key].append(value)
	else:
		mystorage[key] = [value,]
	#print(f'mystorage is {type(mystorage)}')
	f.seek(0)
	json.dump(mystorage,f)
	f.truncate()
	f.close()
	

def fetch_value(key, f):
	#print(f'Fetch value(s) with key - {key} from {f}')
	mystorage = json.load(f)
	if mystorage.get(key) == None:
		print('None')
	elif isinstance(mystorage[key], list):
		print(', '.join(mystorage.get(key)))
	else:
		print(None)
	f.close()

	
if __name__ == '__main__': 
	f = temp_file()
	get_args()
	
	
