def main ():
    m=float(input("Enter mass: "))
    v=float(input("Enter velocity: "))
    ke= kinetic_energy(m,v)
    display(ke)
    main()
def kinetic_energy(m,v):
    ke=0.5*m**v
    return ke
def display(ke):
    print("The value of kinetic energy is: ", ke)
