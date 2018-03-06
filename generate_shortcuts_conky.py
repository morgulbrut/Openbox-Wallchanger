#!/bin/env python3

import xmltodict
from string import Template

with open('/home/tillo/.config/openbox/rc.xml') as fd:
    doc = xmltodict.parse(fd.read())

temp = Template("""
conky.config = {
	alignment = 'top_left',
	background = true,
        draw_shades = false,
        default_color = '8B8C8C',
        color1 = '1DCBA6',
        color2 = '556876',
	cpu_avg_samples = 2,
	double_buffer = true,
	font = 'Consolas:size=9:bold',
	gap_x = 25,
	gap_y = 40,
	minimum_width = 350,
	no_buffers = true,
	own_window = true,
	own_window_type = 'override',
	own_window_transparent = true,
	update_interval = 1.0,
	use_xft = true,
	if_up_strictness = 'address',
}
conky.text = [[
$text
]]
""")

text = ['${execpi 5 cat ~/Wallpaper/color.txt}\n${color1}shortcuts$color']
for i in doc['openbox_config']['keyboard']['keybind']:
    key=i['@key']
    try:
        action = i['action']['@name']
    except TypeError:
        action = ('{}'.format(i['action'][0]['@name']))
    if 'Execute' in action:
        action = i['action']['command']
    if 'ShowMenu' in action:
        action = 'Show '+ i['action']['menu']
    if action == 'Desktop':
        action = i['action']['@name']+' '+i['action']['desktop']
    text.append('\n{} $alignr {}'.format(key,action))
with open('/home/tillo/.conkyrc_shortcuts','w') as f:
    f.write(temp.substitute(text=''.join(text)))
    print(temp.substitute(text=''.join(text)))

