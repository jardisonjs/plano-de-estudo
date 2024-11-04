from veiculos_poo import Veiculo

veiculo = Veiculo()

while True:
        print("Sistema de Gerenciamento de Estação de Carregamento de Veículos Elétricos")
        opcao = int(input("1. Cadastrar Veículo\n2. Consultar Veículos\n3. Iniciar Carregamento\n4. Finalizar Carregamento\n5. Consultar Status\n6. Deletar Veículo\n7. Sair\nEscolha uma opção: "))

        if opcao == 1:
            placa = input("Informe a placa do veículo: ")
            modelo = input("Informe o modelo do veículo: ")
            veiculo.cadastrarVeiculo(placa, modelo)

        elif opcao == 2:
            veiculo.consultarVeiculos()

        elif opcao == 3:
            id = int(input("Informe o ID do veículo para iniciar o carregamento: "))
            veiculo.iniciarCarregamento(id)

        elif opcao == 4:
            id = int(input("Informe o ID do veículo para finalizar o carregamento: "))
            custo_por_hora = float(input("Informe o custo por hora: "))
            veiculo.finalizarCarregamento(id, custo_por_hora)

        elif opcao == 5:
            id = int(input("Informe o ID do veículo para consultar o status: "))
            veiculo.consultarStatus(id)

        elif opcao == 6:
            id = int(input("Informe o ID do veículo para deletar: "))
            veiculo.deletarVeiculo(id)

        elif opcao == 7:
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida.")
