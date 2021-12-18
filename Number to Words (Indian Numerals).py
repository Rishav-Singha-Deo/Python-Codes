num=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
n=eval(input("Enter a number : "))
if n>9999999999999:
    print("Too Large!")
elif n==0:
    print("Zero Rupees")
elif n==1:
    print("One Rupee")
else:
    d=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    i=0
    while n>0:
        d[i]=n%10
        i+=1
        n=n//10
    numb=""
    if d[12] != 0:
        if d[12] == 1:
            numb += tens[d[11]] + " Kharab "
        else:
            numb += nty[d[12]] + " " + num[d[11]] + " Kharab "
    else:
        if d[11] != 0:
            numb += num[d[11]] + " Kharab "
    if d[10] != 0:
        if d[10] == 1:
            numb += tens[d[9]] + " Arab "
        else:
            numb += nty[d[10]] + " " + num[d[9]] + " Arab "
    else:
        if d[9] != 0:
            numb += num[d[9]] + " Arab "
    if d[8] != 0:
        if d[8] == 1:
            numb += tens[d[7]] + " Crore "
        else:
            numb += nty[d[8]] + " " + num[d[7]] + " Crore "
    else:
        if d[7] != 0:
            numb += num[d[7]] + " Crore "
    if d[6] != 0:
        if d[6] == 1:
            numb += tens[d[5]] + " Lakh "
        else:
            numb += nty[d[6]] + " " + num[d[5]] + " Lakh "
    else:
        if d[5] != 0:
            numb += num[d[5]] + " Lakh "
    if d[4]!=0:
        if d[4]==1:
            numb+=tens[d[3]]+" Thousand "
        else:
            numb+=nty[d[4]]+" "+num[d[3]]+" Thousand "
    else:
        if d[3]!=0:
            numb+=num[d[3]]+" Thousand "
    if d[2]!=0:
        numb+=num[d[2]]+" Hundred "
    if d[1] != 0:
        if d[1] == 1:
            numb += tens[d[0]]
        else:
            numb += nty[d[1]] + " " + num[d[0]]
    else:
        if d[0] != 0:
            numb += num[d[0]]
    print(numb,"Rupees")