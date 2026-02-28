from PIL import Image, ImageDraw

def create_image(filename, text, size=(800, 600), bg_color="#F5F2EB", text_color="#333333"):
    img = Image.new('RGB', size, color=bg_color)
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, size[0]-10, size[1]-10], outline="#B09B84", width=4)
    img.save(filename)
    print(f"Created {filename}")

create_image("manga_concept_1.png", "ビジネスマンガの事例・イメージ 1")
create_image("manga_concept_2.png", "ビジネスマンガの事例・イメージ 2")
