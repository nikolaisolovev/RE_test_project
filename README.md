Ниже приведен фрагмент скрипта по сборке отчета.

Требуется внести изменения (дописать/поправить маленький фрагмент):

проставить признак КГТ ("КГТ") для площадки ('источник') озон ('Ozon'), если:

длина >180, или ширина > 80, или ОВХ >= 25
причем, под длиной подразумевается самое большое измерение, а под шириной - самое маленькое
ОВХ = длина*ширина*высота / 5000, но если ОВХ больше, чем вес (в кг), тогда ОВХ = вес (в кг).

если габариты не указаны, то проставить признак КГТ "Габариты отсутствуют"
в остальных случаях проставить "не КГТ"

rep - датафрейм с отчетом (строки - номера заказов с товарами, файл xlsx из задания 1),  
в котором уже имеются столбцы: 
'Источник' ,'Длина', 'Ширина' ,'Высота', 'Вес' (уже содержат значения)
'ОВХ','признак КГТ' - столбцы есть, но значений в них нет

Скрипт, который нужно дописать/поправить (на ваше усмотрение):

for i in range(len(rep)):
    
    if rep.loc[i, 'Источник'] == 'Ozon':
        
    
    else:
        rep.loc[i, 'ОВХ'] = rep.loc[i, 'Длина']+rep.loc[i, 'Ширина']+rep.loc[i, 'Высота']
        rep.loc[i, 'Вес']

            
for i in range(len(rep)):
    if rep.loc[i, 'Источник'] == 'Ozon':