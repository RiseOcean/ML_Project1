from classes.plate import Plate
import setup

# This function can be used to create a list with all entries
# Example: L(7,12) produces [7,8,9,10,11,12]
def L(first, last):
	return [i for i in range(first, last+1)]


# PLATE 1 ======================================================================

plate1 = Plate(72,12)#（行，列）

# 胺(列)
plate1.fillRow(L(1,12), 'amine', 'benan') # 胺 1
plate1.fillRow(L(13,24), 'amine', 'naian') # 胺 2
plate1.fillRow(L(25,36), 'amine', 'lingjiabenan') # 胺 3
plate1.fillRow(L(37,48), 'amine', 'duijiabenan') # 胺 4
plate1.fillRow(L(49,60), 'amine', 'duijiayangjibenan') # 胺 5
plate1.fillRow(L(61,72), 'amine', 'duixiaojibenan') # 胺 6
# plate1.fillRow(L(37,48), 'amine', 'jianjiabenan') # 胺 4
# plate1.fillRow(L(73,84), 'amine', 'duixiubenan') # 胺 7

# 催化剂(列)
plate1.fillColumn([1,5,9,11], 'cata', 'HBTU')
plate1.fillColumn([2,6,10,12], 'cata', 'PyBOP')
plate1.fillColumn([3,7], 'cata', 'DPP-CL')
plate1.fillColumn([4,8], 'cata', 'BOP-CL')

# 羧酸(行)
plate1.fillRow([1,13,25,37,49,61], 'car_acid', 'yisuan') # 羧酸 1
plate1.fillRow([2,14,26,38,50,62], 'car_acid', 'bingsuan') # 羧酸 2
plate1.fillRow([3,15,27,39,51,63], 'car_acid', 'bingxisuan') # 羧酸 3
plate1.fillRow([4,16,28,40,52,64], 'car_acid', 'dingsuan') # 羧酸 4
plate1.fillRow([5,17,29,41,53,65], 'car_acid', 'zhengjisuan') # 羧酸 5
plate1.fillRow([6,18,30,42,54,66], 'car_acid', 'yixianbingsuan') # 羧酸 6
plate1.fillRow([7,19,31,43,55,67], 'car_acid', 'benjiasuan') # 羧酸 7
plate1.fillRow([8,20,32,44,56,68], 'car_acid', 'duilvbenjiasuan') # 羧酸 8
plate1.fillRow([9,21,33,45,57,69], 'car_acid', 'duijiayangjibenjiasuan') # 羧酸 9
plate1.fillRow([10,22,34,46,58,70], 'car_acid', 'yansuan') # 羧酸 10
plate1.fillRow([11,23,35,47,59,71], 'car_acid', 'yiyansuan') # 羧酸 11
plate1.fillRow([12,24,36,48,60,72], 'car_acid', 'yixianshuiyangsuan') # 羧酸 12

# 溶剂(行)
plate1.fillColumn(L(1,4), 'solvent', 'DMAc')
plate1.fillColumn(L(5,8), 'solvent', 'DMF')
plate1.fillColumn(L(9,10), 'solvent', 'MeCN')
plate1.fillColumn(L(11,12), 'solvent', 'DMSO')

# uncomment to view layout for plate1
# plate1.printLayout()

# PLATE 2 ======================================================================

plate2 = Plate(48,8)

# 胺(列)
plate2.fillRow(L(1,12), 'amine', '4-anjisanfujiaben') # 胺 1
plate2.fillRow(L(13,24), 'amine', 'jianlvbenan') # 胺 2
plate2.fillRow(L(25,36), 'amine', 'duidianbenan') # 胺 3
plate2.fillRow(L(37,48), 'amine', 'duilvbenan') # 胺 4
# plate2.fillRow(L(25,36), 'amine', 'N-jiajibenan') # 胺 3

# 催化剂(列)
plate2.fillColumn([1,5], 'cata', 'HBTU')
plate2.fillColumn([2,6], 'cata', 'PyBOP')
plate2.fillColumn([3,7], 'cata', 'DPP-CL')
plate2.fillColumn([4,8], 'cata', 'BOP-CL')

# 羧酸(行)
plate2.fillRow([1,13,25,37], 'car_acid', 'yisuan') # 羧酸 1
plate2.fillRow([2,14,26,38], 'car_acid', 'bingsuan') # 羧酸 2
plate2.fillRow([3,15,27,39], 'car_acid', 'bingxisuan') # 羧酸 3
plate2.fillRow([4,16,28,40], 'car_acid', 'dingsuan') # 羧酸 4
plate2.fillRow([5,17,29,41], 'car_acid', 'zhengjisuan') # 羧酸 5
plate2.fillRow([6,18,30,42], 'car_acid', 'yixianbingsuan') # 羧酸 6
plate2.fillRow([7,19,31,43], 'car_acid', 'benjiasuan') # 羧酸 7
plate2.fillRow([8,20,32,44], 'car_acid', 'duilvbenjiasuan') # 羧酸 8
plate2.fillRow([9,21,33,45], 'car_acid', 'duijiayangjibenjiasuan') # 羧酸 9
plate2.fillRow([10,22,34,46], 'car_acid', 'yansuan') # 羧酸 10
plate2.fillRow([11,23,35,47], 'car_acid', 'yiyansuan') # 羧酸 11
plate2.fillRow([12,24,36,48], 'car_acid', 'yixianshuiyangsuan') # 羧酸 12

