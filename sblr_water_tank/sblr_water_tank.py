#!/usr/bin/python

####################################################################################################
# solution to the square bottom line relief
# tank problem at http://www.vkedco.blogspot.com/2013/02/python-perl-square-bottom-line-relief.html
# bugs to vladimir dot kulyukin at gmail dot com
####################################################################################################

def square_relief_tank_water_volume(tank, tw, th, wl):
    if wl > th:
        raise 'Water level cannot be greater than tank height'
    vol = 0
    for col_num in xrange(1, tw+1):
        relief_h = tank[col_num]
        if relief_h < wl:
            vol += (wl - relief_h)
    return vol

def build_sblr_tank(cn_sh_tuple_list):
    sblr_tank = {}
    for col_num, stack_height in cn_sh_tuple_list:
        sblr_tank[col_num] = stack_height
    return sblr_tank

left_tank_fig_01  = build_sblr_tank(((1, 1), (2, 2), (3, 3)))
mid_tank_fig_01   = build_sblr_tank(((1, 1), (2, 2), (3, 1)))
right_tank_fig_01 = build_sblr_tank(((1, 1), (2, 1), (3, 1)))

print left_tank_fig_01
print mid_tank_fig_01
print right_tank_fig_01

tank_fig_07 = build_sblr_tank(((1, 2), (2, 5), (3, 0), (4, 4),
                               (4, 4), (5, 6), (6, 3), (7, 4)))


print square_relief_tank_water_volume(left_tank_fig_01,
                                      3, 3, 1)
print square_relief_tank_water_volume(mid_tank_fig_01,
                                      3, 3, 2)
print square_relief_tank_water_volume(right_tank_fig_01,
                                      3, 3, 3)
print square_relief_tank_water_volume(tank_fig_07,
                                      7, 7, 4)
print square_relief_tank_water_volume(tank_fig_07,
                                      7, 7, 5)
print square_relief_tank_water_volume(tank_fig_07,
                                      7, 7, 7)

