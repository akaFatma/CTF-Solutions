import math
import decimal
import cryptography
D = decimal.Decimal

e = D(9987754936923856376598147340336831658440345161735241391579454561653424914518863664425322421520390210989520871856034416676871944867613957933148827937968618480347889028744863237831998463128700368766426213670935402088247860753492063205295775627140974107591089661599884856905389251607814958649064415617483640743)
N = D(55310949399356723651582530748110437266948363166398694064483055882784340402082422504058974332154839404371086364619291117377038703996260133484925434349751963261973973993162917108809138428316795853303003983426064973308155200211996229569212629682418622780277679871197506830192444037878720680378501806071551230253)
c_m = 3999391151231954322511910137742197501204717741014277889992435785916153768931773902160757375088110551950358272409292006689480608257792843116416796772747240147893424442590691608181691007398848741517074516893527925465592278981131470259040287991141712157683694421461943174673135509005146322528315168246350177434

#Continued fraction expansion of e/N (see https://en.wikipedia.org/wiki/Continued_fraction):
n_fe = e #nominator
d_fe = N #denominator
fraction_list = []

def expand_fraction_list(n_fe, d_fe):
    with decimal.localcontext() as ctx:
        ctx.prec = 350    
        cap = math.floor(n_fe/d_fe)
        rest = n_fe%d_fe
        fraction_list.append(cap)
        
        n_fe = d_fe
        d_fe = rest
    return (n_fe, d_fe)

def cfe(a_list, j): #Calculate fraction from fraction_list
    n_next = 0
    d_next = 1
    while j >= 0:
        d = d_next
        k = a_list[j]*d_next+n_next
        n_next = d
        d_next = k
        j = j-1
    return k,d #returns guess for k and d. d is the private key.




#Perform Wieners Attack (see https://en.wikipedia.org/wiki/Wiener%27s_attack)

n_fe, d_fe = expand_fraction_list(n_fe, d_fe) #creates 0th element in fraction list

for i in range(1,1000):   
    n_fe, d_fe = expand_fraction_list(n_fe, d_fe) #adds new element to fraction list
    k,d = cfe(fraction_list, i) #calculates the fraction for the i'th fraction expansion
    with decimal.localcontext() as ctx:
        ctx.prec = 10000
        PhiN = D((e*d-1)/k)
        if PhiN%1 == 0 and d%2 == 1: #Checks if phi(N) is a natural number and if d is odd
            with decimal.localcontext() as ctx: #try to solve square equation x2 + bx + c == 0
                ctx.prec = 1000
                b = -(N-PhiN+1)
                c = N
                sqr2 = b**2-4*c
                if sqr2 > 0: #checks if squareroot therm is larger than 0
                    sqr = D(sqr2.sqrt())
                    if sqr%1 == 0 and ((-b+sqr)/2)%1 == 0 and ((-b-sqr)/2)%1 == 0: #checks if squareroot-therm and the two solutions are all natural numbers
                        break

print("d = ", d)            

N = int(N)

m_c = pow(c_m, d, N)
print("Decrypted message: ", m_c)

from Crypto.Util.number import long_to_bytes
text = long_to_bytes(m_c)

print("Plain text: ", text)