# 溶剂(行)
plate2.fillColumn(L(1,4), 'solvent', 'DMAc')
plate2.fillColumn(L(5,8), 'solvent', 'DMF')

# uncomment to view layout for plate2
# plate2.printLayout()

# PLATE 3 ======================================================================

plate3 = Plate(12,8)

# 胺(列)
plate3.fillRow(L(1,12), 'amine', 'N-jiajibenan') # 胺 1

# 催化剂(列)
plate3.fillColumn([1,5], 'cata', 'HBTU')
plate3.fillColumn([2,6], 'cata', 'PyBOP')
plate3.fillColumn([3,7], 'cata', 'DPP-CL')
plate3.fillColumn([4,8], 'cata', 'BOP-CL')

# 羧酸(行)
plate3.fillRow([1], 'car_acid', 'yisuan') # 羧酸 1
plate3.fillRow([2], 'car_acid', 'bingsuan') # 羧酸 2
plate3.fillRow([3], 'car_acid', 'bingxisuan') # 羧酸 3
plate3.fillRow([4], 'car_acid', 'dingsuan') # 羧酸 4
plate3.fillRow([5], 'car_acid', 'zhengjisuan') # 羧酸 5
plate3.fillRow([6], 'car_acid', 'yixianbingsuan') # 羧酸 6
plate3.fillRow([7], 'car_acid', 'benjiasuan') # 羧酸 7
plate3.fillRow([8], 'car_acid', 'duilvbenjiasuan') # 羧酸 8
plate3.fillRow([9], 'car_acid', 'duijiayangjibenjiasuan') # 羧酸 9
plate3.fillRow([10], 'car_acid', 'yansuan') # 羧酸 10
plate3.fillRow([11], 'car_acid', 'yiyansuan') # 羧酸 11
plate3.fillRow([12], 'car_acid', 'yixianshuiyangsuan') # 羧酸 12

# 溶剂(行)
plate3.fillColumn(L(1,4), 'solvent', 'DMAc')
plate3.fillColumn(L(5,8), 'solvent', 'DMF')

# uncomment to view layout for plate3
# plate3.printLayout()

# PLATE 4 ======================================================================

plate4 = Plate(24,12)#（行，列）

# 胺(列)
plate4.fillRow(L(1,12), 'amine', 'duixiubenan') # 胺 1
plate4.fillRow(L(13,24), 'amine', 'jianjiabenan') # 胺 2

# 催化剂(列)
plate4.fillColumn([1,5,9,11], 'cata', 'HBTU')
plate4.fillColumn([2,6,10,12], 'cata', 'PyBOP')
plate4.fillColumn([3,7], 'cata', 'DPP-CL')
plate4.fillColumn([4,8], 'cata', 'BOP-CL')

# 羧酸(行)
plate4.fillRow([1,13], 'car_acid', 'yisuan') # 羧酸 1
plate4.fillRow([2,14], 'car_acid', 'bingsuan') # 羧酸 2
plate4.fillRow([3,15], 'car_acid', 'bingxisuan') # 羧酸 3
plate4.fillRow([4,16], 'car_acid', 'dingsuan') # 羧酸 4
plate4.fillRow([5,17], 'car_acid', 'zhengjisuan') # 羧酸 5
plate4.fillRow([6,18], 'car_acid', 'yixianbingsuan') # 羧酸 6
plate4.fillRow([7,19], 'car_acid', 'benjiasuan') # 羧酸 7
plate4.fillRow([8,20], 'car_acid', 'duilvbenjiasuan') # 羧酸 8
plate4.fillRow([9,21], 'car_acid', 'duijiayangjibenjiasuan') # 羧酸 9
plate4.fillRow([10,22], 'car_acid', 'yansuan') # 羧酸 10
plate4.fillRow([11,23], 'car_acid', 'yiyansuan') # 羧酸 11
plate4.fillRow([12,24], 'car_acid', 'yixianshuiyangsuan') # 羧酸 12

# 溶剂(行)
plate4.fillColumn(L(1,4), 'solvent', 'DMAc')
plate4.fillColumn(L(5,8), 'solvent', 'DMF')
plate4.fillColumn(L(9,10), 'solvent', 'MeCN')
plate4.fillColumn(L(11,12), 'solvent', 'DMSO')

# uncomment to view layout for plate4
# plate4.printLayout()

# CREATE OUTPUT FILE ===========================================================

# creates an output.csv file in the rxnpredict folder
# the plates must be populated with the same rxn components (base, ligand, etc.)
setup.export_reactions([plate1, plate2, plate3, plate4])
setup.export_for_pca([plate1, plate2, plate3, plate4])