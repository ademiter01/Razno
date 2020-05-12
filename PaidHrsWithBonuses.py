hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
ot = r * 1.5

if h <= 40 :
    print("Pay:", h * r)
elif h > 40 :
    print("Pay:", (h - 40) * ot + (40 * r))
print("")

print("Regular Hours Pay: ", h * r)
if h <= 40 :
    print("Bonus Hours Pay:", 0 * ot)
elif h > 40 :
    print("Bonus Hours Pay:", (h - 40) * ot + (40 * r))
#line13-15 bonus sati ne treba da se racunaju ako je h <= 40;
