class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    vacancy = list()
    for i in range(9):
        for j in range(9):
            if board 



    def cells_related(self, cell):
        return list(self.cells_in_same_row(cell) +
                    self.cells_in_same_col(cell) +
                    self.cells_in_same_block(cell)
                    )

    def cells_in_same_row(self, cell):
        return set((cell[0], ci) for ci in range(9))

    def cells_in_same_col(self, cell):
        return set((ri, cell[1]) for ri in range(9))

    def cells_in_same_block(self, cell):
        ri_base = cell[0] //3 * 3
        ci_base = cell[1] //3 * 3
        return set((ri, ci)
                   for ri in ri_base+range(3)
                   for ci in ci_base+range(3)
                   )


        
