import zipfile

zip_file = zipfile.ZipFile('../data/zip_archive.zip', 'w')
zip_file.write('../data/textfile_for_zip_01.txt')
zip_file.write('../data/textfile_for_zip_02.txt')
zip_file.write('../data/textfile_for_zip_03.txt')
# zip_file.close()
#
# print(zipfile.is_zipfile('../data/zip_archive.zip'))
# zip_file = zipfile.ZipFile('../data/zip_archive.zip')
# print(zip_file.namelist())
# print(zip_file.infolist())
#
# zip_info = zip_file.getinfo('../data/textfile_for_zip_02.txt')
# print(zip_info.file_size)
# print(zip_file.read('../data/textfile_for_zip_01.txt'))
zip_file.extract('../data/textfile_for_zip_02.txt')
zip_file.extractall()
zip_file.close()
