weight = int(input('Enter weight: '));
choose = input('(K)g or (L)bs:');
if choose == 'K' or choose == 'k':
    updated = weight * 2.2;
    print('Weight in LBs: ' + str(updated));
elif choose == 'l' or choose == 'L':
    updated = weight/2.2;
    print("weight in Kg: " + str(updated));
else:
    print("command not found");


