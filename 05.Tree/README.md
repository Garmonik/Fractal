# Дерево #

Основа решения данной задачи лежит в L-системах. L-система или система Линденмайера — это параллельная система переписывания и вид формальной грамматики. L-система состоит из алфавита символов, которые могут быть использованы для создания строк, набора порождающих правил, которые задают правила подстановки вместо каждого символа, начальной строки («аксиомы»), с которой начинается построение, и механизма перевода образованной строки в геометрические структуры. L-системы предложил и развивал в 1968 Аристид Линденмайер, венгерский биолог и ботаник из Утрехтского университета. Линденмайер использовал L-системы для описания поведения клеток растений и моделирования процесса развития растения. L-системы использовались также для моделирования морфологии различных организмов и могут быть использованы для генерации самоподобных фракталов, таких как системы итерируемых функций.

   ***переменные: X F***
   
   ***константы: + − [ ] @***
    
   ***старт: X***
    
   ***правило: (X → F[@[-X]+X])***
    
   ***угол: случайный от 0 до 45°***

Отрезки, образующие дерево, разделим на два типа. Отрезок типа X — это ветвь, на которой в следующем поколении вырастут две ветви потоньше, покороче и светлее, и, кроме того, наклонённые вправо и влево на случайный угол, равномерно распределённый в пределах от 0° до 45°. Отрезок типа F — это ветвь, от которой уже ответвились две ветви. Ветви типа X назовём терминальными (конечными), а ветви типа F — нетерминальными. Дерево в нулевом поколении представляет собой одну терминальную ветвь.Для построения нужной L-системы нам понадобятся символы X и F (для ветвей обоих типов), + и - (для поворота черепахи соответственно влево и вправо на случайный угол), @ (для осветления текущего цвета рисования, уменьшения толщины и длины штрихов), и, конечно, скобки [ и ] (для запоминания и последующего восстановления запомненных состояний черепахи — её положения и направления, а также цвета, толщины и длины штриха).Теперь займёмся правилом L-системы. В каждом цикле развития дерева каждая терминальная ветвь превращается в нетерминальную, от которой что-то ответвилось: X→F[…]. Эту ответвившуюся растительность мы заключаем в скобки, в которые первым делом помещает символ @, ответственный за осветление, утоньшение и укорачивание ветвей. Затем рисуем правую ветвь: [-X]. Скобки здесь нужны для того, чтобы запомнить положение и направление черепахи; ведь предстоит поворот на случайный угол. Рисуем левую ветвь: +X. 

![image](https://github.com/Garmonik/Fractal/blob/main/05.Tree/Tree.png)

![image](https://github.com/Garmonik/Fractal/blob/main/05.Tree/Tree1.png)
