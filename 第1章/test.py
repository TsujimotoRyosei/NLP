# 00. 文字列の逆順
# 文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
character = "stressed"
character = list(character)
answer = ''.join(character[::-1])
print("00の答え: ",answer)

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
character = "パタトクカシーー"
answer = character[0] + character[2] + character[4] + character[6]
print("01の答え: ",answer)

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
character1 = "パトカー"
character2 = "タクシー"
answer = character1[0] + character2[0] + character1[1] + character2[1] + character1[2] + character2[2] + character1[3] + character2[3]
print("02の答え: ",answer)

# 03. 円周率
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
character = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
character = character.split()
answer = []
for word in character:
    answer.append(len(word))
print("03の答え: ",answer)

# 04. 元素記号
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
character = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
character = character.split()
answer = {}
for i, word in enumerate(character):
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        answer[word[0]] = i+1
    else:
        answer[word[:2]] = i+1
print("04の答え: ",answer)

# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
def n_gram(n, sequence):
    answer = []
    for i in range(len(sequence) - n + 1):
        answer.append(sequence[i:i+n])
    return answer

sequence = "I am an NLPer"
word_sequence = sequence.split()
answer = n_gram(2, word_sequence)
print("05の答え(単語bi-gram): ",answer)
list_sequence = list(sequence)
list_sequence = [i for i in list_sequence if i != " "] # 空白を削除
answer = n_gram(2, list_sequence)
print("05の答え(文字bi-gram): ",answer)

# 06. 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
sequence1 = "paraparaparadise"
sequence2 = "paragraph"
sequence1 = list(sequence1)
sequence2 = list(sequence2)
sequence1 = n_gram(2, sequence1)
sequence2 = n_gram(2, sequence2)
X = set(map(tuple,sequence1))
Y = set(map(tuple,sequence2))
print(X)
answer = X | Y
print("06の答え(和集合): ",answer)
answer = X & Y
print("06の答え(積集合): ",answer)
answer = X - Y
print("06の答え(差集合): ",answer)
answer = ("s","e") in X
print("06の答え(Xにseが含まれるか): ",answer)
answer = ("s","e") in Y
print("06の答え(Yにseが含まれるか): ",answer)

# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
def template(x, y, z):
    return f"{x}時の{y}は{z}"

x = 12
y = "気温"
z = 22.4
result = template(x, y, z)
print("07の答え: ",result)

# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
def cipher(character):
    answer = ""
    for c in character:
        if c.islower():
            answer += chr(219 - ord(c))
        else:
            answer += c
    return answer


# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）
# を与え，その実行結果を確認せよ．
import random

character = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
character = character.split()
answer = []
for word in character:
    if len(word) <= 4:
        answer.append(word)
    else:
        middle = list(word[1:-1])
        random.shuffle(middle)
        answer.append(word[0] + ''.join(middle) + word[-1])
print("09の答え: ",' '.join(answer))
