import tkinter as tk
from tkinter import messagebox

class ConnectFourGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")

        self.canvas = tk.Canvas(self.root, width=700, height=600, bg="blue")
        self.canvas.pack()

        self.board = [[0] * 7 for _ in range(6)]  # Initialize the game board

        self.draw_board()

        self.current_player = 1

        self.canvas.bind("<Button-1>", self.drop_piece)

        self.root.mainloop()

    def draw_board(self):
        self.canvas.delete("pieces")
        for i in range(7):
            for j in range(6):
                color = "white" if self.board[j][i] == 0 else ("red" if self.board[j][i] == 1 else "yellow")
                self.canvas.create_oval(i*100+10, j*100+10, (i+1)*100-10, (j+1)*100-10, fill=color, tags="pieces")

    def drop_piece(self, event):
        if self.check_winner():
            return
        
        column = event.x // 100
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                self.draw_board()
                if self.check_win(row, column):
                    winner = "Player 1" if self.current_player == 1 else "Player 2"
                    messagebox.showinfo("Winner", f"{winner} wins!")
                    self.root.quit()
                    return
                self.current_player = 1 if self.current_player == 2 else 2
                return

    def check_win(self, row, col):
        # Check for horizontal win
        if col <= 3 and self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
            return True
        # Check for vertical win
        if row <= 2 and self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
            return True
        # Check for diagonal win (down-right)
        if row <= 2 and col <= 3 and self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
            return True
        # Check for diagonal win (up-right)
        if row >= 3 and col <= 3 and self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3]:
            return True
        return False
    
    def check_winner(self):
        for row in range(6):
            for col in range(7):
                if self.board[row][col] != 0:
                    # Check horizontally
                    if col <= 3 and self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                        return True
                    # Check vertically
                    if row <= 2 and self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                        return True
                    # Check diagonally (down-right)
                    if row <= 2 and col <= 3 and self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
                        return True
                    # Check diagonally (up-right)
                    if row >= 3 and col <= 3 and self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3]:
                        return True
        return False

ConnectFourGUI()
