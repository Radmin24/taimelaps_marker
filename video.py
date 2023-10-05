#!/usr/bin/python3
import cv2
import os

# Указываем путь к папке с фотографиями
path = "/Users/radmilginiatullin/Desktop/new_2"

# Получаем список файлов в папке
files = os.listdir(path)

# Сортируем файлы по имени
sorted_files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))

# Указываем размеры видео и частоту кадров
fps = 24
width = 1920    
height = 1080


# Создаем объект VideoWriter для записи видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('/Users/radmilginiatullin/Desktop/timelaps_new.mp4', fourcc, fps, (width, height))

# Проходимся по списку файлов и добавляем их в видео
for file in files:
    # Удаляем файл .DS_Store, если он есть
    ds_store_path = os.path.join(path, '.DS_Store')
    if os.path.exists(ds_store_path):
        os.remove(ds_store_path)
        print(f"Удален файл .DS_Store в {path}")
        
    print(f"Фаил: {file}")
    img = cv2.imread(os.path.join(path, file))
    video.write(img)

# Освобождаем ресурсы и закрываем видео
cv2.destroyAllWindows()
video.release()
