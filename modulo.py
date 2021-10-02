import classe

conta1 = classe.Conta('Marcio', 2)
conta1.Depositar(200.0)
print(conta1.getCliente())

conta2 = classe.Conta('Ana', 3)
conta2.Depositar(200.0)

conta1.Transferencia(conta2, 100)

print(conta1.Saldo())
print(conta2.Saldo())
