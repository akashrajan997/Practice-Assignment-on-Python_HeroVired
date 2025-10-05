import tempfile
import os
import shutil
import importlib.util

SRC = tempfile.mkdtemp(prefix='src_')
DST = tempfile.mkdtemp(prefix='dst_')
print('src', SRC)
print('dst', DST)
open(os.path.join(SRC, 'test.txt'), 'w').write('hello')

backup_path = 'd:/Vlearn/Practice-Assignment-on-Python_HeroVired/Q4_File_Backup/backup.py'
spec = importlib.util.spec_from_file_location('backup_mod', backup_path)
backup_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backup_mod)

backup_mod.backup_files(SRC, DST)
print('dst files:', os.listdir(DST))

# cleanup
shutil.rmtree(SRC)
shutil.rmtree(DST)
