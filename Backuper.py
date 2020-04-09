# Решил написать бекапер для сохранений игры, с помощью pyinstaler превратил Beckup.py в exe
# ( При этом выставлял --noconsole ) и запускал его через Планировщик заданий При этом еще сделал
# что если собираеться больше 10 бекапов последний стираеться
import os
import time

source = [r'"C:\Users\Alex\Documents\My Games\Grim Dawn"']
target_dir = r'C:\Users\Alex\Desktop\BeckupGrim'
CountBackups = os.listdir(path=target_dir)
if len(CountBackups) > 10:
    os.remove("{}\{}".format(target_dir, CountBackups[0]))
target = target_dir + os.sep + time.strftime('%Y.%m.%d_') + time.strftime('%H.%M.%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

if __name__ == "__main__":
    time.sleep(3)
