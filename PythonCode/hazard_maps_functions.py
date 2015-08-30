
hc_plots = """HazardCurveFarCascacadiaAll_GridPoint_019084.png
HazardCurveFarCascacadiaAll_GridPoint_019192.png
HazardCurveFarCascacadiaAll_GridPoint_019300.png
HazardCurveFarCascacadiaAll_GridPoint_019516.png
HazardCurveFarCascacadiaAll_GridPoint_019624.png
HazardCurveFarCascacadiaAll_GridPoint_019732.png
HazardCurveFarCascacadiaAll_GridPoint_043650.png
HazardCurveFarCascacadiaAll_GridPoint_057513.png
HazardCurveFarCascacadiaAll_GridPoint_086900.png
HazardCurveFarCascacadiaAll_GridPoint_093474.png
HazardCurveFarCascacadiaAll_GridPoint_130150.png
HazardCurveFarCascacadiaAll_GridPoint_130200.png
HazardCurveFarCascacadiaAll_GridPoint_130250.png
HazardCurveFarCascacadiaAll_GridPoint_130300.png
HazardCurveFarCascacadiaAll_GridPoint_130350.png
HazardCurveFarCascacadiaAll_GridPoint_140184.png
HazardCurveFarCascacadiaAll_GridPoint_176862.png""".split()
n_hc_plots = len(hc_plots)
hc_dir = '/Users/rjl/student_workshop/Realizations/HC_SAMEGRAPH'

hmax_plots = """AASZe01r01/tide+077/depth-contours_map.png
AASZe03r01/tide+077/depth-contours_map.png
AASZe05r01/tide+077/depth-contours_map.png
CSZRe01r01/tide+077/depth-contours_map.png
CSZRe02r01/tide+077/depth-contours_map.png
CSZRe03r01/tide+077/depth-contours_map.png
CSZRe04r01/tide+077/depth-contours_map.png
CSZRe05r01/tide+077/depth-contours_map.png
KmSZe09r01/tide+077/depth-contours_map.png
KrSZe12r01/tide+077/depth-contours_map.png
SChSZe14r01/tide+077/depth-contours_map.png
TOHe01r03/tide+077/depth-contours_map.png""".split()
n_hmax_plots = len(hmax_plots)
hmax_dir = '/Users/rjl/student_workshop/Realizations'

hmax_small_plots = """AASZe01r01/tide+077/depth-contours_small_map.png
AASZe03r01/tide+077/depth-contours_small_map.png
AASZe05r01/tide+077/depth-contours_small_map.png
CSZRe01r01/tide+077/depth-contours_small_map.png
CSZRe02r01/tide+077/depth-contours_small_map.png
CSZRe03r01/tide+077/depth-contours_small_map.png
CSZRe04r01/tide+077/depth-contours_small_map.png
CSZRe05r01/tide+077/depth-contours_small_map.png
KmSZe09r01/tide+077/depth-contours_small_map.png
KrSZe12r01/tide+077/depth-contours_small_map.png
SChSZe14r01/tide+077/depth-contours_small_map.png
TOHe01r03/tide+077/depth-contours_small_map.png""".split()
n_hmax_small_plots = len(hmax_plots)
hmax_small_dir = '/Users/rjl/student_workshop/Realizations'

p_contours_plots = """
p-contours_zeta_00000.png
p-contours_zeta_00050.png
p-contours_zeta_00100.png
p-contours_zeta_00200.png
p-contours_zeta_00300.png""".split()
p_contours_dir = '/Users/rjl/student_workshop/Realizations/ALL_CSZR'

zeta_contours_plots = """
zeta-contours_prob_0002.png
zeta-contours_prob_0004.png
zeta-contours_prob_001026.png
zeta-contours_prob_002.png
zeta-contours_prob_00333.png
zeta-contours_prob_010.png""".split()
zeta_contours_dir = '/Users/rjl/student_workshop/Realizations/ALL_CSZR'


def make_show_image(images, image_dir='.', width=500):
    def show_image(k):
        from IPython.display import Image, display
        import os  
        file_path = os.path.join(image_dir, images[k])
        display(Image(file_path,width=width))
        print images[k]
    return show_image

#interact(show_image,k=(0,n_images-1))
