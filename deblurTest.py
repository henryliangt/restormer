import os


folder = "./demo/degraded1"
image = "./demo/degraded1/tile__1a8e337b-7a14-56a8-b60d-553233d59b49.png"
print(os.listdir(folder))
print(os.path.exists(image))

# python demo.py --task Task_Name --input_dir path_to_images --result_dir save_images_here

# python demo.py --task Single_Image_Defocus_Deblurring --input_dir './demo/degraded/' --result_dir './demo/restored/'

# python demo.py --task Single_Image_Defocus_Deblurring --input_dir ./demo/degraded/ --result_dir ./demo/restored/
# python demo.py --task Single_Image_Defocus_Deblurring --input_dir ./demo/degraded1/ --result_dir ./demo/restored1/

# python demo.py --task Single_Image_Defocus_Deblurring --input_dir './demo/degraded/portrait.jpg' --result_dir './demo/restored/'




