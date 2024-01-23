# https://www.geeksforgeeks.org/pad-or-fill-a-string-by-a-variable-in-python-using-f-string/
limites = [
	762,
	886.57,
	932.14,
	999.14,
	1106.93,
	1600.36,
	1961.36,
	2529.05,
	3694.46,
	5469.9,
	6420.55,
	20064.21,
	9999999.99]

taxas = [
	0.0,
	0.1450,
	0.2100,
	0.2100,
	0.2650,
	0.2850,
	0.3500,
	0.3700,
	0.3872,
	0.4005,
	0.4272,
	0.4495,
	0.4717]

pabater = [
	0.0,
	0.0,
	0.0,
	114.14,
	169.09,
	191.23,
	295.26,
	334.48,
	377.86,
	427.18,
	573.22,
	716.08,
	1162.51]

width = 15
filler = '.'
for i in range(6, width):
	print(f'{"geeks" :{filler}<{i}}')


print(f"{'IRS':.<10}")

#
# sb = 1424.34
# taxa_irs_marginal = 28.50/100
# p = 1
# irs_marginal = 405.94
# pa = 191.23
# irs = 214.71
# td = 371.38
# ss = 156.68
# tirs_efetiva = 15.07/100
# si= 1052.96
# print(f"{sb:10.2f} {p:5d} {taxa_irs_marginal * 100:10.2f}% {irs_marginal:10.2f} {pa:10.2f} {irs:10.2f} {td:10.2f} {ss:10.2f} {tirs_efetiva * 100:10.2f}% {si:10.2f}")
#
# irs = irs_marginal - pa
# tirs_efetiva = irs / sb
# taxa_ss = 0.11
# ss = sb * taxa_ss
# td = irs + ss
# si = sb - td
# print(f"{sb:10.2f} {p:5d} {taxa_irs_marginal * 100:10.2f}% {irs_marginal:10.2f} {pa:10.2f} {irs:10.2f} {td:10.2f} {ss:10.2f} {tirs_efetiva * 100:10.2f}% {si:10.2f}")
#
# exit()

print(f"{'sb':*<10} {'p':*<5} {'tirs':*<10}% {'irs_a':*<10} {'pa':*<10} {'irs':*<10} {'tirse':*<10}%")

f = open('casos.txt', "wt")

caso=0
for hh in [(10, 10), (40, 4.5), (40, 5.3),(38, 5.88), (45, 6.59), (60, 12.34), (50, 21.25), (55, 125.24)]:
	sh = hh[1]
	horas = hh[0] * 4
	sb = horas * sh
	for x in [1]:
		p = 0
		while limites[p] < sb:
			p = p + 1
		taxa_irs_marginal = taxas[p]
		irs_marginal = sb * taxa_irs_marginal
		pa = pabater[p]
		pa_s = ''
		if p == 1:
			pa = 14.5 / 100 * 2.3 * (1093.31 - sb)
			pa_s = f"14.5%×2.3×(1093.31-{sb:.2f})"
		if p == 2:
			pa = 21.0 / 100 * 1.3 * (1350.22 - sb)
			pa_s = f"21.0%×1.3×(1350.22-{sb:.2f})"
		irs = irs_marginal - pa
		tirs_efetiva = irs / sb
		taxa_ss = 0.11
		ss = sb * taxa_ss
		td = irs + ss
		si = sb - td
		si2 = sb - ss - irs

		# print('.'  * 60 )
		# print(f"{sb:10.2f} {p:5d} {taxa_irs_marginal * 100:10.2f}% irsm {irs_marginal:10.2f} {pa:10.2f} irs {irs:10.2f} td {td:10.2f} ss {ss:10.2f} {tirs_efetiva * 100:10.2f}% si {si:10.2f} | {si2:10.2f}")
		# print(f"{sb:10.5f} {p:5d} {taxa_irs_marginal * 100:10.5f}% irsm {irs_marginal:10.5f} {pa:10.5f} irs {irs:10.5f} td {td:10.5f} ss {ss:10.5f} {tirs_efetiva * 100:10.5f}% si {si:10.5f} | {si2:10.5f}")

		irs_marginal = round(irs_marginal,2)
		pa= round(pa,2)
		ss= round(ss,2)
		irs = irs_marginal - pa
		tirs_efetiva = irs / sb
		tirs_efetiva = round(tirs_efetiva, 4)
		td = irs + ss
		si = sb - td
		si2 = sb - ss - irs

		# print(f"{sb:10.5f} {p:5d} {taxa_irs_marginal * 100:10.5f}% irsm {irs_marginal:10.5f} {pa:10.5f} irs {irs:10.5f} td {td:10.5f} ss {ss:10.5f} {tirs_efetiva * 100:10.5f}% si {si:10.5f} | {si2:10.5f}")
		# print(f"{sb:10.5f} {p:5d} {taxa_irs_marginal * 100:10.5f}% {irs_marginal:10.5f} {pa:10.5f} {irs:10.5f} {td:10.5f} {ss:10.5f} {tirs_efetiva * 100:10.5f}% {si:10.5f}")
		if True:
			caso = caso + 1

			print('Caso:', caso, file=f)
			print(f"\tHoras......: {horas}", file=f)
			print(f"\tValor Hora.: {sh:.2f}\n\n", file=f)

			print('Caso:', caso)
			print(f"Horas......: {horas}")
			print(f"Valor Hora.: {sh:.2f}")
			print('\n')
			print(f"{'RECIBO':^39}")
			print('='  * 38 )
			print(f"Salário bruto{'':.>15}:{sb:>9,.2f}")
			print(f"Horas({horas})×Valor Hora({sh:.2f})")
			n = 8
			if taxa_irs_marginal > .10:
				n = 7
			print('-'  * 38)
			print(f"IRS marginal ({taxa_irs_marginal * 100:>.2f}%){'':.>{n}}:{irs_marginal:>9.2f}")
			print(f"  Parcela a abater {'':.>9}:{pa:>9.2f}")
			if pa_s != '':
				print(f"{' ':2}{pa_s}")
			n = 17
			if tirs_efetiva > .10:
				n = 16
			print(f"IRS ({tirs_efetiva * 100:>.2f}%){'':.>{n}}:{irs:>9.2f}")
			print(f"SS ({taxa_ss * 100:>.2f}%){'':.>17}:{ss:>9.2f}")
			print(f"Total descontos{'':.>13}:{td:>9.2f}")
			print('-'  * 38)
			print(f"Salário líquido{'':.>13}:{si:>9.2f}")
			print('\n\n')
			# -----------
			# print('.'  * 60 )
			# print(f"Salário bruto{'':.>15}:{sb:>9.5f}")
			# print(f"  IRS marginal({taxa_irs_marginal * 100:>.5f}%){'':.>6}:{irs_marginal:>9.5f}")
			# print(f"  Parcela a abater {'':.>9}:{pa:>9.5f}")
			# if pa_s != '':
			# 	print(f"{' ':2}{pa_s}")
			# print(f"IRS({tirs_efetiva * 100:>.5f}%){'':.>17}:{irs:>9.5f}")
			# print(f"SS({taxa_ss * 100:>.5f}%){'':.>18}:{ss:>9.5f}")
			# print(f"Total descontos{'':.>13}:{td:>9.5f}")
			# print(f"Salário líquido{'':.>13}:{si:>9.5f}")


