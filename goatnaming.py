#!/usr/bin/python
#coding:utf-8
goat_words = {1: ['乙'],
              2: ['丁', '乃', '几', '力'],
              3: ['丸', '凡', '久', '也', '士', '寸', '小', '川', '己', '巳'],
              4: ['丹', '之', '尹', '云', '允', '午', '升', '少', '屯', '巴',
                  '引', '木', '火'],
              5: ['丙', '世', '乏', '充', '尼', '巧', '平', '弘', '本', '玄',
                  '田', '由', '甲', '禾', '立'],
              6: ['先', '印', '名', '合', '回', '圳', '地', '在', '圭', '妃',
                  '宇', '守', '安', '弛', '曲', '朵', '竹', '老', '而', '臣',
                  '自', '至'],
              7: ['兌', '克', '助', '均', '圻', '妙', '妍', '妤', '宋', '宏',
                  '廷', '村', '杞', '步', '甫', '男', '私', '秀', '豆', '里',
                  '妘', '町'],
              8: ['亞', '兔', '典', '和', '坤', '妹', '定', '宜', '宙', '宛',
                  '尚', '居', '屆', '岳', '幸', '延', '弦', '杭', '東', '果',
                  '林', '杰', '松', '炎', '秉', '舍', '青'],
              9: ['芋', '亮', '信', '勇', '勉', '匍', '南', '品', '垂', '室',
                  '宥', '封', '巷', '建', '扁', '柵', '柄', '柳', '炫', '為',
                  '炳', '盈', '科', '秒', '秋', '風', '芎', '垚'],
              10: ['迅', '巡', '芳', '芝', '芽', '芹', '花', '芸', '芷', '原',
                   '圃', '埔', '堉', '娜', '娟', '娥', '家', '容', '庭', '桂',
                   '桃', '殊', '烈', '畔', '秦', '秩', '航', '起', '軒', '馬',
                   '芫'],
              11: ['邦', '那', '迎', '近', '若', '茂', '苗', '英', '苑', '堅',
                   '基', '培', '婉', '專', '庶', '強', '梁', '梵', '梨', '烽',
                   '畢', '笛', '章', '苹', '埜', '婕', '娸'],
              12: ['述', '迪', '草', '捷', '凱', '博', '喜', '喬', '媚', '富',
                   '弼', '棟', '森', '棣', '棋', '焚', '無', '登', '發', '程',
                   '稅', '童', '筍', '筑', '粟', '舒', '貴', '開', '閑', '閎',
                   '雅', '雄', '集', '順', '茜', '焱'],
              13: ['莞', '莆', '圓', '廉', '彙', '敬', '業', '楠', '楓', '楣',
                   '煉', '煥', '萬', '稜', '稚', '節', '筠', '粱', '義', '詩',
                   '跳', '靖', '馳', '馴', '郅', '楙', '稑', '粲', '豊'],
              14: ['通', '速', '逐', '逢', '菁', '華', '菊', '嘉', '境', '夢',
                   '榮', '榴', '槐', '熙', '睿', '端', '筵', '精', '豪', '輔',
                   '颯', '魁', '菀', '菫', '菘', '墉', '墐', '槊', '榞', '箐',
                   '箖'],
              15: ['逸', '進', '葉', '嫻', '寬', '樂', '毅', '稼', '穀', '範',
                   '蝶', '豎', '賢', '逯', '萩', '槿'],
              16: ['道', '遂', '達', '蓉', '蒙', '蒼', '樺', '橙', '樹', '橡',
                   '橋', '燕', '篤', '臻', '螢', '豫', '霖', '靜', '蓁', '燁'],
              17: ['遠', '遙', '遛', '蔗', '蓮', '蔬', '燭', '穗', '篷', '臨',
                   '駿', '檡'],
              18: ['適', '檬', '簧', '豐', '蹕', '蕓'],
              19: ['鄰', '選', '薪', '穫', '簾', '證', '韻'],
              20: ['邁', '薰', '躂', '馨'],
              21: ['隧', '藝', '躍'],
              22: ['蘋', '驊'],
              23: ['蘭', '驛'],
              24: ['艷'],
              26: ['驥']}
good_pairs = [(1, 2), (2, 4), (3, 5), (2, 6), (1, 7), (10, 6), (9, 7), (2, 14),
              (1, 5), (10, 7), (3, 14), (2, 15), (1, 16), (3, 15), (2, 16),
              (1, 17), (20, 4), (18, 6), (10, 14), (9, 15), (8, 16), (1, 23),
              (18, 14), (9, 23), (8, 24), (18, 15), (10, 23), (9, 24),
              (22, 15), (20, 17)]


with open('chinese-names.txt', 'w') as f:
    family_name = '劉'
    for first, second in good_pairs:
        first_words = goat_words[first]
        second_words = goat_words[second]
        f.write('%d %d\n' % (first, second))
        for first_word in first_words:
            for second_word in second_words:
                f.write('%s\n' % (family_name + first_word + second_word))