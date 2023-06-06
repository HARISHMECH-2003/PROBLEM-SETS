def rock_paper_scissors(I1,I2):
    if I1==I2:
        return "draw"
    elif I1=="rock" and I2=="scissors":
        print("I1 won")
    elif I1=="paper" and I2=="rock":
        print("I1 won")
    elif I1=="scissors" and I2=="paper":
        print("I2 won")

I1="rock"
I2="paper"
result=rock_paper_scissors(I1,I2)
print(result)