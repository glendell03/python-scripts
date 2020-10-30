import os, shutil


class Automate:
    def __init__(self):
        self.download_dir = "/home/glendell03/Downloads/"
        self.home_dir = "/home/glendell03/"
        self.path = ""

    def create_dir(self, dir):
        if not os.path.exists(dir):
            try:
                self.path = os.path.join(self.home_dir, dir)
                os.makedirs(self.path)
                print("Directory '{}' create".format(dir))
            except:
                self.path = os.path.join(self.home_dir, dir)
                print("Successfully Move to {} directory".format(dir))
        return dir
    
    def move(self, file_extension):
        os.chdir(self.download_dir)
        for file in os.listdir(self.download_dir):
            if file.endswith(file_extension):
                path_current = os.path.join(self.download_dir, file)
                shutil.move(path_current, self.path)
        return file_extension

    def move_photo(self):
        self.create_dir("Photos")
        file_extensions = (".jpeg", ".jpg", ".png")
        self.move(file_extensions)

    def move_documents(self):
        file_extensions = (".docx", ".pdf")
        self.create_dir("Documents")
        self.move(file_extensions)

    def move_custom_icons(self):
        self.create_dir("Custom Icons")
        self.move(".icns")


if __name__ == "__main__":
    not_number = True

    while not_number:
        print("Which file do you like me to move?")
        print("[1] Photos")
        print("[2] Documents")
        print("[3] Icons")
        user = input("Enter a number: ")

        try:
            val = int(user)

            if val == 1:
                move_photo = Automate()
                move_photo.move_photo()
            elif val == 2:
                move_documents = Automate()
                move_documents.move_documents()
            elif val == 3:
                move_custom_icons = Automate()
                move_custom_icons.move_custom_icons()
            not_number = False
            
        except ValueError:
            print()