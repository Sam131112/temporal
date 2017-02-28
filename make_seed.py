def seed_file(c,typ):
                f  = open("seed_"+typ+".txt","w")
                for v in c:
                        f.write(str(v[0])+"\n")
                f.close()

