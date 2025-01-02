from PIL import Image, ImageTk

class UserInformationClasses2:
    @staticmethod
    def load_profile_image():
        profile_image_path = 'C:\\Users\\acer\\Desktop\\useraccount.png'
        try:
            profile_image = Image.open(profile_image_path)
            profile_image = profile_image.resize((120, 120))
            return ImageTk.PhotoImage(profile_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
