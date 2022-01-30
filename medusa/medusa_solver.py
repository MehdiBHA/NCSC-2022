from Crypto.Util.number import GCD, inverse, long_to_bytes

n = 125970918998429941755207092719000093859584326398515340271507098461981127858684794527758435547477980020672812763105983709637516416042141239344165968387573604439356684429777088090098851525679251078931951969773090071630788561053845383929190807803704436638397099166945237499724615541844214395325019333699387796277
c_mat = [[47174277818146406918623818468357369713157374294183574342895391625978489217216729765260815472630182191867339511825396840413054089287666788138829278776317980075849258054288274637784593311539620629018460032712554996946200775030306319762625393202437084263312703766201193155145363603402668332097900885517445557871, 63939307262042906324634450546064445433495611330146378275959550129402709562854542848943900610493914229879423659793506299556754703033999723131202332828916727949941302936539704181512596016540980208986623826424139560266388530586160735708426515931846215519934731706810547449176052259779669761925791883753809686664], [0, 47174277818146406918623818468357369713157374294183574342895391625978489217216729765260815472630182191867339511825396840413054089287666788138829278776317980075849258054288274637784593311539620629018460032712554996946200775030306319762625393202437084263312703766201193155145363603402668332097900885517445557871]]
c = 112031476794611849291468051797352481299885232833663228152303134349588972390556482343082717639427660528486631937831094182659297169565820835283205322707411446855401640420625441061554468265291934496011096890715682558425840134847295758910234889807175803114418971483777194566174666647125390843452095980691446461069
e = 65537

p = GCD(n, c_mat[0][1])
q = n//p
phi = (p-1)*(q-1)
d = inverse(e, phi)

print(long_to_bytes(pow(c, d, n)))