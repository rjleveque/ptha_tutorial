
"""
Make lists of plots to display in notebooks.
"""

import os,sys

data_dir = os.path.abspath('../DataFiles')

events_dir = os.path.join(data_dir, 'Events')

sample_dir = os.path.join(data_dir, 'SampleResults')

all_events = ['AASZa', 'AASZb', 'AASZc', 'AASZd', 'CSZa', 'CSZb', 'CSZc', 'CSZd', 'CSZe', \
              'CSZf', 'KmSZa', 'KrSZa', 'SChSZa', 'TOHa']
hmax_plots = []
for event in all_events:
    hmax_plots.append(os.path.join(events_dir, event, 'depth-contours_map.png'))

hc_split_plots = """HazardCurveFarCascacadiaAll_GridPoint_019084.png
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

hc_split_plots = [os.path.join(sample_dir, hc) for hc in hc_split_plots]

    
hc_plots = """
HazardCurve_WaveHt_GridPoint_019516.png
HazardCurve_WaveHt_GridPoint_043640.png
HazardCurve_WaveHt_GridPoint_057513.png
HazardCurve_WaveHt_GridPoint_086900.png
HazardCurve_WaveHt_GridPoint_130150.png
HazardCurve_WaveHt_GridPoint_130200.png
HazardCurve_WaveHt_GridPoint_130250.png
HazardCurve_WaveHt_GridPoint_130300.png
HazardCurve_WaveHt_GridPoint_130350.png
HazardCurve_WaveHt_GridPoint_130937.png
HazardCurve_WaveHt_GridPoint_152611.png
HazardCurve_WaveHt_GridPoint_176862.png
HazardCurve_Zeta_GridPoint_019516.png
HazardCurve_Zeta_GridPoint_043640.png
HazardCurve_Zeta_GridPoint_057513.png
HazardCurve_Zeta_GridPoint_086900.png
HazardCurve_Zeta_GridPoint_130150.png
HazardCurve_Zeta_GridPoint_130200.png
HazardCurve_Zeta_GridPoint_130250.png
HazardCurve_Zeta_GridPoint_130300.png
HazardCurve_Zeta_GridPoint_130350.png
HazardCurve_Zeta_GridPoint_130937.png
HazardCurve_Zeta_GridPoint_152611.png
HazardCurve_Zeta_GridPoint_176862.png""".split()

hc_plots = [os.path.join(sample_dir, hc) for hc in hc_plots]

p_contours_plots = """
p-contours_zeta_00000.png
p-contours_zeta_00050.png
p-contours_zeta_00100.png
p-contours_zeta_00200.png
p-contours_zeta_00300.png""".split()

p_contours_plots = [os.path.join(sample_dir, p) for p in p_contours_plots]

zeta_contours_plots = """
zeta-contours_prob_0002.png
zeta-contours_prob_0004.png
zeta-contours_prob_001026.png
zeta-contours_prob_002.png
zeta-contours_prob_00333.png
zeta-contours_prob_010.png""".split()

zeta_contours_plots = [os.path.join(sample_dir, zeta) for zeta in zeta_contours_plots]

