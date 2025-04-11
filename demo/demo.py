import os
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="OCR")

pic_dir = "./pic"
res_idr = "./output"
os.makedirs(pic_dir, exist_ok=True)


for pic in os.listdir(pic_dir):
    if pic.endswith(".jpg") or pic.endswith(".png"):
        output = pipeline.predict(
            input=os.path.join(pic_dir, pic),
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
        )
        for res in output:
            res.print()
            res.save_to_img(save_path="./output/")
            res.save_to_json(save_path="./output/")
            print(res.json['res']['rec_texts'])