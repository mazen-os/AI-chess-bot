# -*- coding: utf-8 -*-
"""untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/mazen-os/0af8851ca4e203b9cf7876e5dfb6016e/untitled7.ipynb
"""

!pip install python-chess

import chess
import chess.svg  # لعرض الرقعة كصورة
import IPython.display

# إنشاء رقعة شطرنج جديدة
board = chess.Board()

# عرض الرقعة
IPython.display.display_svg(chess.svg.board(board=board, size=400))

move = chess.Move.from_uci("e2e4")  # تحديد الحركة بصيغة UCI
board.push(move)  # تنفيذ الحركة

# عرض الرقعة بعد الحركة
IPython.display.display_svg(chess.svg.board(board=board, size=400))

print(list(board.legal_moves))

move = chess.Move.from_uci("e2e3")
print(move in board.legal_moves)  # هيرجع True لو قانونية، False لو لأ

move = chess.Move.from_uci("e7e5")  # تحديد الحركة بصيغة UCI
board.push(move)  # تنفيذ الحركة

print(list(board.legal_moves))

move("g1f3")

!apt-get install stockfish

import chess
import chess.svg
import chess.engine
import IPython.display

# تشغيل محرك Stockfish
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

# إنشاء رقعة شطرنج جديدة
board = chess.Board()

# دالة لعرض الرقعة
def br(board):
    IPython.display.display_svg(chess.svg.board(board=board, size=400))

br(board)

def move(move_uci):
  if chess.Move.from_uci(move_uci) in board.legal_moves:
    board.push(chess.Move.from_uci(move_uci))
    IPython.display.display_svg(chess.svg.board(board=board, size=400))
  else:
    return "you cannot play this"


    # 🚀 Stockfish يحسب أفضل نقلة للأسود
    if not board.is_game_over():
        best_move = engine.play(board, chess.engine.Limit(time=0.5))  # يحسب أفضل حركة في 0.5 ثانية
        board.push(best_move.move)
        print(f"🤖 Stockfish لعب: {best_move.move}")

    # عرض الرقعة بعد النقلتين
    br(board)

br(board)

move("e2e4")

br(board)

# 🚀 Stockfish يحسب أفضل نقلة للأسود
    def play() :
      if not board.is_game_over():
        best_move = engine.play(board, chess.engine.Limit(time=0.5))  # يحسب أفضل حركة في 0.5 ثانية
        board.push(best_move.move)
        print(f"🤖 Stockfish لعب: {best_move.move}")

    # عرض الرقعة بعد النقلتين
      br(board)

play()

import chess
import chess.svg
import chess.engine
import IPython.display

# تشغيل محرك Stockfish
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

# إنشاء رقعة شطرنج جديدة
board = chess.Board()

# دالة لعرض الرقعة مع تلوين حركة Stockfish فقط
def br(stockfish_move=None):
    board_svg = chess.svg.board(
        board=board,
        size=400,
        lastmove=stockfish_move,  # تلوين حركة Stockfish فقط
        colors={"lastmove": "#00FF00"}  # أخضر لحركة الذكاء الاصطناعي
    )
    IPython.display.display_svg(board_svg)

br()  # عرض الرقعة لأول مرة

# دالة لتنفيذ الحركة ثم رد Stockfish مع تلوين حركته
def move(move_uci):
    move = chess.Move.from_uci(move_uci)
    if move in board.legal_moves:
        board.push(move)  # تنفيذ حركة اللاعب
        print(f"✅ أنت لعبت: {move_uci}")

        # 🚀 Stockfish يحسب أفضل نقلة للأسود
        if not board.is_game_over():
            best_move = engine.play(board, chess.engine.Limit(time=0.00001))  # اختيار أفضل نقلة خلال 0.5 ثانية
            board.push(best_move.move)  # تنفيذ حركة Stockfish
            print(f"🤖 Stockfish لعب: {best_move.move}")

            # عرض الرقعة مع تلوين حركة Stockfish
            br(stockfish_move=best_move.move)
        else:
            br()  # عرض الرقعة بدون تلوين (اللعبة انتهت)
    else:
        print(f"❌ الحركة {move_uci} غير قانونية!")

move("d2d6")



