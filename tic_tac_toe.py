import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [" "]*9
        self.current_player = "X"
        self.buttons = []
        self.create_board()
    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", width=10, height=5, command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)
    def clicked(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win():
                messagebox.showinfo("Game Over", "Player " + self.current_player + " wins!")
                self.reset()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset()
            else:
                self.switch_player()
    def check_win(self):
        win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False
    def check_tie(self):
        return " " not in self.board
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    def reset(self):
        self.board = [" "]*9
        self.current_player = "X"
        for i in range(9):
            self.buttons[i].config(text=" ")
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
