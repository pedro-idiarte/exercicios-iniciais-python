#senha_perm[0] >= 4 = OWNER_READ = True
# senha_perm[1] >= 4 = GROUP_READ = True 
# senha_perm[2] >= 4 = OTHER_READ = True
# senha_perm[] >= 4 =  WORLD_READ = True

#valor_um = 0
# valor_dois = 0
# valor_tres = 0

# senha_perm = input("Insira a senha de permissão: ")

# senha_perm[0] = valor_um
# senha_perm[1] = valor_dois
# senha_perm[2] = valor_tres


# senha_perm = int(senha_perm)

OWNER_READ: bool    
OWNER_WRITE: bool
OWNER_EXEC: bool

GROUP_READ: bool
GROUP_WRITE: bool
GROUP_EXEC: bool

OTHER_READ: bool
OTHER_WRITE: bool
OTHER_EXEC: bool

OWNER_ALL: bool

WORLD_READ: bool

NO_WORLD_WRITE: bool

senha_perm = "755"

OWNER_READ, GROUP_READ, OTHER_READ = int(senha_perm[0]) >= 4, int(senha_perm[1]) >= 4, int(senha_perm[2]) >= 4
OWNER_WRITE, GROUP_WRITE, OTHER_WRITE = int(senha_perm[0]) == 2 | 3 | 6 | 7, int(senha_perm[1]) == 2 | 3 | 6 | 7 , int(senha_perm[2]) == 2 | 3 | 6 | 7
OWNER_EXEC, GROUP_EXEC, OTHER_EXEC = int(senha_perm[0]) % 2 == 1, int(senha_perm[1]) % 2 == 1, int(senha_perm[2]) % 2 == 1
OWNER_ALL = int(senha_perm[0]) >= 4 or int(senha_perm[0]) == 2 | 3 | 6 | 7 or int(senha_perm[0]) % 2 == 1
WORLD_READ =  OWNER_READ and GROUP_READ and OTHER_READ
NO_WORLD_WRITE = not(OWNER_WRITE and GROUP_WRITE and OTHER_WRITE)

print("\n",
"OWNER_READ:",OWNER_READ,"\n",  
"OWNER_WRITE:",OWNER_WRITE,"\n",
"OWNER_EXEC:",OWNER_EXEC,"\n",
"GROUP_READ:",GROUP_READ,"\n",
"GROUP_WRITE:",GROUP_WRITE,"\n",
"GROUP_EXEC:",GROUP_EXEC,"\n",   
"OTHER_READ:",OTHER_READ,"\n",
"OTHER_WRITE:",OTHER_WRITE,"\n",
"OTHER_EXEC:",OTHER_EXEC,"\n",
"OWNER_ALL:",OWNER_ALL,"\n",
"WORLD_READ:",WORLD_READ,"\n",
"NO_WORLD_WRITE:",NO_WORLD_WRITE,"\n",
)