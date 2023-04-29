instituicao = int(input("Digite sua instituição de ensino, 1 para Unit e 2 para UFS: "))
nota1 = float(input("Digite a nota da 1ª unidade: "))
nota2 = float(input("Digite a nota da 2ª unidade: "))
falta = int(input("Número de faltas: "))

media = (nota1 + nota2) / 2

aprovado_unit = media >= 6 and falta <= 21
aprovado_ufs = (media >= 5 and falta <= 12) or (media >= 7 and falta > 12)

aprovado = aprovado_unit if instituicao == 1 else aprovado_ufs

print("Você foi aprovado" if aprovado else "Você foi reprovado")