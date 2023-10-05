#!/usr/bin/python3
import os
import shutil

# Указываем путь к директории, в которой будем искать фотографии
source_dir = "/Users/radmilginiatullin/Desktop/exit"

# Указываем путь к директории, в которую будем переносить фотографии
destination_dir = "/Users/radmilginiatullin/Desktop/new_2"

# Счетчик для переименования файлов
counter = 1

# Перебираем все дни в исходной директории
for day_dir in sorted(os.listdir(source_dir)):
    day_path = os.path.join(source_dir, day_dir)
    print(f"День - {day_dir}")
    
    # Проверяем, является ли текущий элемент директорией
    if not os.path.isdir(day_path):
        continue
    
    # Путь к папке "001" внутри текущего дня
    sub_dir_path = os.path.join(day_path, "001")
    
    # Проверяем, существует ли папка "001"
    if not os.path.exists(sub_dir_path):
        continue
    
    # Путь к папке "jpg" внутри папки "001"
    jpg_dir_path = os.path.join(sub_dir_path, "jpg")
    
    # Проверяем, существует ли папка "jpg"
    if not os.path.exists(jpg_dir_path):
        continue
    
    # Перебираем все подпапки внутри папки "jpg"
    for hour_dir in sorted(os.listdir(jpg_dir_path)):
        hour_path = os.path.join(jpg_dir_path, hour_dir)

        # Удаляем файл .DS_Store, если он есть
        ds_store_path = os.path.join(hour_path, ".DS_Store")
        if os.path.exists(ds_store_path):
            os.remove(ds_store_path)
            print(f"Удален файл .DS_Store в {hour_path}")

        print(f"Час - {hour_dir}")
        
        # Проверяем, является ли текущий элемент директорией
        if not os.path.isdir(hour_path):
            continue
        
        # Перебираем все файлы внутри текущей подпапки
        for file_name in sorted(os.listdir(hour_path)):
            file_path = os.path.join(hour_path, file_name)
            
            # Проверяем, является ли текущий элемент файлом формата jpg
            if not file_name.endswith(".jpg"):
                continue
            
            # Переносим файл в конечную директорию и переименовываем его
            new_file_name = str(counter) + ".jpg"
            new_file_path = os.path.join(destination_dir, new_file_name)
            shutil.copy(file_path, new_file_path)
            print(f"Копирую - {file_name} - {new_file_name}")
            
            # Увеличиваем счетчик для следующего файла
            counter += 1