from rename_files import rename_files

if __name__ == "__main__":
    download_directory_path = input("Please enter download directory path: ")
    file_names = input("Please enter file_names.txt path: ")
    rename_files(download_directory_path, file_names)
