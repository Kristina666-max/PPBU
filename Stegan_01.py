from PIL import Image
import stepic


def encode_text(image_path, text, output_path):
    image = Image.open(image_path)
    encoded_image = stepic.encode(image, text.encode())
    encoded_image.save(output_path)

encode_text("C:\\Users\\89096\\OneDrive\\Изображения\\image_1.jpg", 'Parol 100500%@', 'encoded_image.png')
print('Текст скрыт в изображении')

