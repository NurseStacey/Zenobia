BACKSPACE = 8

#colors


class One_Color():
    def __init__(self, name, hex):
        self.name = name
        self.hex = hex

def get_color(color_name):

    for one_color in the_colors:
        temp = one_color.name.lower().strip()

        if color_name.lower() == one_color.name.lower().strip():
            return(one_color.hex)

the_colors = []

the_colors.append(One_Color('white ', '#FFFFFF'))
the_colors.append(One_Color('black ', '#000000'))
the_colors.append(One_Color('FireBrick ', '#B22222'))
the_colors.append(One_Color('AliceBlue ', '#F0F8FF'))
the_colors.append(One_Color('AntiqueWhite ', '#FAEBD7'))
the_colors.append(One_Color('Aqua ', '#00FFFF'))
the_colors.append(One_Color('Aquamarine ', '#7FFFD4'))
the_colors.append(One_Color('Azure ', '#F0FFFF'))
the_colors.append(One_Color('Beige ', '#F5F5DC'))
the_colors.append(One_Color('Bisque ', '#FFE4C4'))

the_colors.append(One_Color('BlanchedAlmond ', '#FFEBCD'))
the_colors.append(One_Color('Blue ', '#0000FF'))
the_colors.append(One_Color('BlueViolet ', '#8A2BE2'))
the_colors.append(One_Color('Brown ', '#A52A2A'))
the_colors.append(One_Color('BurlyWood ', '#DEB887'))
the_colors.append(One_Color('CadetBlue ', '#5F9EA0'))
the_colors.append(One_Color('Chartreuse ', '#7FFF00'))
the_colors.append(One_Color('Chocolate ', '#D2691E'))
the_colors.append(One_Color('Coral ', '#FF7F50'))
the_colors.append(One_Color('CornflowerBlue ', '#6495ED'))
the_colors.append(One_Color('Cornsilk ', '#FFF8DC'))
the_colors.append(One_Color('Crimson ', '#DC143C'))
the_colors.append(One_Color('Cyan ', '#00FFFF'))
the_colors.append(One_Color('DarkBlue ', '#00008B'))
the_colors.append(One_Color('DarkCyan ', '#008B8B'))
the_colors.append(One_Color('DarkGoldenrod ', '#B8860B'))
the_colors.append(One_Color('DarkGray ', '#A9A9A9'))
the_colors.append(One_Color('DarkGreen ', '#006400'))
the_colors.append(One_Color('DarkKhaki ', '#BDB76B'))
the_colors.append(One_Color('DarkMagenta ', '#8B008B'))
the_colors.append(One_Color('DarkOliveGreen ', '#556B2F'))
the_colors.append(One_Color('DarkOrange ', '#FF8C00'))
the_colors.append(One_Color('DarkOrchid ', '#9932CC'))
the_colors.append(One_Color('DarkRed ', '#8B0000'))
the_colors.append(One_Color('DarkSalmon ', '#E9967A'))
the_colors.append(One_Color('DarkSeaGreen ', '#8FBC8B'))
the_colors.append(One_Color('DarkSlateBlue ', '#483D8B'))
the_colors.append(One_Color('DarkSlateGray ', '#2F4F4F'))
the_colors.append(One_Color('DarkTurquoise ', '#00CED1'))
the_colors.append(One_Color('DarkViolet ', '#9400D3'))
the_colors.append(One_Color('DeepPink ', '#FF1493'))
the_colors.append(One_Color('DeepSkyBlue ', '#00BFFF'))
the_colors.append(One_Color('DimGray ', '#696969'))
the_colors.append(One_Color('DodgerBlue ', '#1E90FF'))
the_colors.append(One_Color('FireBrick ', '#B22222'))
the_colors.append(One_Color('firebrick1 ', '#FF3030'))
the_colors.append(One_Color('FloralWhite ', '#FFFAF0'))
the_colors.append(One_Color('ForestGreen ', '#228B22'))
the_colors.append(One_Color('Fuchsia ', '#FF00FF'))
the_colors.append(One_Color('Gainsboro ', '#DCDCDC'))
the_colors.append(One_Color('GhostWhite ', '#F8F8FF'))
the_colors.append(One_Color('Gold ', '#FFD700'))
the_colors.append(One_Color('Goldenrod ', '#DAA520'))
the_colors.append(One_Color('Gray ', '#808080'))
the_colors.append(One_Color('Green ', '#008000'))
the_colors.append(One_Color('GreenYellow ', '#ADFF2F'))
the_colors.append(One_Color('HoneyDew ', '#F0FFF0'))
the_colors.append(One_Color('HotPink ', '#FF69B4'))
the_colors.append(One_Color('IndianRed ', '#CD5C5C'))
the_colors.append(One_Color('Indigo ', '#4B0082'))
the_colors.append(One_Color('Ivory ', '#FFFFF0'))
the_colors.append(One_Color('Khaki ', '#F0E68C'))
the_colors.append(One_Color('Lavender ', '#E6E6FA'))
the_colors.append(One_Color('LavenderBlush ', '#FFF0F5'))
the_colors.append(One_Color('lawngreen ', '#7CFC00'))
the_colors.append(One_Color('LemonChiffon ', '#FFFACD'))
the_colors.append(One_Color('LightBlue ', '#ADD8E6'))
the_colors.append(One_Color('LightCoral ', '#F08080'))
the_colors.append(One_Color('LightCyan ', '#E0FFFF'))
the_colors.append(One_Color('LightGoldenrodYellow ', '#FAFAD2'))
the_colors.append(One_Color('LightGray ', '#D3D3D3'))
the_colors.append(One_Color('LightGreen ', '#90EE90'))
the_colors.append(One_Color('LightPink ', '#FFB6C1'))
the_colors.append(One_Color('LightSalmon ', '#FFA07A'))
the_colors.append(One_Color('LightSeaGreen ', '#20B2AA'))
the_colors.append(One_Color('LightSkyBlue ', '#87CEFA'))
the_colors.append(One_Color('LightSlateGray ', '#778899'))
the_colors.append(One_Color('LightSteelBlue ', '#B0C4DE'))
the_colors.append(One_Color('LightYellow ', '#FFFFE0'))
the_colors.append(One_Color('Lime ', '#00FF00'))
the_colors.append(One_Color('LimeGreen ', '#32CD32'))
the_colors.append(One_Color('Linen ', '#FAF0E6'))
the_colors.append(One_Color('Magenta ', '#FF00FF'))
the_colors.append(One_Color('Maroon ', '#800000'))
the_colors.append(One_Color('MediumAquamarine ', '#66CDAA'))
the_colors.append(One_Color('MediumBlue ', '#0000CD'))
the_colors.append(One_Color('MediumOrchid ', '#BA55D3'))
the_colors.append(One_Color('MediumPurple ', '#9370DB'))
the_colors.append(One_Color('MediumSeaGreen ', '#3CB371'))
the_colors.append(One_Color('MediumSlateBlue ', '#7B68EE'))
the_colors.append(One_Color('MediumSpringGreen ', '#00FA9A'))
the_colors.append(One_Color('MediumTurquoise ', '#48D1CC'))
the_colors.append(One_Color('MediumVioletRed ', '#C71585'))
the_colors.append(One_Color('MidnightBlue ', '#191970'))
the_colors.append(One_Color('MintCream ', '#F5FFFA'))
the_colors.append(One_Color('MistyRose ', '#FFE4E1'))
the_colors.append(One_Color('Moccasin ', '#FFE4B5'))
the_colors.append(One_Color('NavajoWhite ', '#FFDEAD'))
the_colors.append(One_Color('Navy ', '#000080'))
the_colors.append(One_Color('OldLace ', '#FDF5E6'))
the_colors.append(One_Color('Olive ', '#808000'))
the_colors.append(One_Color('OliveDrab ', '#6B8E23'))
the_colors.append(One_Color('Orange ', '#FFA500'))
the_colors.append(One_Color('OrangeRed ', '#FF4500'))
the_colors.append(One_Color('Orchid ', '#DA70D6'))
the_colors.append(One_Color('PaleGoldenrod ', '#EEE8AA'))
the_colors.append(One_Color('PaleGreen ', '#98FB98'))
the_colors.append(One_Color('PaleTurquoise ', '#AFEEEE'))
the_colors.append(One_Color('PaleVioletRed ', '#DB7093'))
the_colors.append(One_Color('PapayaWhip ', '#FFEFD5'))
the_colors.append(One_Color('PeachPuff ', '#FFDAB9'))
the_colors.append(One_Color('Peru ', '#CD853F'))
the_colors.append(One_Color('Pink ', '#FFC0CB'))
the_colors.append(One_Color('Plum ', '#DDA0DD'))
the_colors.append(One_Color('PowderBlue ', '#B0E0E6'))
the_colors.append(One_Color('Purple ', '#800080'))
the_colors.append(One_Color('RebeccaPurple ', '#663399'))
the_colors.append(One_Color('Red ', '#FF0000'))
the_colors.append(One_Color('RosyBrown ', '#BC8F8F'))
the_colors.append(One_Color('RoyalBlue ', '#4169E1'))
the_colors.append(One_Color('SaddleBrown ', '#8B4513'))
the_colors.append(One_Color('Salmon', '#FA8072'))
the_colors.append(One_Color('SandyBrown ', '#F4A460'))
the_colors.append(One_Color('SeaGreen ', '#2E8B57'))
the_colors.append(One_Color('SeaShell ', '#FFF5EE'))
the_colors.append(One_Color('Sienna ', '#A0522D'))
the_colors.append(One_Color('Silver ', '#C0C0C0'))
the_colors.append(One_Color('SkyBlue ', '#87CEEB'))
the_colors.append(One_Color('SlateBlue ', '#6A5ACD'))
the_colors.append(One_Color('SlateGray ', '#708090'))
the_colors.append(One_Color('Snow ', '#FFFAFA'))
the_colors.append(One_Color('SpringGreen ', '#00FF7F'))
the_colors.append(One_Color('SteelBlue ', '#4682B4'))
the_colors.append(One_Color('Tan ', '#D2B48C'))
the_colors.append(One_Color('Teal ', '#008080'))
the_colors.append(One_Color('Thistle ', '#D8BFD8'))
the_colors.append(One_Color('Tomato ', '#FF6347'))
the_colors.append(One_Color('Turquoise ', '#40E0D0'))
the_colors.append(One_Color('Violet ', '#EE82EE'))
the_colors.append(One_Color('Wheat ', '#F5DEB3'))
the_colors.append(One_Color('Light Green', '#BBFFFF'))
the_colors.append(One_Color('WhiteSmoke ', '#F5F5F5'))
the_colors.append(One_Color('Yellow ', '#FFFF00'))
the_colors.append(One_Color('YellowGreen ', '#9ACD32'))
